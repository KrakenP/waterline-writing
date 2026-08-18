# Publish Package contract

A Publish Package is the final draft artifact produced for one platform. It is ready for human review and possible handoff to a publisher, but it is not itself authorization to publish.

## Common fields

Each platform package should contain, as applicable:

- `title_options`
- `cover_text`
- `hook`
- `body_or_script`
- `visual_brief`
- `source_trace`
- `counterpoint_or_uncertainty`
- `cta`
- `compliance_flags`
- `style`
- `platform`
- `as_of`
- `truth_pack_id_or_path`

## Preferred filesystem shape

```text
outputs/<topic>/<platform>/
├── draft.md
├── metadata.yaml
└── assets/
```

Platform adapters may add native artifacts such as `cards.md`, `thread.md`, `shot-list.md`, or `chapter-outline.md`.

## Authority

Publish Packages are `draft-only` until an explicit human/user approval and a configured publisher are present.
