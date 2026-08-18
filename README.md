# waterline-writing

Waterline's social-finance editorial layer: **one research truth layer, three writing identities, six platform adapters, and one distribution router**.

## What this repository does

The repo transforms already-completed Waterline research into platform-native social content while preserving facts, uncertainty, provenance, and research conclusions.

Completed Waterline research is read from macOS/NAS at:

```text
/Volumes/NAS/quant/Waterline-Research
```

The writing layer treats that upstream research as read-only by default.

## Architecture

```text
Waterline Research
       ↓
   Truth Pack
       ↓
Content Router
       ↓
Style Skill × Platform Adapter
       ↓
Publish Package
       ↓
Human review
       ↓
Optional Publisher
```

### Style Skills

The three existing Skills remain editorial identities rather than platform-specific copies:

- `skills/waterline-research-authority` — evidence-first authority content for research-brand trust and conversion.
- `skills/waterline-finance-story` — narrative finance storytelling for broad reach without changing upstream facts.
- `skills/waterline-researcher-voice` — first-person research-process content that builds trust without inventing personal experience.

### Content Router

- `skills/waterline-content-router` — builds one shared Truth Pack and fans it out into independent `style × platform` generation tasks.

The anti-drift rule is strict: **never create one universal article and then use it as the source for other platforms.** Every platform draft descends directly from the same Truth Pack.

### Platform adapters

`platforms/` contains packaging rules for:

- WeChat Official Accounts / 微信公众号
- Xiaohongshu / 小红书
- Xueqiu / 雪球
- Weibo / 微博
- Douyin / 抖音
- Bilibili / B站

Platform adapters define length, hook, pacing, evidence density, visuals, CTA, and output shape. They do not redefine style or research truth.

Default routes live in `config/routes.yaml`:

- WeChat → Research Authority
- Xiaohongshu → Researcher Voice
- Xueqiu → Research Authority
- Weibo → Researcher Voice
- Douyin → Finance Story
- Bilibili → Finance Story

These are defaults, not restrictions.

## Core contracts

- `contracts/truth-pack.md` — canonical truth state shared by all downstream outputs.
- `contracts/publish-package.md` — ready-to-review platform package.
- `workflows/distribute.md` — one-research-to-many-platform workflow.
- `publishers/README.md` — publication boundary and future publisher interface.

## Research benchmark

`research/` contains the August 18, 2026 benchmark used to design the Skills:

- 120-account operating sample across Xiaohongshu, Douyin, Bilibili, WeChat Official Accounts, Xueqiu, and Weibo.
- cross-platform creator mechanisms and platform playbooks.
- source/confidence ledger.
- China finance-content compliance guardrails.

The benchmark is an operating sample, not an official all-platform popularity ranking.

## Validation

Run from the repository root:

```bash
python skills/waterline-research-authority/scripts/validate.py
python skills/waterline-finance-story/scripts/validate.py
python skills/waterline-researcher-voice/scripts/validate.py
python skills/waterline-content-router/scripts/validate.py
```

## Publishing boundary

All writing Skills and the router are `draft-only`. They may create ready-to-publish packages, but they must not publish unless the user explicitly requests it and an approved publisher integration is configured.

See `AGENTS.md` for Kimi Code operating instructions.
