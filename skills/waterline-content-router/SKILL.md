---
name: waterline-content-router
description: Route one completed Waterline research package through shared truth locking and one or more style × platform combinations to produce platform-native draft packages without changing upstream facts or uncertainty.
---

# Waterline Content Router Skill

## Mission
Turn **one research truth state** into many platform-native editorial outputs while keeping style, platform, and publication authority separate.

## Scope
This is an orchestration Skill for writing and social-content generation only. It does not perform portfolio management, investment underwriting, or autonomous research expansion.

## Upstream research
Default macOS research root:

```text
/Volumes/NAS/quant/Waterline-Research
```

Treat upstream research as read-only. If the path is unavailable or the requested research cannot be resolved, stop with a clear error instead of substituting invented or unrelated material.

## Inputs
Required:
- `master_research` or explicit research path
- `as_of`

Optional:
- `platforms`
- `styles`
- explicit `routes`
- `goal`
- `audience`
- assets
- approved CTA
- verified author identity / first-person facts

If no routes are supplied, read `../../config/routes.yaml`.

## Style layer
Available default style Skills:
- `../waterline-research-authority/SKILL.md`
- `../waterline-finance-story/SKILL.md`
- `../waterline-researcher-voice/SKILL.md`

A style answers **who is speaking and how the content frames the research**.

## Platform layer
Read the selected adapter under `../../platforms/`.

A platform answers **where the content is being published and what native packaging it requires**.

Never create platform-specific copies of the style Skills merely to change length, hook, cards, script structure, or CTA.

## Procedure
1. Resolve and read the upstream research package.
2. Build exactly one Truth Pack using `../../contracts/truth-pack.md`.
3. Freeze the Truth Pack for this run.
4. Resolve routes from explicit user input or `../../config/routes.yaml`.
5. For every route, independently combine:
   - the selected style Skill;
   - the selected platform adapter;
   - the same frozen Truth Pack.
6. Generate the platform-native output directly from the Truth Pack.
7. Validate research integrity, source/date trace, uncertainty, and compliance.
8. Package each result according to `../../contracts/publish-package.md`.
9. Produce a run manifest containing source path, `as_of`, routes, and output paths.
10. Stop at draft/package generation unless publication is explicitly requested and an approved publisher is configured.

## Critical anti-drift rule
Do not generate a universal article and use that article as the source for other platforms.

Each platform output must descend directly from the same Truth Pack.

## Research integrity
Internally preserve:
- `F` sourced fact
- `I` inference
- `H` hypothesis/scenario
- `U` unknown

Platform adaptation may change angle, title, hook, order, pacing, length, evidence density, visuals, and CTA. It must not change facts, material caveats, source provenance, claim type, or research conclusion.

## Default routing
See `../../config/routes.yaml`.

Default intent:
- WeChat → Research Authority
- Xiaohongshu → Researcher Voice
- Xueqiu → Research Authority
- Weibo → Researcher Voice
- Douyin → Finance Story
- Bilibili → Finance Story

## Output authority
`draft-only`.

Return or write:
- one Truth Pack;
- one Publish Package per requested platform;
- one generation manifest;
- explicit `RESEARCH_GAP`, `COMPLIANCE_REVIEW_REQUIRED`, or route errors when applicable.
