# Optional learning data policy

**Data collection status: OFF.** The initial private repository mirrors only already-public learning content.

Only add telemetry after explicit agreement about what to collect. Suggested abstract event types: `lesson_generated`, `lesson_acknowledged`, `exercise_responded`, `practice_self_reported`, and `delayed_transfer_reported`. An event should record only a day, pseudonymous lesson ID, approved source and type, and (where justified) a broad evidence category.

Do **not** record raw ChatGPT messages, third-party conversations, voice recordings, exact locations, health data, work activity, browsing data, notifications seen, typing patterns, IP addresses, or daily tracking gaps.

A `lesson_acknowledged` event must come from an intentional user action. There is no supported automatic ChatGPT `lesson_viewed` or open/read receipt here, and `lesson_generated` cannot imply it.

The repository is private to authorised users/apps, but Git preserves commit history: deleting a file does not erase previous committed versions. Avoid committing personal materials that may need complete erasure.

**Missing evidence is unknown, not negative performance.** No streaks, alerts for inactivity, additional reminders, or productivity scores. This is a learning aid, not behaviour monitoring.

Data never goes automatically from this repository to public GitHub. If a general teaching-method improvement is worth publishing, submit only a manually reviewed abstract recommendation without raw events or personal statistics.
