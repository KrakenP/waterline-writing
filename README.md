# waterline-writing

Waterline's social-finance editorial layer: one research truth layer, three distinct writing engines, six-platform adaptation.

## Skills

- `skills/waterline-research-authority` — evidence-first authority content for research-brand trust and conversion.
- `skills/waterline-finance-story` — narrative finance storytelling for broad reach without changing upstream facts.
- `skills/waterline-researcher-voice` — first-person research-process content that builds trust without inventing personal experience.

All three Skills accept the same underlying Waterline research but optimize for different audience jobs. They may change framing, structure, pacing, title, and platform packaging; they must not change facts, uncertainty, provenance, or research conclusions.

## Shared research

`research/` contains the August 18, 2026 benchmark used to design the Skills:

- 120-account operating sample across Xiaohongshu, Douyin, Bilibili, WeChat Official Accounts, Xueqiu, and Weibo.
- cross-platform creator mechanisms and platform playbooks.
- source/confidence ledger.
- China finance-content compliance guardrails.

The benchmark is an operating sample, not an official all-platform popularity ranking.

## Repository layout

```text
waterline-writing/
├── skills/
│   ├── waterline-research-authority/
│   ├── waterline-finance-story/
│   └── waterline-researcher-voice/
└── research/
    ├── benchmark-accounts-2026-08.csv
    ├── benchmark-findings.md
    ├── platform-playbook.md
    ├── creator-benchmark-report.md
    ├── source-ledger.md
    ├── compliance-cn.md
    └── waterline-finance-creator-benchmark-2026-08.md
```

## Validation

Run each Skill's validator from the repository root:

```bash
python skills/waterline-research-authority/scripts/validate.py
python skills/waterline-finance-story/scripts/validate.py
python skills/waterline-researcher-voice/scripts/validate.py
```
