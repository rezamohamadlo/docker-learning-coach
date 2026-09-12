# Listening and published ports

## Previous-note recap

Recall: Lifecycle, logs, and exec. Connect that distinction to today’s observation.

## Mental model

An application must listen on a reachable container interface. Publishing maps a host address and port to a container port. EXPOSE documents a port; it does not publish it.

## Guided practice

Use Lab 01 to identify host port 8080 and container port 80. Change only the host port after removing your own lab container.

## Independent evidence

Explain why -p 127.0.0.1:8081:80 and a process listening on container port 8080 do not match.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

An application must listen on a reachable container interface.
