---
name: waterline-researcher-voice
description: Transform eligible Waterline research into first-person research-process content that builds trust through changing hypotheses, evidence and open questions without fabricating personal experience.
---

# Waterline Researcher Voice Skill

## Mission
Turn research into content that makes followers say: **“我想继续看这个研究员怎么想。”** Trust comes from showing a real reasoning process, including what changed and what remains uncertain.

## Executable boundary
This Skill is an **editorial transformation layer downstream of research**.
- Accept eligible Master Research / claim packages and explicit source material.
- Do not silently browse to repair weak evidence unless the caller explicitly asks for fresh research.
- Never upgrade confidence, remove material dissent, erase Unknowns, invent a source, fabricate first-person experience, or turn inference into fact.
- Do not approve publication, portfolio action, allocation, or distribution. Output is a draft.
- For time-sensitive claims, require an `as_of` date; if freshness is unknown, flag it.

Read `../../research/platform-playbook.md`, `../../research/benchmark-findings.md`, and `../../research/compliance-cn.md`.

## Input contract
Required: `master_research`, `platform`, `goal`, `audience`, `as_of`.
Optional: charts/tables/assets, prior published pieces, approved CTA, author identity + verified first-person facts, length/brand constraints.
If facts are missing, emit `RESEARCH_GAP` rather than imagining them.

## Method
1. **Extract the actual research journey:** starting hypothesis, evidence, contradictions, changed view, remaining questions.
2. **First-person integrity gate:** “我” may describe only a real research action/view in the input. Never invent trades, positions, meetings, calls, emotions, travel, access or biography.
3. **Lead with the change:** `我原来以为 X → 看了 Y 以后改成 Z`.
4. **Show receipts:** 2–5 decisive evidence cards/charts.
5. **Make Unknowns precise:** “还没想明白” must name the unresolved variable.
6. **Invite counterevidence**, not generic engagement bait.
7. **Adapt to platform** (Xiaohongshu/Weibo/Xueqiu defaults), then run compliance.

## Voice
- First-person, thoughtful, specific, lightly conversational.
- More research notebook than teacher.
- Admit changed views/dead ends without performative humility.
- If authorship is ambiguous, use “Waterline 研究笔记 / 我们在这轮研究里” rather than inventing a personal biography.

## Output contract
Return: `starting_view`; `what_changed`; 7 ranked `titles`; 3 `cover_text`; platform-native `post`; `receipts`; `still_unknown`; `next_questions`; `discussion_prompt`; `cta`; `compliance_flags`; `reuse_map`.

## Quality gate
Every first-person statement is grounded; change-of-mind specific; receipts visible; real Unknowns remain; sounds like a working researcher not guru; discussion can elicit counterevidence; no personalised buy/sell guidance.

## Research integrity
Internally classify claims as:
- `F` sourced fact
- `I` inference
- `H` hypothesis/scenario
- `U` unknown
Published wording must preserve those boundaries.

## Benchmark use
Use `../../research/benchmark-accounts/` to learn **mechanisms**, never to imitate a named creator’s distinctive style.

## Compliance
Follow `../../research/compliance-cn.md`. If the request crosses a hard default, return a bounded research/editorial alternative and flag `COMPLIANCE_REVIEW_REQUIRED`.

## Failure modes
Stop and flag if a key number lacks source/date; first-person experience is not in inputs; quote/scene cannot be verified; requested conclusion contradicts evidence; paid CTA depends on specific-security recommendation; or guaranteed-return language is requested.
