# Lab 00 — Verify your environment

Goal: distinguish a client installation from a reachable engine. Record OS and shell first. Use Linux containers for this course. Choose installation instructions from [Docker](https://docs.docker.com/get-started/get-docker/) if needed; installation is a separate host change.

```sh
docker version
docker context show
docker info
docker compose version
```

Expected: client and server information, the intended learning context and a Compose version. Redact machine details before sharing. If only Client appears, inspect whether Docker Desktop/the engine is running and whether the context is correct; do not reinstall blindly. Permission denied and daemon unavailable are different observations.

Once the selected engine is confirmed and image downloads are acceptable:

```sh
docker run --rm hello-world
```

Expected: hello-world prints its message and exits. The temporary container is removed; the downloaded image remains. Completion requires the actual outputs and your explanation of which component each command verifies. No further cleanup is required.
