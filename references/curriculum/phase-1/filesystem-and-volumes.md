# Writable Layers and Volumes

## Previous-note recap

Image: read-only template; container: isolated instance; lifecycle: created, running, stopped, removed.

## Visual model

```text
Image layers (read-only)
          +
Container writable layer (temporary)
          +
Named volume (outside container lifecycle)
```

Changes written inside a container's writable layer disappear when the container is removed. A **named volume** is Docker-managed persistent storage and can be mounted into more than one container when appropriate. A bind mount maps a specific host path and therefore needs extra care.

## Small lab

```powershell
docker volume create dlc-session-03-data
docker run --rm --mount source=dlc-session-03-data,target=/data alpine sh -c "echo saved > /data/message.txt"
docker run --rm --mount source=dlc-session-03-data,target=/data alpine cat /data/message.txt
docker volume rm dlc-session-03-data
```

Predict why the second container can read a file created by the first, even though the first container was removed automatically.

## Summary

Container writable-layer data is temporary; named volumes preserve data beyond a container and should be removed deliberately.
