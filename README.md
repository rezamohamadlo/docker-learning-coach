# Docker Learning Coach

Docker Learning Coach is a visual-first, evidence-based learning workspace for building practical Docker skills in 20–30 minutes a day.

The project turns each short session into a repeatable loop:

```text
Visual recap → One concept → Small lab → Inspect the result → Summarize → Review
```

Reading alone does not count as mastery. A concept normally becomes **Demonstrated** when the learner can explain it, use it independently, and interpret the result.

## Daily session

Each session follows the same timebox:

| Time | Activity |
|---|---|
| 2–3 min | Recall yesterday's diagram or command |
| 5–7 min | Learn one concept through a diagram and short explanation |
| 10–15 min | Run one bounded hands-on lab and predict the result first |
| 3–5 min | Update a visual map and concise summary |
| 2 min | Answer one transfer question and record the next step |

Lessons should use Mermaid or ASCII diagrams, before/after views, command-to-result flows, and troubleshooting decision trees wherever useful.

## Repository layout

```text
docker-learning-coach/
├── SKILL.md
├── assets/
│   ├── daily-session-template.md
│   └── roadmap-template.md
├── references/curriculum/phase-1/
│   ├── overview.md
│   ├── image-container-model.md
│   ├── docker-run-lifecycle.md
│   └── filesystem-and-volumes.md
└── learner/
    └── reza/
        ├── ROADMAP.md
        ├── notes/
        ├── experiments/
        ├── reports/
        └── reviews/
```

Reusable curriculum lives under `references/`. Personal notes, lab output, progress, and review history belong under `learner/`.

## Getting started

1. Copy `assets/roadmap-template.md` to `learner/reza/ROADMAP.md`.
2. Set the start date and choose a 20–30 minute daily schedule.
3. Read `references/curriculum/phase-1/overview.md`.
4. Use `assets/daily-session-template.md` for each session.

The learner may use an AI coach with a request such as:

```text
Use $docker-learning-coach for today's 20-minute visual Docker session.
```

## Safety

Labs should use disposable images and clearly named resources. Never remove volumes, images, containers, or host files without explicit confirmation. Keep secrets out of notes and command history.

## License

MIT
