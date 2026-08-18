# Example: one research package → multiple platform drafts

## User intent

Use an existing Physical AI research package under the Waterline Research NAS root and generate platform-native drafts from the same research truth state.

## Example input

```yaml
research_path: /Volumes/NAS/quant/Waterline-Research/<physical-ai-project>
as_of: 2026-08-18
routes:
  - platform: wechat
    style: waterline-research-authority
  - platform: xiaohongshu
    style: waterline-researcher-voice
  - platform: xueqiu
    style: waterline-research-authority
```

## Required execution

```text
research package
    ↓
one frozen Truth Pack
    ├── Research Authority × WeChat
    ├── Researcher Voice × Xiaohongshu
    └── Research Authority × Xueqiu
```

Do not generate the WeChat article first and summarize it into Xiaohongshu or Xueqiu. All three drafts must descend independently from the same frozen Truth Pack.

## Expected output

```text
outputs/<topic>/
├── truth-pack.yaml
├── manifest.yaml
├── wechat/
│   ├── draft.md
│   └── metadata.yaml
├── xiaohongshu/
│   ├── draft.md
│   ├── cards.md
│   └── metadata.yaml
└── xueqiu/
    ├── draft.md
    └── metadata.yaml
```

Publishing remains outside the router's authority.
