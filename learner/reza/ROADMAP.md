# Docker learning roadmap

Learner: Reza
Roadmap created (Jalali): 1405-06-22
Study start date (Jalali): 1405-06-22
Timezone: Asia/Tehran
Language: English
English preference: applies to both conversations and documents. B2–C1; use simple B2 wording, short sentences and clear examples. Explain new Docker terms. Avoid complex sentence structures and formal phrases.
Suggested duration: eight weeks, adjustable
Learning OS/shell: Windows / PowerShell (learner output). Docker client: 28.0.4. Selected context: desktop-linux. Engine now reachable: 28.0.4, linux/amd64, Docker Desktop 4.40.0 (187762), confirmed by learner output after an earlier connection failure. Compose: v2.34.0-desktop.1 (confirmed by learner). Docker info confirms Operating System: Docker Desktop; OSType: linux. Learner supplied successful hello-world download and run output on 1405-06-22; independent lab explanation pending.
Daily time budget: 20–30 minutes (normally 25)
Weekly rhythm: six small learning/practice sessions plus one review session
Learning preference: diagrams when useful; recap and summary every session; spaced retrieval
Schedule: On track as of 1405-06-22 — active sections started on time; no section is overdue. See Section dates for planned and actual dates.
Current position: Phase 0, session 1. Client and engine: guided checks completed; independent assessment pending.
Goal: Independently build, run, debug, persist and recover a small containerized application.

## Commands we learn

We add each new lesson command here with a short explanation. Seeing a command here does not mean you have mastered it.

| Command | What it does |
|---|---|
| `docker run --rm hello-world` | Creates and starts a small test container. Downloads its image if missing. Removes this container after it exits; keeps the image. |
| docker ps | Lists running containers on the selected engine. |
| `docker context show` | Shows the name of the selected Docker context. |
| `docker version` | Shows the client version and asks the engine for its version. A connection error means the engine could not be reached. |
| `docker info` | Shows details about the client and selected engine, including container counts and the engine operating system. |
| `docker compose version` | Shows the installed Compose version; this does not check whether the engine is reachable. |

## Phase 0: Environment

### Learn

- [ ] P0-environment: Client, engine, and context — Practiced; see [lesson note](notes/client-engine.md). Independent explanation pending.
- [ ] P0-shell-and-setup: Shell and installation readiness — Not started

### Build

- [ ] Verify client, server, context and Compose using Lab 00. — In progress: client, context and Linux engine confirmed; learner Compose/info checks and hello-world run complete; independent explanation pending.

### Exit criteria

- [ ] Independently explain/apply this phase and pass a fresh phase review — Not started

## Phase 1: Container foundations

### Learn

- [ ] P1-image-container: Image versus container — Not started
- [ ] P1-lifecycle: Lifecycle, logs, and exec — Not started
- [ ] P1-ports: Listening and published ports — Not started

### Build

- [ ] Run and inspect Lab 01; explain its port and lifecycle observations. — Not started

### Exit criteria

- [ ] Independently explain/apply this phase and pass a fresh phase review — Not started

## Phase 2: Building images

### Learn

- [ ] P2-dockerfile: Dockerfile and build context — Not started
- [ ] P2-cache: Layers and cache — Not started
- [ ] P2-image-hygiene: Image identity and multi-stage builds — Not started

### Build

- [ ] Build and recreate Lab 02 after changing source. — Not started

### Exit criteria

- [ ] Independently explain/apply this phase and pass a fresh phase review — Not started

## Phase 3: Storage and networking

### Learn

- [ ] P3-storage: Writable layers, bind mounts, and volumes — Not started
- [ ] P3-networks: Bridge networks and DNS — Not started
- [ ] P3-configuration: Runtime configuration and secrets — Not started

### Build

- [ ] Complete Labs 03 and 04; prove persistence and name resolution. — Not started

### Exit criteria

- [ ] Independently explain/apply this phase and pass a fresh phase review — Not started

