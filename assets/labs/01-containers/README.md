# Lab 01 — Container lifecycle and ports

On the confirmed learning engine, check `docker ps -a` for a name collision before creating `dlc-web`. These commands may download nginx.

```sh
docker run -d --name dlc-web -p 127.0.0.1:8080:80 nginx:alpine
docker ps
docker port dlc-web
docker logs dlc-web
docker exec dlc-web nginx -v
```

Open http://localhost:8080 on the Docker host. Expected: the nginx welcome page. Explain both port numbers and why another computer should not use this loopback-only mapping.

```sh
docker stop dlc-web
docker ps -a
docker start dlc-web
```

Expected: stopped container is visible in ps -a; start reuses it. Verify the page again. Now clean up only this lab:

```sh
docker stop dlc-web
docker rm dlc-web
```

Independent task: run a differently named container on host port 8081, show the mapping and explain the lifecycle without following the command list. Capture observations before removing your container. Keep images for later labs.
