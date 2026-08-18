# Distribute one research package to multiple platforms

## Goal

Use one completed Waterline research package to generate multiple platform-native pieces without changing its underlying facts, uncertainty, provenance, or conclusions.

## Inputs

Required:

- `master_research` or an explicit research path
- `as_of`

Optional:

- `routes`
- `goal`
- `audience`
- `assets`
- `approved_cta`
- `author_identity` and verified first-person facts

If routes are omitted, load `config/routes.yaml`.

## Procedure

1. Read the upstream research package completely enough to understand decisive claims and caveats.
2. Create one Truth Pack using `contracts/truth-pack.md`.
3. Freeze that Truth Pack for this generation run.
4. Expand requested routes into independent `style × platform` tasks.
5. For every task:
   - load the selected style Skill;
   - load the selected platform adapter;
   - generate directly from the frozen Truth Pack;
   - run research-integrity and compliance checks;
   - produce a Publish Package.
6. Write a run manifest recording source path, `as_of`, selected routes, and output paths.
7. Stop before publication unless an explicit user request and a configured publisher authorize the next step.

## Anti-drift rule

Never use one downstream draft as the truth source for another downstream draft.

Bad:

```text
research → WeChat article → summarize to Xiaohongshu → compress to Weibo
```

Required:

```text
research → Truth Pack → WeChat
                     → Xiaohongshu
                     → Weibo
```

## Failure behavior

Stop and report rather than improvise when:

- NAS is unavailable;
- requested research cannot be found;
- a decisive claim lacks required source/date context;
- the requested first-person framing is unsupported;
- a requested platform has no adapter;
- the requested style has no Skill;
- the requested conclusion contradicts the research.
