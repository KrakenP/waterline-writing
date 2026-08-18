from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
required = [
    ROOT / "config" / "routes.yaml",
    ROOT / "contracts" / "truth-pack.md",
    ROOT / "contracts" / "publish-package.md",
    ROOT / "workflows" / "distribute.md",
    ROOT / "platforms" / "wechat.md",
    ROOT / "platforms" / "xiaohongshu.md",
    ROOT / "platforms" / "xueqiu.md",
    ROOT / "platforms" / "weibo.md",
    ROOT / "platforms" / "douyin.md",
    ROOT / "platforms" / "bilibili.md",
    ROOT / "skills" / "waterline-research-authority" / "SKILL.md",
    ROOT / "skills" / "waterline-finance-story" / "SKILL.md",
    ROOT / "skills" / "waterline-researcher-voice" / "SKILL.md",
]

missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    print("Missing required Waterline Writing files:")
    for item in missing:
        print(f"- {item}")
    sys.exit(1)

print("waterline-content-router: OK")
