# Two-repository learning architecture and optional telemetry

## Status (2026-11-09)

**Proposed architecture; no personal telemetry collection is enabled.**

- **Public**: `tollybe/Learning_Dutch` — lessons, vocabulary, strategies, prompts, regression tests and anonymised design decisions.
- **Private (to create)**: `tollybe/Learning_Dutch_Private` — optional, consented engagement/learning evidence and an automatically refreshed **copy of approved public material**.
- Visibility is repository-wide. A “private branch” inside the public repository is **not private**.
- The connected GitHub integration can modify existing repositories but cannot create a new repository, so the owner must create the private repository with visibility **Private** before these templates can be installed.

## Direction of sync

```text
Learning_Dutch [PUBLIC]
  README.md + allowlisted public docs
                 |
                 | GitHub Actions, weekly/manual; read-only checkout
                 v
Learning_Dutch_Private [PRIVATE]
  public_reference/       <--- public mirror, overwritten safely
  data/                   <--- optional private telemetry, NEVER exported
  docs/                   <--- private privacy policy
```

The **only automatic direction is public → private**. The private workflow copies specific, approved public text files. It never checks out or pushes private data to the public repository, and never runs code from the public checkout.

Private → public is **not automatic**. If a private learning insight improves our teaching methodology, propose a short, manually reviewed and explicitly approved *generalised lesson-design change* in the public PR. Do not export raw events, timestamps, individual responses, voice transcripts, statistics about the learner's schedule or third-party information.

## What we can actually observe

| Event | Possible evidence | Supported today? |
| --- | --- | --- |
| Scheduled lesson generated | Task run metadata, where accessible | Potentially; depends on the connected scheduling tool |
| Lesson notification delivered | Provider delivery receipts, if exposed | Not guaranteed |
| ChatGPT message opened/read | Reliable client open/read event | **No accessible read receipt** — never infer one |
| Explicit acknowledgement | User consciously clicks an action or replies “seen” | Only if explicitly implemented and captured; not equivalent to learning |
| Exercise response | Learner's submitted message | Available to the tutor in conversation; automatic private GitHub export **not implemented** |
| Independent language use | Optional learner statement or authentic unprompted example | Self-report or explicitly consented evidence only |

Do not substitute message creation, notification delivery or an absence of replies for “opened/read”. Do not install tracking pixels, link shorteners or surreptitious tracking.

## Proposed minimal telemetry vocabulary (future, opt-in)

Only these abstract events are eligible for the private repository's schema: `lesson_generated`, `lesson_acknowledged`, `exercise_responded`, `practice_self_reported`, `delayed_transfer_reported`.

- A **view** is deliberately **not** an event in the schema until there is a genuine, consented source.
- Default: **no events collected**. Nothing here activates telemetry.
- Prefer day-level dates, pseudonymous lesson IDs and categories. No raw message, conversation title, names, full IP addresses, location traces, identifiable third-party anecdotes, voice recording or text of spoken replies.
- Event absence is **missing information**, never “did not study” or “failed”.
- Git retains history, so even deleting an event file does not guarantee removal from past commits. Do not use GitHub as a confidential diary.
- The private repo is accessible to the GitHub account, explicitly authorised collaborators and connected apps with access. “Private” is not end-to-end encryption.

## The lightest viable dashboard

Do not surface daily “read rates”, streak counts or attention metrics. A weekly/private optional recap could separate:
1. **Lessons generated** (delivery operations, if verified),
2. **Voluntary responses** (only if consented),
3. **Known recall/transfer evidence** (not a proficiency percentage),
4. **Unknown engagement** (not a zero score).

A quiet period should prompt **no notification**. The tutor should keep offering the same small daily opportunity.

## Private repository bootstrap (one manual step)

1. Create `tollybe/Learning_Dutch_Private` in GitHub and set **Private** (not Public).
2. Make sure the connected GitHub app has access to that repository; installation access may need to be expanded.
3. Copy the prepared `templates/private-repo/` files into the private repository root. This can be done by the assistant after it can access the newly created repository.
4. Enable GitHub Actions and verify the repository is still **Private**.
5. Run the private `Sync approved public learning material` workflow manually once; then review `public_reference/`.
6. The workflow is scheduled Monday 04:10 UTC (after the existing Sunday archive), but may run late due to GitHub scheduling. It only imports **merged public `main`**, not drafts or PRs.

The template uses the private repo's own `GITHUB_TOKEN` with `contents: write` to commit **allowlisted public material only to the private repository**. It requires no personal access token and grants no private-repository token to the public repository.

If private branch protection blocks direct commits, change this importer to create a reviewable private PR rather than removing protections. This does not change the separate public project-status PR workflow.

## Next implementation phases

- [x] Design directional sync and private telemetry policy.
- [x] Publish a reusable private-repository starter and tests in the **public** plan repo; no real personal data.
- [ ] Create and verify `Learning_Dutch_Private` with private visibility (owner step; GitHub connector cannot create repositories).
- [ ] Install the starter files in that existing private repository.
- [ ] Run and verify first public → private import; confirm privacy boundary.
- [ ] Explicitly agree what, if anything, can be logged about ChatGPT usage.
- [ ] Implement **consented** response/acknowledgement capture through a supported integration. Read receipts are not available from the current ChatGPT workflow.
- [ ] Optional: privately summarise evidenced difficulties, without generating additional homework.

## Design decision

**The private repo is a one-way learning mirror and optional evidence store, not a telemetry surveillance project.** The primary goal remains enjoying one Dutch word a day and transferring it into ordinary spoken language.
