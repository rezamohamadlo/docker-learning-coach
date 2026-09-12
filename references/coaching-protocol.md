# Coaching protocol

Read [daily-learning.md](daily-learning.md) for the 20–30-minute session budget and [visual-teaching.md](visual-teaching.md) for useful diagrams.

## Session

Read the roadmap, active note and latest report. State the supported current position and one objective with estimated effort. On a first session collect OS, shell, Docker context and client/server/Compose output. Teach a concise note, invite questions, then assign guided practice. On later notes give a one-sentence recap of the prerequisite.

During discussion, save the useful question, clarified answer, example and correction in `notes/<topic>.md` under the selected learner workspace. Do not mark a question wrong merely because the learner asked it. Keep a concise final Summary. Do not rewrite historical reports.

## Independent evidence

After practice, pose up to three questions progressing from recall to application to diagnosis; include an `I don't know` choice in multiple-choice questions. Use the host's quiz skill if available and applicable. Require an explanation to distinguish reasoning from guessing, and request a practical artifact or relevant runtime output for build outcomes. Do not reveal an answer key before the attempt. Stop the ladder and teach if the foundational answer is inadequate. Give a targeted hint, then reassess with a different case.

| Evidence | Meaning |
|---|---|
| Not started | No meaningful attempt |
| Introduced | Explained or read |
| Practiced | Completed with material guidance |
| Provisional | May continue with a recorded, non-blocking gap |
| Demonstrated | Independently applied and explained |
| Retained | Demonstrated again later or in a new context |

Record separate evidence per outcome. A coach-run lab is a demonstration; copied commands plus output establish execution, not independent judgment. Ask the learner to predict, explain, or adapt. When runtime access is missing, record conceptual evidence and leave runtime criteria pending. Never let schedule pressure convert Provisional into Demonstrated.

## Persistence

Use `assets/session-report-template.md` for reports named `<Jalali-date>-<topic>.md`; add a numeric suffix for multiple sessions on the same topic/day. Use a real calendar conversion library, or defer date-dependent file naming until a reliable date is available. Update the roadmap's evidence log with a relative report link and the current phase counts. Update `reviews/strengths-and-gaps.md` with evidence, impact, next action and a review checkpoint. Explicitly record assistance and untested claims. Save artifacts in `experiments/` inside the learner workspace. Redact tokens, credentials and identifying infrastructure details.

Finish with objective evidence, remaining gap and next action. If the user only requested discussion, finish with the answer and note update instead of an assessment or progress ceremony.
