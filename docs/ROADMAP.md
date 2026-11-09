# Roadmap — learner benefit before engineering complexity

**The learner's commitment is already full.** All checklist items below are tasks for the AI/developer, not homework.

The authoritative project-task ledger is `progress/project-state.json`; `docs/STATUS.md` is generated. The checkboxes here are directional planning only. A verified *file* shows that a component exists, not that it works in production or improves Dutch.

## Phase 0 — Preserve the habit (current baseline)
- [x] Existing daily 08:00 single-word reminder.
- [x] Existing Wednesday and Saturday short B1 practice.
- [x] GitHub README contains 56 numbered vocabulary entries (inspected 2026-11-09).
- [x] GitHub README contains the 2–8 November 2026 weekly table.
- [ ] **Verify** that the Sunday GitHub archive automation continues to update the repository; an existing table is not proof of reliability.
- [ ] Check user experience: the reminder is still enjoyable, and missed days never accumulate work.

## Phase 1 — Small, trustworthy methodology and tools
- [x] Document workload limits and optional Rosie-walk mode.
- [x] Default to one useful correction and evidence-based adaptation.
- [x] Add expert-review safeguards: listening, interaction, retrieval, register and spontaneous transfer.
- [x] Document evidence ladder, feedback QA cases and privacy boundaries.
- [x] Add deterministic project evidence and status generation, with tests defined.
- [x] Define PR-based status refresh (no direct `main` write).
- [ ] Verify CI and automation run correctly **after** merging the PR.
- [ ] Review the plan with the learner before introducing personal evidence capture.

## Separate private repository and automation setup
- [x] Document the public/private visibility boundary and ChatGPT read-receipt limitations.
- [x] Prepare private-repo starter: one-way allowlisted public → private materials sync.
- [x] Prepare explicit-event writer contract, private commit-triggered report and tests.
- [ ] Create `tollybe/Learning_Dutch_Private` **as a private repository**; GitHub integration cannot create new repositories.
- [ ] Grant the connected GitHub app access to the new private repository.
- [ ] Install `templates/private-repo/` files into that private repository, verify its visibility and Actions permissions.
- [ ] Run and verify one-way sync; only **merged** public `main` material should be imported.
- [ ] Test a deliberately non-sensitive example event after explicitly approving it.
- [ ] Verify a private event commit triggers the learning report workflow.
- [ ] Only then consider a scheduled ChatGPT task to propose/commit approved event summaries; do not assume read/open tracking exists.
- [ ] Keep any private → public insight sharing manual, anonymised and reviewed.

## Phase 2 — Tiny, consent-first evidence capture (optional)
- [ ] Define a minimal, stable concept identifier and evidence schema.
- [ ] Ask whether **any** abstract feedback should be recorded; default to no logging.
- [ ] Validate JSON and strip names, stories, conversations and voice transcripts.
- [ ] Capture prompted vs independent vs delayed use without treating silence as failure.
- [ ] Pilot with a small number of voluntarily provided examples, then evaluate burden before expanding.

## Phase 3 — Adaptation and real-life transfer
- [ ] Revisit known vocabulary naturally inside the existing word schedule; do not add reminders.
- [ ] Prioritise patterns supported by repeated evidence, not one AI correction.
- [ ] Offer a **voluntary**, unprompted 1-minute conversation check every few weeks at most, not a new recurring notification.
- [ ] Compare qualitative usefulness and enjoyment, not streaks or raw word counts.
- [ ] Allow a quick “no correction today” mode.

## Phase 4 — Optional deeper B2/C1 analysis
- [ ] Version the long-form article decomposition prompt.
- [ ] Keep source evidence and copyright constraints.
- [ ] Test idiomaticity and alternative registers before presenting absolute corrections.
- [ ] Only build advanced reporting if it leads to a meaningful learner benefit.

## Phase gates (do not auto-promote)
- **0 → 1:** Existing experience protected, archive behaviour checked.
- **1 → 2:** Plan and tooling merged, CI passes, user consents to any learning-data collection.
- **2 → 3:** A small set of real consented examples exists and produces useful advice without extra workload.
- **3 → 4:** Learner explicitly wants more advanced analysis and simpler options have been tried.

When two phases have incomplete dependencies, the status remains **not evidenced** even if implementation files exist.

## AI engineering to-do (not for the learner)
- [x] Add project-status generator, deterministic evidence auditor and basic regression tests.
- [x] Make status updates reviewable pull requests instead of direct writes to `main`.
- [ ] Verify the first CI run and repository permission for bot-created PRs.
- [ ] Verify the existing weekly vocabulary archive separately.
- [ ] Later, optionally implement an AI project assessor that links evidence to proposed task changes in a PR, with human review.
- [ ] Later, optionally add consent-first progress records and prompt regression tests for Dutch-language feedback.

## Decision rule for new features

Only proceed if it demonstrably supports **sustainability → real-world transfer → accuracy**, without adding more learner-facing reminders or making GitHub a daily task. Prefer removing a burden to collecting more data.
