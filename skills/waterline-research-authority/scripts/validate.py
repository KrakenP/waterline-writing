from pathlib import Path
import json, csv
ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT.parents[1] / "research"
required = ["README.md","SKILL.md","manifest.json","examples/physical-ai.md"]
shared_required = ["platform-playbook.md","benchmark-findings.md","source-ledger.md","compliance-cn.md"]
missing=[x for x in required if not (ROOT/x).exists()] + [f"../../research/{x}" for x in shared_required if not (RESEARCH/x).exists()]
if missing: raise SystemExit("Missing: "+", ".join(missing))
skill=(ROOT/"SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n") or "\nname:" not in skill or "\ndescription:" not in skill: raise SystemExit("bad SKILL front matter")
manifest=json.loads((ROOT/"manifest.json").read_text(encoding="utf-8"))
for k in ("name","version","entrypoint","description"):
    if k not in manifest: raise SystemExit("manifest missing "+k)
rows=[]
for fp in sorted((RESEARCH/"benchmark-accounts").glob("*.csv")):
    with fp.open(encoding="utf-8-sig") as f:
        rows.extend(csv.DictReader(f))
if len(rows)!=120: raise SystemExit(f"expected 120 rows, got {len(rows)}")
if len({r["platform"] for r in rows})!=6: raise SystemExit("expected 6 platforms")
print("OK")
