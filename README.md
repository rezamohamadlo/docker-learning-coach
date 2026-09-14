# Docker Learning Coach

A Docker counterpart to Reza's Agent Learning Coach: focused notes, practical exercises, independent assessments, a living roadmap, strengths/gaps, and retention reviews. It keeps the original English default, Jalali report dates, and `@#` maintenance convention. Docker progress begins at **Not started**.

## Start learning

Use the installed skill in a writable learning workspace:

> Use $docker-learning-coach to initialize my Docker roadmap and start Phase 0. First check my operating system, shell, and Docker setup.

To resume:

> Use $docker-learning-coach to continue my roadmap at learner/reza/ROADMAP.md.

To discuss without assessment:

> Use $docker-learning-coach to explain why localhost inside a container does not refer to my host.

The coach initializes learner files from `assets/`. If working from a downloaded project copy, keep it as your editable learning workspace and tell the coach its path. Linux-container labs work with Docker Desktop on Windows/macOS or Docker Engine plus Compose on Linux. See the official installation links in `references/sources.md`; do not install Docker inside the coach merely to run lessons.

## Your daily learning style

In both conversations and documents, the coach uses simple English for a B2–C1 learner: short sentences, familiar words and clear examples. New Docker terms get a brief explanation. Questions test Docker knowledge, not English grammar.

Sessions fit **20–30 minutes a day**, with a quick retrieval review, one visual explanation, one small practical step, and a concise closing summary. Diagrams clarify image/container relationships, ports, networks, storage and Compose. Large labs span multiple sessions. Every seventh session consolidates the week; spaced checks revisit topics the next session and roughly 7 and 21 days after demonstration. The roadmap tracks due reviews and exact resume checkpoints.

The roadmap includes a **Commands we learn** section. The coach adds each new lesson command with a short explanation, including useful new flags, so you can review commands in one place.

The personal roadmap records planned and actual section dates in the Jalali calendar. At each section start and finish, the coach reports whether it is early, on time or late, with the number of days. Timing and learning quality are reported separately. Updates happen during your learning conversations.

## Included learning path

| Phase | Suggested week | Outcome |
|---|---|---|
| 0: Environment | 1 | Verify client, engine, context, shell, and Compose |
| 1: Containers | 1–2 | Explain and control container lifecycle and ports |
| 2: Images | 3 | Build a Python service and reason about layers/cache |
| 3: Storage and networking | 4–5 | Prove persistence and service-name connectivity |
| 4: Compose | 6 | Run an application plus Redis with health checks |
| 5: Operations and capstone | 7–8 | Diagnose failures and independently containerize an app |

The eight-week timetable is a suggestion, not a deadline. Until a start date and due outcomes are agreed, schedule status is Unknown. The curriculum has 18 notes, six phase reviews, five guided labs, and an independent capstone brief. No paid API or model service is needed for the sample app; using an AI coach depends on your chosen agent environment.

## Structure

- `SKILL.md`, `agents/openai.yaml`: coach behavior and skill metadata.
- `references/`: coaching, reporting, retention review, lessons, lab routing, and official sources.
- `assets/`: blank roadmap, report and profile templates, and lab files.
- Your editable workspace's `learner/reza/`: created during first coaching use for notes, experiments, reports, and reviews. Personal state is separate from reusable curriculum; choose whether to track it in your own version control.

The lab application uses Python's standard library, SQLite for the single-container persistence lab, and Redis for the Compose counter. Working examples are teaching material. The coach assigns a different task for independent assessment. Read the relevant lab README before running commands; commands use bounded names and cleanup and retain data by default.

## Evidence and maintenance

Reading earns Introduced; guided practice earns Practiced; independent application with explanation earns Demonstrated. Retained requires a later fresh check. A correct multiple-choice guess does not establish practical skill. Each completion updates the roadmap, session report, and strengths/gaps. The coach resumes only when invoked; it does not monitor in the background.

Use `@# <change>` for coach maintenance. Review this README when behavior, setup, content, or structure changes. Derived from Agent Learning Coach, copyright Reza Mohamadlo; see LICENSE.

## Validation limits

The skill metadata, relative document links, configuration structure, and sample app are validated during creation. Docker is unavailable in the creation environment, so image builds, actual networking, volume permissions, and Compose execution require verification on your Docker machine. These are explicit learner lab checkpoints, not pre-recorded successes.
