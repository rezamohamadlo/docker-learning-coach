# Compose services, networks, and volumes

## Previous-note recap

Recall: Runtime configuration and secrets. Connect that distinction to today’s observation.

## Mental model

A Compose file declares a related application stack. Services describe containers, and project names scope generated resources. The project network provides service discovery. Use docker compose config to validate the resolved configuration.

## Guided practice

Read and run Lab 05. Match app, redis, the default network and redis-data to their purpose.

## Independent evidence

Reconstruct a two-service Compose file using the supplied app and explain each relationship.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

A Compose file declares a related application stack.
