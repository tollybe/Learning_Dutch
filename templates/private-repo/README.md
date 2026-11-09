# Learning_Dutch_Private (starter)

This starter must be installed in a **private GitHub repository**. It contains **no personal data** and does not activate ChatGPT telemetry.

## What it does

Two private GitHub Actions workflows are provided. The public-material sync copies a strict allowlist of *public* teaching materials from `tollybe/Learning_Dutch` at `main` into `public_reference/`, on Monday morning UTC or on manual dispatch. The optional learning-report workflow validates event files in `data/events/` and regenerates a **private** activity summary whenever an authorised tool commits a consented event. Neither workflow exports private data to the public project.

## Setup

1. Create `tollybe/Learning_Dutch_Private` and verify its visibility is **Private**.
2. Install these starter files at the private repository root (an assistant with connected GitHub access can write them after the repo exists).
3. Run the `Sync approved public learning material` workflow using **Actions → Run workflow**.
4. Verify `public_reference/README.md` appears, and the GitHub Action commits to **this private repository**.
5. Review [docs/PRIVACY.md](docs/PRIVACY.md) before ever recording a learning event.

**Requirements:** Actions permission to write repository contents for the private sync job; no GitHub personal access token or third-party service. Repository branch protection may require converting the direct-copy job to a reviewed PR. The public learning project and its workflows never receive a credential for this private repository.

## Directories

- `public_reference/`: generated allowlisted copies of public lessons, safe to overwrite.
- `docs/PRIVACY.md`: privacy and evidence boundaries.
- `schemas/telemetry-event.schema.json`: future opt-in event format; no event capture process is enabled.
- `scripts/sync_public.py`: deterministic, non-networked text-file copier.
- `scripts/learning_events.py`: validates event files and creates a private summary without assigning a mastery score.
- `docs/LEARNING_ACTIVITY.md`: empty-by-default, generated private summary.

### How ChatGPT could write events

Once the GitHub app has **write** access to this private repository, the learner can explicitly request a minimal event commit. A supported ChatGPT/Codex tool creates a file such as `data/events/testevent_001.json`; the `learning-report.yml` workflow then validates records and updates `docs/LEARNING_ACTIVITY.md`. **This is not automatic observation of chat replies or message views.** A scheduled writer or a custom capture integration is a separate feature requiring verified tool access and consent. See the public project's `docs/CHATGPT_INTEGRATION.md`.

**No ChatGPT read receipts:** The ChatGPT task notification being generated does not tell us whether the message was opened. Never infer “viewed” or engagement from a task run.
