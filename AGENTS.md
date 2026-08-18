# AGENTS.md

## Project purpose

`waterline-writing` is Waterline's editorial and social-media production layer. Its job is to transform already-completed Waterline research into platform-native drafts and ready-to-publish content packages without changing the underlying research truth state.

This repository is **not** responsible for Waterline research orchestration, PQuant underwriting, portfolio management, or trading decisions.

## Research source

On the user's macOS machine, completed Waterline research is available at:

```text
/Volumes/NAS/quant/Waterline-Research
```

Treat this path as a **read-only upstream source** unless the user explicitly asks to modify research files. Never move, rename, delete, or rewrite files under this path as part of normal writing work.

Before writing from a research result:
1. Verify that `/Volumes/NAS/quant/Waterline-Research` is mounted and readable.
2. Locate the requested research project or file.
3. Read enough of the source package to identify its decisive claims, evidence, dates, uncertainty, counterevidence, and unknowns.
4. If the NAS is unavailable or the requested research cannot be found, stop and report the exact problem. Do not silently substitute web research or invent missing findings.

## Editorial architecture

Keep **style** and **platform** as separate dimensions.

### Style layer

The existing writing Skills are editorial identities, not platform-specific Skills:

- `skills/waterline-research-authority` — evidence-first research authority.
- `skills/waterline-finance-story` — narrative finance storytelling.
- `skills/waterline-researcher-voice` — first-person research-process voice.

Do not clone these into `wechat-*`, `xiaohongshu-*`, etc. A style defines who is speaking and how the argument is framed.

### Platform layer

Platform adapters live under `platforms/` and define where the content is being published: length, hook form, pacing, evidence density, visual packaging, CTA, and output shape.

Supported first-class platforms:

- WeChat Official Accounts / 微信公众号
- Xiaohongshu / 小红书
- Xueqiu / 雪球
- Weibo / 微博
- Douyin / 抖音
- Bilibili / B站

A platform adapter must not redefine the Waterline research truth state or editorial identity.

### Router

`skills/waterline-content-router` combines one upstream research package with one or more `style × platform` routes.

Default routes are configured in `config/routes.yaml`. Users may override them per request.

## Truth Pack

For multi-platform generation, first derive a single Truth Pack from the upstream research. Follow `contracts/truth-pack.md`.

All downstream outputs for the same research item must inherit the same:

- core thesis
- sourced facts and dates
- inference / hypothesis boundaries
- counterevidence
- unknowns
- key numbers
- source trace
- forbidden confidence upgrades

Do **not** generate a universal article and then repeatedly summarize/rewrite it for other platforms. Generate every final platform draft directly from the shared Truth Pack.

## Required workflow

For a request such as “turn this research into social content”:

1. Resolve the research input from the explicit path or from `/Volumes/NAS/quant/Waterline-Research`.
2. Build or validate the Truth Pack.
3. Resolve requested routes. If none are supplied, use `config/routes.yaml`.
4. For each route, combine:
   - one style Skill
   - one platform adapter
   - the shared Truth Pack
5. Generate each platform-native draft independently from the Truth Pack.
6. Run research-integrity and compliance checks.
7. Write a ready-to-publish package following `contracts/publish-package.md`.
8. Stop at draft/package generation unless the user explicitly requests publishing and an approved publisher integration exists.

## Default route behavior

Default editorial mapping:

- WeChat → `waterline-research-authority`
- Xiaohongshu → `waterline-researcher-voice`
- Xueqiu → `waterline-research-authority`
- Weibo → `waterline-researcher-voice`
- Douyin → `waterline-finance-story`
- Bilibili → `waterline-finance-story`

These are defaults, not restrictions. Any valid style can be paired with any platform when the user asks or an evaluation justifies it.

## Model policy

Kimi Code is the current harness. Keep the repository model-neutral.

- Do not hard-code Kimi K3, GPT, Claude, Gemini, DeepSeek, Qwen, or another model into a Skill unless a user explicitly asks for a model-specific experiment.
- Use the currently selected Kimi Code model by default.
- Model routing may be added later through configuration without changing the writing Skills.

## Research integrity

Never change upstream meaning for engagement.

Internally preserve claims as:

- `F` — sourced fact
- `I` — inference
- `H` — hypothesis / scenario
- `U` — unknown

Never:

- turn inference into fact
- upgrade confidence
- delete material counterevidence merely to simplify a post
- invent sources, dates, quotes, meetings, positions, trades, emotions, or first-person experiences
- state a time-sensitive fact without an `as_of` date when freshness matters

If evidence is insufficient, emit `RESEARCH_GAP` and identify what is missing.

## Platform generation rule

Platform adaptation may change:

- angle
- title
- hook
- ordering
- pacing
- length
- evidence density
- chart/card/video treatment
- CTA

It must not change:

- facts
- material caveats
- claim type
- source provenance
- research conclusion

## Output layout

Preferred generated structure:

```text
outputs/<topic-or-slug>/
├── truth-pack.yaml
├── manifest.yaml
├── wechat/
├── xiaohongshu/
├── xueqiu/
├── weibo/
├── douyin/
└── bilibili/
```

Only create requested platform folders. Generated content is a working artifact and should not be committed by default.

## Publishing boundary

Writing Skills and the content router have **draft-only authority**.

Do not publish, schedule, log in, upload, click confirmation buttons, or call a platform publishing API unless:

1. the user explicitly requests publication;
2. a platform publisher exists and is configured;
3. required credentials/permissions are available through an approved secret mechanism;
4. the final draft has passed the required approval gate.

See `publishers/README.md`.

## Security

Never commit:

- `.env` files
- API keys
- cookies
- OAuth tokens
- session files
- browser profiles
- platform credentials
- NAS credentials

Use environment variables or a local secret store. Keep generated outputs and local caches out of version control unless the user explicitly asks to preserve an example fixture.

## Validation

Run the existing Skill validators from the repository root:

```bash
python skills/waterline-research-authority/scripts/validate.py
python skills/waterline-finance-story/scripts/validate.py
python skills/waterline-researcher-voice/scripts/validate.py
python skills/waterline-content-router/scripts/validate.py
```

When changing platform contracts or routing behavior, also verify that every platform named in `config/routes.yaml` has a corresponding adapter in `platforms/`.
