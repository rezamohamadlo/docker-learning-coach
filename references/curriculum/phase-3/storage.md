# Writable layers, bind mounts, and volumes

## Previous-note recap

Recall: Image identity and multi-stage builds. Connect that distinction to today’s observation.

## Mental model

The writable layer belongs to one container. A named volume has a separate lifetime. A bind mount exposes a chosen host path, useful for source editing. Mounts can hide files already at their destination.

## Guided practice

Run Lab 03 and compare restart with removal/recreation. Read the mounted SQLite counter after recreation.

## Independent evidence

Choose storage for editable source versus persistent application data and explain the tradeoff.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

The writable layer belongs to one container.
