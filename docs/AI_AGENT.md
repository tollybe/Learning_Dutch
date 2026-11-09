# AI agent instructions: Dutch learning maintainer

## Objective
Reduce learner workload. Protect the single daily word and existing Wednesday/Saturday practice. Never introduce more mandatory studying or turn Rosie walks, Daan or family time into obligations.

## Inputs in order of trust
1. The repository's actual files, commits and workflow runs.
2. `progress/project-state.json` (tracked declarations with evidence paths).
3. Voluntary learner submissions (only with explicit consent for storage).
4. Generated explanations and AI assessments (hypotheses; not verified learning).

Read [LEARNING_PLAN.md](LEARNING_PLAN.md), [ROADMAP.md](ROADMAP.md), and generated [STATUS.md](STATUS.md) before proposing changes.

## Phase assessment and auto-updates
- Run `python scripts/update_status.py --check` to detect stale generated documentation.
- The automation refreshes `docs/STATUS.md` using deterministic structured data; it does **not** call a language model or claim learning improvement.
- To change project-state flags, verify the corresponding repository evidence first, update the JSON in a PR, and include a rationale and links. Do not mark tasks completed from plan text alone.
- A future AI assessor may compare roadmap tasks with files, commits, test outcomes and workflow runs; it must label findings `verified`, `needs_review` or `not_evidenced`. It should create a PR for review, not silently edit `main`.
- Automatic phase progression is forbidden; next-phase suggestions are advisory and must consider user effort.

## Privacy, workload and quality guardrails
- The repository was public on 2026-11-09: do not commit private dialogues, voice transcripts, health details, identifiable third-party anecdotes or unapproved exercise answers.
- Never store recordings of Daan, Rosie walks, family, or friends.
- Do not set an arbitrary streak, completion quota or alert on inactivity.
- Never interpret lack of logged attempts as lack of learning.
- Avoid daily AI maintenance messages; weekly status regeneration can run silently.
- Prefer one small proposed task per pull request with an explicit workload/benefit rationale.
- Make changes idempotent; keep machine-generated files clearly marked and never overwrite hand-authored plan docs.
- Treat long-form B2/C1 analysis as optional enrichment and verify source excerpts rather than inventing attestations.

## AI assessor output contract (future implementation)
For each task: `task_id`, `proposed_status`, `evidence` (file path or commit URL), `confidence_rationale`, `learner_effort`, `needs_human_review`. Do not use an arbitrary numeric confidence percentage as a factual reliability measure.

## Phase transition criteria
Phase 0: Preserve reminders and existing archive.
Phase 1: Documents and automated report exist and have been reviewed/merged; workflow run verified.
Phase 2: Opt-in capture is implemented and privacy-checked.
Phase 3: Real feedback evidence exists and the learner wants adaptation.
Phase 4: Optional corpus methodology passes quality checks and is explicitly desired.

## Next recommended action
Review the documentation PR and verify that the weekly archive still works. Do not ask the learner for daily admin.
