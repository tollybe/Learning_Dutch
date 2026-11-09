# How ChatGPT updates GitHub

**Implementation stage (2026-11-09):** Separate private repository created and verified; workflows and minimal event-format tools installed. A public → private README sync commit has been verified. No automatic capture of ChatGPT replies/views is enabled.

## Three distinct mechanisms

### 1. ChatGPT → private GitHub (event producer)

When a user **explicitly chooses** to record a learning interaction, an authorised ChatGPT/Codex/GitHub tool can create a new JSON file under `Learning_Dutch_Private/data/events/`. The message to save is a **small metadata record**, never the text of the conversation. The connected surface must support GitHub writes. If not, do not pretend a file was saved.

For example, after a reply the learner can say:

> Record this Dutch exercise to my private learning history.

The assistant should:
1. Confirm the private repository exists, is genuinely **Private**, and is authorised for the connected tool.
2. Summarise only evidence actually observed and approved for recording.
3. Create a uniquely named event file matching `schemas/telemetry-event.schema.json` in the private repository.
4. Never include raw learner text, personal details, user identity, comments from Daan, or inferred read receipts.
5. State whether the write succeeded and link to the committed file.

**A message shown by ChatGPT is not evidence of a view.** The chat product does not provide an accessible general-purpose read/open hook for this learning project.

### 2. GitHub Actions (event processor)

The private `learning-report.yml` workflow is triggered by a push to `data/events/**`, a manual dispatch or a weekly schedule. It:
- validates every JSON record, with strict allowed fields and type/event-source checks;
- generates `docs/LEARNING_ACTIVITY.md`, a private summary of *recorded* activities only;
- commits only that generated summary in the private repository;
- never touches the public repository.

This is a real **GitHub event-driven workflow**, unlike assuming ChatGPT can emit an automatic chat hook.

### 3. GitHub Actions → AI (optional, later)

A separate future private workflow can read only consented summaries and call an AI model through the OpenAI API, if the user opts in, adds an API key as an encrypted **GitHub Actions secret**, and accepts potential API costs. It would propose an adaptive study focus in a PR, not commit a proficiency label automatically.

**The OpenAI API does not automatically contain the user's ChatGPT conversations or scheduled-task replies.** Any events passed to it must come from a consented recording pipeline. Do not pass entire private chat exports to the workflow.

## Can a scheduled ChatGPT task commit every day?

Possibly, depending on the task's connected apps and write permissions. Treat this as **unverified** until a real scheduled run successfully writes to the private repository. The existing Sunday `Weekly Dutch Archive` task requests a GitHub README update; check actual repository changes rather than assuming the instruction guarantees a commit.

Recommended path:

1. **Now:** GitHub event validation + reporting and one-way public → private lesson mirror.
2. **Next:** Test the explicit ChatGPT instruction “record this exercise” against the private repository, with one deliberately non-sensitive sample.
3. **Only if tested and desired:** add a consented, low-frequency scheduled writer. Avoid extra daily prompts or manual steps.
4. **If fully automatic capture of every chat reply becomes essential:** build an explicit client/integration that can observe user-submitted events, gain separate consent, and send them to a private authenticated endpoint. GitHub Actions alone cannot provide ChatGPT read receipts.

## Security and privacy design

- Never put a private GitHub access token, webhook secret, or OpenAI API key in a public workflow, file or prompt.
- Do not add a cross-repository workflow that reads private data from the public repo.
- All writes remain constrained to one private repo, and the event schema rejects arbitrary fields.
- No engagement percentages, streaks, read-rate claims, alerts for gaps, or negative interpretations of missing activity.
- Review event retention before enabling collection: Git commits are historical and event deletion does not erase old commit objects.

## Hand-off prompt (for an authorised ChatGPT tool)

“When I explicitly ask to record a Dutch learning event, inspect `tollybe/Learning_Dutch_Private` and validate its privacy. Create only a minimal JSON file under `data/events/` that conforms to the private event schema. Treat missing responses as unknown and do not invent a read receipt. Never include message content or third-party details. If repository access, approval, or validation fails, report that nothing was saved.”

This prompt is a **behaviour specification**; it does not magically connect the ChatGPT UI to GitHub.
