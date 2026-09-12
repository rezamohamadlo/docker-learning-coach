# Startup versus readiness

## Previous-note recap

Recall: Compose services, networks, and volumes. Connect that distinction to today’s observation.

## Mental model

A process can be running before it can answer requests. A dependency health check with service_healthy gates initial Compose startup. Applications still need to handle later dependency failures. An unhealthy status alone is not an automatic restart policy.

## Guided practice

In Lab 05 stop redis, request /health, then start redis and retry. Compare running state, health status and HTTP result.

## Independent evidence

Explain why startup ordering does not guarantee a dependency will remain available.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

A process can be running before it can answer requests.
