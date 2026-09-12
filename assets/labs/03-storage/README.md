# Lab 03 — Persistence and a verified restore

Prerequisite: build dlc-counter:1 in Lab 02; its container is removed. Confirm the names below are unused or belong to this exercise. A fresh named volume receives /data's image directory ownership on first mount; reused volumes with other ownership may require investigation.

```sh
docker volume create dlc-data
docker run -d --name dlc-counter -p 127.0.0.1:8080:8080 --mount type=volume,src=dlc-data,dst=/data dlc-counter:1
```

Open http://localhost:8080 twice and record visits. Restart the container, then visit again. Next replace it:

```sh
docker stop dlc-counter
docker rm dlc-counter
docker run -d --name dlc-counter -p 127.0.0.1:8080:8080 --mount type=volume,src=dlc-data,dst=/data dlc-counter:1
```

Expected: another request continues the counter. Record actual output; compare with Lab 02. A volume is not an off-host backup.

## Stop, back up, restore into a separate volume

This uses a stopped SQLite app to make a consistent file copy. The backup volume is local exercise storage, not disaster protection. Use fresh dlc-backup and dlc-restored names so this does not overwrite an earlier backup.

```sh
docker stop dlc-counter
docker volume create dlc-backup
docker run --rm --mount type=volume,src=dlc-data,dst=/source,readonly --mount type=volume,src=dlc-backup,dst=/backup alpine:3.22 sh -c 'cd /source && tar czf /backup/data.tgz .'
docker volume create dlc-restored
docker run --rm --mount type=volume,src=dlc-backup,dst=/backup,readonly --mount type=volume,src=dlc-restored,dst=/restore alpine:3.22 sh -c 'cd /restore && tar xzf /backup/data.tgz'
docker run -d --name dlc-restore-check -p 127.0.0.1:8081:8080 --mount type=volume,src=dlc-restored,dst=/data dlc-counter:1
```

Open http://localhost:8081. Expected: previous saved value plus one. Record it, then:

```sh
docker stop dlc-restore-check
docker rm dlc-restore-check
docker rm dlc-counter
```

Data and backup volumes remain. Only if you intentionally want to delete all three lab datasets, run `docker volume rm dlc-data dlc-backup dlc-restored` after checking their contents are no longer needed.

## Bind-mount comparison

Create an index.html in a dedicated exercise directory. For Bash run `docker run --rm -d --name dlc-bind -p 127.0.0.1:8082:80 --mount "type=bind,src=$(pwd),dst=/usr/share/nginx/html,readonly" nginx:alpine` from that directory. In PowerShell replace `$(pwd)` with `$($PWD.Path)` in the same double-quoted mount argument. Visit http://localhost:8082, edit the host index.html, and refresh. Stop with `docker stop dlc-bind` (its --rm removes it). Explain why this read-only container mount still reflects host edits.
