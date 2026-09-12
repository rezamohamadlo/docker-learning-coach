# Lab 05 — App plus Redis

Run from this directory on the confirmed learning engine. Ensure host port 8080 is free and no other project uses dlc-compose. For a second learner use a distinct project with `docker compose -p dlc-yourname ...` consistently and edit the host port to an unused one.

```sh
docker compose config
docker compose up -d --build
docker compose ps
docker compose logs --tail 30
```

Open http://localhost:8080 twice and record visits; /health should return ok. The Python app is non-root with a read-only root filesystem. It uses Redis at `redis:6379`; Redis is not published to the host. Redis persistence uses a named volume and append-only writes. This unauthenticated, bounded learning stack is not a production deployment.

```sh
docker compose exec redis redis-cli GET dlc:visits
docker compose down
docker compose up -d
```

Expected: another page visit increases the prior counter. `down` retained the named volume. Record the actual result.

## Failure drills

1. Stop Redis with `docker compose stop redis`. Visit /health and /; expect 503 storage unavailable. Compare that with `docker compose ps` after health checks have run. Start Redis with `docker compose start redis` and confirm recovery. The app handles request errors; it is not a general-purpose resilient Redis client.
2. In your exercise copy, change REDIS_HOST to an invalid name, then `docker compose up -d`. Diagnose from config, health result and name resolution. Restore the service name and apply again.
3. Change only the published host port to 8081; apply and explain which URL changes and why Redis's address does not.

Do one drill at a time. Keep output as evidence. Restore the original configuration between drills.

## Cleanup

`docker compose down` removes this project's containers and network, keeping data. Only when intentionally discarding this lab's counter, use `docker compose down --volumes`; this deletes its declared data volume. Never replace this with a global prune.
