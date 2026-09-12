# Lab 02 — Build a Python counter

Run from this directory in your editable lab copy. No pip dependencies are needed.

```sh
docker build -t dlc-counter:1 .
docker run -d --name dlc-counter -p 127.0.0.1:8080:8080 -e GREETING="Learning Docker" dlc-counter:1
docker logs dlc-counter
```

Open http://localhost:8080 and refresh: visits should increase. Open /health: expect status ok. Explain build context, USER, CMD, EXPOSE and why the app binds to 0.0.0.0 inside the container. The counter lives in this container's writable /data directory for this lab.

```sh
docker image inspect dlc-counter:1
docker history dlc-counter:1
docker exec dlc-counter id
docker stop dlc-counter
docker rm dlc-counter
```

The image remains for Lab 03. A replacement without a volume starts a fresh database. Independent task: change the greeting default in app.py, rebuild and recreate without the GREETING override. Show the changed response and explain why rebuilding alone does not change an already running container. Clean up the replacement by its own name.
