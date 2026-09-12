# Image versus container

## Previous-note recap

Recall: Shell and installation readiness. Connect that distinction to today’s observation.

## Mental model

An image packages filesystem content and runtime defaults. A container is a created instance with its own writable layer and process configuration. Removing a container does not remove its image.

## Guided practice

Run Lab 01. Predict why a one-shot command exits while a server keeps running.

## Independent evidence

Explain how two containers from one image can hold different temporary files.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

An image packages filesystem content and runtime defaults.
