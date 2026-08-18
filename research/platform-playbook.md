# Platform playbook

Defaults, not hard limits.

This file is the benchmark-era summary. Executable platform packaging rules now live under `../platforms/`. Style Skills should use the selected platform adapter as the primary packaging instruction and use this file as cross-platform context.

| Platform | Primary job | Default unit | Hook | Evidence | CTA |
|---|---|---|---|---|---|
| 小红书 | trust + saves | 6–10 cards or 500–1200 Chinese chars | first-person discovery / counterintuitive result | 3–5 decisive facts + one chart/table | save/follow; deeper brief |
| 抖音 | reach | 30–120s | conflict or one sharp question in first 1–2 lines | 2–4 decisive facts | follow for next part / full brief |
| B站 | understanding + brand | 6–20 min | event/puzzle + why it matters | causal chain, charts, counterthesis | full research / related episode |
| 公众号 | canonical free research | 1800–5000+ Chinese chars | thesis + why-now | highest evidence density; source notes | research subscription / website |
| 雪球 | investment-research trust | 800–2500 Chinese chars | thesis / update trigger | facts + risks + invalidation | follow research updates; no paid call |
| 微博 | habit + timeliness | 100–500 chars or thread | immediate inference | one key data point/source | follow / thread / long-form |

## Platform adapters

- `../platforms/wechat.md`
- `../platforms/xiaohongshu.md`
- `../platforms/xueqiu.md`
- `../platforms/weibo.md`
- `../platforms/douyin.md`
- `../platforms/bilibili.md`

## Packaging checklist

Every output should include, as applicable:
- ranked title/cover-text options;
- the opening hook separately;
- the core claim and one-sentence payoff;
- platform-native body/script;
- visual brief;
- source trace for material numeric claims;
- counterpoint / uncertainty appropriate to the format;
- CTA;
- compliance flags.

For multi-platform generation, create one Truth Pack and generate each platform draft directly from it. Do not use one downstream draft as the source for another.
