# Lifecycle, logs, and exec

## Previous-note recap

Recall: Image versus container. Connect that distinction to today’s observation.

## Mental model

docker run creates and starts a new container. start reuses a stopped one. ps shows running containers; ps -a includes stopped ones. logs reads the application output; exec starts another process only in a running container.

## Guided practice

Inspect Lab 01 with ps -a, logs and inspect. Stop and start its server.

## Independent evidence

Choose evidence that distinguishes a normal exit from a crash.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

docker run creates and starts a new container.
