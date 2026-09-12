# Image, Container, and Engine

## Mental model

```text
Dockerfile ──build──> Image ──run──> Container ──starts──> Process
                                      ↑
                                Docker Engine
```

An **image** is a packaged, read-only template. A **container** is a runnable instance created from an image. The Docker Engine manages the container lifecycle and isolation. A registry stores and distributes images; it is not the running container.

## Small lab

```powershell
docker pull hello-world
docker image ls hello-world
docker run --name dlc-session-01 hello-world
docker ps -a --filter name=dlc-session-01
```

Predict which command will show an image, which will create a container, and why the container may already be stopped.

## Review prompt

If two containers use the same image, are they the same container? Explain what is shared and what is separate.

## Summary

An image is a reusable template; a container is an instance; the Engine runs and manages instances; a registry distributes images.