## Phase 4: Docker Compose

### Learn

- [ ] P4-compose-model: Compose services, networks, and volumes — Not started
- [ ] P4-readiness: Startup versus readiness — Not started
- [ ] P4-compose-lifecycle: Recreation and persisted state — Not started

### Build

- [ ] Run Lab 05; prove readiness behavior and counter persistence. — Not started

### Exit criteria

- [ ] Independently explain/apply this phase and pass a fresh phase review — Not started

## Phase 5: Operations and capstone

### Learn

- [ ] P5-diagnosis: Diagnose from evidence — Not started
- [ ] P5-operations: Resource limits and safer execution — Not started
- [ ] P5-backup: Backup, restore, and release evidence — Not started
- [ ] P5-capstone: Independent capstone — Not started

### Build

- [ ] Complete a backup/restore and the independent capstone with observed evidence. — Not started

### Exit criteria

- [ ] Independently explain/apply this phase and pass a fresh phase review — Not started

## Weekly plan

Eight-week schedule begins on 1405-06-22. All dates use the Jalali calendar. The section table below sets the exact targets. Review work takes priority when time is short.

| Week | Proposed outcome | Due date (Jalali) | Actual evidence | Gap / next action |
|---|---|---|---|---|
| 1 | Environment verified; image/container distinction introduced | 1405-06-28 | Guided setup checks; context question answered | Finish Lab 00 and Phase 0 review |
| 2 | Lifecycle and ports demonstrated | 1405-07-04 | None | Lab 01 in daily slices |
| 3 | Dockerfile build and cache demonstrated | 1405-07-11 | None | Lab 02 in daily slices |
| 4 | Storage persistence and bind mounts demonstrated | 1405-07-18 | None | Lab 03 persistence slices |
| 5 | Network names and runtime config demonstrated | 1405-07-25 | None | Lab 04 and phase review |
| 6 | Compose, readiness and persistence demonstrated | 1405-08-02 | None | Lab 05 in daily slices |
| 7 | Diagnose failures; restore data; begin capstone | 1405-08-09 | None | Lab 03 restore plus design |
| 8 | Capstone runtime evidence and cumulative review | 1405-08-16 | None | Independent defense |

## Section dates

Calendar: Jalali (Solar Hijri), Asia/Tehran. Schedule set on 1405-06-22, using the recorded study start date. Daily budget: 20–30 minutes, usually 25. The plan ends on 1405-08-16. These are target dates, not guarantees.

Lessons and lab practice share the same daily time budget; overlapping rows do not mean extra sessions. Every seventh study session is a review. Keep day 28 for storage review and catch-up. No fixed time of day is required.

At each section start, record the actual start date and compare it with the planned start. At completion, record the actual finish date and compare it with the due date. Report the difference in calendar days: early, on time, or late. Keep finish dates blank until the required learning evidence is complete. Being late describes timing, not ability.

At each check, also report any unfinished section whose due date has passed. Keep original dates if we later change the plan; record the revised dates and reason separately. Study minutes are estimates unless the learner supplies actual time; chat time does not measure study time.

Current timing: On track as of 1405-06-22. The active lesson and Lab 00 started on their planned date, and no section is overdue. No section has a verified finish date yet. First target: P0-environment by 1405-06-23.

