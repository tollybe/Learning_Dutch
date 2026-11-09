# Roadmap and checklist

**Source of truth for completion:** `progress/project-state.json`. The generated assessment lives in [STATUS.md](STATUS.md). Checkboxes below are the design backlog, not an automatically verified source of truth.

## Phase 0 — Preserve existing habits
- [x] Daily single-word routine is established externally.
- [x] Wednesday and Saturday B1 practices established externally.
- [x] README contains 56 numbered vocabulary words as checked 2026-11-09.
- [x] README has a weekly archive for 2–8 November 2026.
- [ ] Verify the Sunday archive automation reliably updates GitHub; the existing archive is not evidence that it always succeeds.
- [ ] Confirm that all reminders remain optional and lightweight.

## Phase 1 — Clear plan and maintainable documentation
- [x] Define sustainable habits, energy modes and use of native speakers.
- [x] Document AI agent workflow and guarded completion assessment.
- [x] Implement reproducible status reporting from structured project state.
- [ ] Review and merge this documentation proposal.
- [ ] Confirm privacy expectations before storing individual attempts.

## Phase 2 — Lightweight evidence capture (opt-in)
- [ ] Create stable concept IDs and a tiny format for voluntary responses.
- [ ] Add schema validation and test fixtures.
- [ ] Preserve existing README and avoid premature migration.
- [ ] Ensure skipped sessions remain valid and unpenalised.

## Phase 3 — Adaptation after evidence is available
- [ ] Review genuine, voluntarily submitted errors for recurring patterns.
- [ ] Offer delayed recall in small doses, without creating backlogs.
- [ ] Keep accuracy, naturalness, register and independent production separate.
- [ ] Evaluate whether personalisation improves learning without adding burden.

## Phase 4 — Optional B2/C1 analytical enrichment
- [ ] Version the linguistic decomposition prompt.
- [ ] Store article provenance and copyright-safe evidence.
- [ ] Test examples and explanations for idiomaticity and source fidelity.
- [ ] Generate presentation Markdown from structured records.

## Phase gates
Do not progress because a calendar date passed. Prioritise enjoyment, actual learner benefit, evidence of completion and manageable maintenance. If the process feels heavy, revert to one daily word.

## AI engineering to-do
- [x] Create an initial machine-readable plan status and generator.
- [x] Add scheduled status regeneration and objective repository-evidence audit, with no autonomous phase promotion.
- [ ] Verify the workflow actually runs successfully after merging.
- [ ] Create an optional AI assessor that reads commits, action runs and learning artefacts and proposes state updates in a PR with links to evidence.
- [ ] Require human review for any unverified or subjective progress claims.
- [ ] Add regression tests before changing exercise generation prompts.
