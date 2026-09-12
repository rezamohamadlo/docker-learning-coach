# Bridge networks and DNS

## Previous-note recap

Recall: Writable layers, bind mounts, and volumes. Connect that distinction to today’s observation.

## Mental model

Containers on a user-defined bridge can resolve each other by name. localhost inside a container is that container. A service does not need a published host port for peers on its Docker network.

## Guided practice

Run Lab 04 and resolve dlc-web from a temporary client. Compare that with the Compose service name redis.

## Independent evidence

Diagnose why an app can reach a peer by service name but cannot use localhost for that peer.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

Containers on a user-defined bridge can resolve each other by name.
