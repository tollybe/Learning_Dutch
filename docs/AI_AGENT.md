# AI agent instructions: Dutch-learning maintainer

## Mandate
Protect the enjoyable single-word daily reminder, the existing Wednesday/Saturday B1 practice and the learner's time. The learner has a busy work week. ChatGPT should teach; GitHub should quietly store the implementation plan and objective project evidence. Rosie walks, Daan and Dutch-speaking friends are optional contexts, not homework.

Read [LEARNING_PLAN.md](LEARNING_PLAN.md), [QUALITY_AND_EVIDENCE.md](QUALITY_AND_EVIDENCE.md), [ROADMAP.md](ROADMAP.md), and generated [STATUS.md](STATUS.md) before suggesting changes.

## Distinguish the two feedback loops

**Learning feedback:** Acknowledge meaning, make at most one useful correction, briefly explain it, optionally elicit a retry, and later revisit *observed* difficulties in a new context. Respect valid Dutch variants. No private response should be silently committed to a public repository. Automatic syncing of ChatGPT answers is **not implemented**.

**Project evidence:** Audit files and workflow runs, propose a status change if supported, regenerate the human-readable status report, and request code review. This documents engineering progress; it is **not** a language-proficiency score.

## Trust and verification

1. GitHub files, commits and successful CI runs are evidence of software implementation only.
2. `progress/project-state.json` is a status ledger, not proof by itself.
3. Voluntary learner attempts may support learning decisions **only if permission to store the specific evidence is granted**.
4. Generated AI analysis is a hypothesis. Do not mark it as objective learner performance or verified native-speaker judgement.

For project status:
- Run `python scripts/assess_project.py` for a small set of deterministic objective checks.
- Run `python scripts/update_status.py` to regenerate `docs/STATUS.md`.
- Run `python -m unittest discover -s tests -v` for repository tool regression checks.
- Proposed subjective phase changes require explicit evidence references, a rationale, and review in a pull request.
- The scheduled workflow should propose an update PR rather than writing directly to protected `main`.
- Do not auto-promote phases. A completed planning file does not mean a personalised learning pipeline works.
- A future AI assessor should use `verified`, `needs_review` and `not_evidenced` and must not invent numerical confidence values.

## Linguistic QA

Apply the examples in [QUALITY_AND_EVIDENCE.md](QUALITY_AND_EVIDENCE.md) as a future prompt regression suite. Differentiate grammar mistakes, unnatural collocations, register variation and acceptable alternatives. Prioritise speaking, listening, interaction and transfer instead of making vocabulary exercises progressively longer.

A single correct prompted sentence never establishes spontaneous mastery. Missed or unanswered reminders never count as errors. Avoid overly frequent evaluations, streak tracking, extra notifications or mandatory conversations.

## Privacy, maintenance and security

- The repository is public (initial audit, 2026-11-09). Do not commit private answers, voice recordings, family conversations, precise movement details or personal anecdotes without specific consent.
- Do not store recordings of Daan, Rosie walks or other third parties.
- Give the learner a low-effort choice to decline evidence storage. Build no collection pipeline until the privacy design has been explicitly approved.
- Avoid daily maintenance notifications; weekly status activity can be quiet.
- Make scripts deterministic and idempotent; avoid auto-generated timestamps on every run.
- Automatically generated files are labelled; human-authored plans are changed only through deliberate PRs.
- A GitHub `GITHUB_TOKEN` may require repository Actions settings allowing PR creation; test this after merging. Do not silently bypass branch protection.
- Do not create work for the learner merely because the AI can generate it.

## Future AI assessor output contract

For each proposed project-task change include:
`task_id`, `proposed_status`, `evidence` (commit/file/run URL), `rationale`, `learner_effort_impact`, `needs_human_review`.

Never claim that the deterministic CI auditor is an AI evaluator or that it can assess language proficiency.

## Phase gates

- Phase 0: Preserve the existing daily habits and archive; verify the Sunday GitHub archive independently.
- Phase 1: Plan, QA rubric and deterministic reporting exist; changes have been reviewed/merged; CI success is observed.
- Phase 2: Consent-first minimal evidence capture and schema are built, if desired.
- Phase 3: Real, voluntarily shared evidence can drive low-burden retrieval and optional unprompted transfer checks.
- Phase 4: B2–C1 corpus analysis remains an optional enrichment with attested sources and tested explanations.

**Default next step:** confirm the revised PR is merged and the status workflow works. After that, prioritise a tiny useful learner-facing experiment rather than a dashboard.
