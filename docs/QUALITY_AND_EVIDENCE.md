# Linguistic quality and learning evidence

This is an **AI implementation guide**, not an extra task for the learner. The guiding question is whether Dutch becomes easier to use in ordinary life without increasing study pressure.

## Evidence ladder (descriptive, not scored)

| Label | Observation | What we must **not** conclude |
| --- | --- | --- |
| `exposed` | A word/structure appeared in a reminder or text | Learner understood or remembered it |
| `recognized` | Learner identified or understood it with context | They can produce it independently |
| `prompted_use` | Learner used the form while shown the target or prompted | They would select it spontaneously |
| `independent_use` | Learner chose the form appropriately without a visible cue | They retain it long-term |
| `delayed_transfer` | Learner independently used it later in a different context | Permanent mastery after a single occurrence |
| `insufficient_evidence` | No relevant attempt was provided or evidence is ambiguous | Failure, regression or disengagement |

Evidence must record the **task type, degree of prompting, context, feedback version and provenance** when consented. Never interpret output quality without those factors. AI-generated examples are not learner attempts.

## Feedback quality rubric

- **Meaning first:** Did the expression communicate the intended message?
- **Grammatical accuracy:** Identify genuine agreement, word-order, inflection or lexical errors; avoid inventing grammatical rules.
- **Naturalness and collocations:** Treat unnatural but comprehensible wording differently from incorrect Dutch.
- **Register and pragmatics:** A formal phrase may be appropriate in a complaint but odd while walking Rosie. Deliberately *bekakt* Dutch may be intentional.
- **Pronunciation and listening:** Without reliable acoustic evidence, do not assert a particular sound was pronounced correctly or incorrectly.
- **Source provenance:** Distinguish original article excerpts from model-generated examples; don't invent citations or cultural claims.
- **Feedback load:** Default to **one high-value correction**, with a brief reason. Invite one optional retry when helpful; honour “just chat”.

## Practical regression cases for future prompt changes

| Scenario | Expected behaviour |
| --- | --- |
| “Hoewel het was koud, gingen we wandelen.” | Identify subordinate-clause word order, optionally invite one retry |
| “Gisteren heb ik Rosie uitgelaten.” | Accept correct inversion; don't fabricate an error |
| A deliberately formal, grammatical complaint to a landlord | Explain register if useful, do not automatically rewrite as casual Dutch |
| An unanswered word reminder | No recorded error, obligation, or catch-up task |
| An old word reappearing in a new topic | Treat as retrieval opportunity, not duplicate-content failure |
| A Rosie-walk voice request | Give a screen-free oral task; stop if the context is distracting |
| User says “Let's just chat” | Do not switch back into constant correction |
| A native speaker and AI prefer different idioms | Treat acceptable variants fairly; ask for context rather than declaring one universally wrong |
| A prompt says “Score my mastery” with no actual learner attempt | Say there is insufficient evidence; don't assign a percentage |
| An article analysis asks for a cultural connection | Ground it in a source or explicitly mark as uncertain |

## Minimal future progress record (opt-in only)

A future implementation may record an abstract entry such as:

```json
{
  "concept_id": "grammar.nl.subordinate_word_order",
  "evidence_type": "prompted_use",
  "context": "short_written_reply",
  "issue_category": "word_order",
  "source": "learner_consented_summary",
  "verification": "needs_review"
}
```

Do not collect raw conversations by default. Do not log names of friends/family, location trails, voice data or full personal messages in this public repository. Store only after the learner deliberately opts in; provide an easy way to withhold or remove individual records before proposing any implementation.

## Success and stop rules

Success is the learner choosing to continue, using language in new situations and reporting real-world usefulness. Never equate a rising number of tracked items with proficiency. If optional checks or documentation add friction, keep only the daily word and short practice.

A future AI assessor can check repository files and tests; it **cannot** certify Dutch fluency from a project phase label. Human review is required for uncertain linguistic claims and any changes to personal progress evidence.
