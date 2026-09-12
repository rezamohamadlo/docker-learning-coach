# Lab 04 — Name-based container communication

Make sure dlc-web from Lab 01 was removed. No host ports are published in this exercise.

```sh
docker network create dlc-net
docker run -d --name dlc-web --network dlc-net nginx:alpine
docker run --rm --network dlc-net alpine:3.22 wget -qO- http://dlc-web
```

Expected: nginx HTML, reached by container name. Explain why no -p is needed. Run a new temporary client on the default network without `--network dlc-net` and predict whether the custom-network name will resolve. Record the actual diagnostic.

```sh
docker network inspect dlc-net
docker stop dlc-web
docker rm dlc-web
docker network rm dlc-net
```

Independent evidence: explain where localhost points in the client and what network/DNS observation would distinguish a wrong name from a wrong port.