| Section | Planned start | Due date | Actual start | Actual finish | Current timing |
|---|---|---|---|---|---|
| P0-environment | 1405-06-22 | 1405-06-23 | 1405-06-22 | — | Started on time; 0 days difference |
| P0-shell-and-setup | 1405-06-24 | 1405-06-25 | — | — | Not started |
| P0-build: Lab 00 | 1405-06-22 | 1405-06-26 | 1405-06-22 | — | Run succeeded 1405-06-22, 4 days before due date; explanation pending |
| P0-review | 1405-06-27 | 1405-06-27 | — | — | Not started |
| P1-image-container | 1405-06-28 | 1405-06-28 | — | — | Not started |
| P1-lifecycle | 1405-06-29 | 1405-06-31 | — | — | Not started |
| P1-ports | 1405-07-01 | 1405-07-02 | — | — | Not started |
| P1-build: Lab 01 | 1405-06-29 | 1405-07-03 | — | — | Not started |
| P1-review | 1405-07-04 | 1405-07-04 | — | — | Not started |
| P2-dockerfile | 1405-07-05 | 1405-07-06 | — | — | Not started |
| P2-cache | 1405-07-07 | 1405-07-08 | — | — | Not started |
| P2-image-hygiene | 1405-07-09 | 1405-07-09 | — | — | Not started |
| P2-build: Lab 02 | 1405-07-05 | 1405-07-10 | — | — | Not started |
| P2-review | 1405-07-11 | 1405-07-11 | — | — | Not started |
| P3-storage | 1405-07-12 | 1405-07-17 | — | — | Not started |
| P3-networks | 1405-07-19 | 1405-07-21 | — | — | Not started |
| P3-configuration | 1405-07-22 | 1405-07-23 | — | — | Not started |
| P3-build: Labs 03 and 04 | 1405-07-12 | 1405-07-24 | — | — | Not started |
| P3-review | 1405-07-25 | 1405-07-25 | — | — | Not started |
| P4-compose-model | 1405-07-26 | 1405-07-27 | — | — | Not started |
| P4-readiness | 1405-07-28 | 1405-07-29 | — | — | Not started |
| P4-compose-lifecycle | 1405-07-30 | 1405-07-30 | — | — | Not started |
| P4-build: Lab 05 | 1405-07-26 | 1405-08-01 | — | — | Not started |
| P4-review | 1405-08-02 | 1405-08-02 | — | — | Not started |
| P5-diagnosis | 1405-08-03 | 1405-08-04 | — | — | Not started |
| P5-operations | 1405-08-05 | 1405-08-05 | — | — | Not started |
| P5-backup | 1405-08-06 | 1405-08-07 | — | — | Not started |
| P5-capstone | 1405-08-08 | 1405-08-14 | — | — | Not started |
| P5-build: restore and capstone | 1405-08-06 | 1405-08-15 | — | — | Not started |
| P5-review: final review | 1405-08-16 | 1405-08-16 | — | — | Not started |

## Review queue

| Topic | Last evidence date | Next review | Evidence link | Gap/status |
|---|---|---|---|---|

Default checkpoints: next session after introduction, about 7 and 21 days after demonstration; weekly consolidation every seventh session. No review is completed yet.

## Evidence log

| Date | Outcome | Evidence level | Report | Assistance / current gap |
|---|---|---|---|---|

## Current progress

All phases: Learn 0 completed; Build 0/1; Exit 0/1. Phase Learn totals: 2, 3, 3, 3, 3, 4. No retention evidence yet.

## Resume checkpoint

Session 1: [client and engine lesson](notes/client-engine.md) practiced with guided commands. Learner output now confirms desktop-linux and a reachable Linux engine. Context question answered correctly; explanation followed confirming coach feedback. Learner supplied successful `docker info` and Compose output. Learner attempted `docker run --rm hello-world`; missing local image, then registry request failed with EOF. Engine remains reachable; image-download cause is unknown. Retry succeeded on 1405-06-22: image downloaded and hello-world greeting printed. Earlier EOF cause remains unknown; no further troubleshooting needed. Learner correctly explained local-image reuse but said --rm removes the image. Correction provided: it removes the container. Two-run check showed container reuse confusion; after correction, learner correctly said container A no longer exists. Learner now correctly explained that another run creates a new container from the image. Correction loop complete; evidence remains Practiced after guidance. Next: shell and setup readiness, with a fresh image/container check next session and independent Phase 0 review still pending. Existing engine workloads are not course-created resources. Guided course container run completed; full independent assessment pending. Recheck context reasoning next session. See [first-session plan](plans/first-session.md).
