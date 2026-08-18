# Truth Pack contract

A Truth Pack is the canonical editorial input derived from one completed Waterline research package. It is created once and reused by every downstream style × platform generation task.

## Purpose

The Truth Pack prevents platform adaptation from drifting away from the research. It is not a second research report and should not add new claims.

## Required fields

```yaml
topic: string
as_of: YYYY-MM-DD
source_root: path-or-package-id

core_thesis: string

facts:
  - id: F1
    claim: string
    source: string
    source_date: string
    applicability: string | null

inferences:
  - id: I1
    claim: string
    based_on: [F1]

hypotheses:
  - id: H1
    claim: string
    trigger_or_test: string

unknowns:
  - id: U1
    question: string
    why_it_matters: string

counterevidence:
  - id: C1
    claim: string
    source: string

key_numbers:
  - metric: string
    value: string
    date: string
    source: string

assets:
  - path: string
    type: chart | table | image | other
    evidentiary: true | false

forbidden_upgrades:
  - string
```

## Rules

- Preserve the research package's existing confidence and uncertainty.
- Every material numeric fact should retain source/date traceability.
- Do not add a first-person statement unless it is explicitly grounded in source material or verified author input.
- If the source package does not support a required field, keep it empty or emit `RESEARCH_GAP`; do not fabricate.
- A Truth Pack may be refreshed when the upstream research changes, but downstream platform drafts should never mutate it.
