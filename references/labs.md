# Lab routing

Copy the needed directory from `assets/labs/` into the learner's `experiments/` before editing. Lab 05 includes its own app source; it does not depend on editing Lab 02. Labs 03 and the capstone reuse the image built in Lab 02.

| Lab | Prerequisite | Instructions |
|---|---|---|
| 00 Setup | None | [Setup](../assets/labs/00-setup/README.md) |
| 01 Containers | 00 | [Lifecycle and ports](../assets/labs/01-containers/README.md) |
| 02 Build | 01 | [Build an app](../assets/labs/02-build/README.md) |
| 03 Storage | 02 image built | [Persistence and restore](../assets/labs/03-storage/README.md) |
| 04 Network | 01 | [Container DNS](../assets/labs/04-network/README.md) |
| 05 Compose | 02–04 | [App and Redis](../assets/labs/05-compose/README.md) |
| Capstone | 00–05 | [Independent brief](../assets/labs/capstone/README.md) |

Commands are single-line and work in Bash and PowerShell unless a section is marked otherwise. Container `sh -c` strings run in the Linux container. Use a browser for HTTP checks, avoiding host curl alias differences. Check the current context first; if it points to a shared or production engine, stop lab execution and choose an authorized learning engine. On name or port collisions, inspect and choose a different lab name/host port; do not delete other workloads.

Expected observations are predictions. Save actual output in reports and explain differences. Image downloads require registry access. None of these labs require registry login, pushing an image, privileged mode or host socket access.
