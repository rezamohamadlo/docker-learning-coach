# Independent capstone — Durable learning service

Create a new exercise directory. Use Lab 02's app.py as application input, but write your own Dockerfile and Compose configuration. You may consult official documentation; record hints or copied configuration as assistance. Do not copy the full Lab 05 solution and claim independent construction.

## Acceptance criteria

- Build an image from a bounded context that excludes secrets and learner reports.
- Run the app as a non-root user and explain write permissions.
- Publish the app only on host loopback; use a named volume for /data with the SQLite variant, or a Redis service and its own persistent volume.
- Supply the greeting at runtime and show its value in an HTTP response.
- Provide a functioning health check; with Redis, distinguish dependency startup from later failure recovery.
- Demonstrate an increasing counter surviving container replacement.
- Introduce one wrong port/name/configuration, diagnose it using relevant observations, then fix it.
- Back up state consistently, restore to a separate target and verify the restored counter.
- Record the image identity, startup commands and data-preserving cleanup procedure so another learner can reproduce the result.

## Submission

Submit your Dockerfile, Compose file, .dockerignore, concise runbook, actual before/after outputs, and explanations for port, storage, identity and recovery choices. An unexecuted configuration can earn conceptual evidence; practical completion remains pending until observed on Docker.

## Coach evaluation

Assess each criterion separately. Run only authorized verification; coach-executed fixes are guided work. Ask one changed scenario after correction. Mark completion only with independent evidence; keep remaining gaps and schedule a later retention review.
