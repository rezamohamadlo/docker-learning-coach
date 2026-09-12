# Image identity and multi-stage builds

## Previous-note recap

Recall: Layers and cache. Connect that distinction to today’s observation.

## Mental model

Tags are movable names. A digest identifies image content. Reproducibility also requires controlled dependencies and build inputs. A multi-stage build can leave compilers in a build stage and copy only runtime artifacts into the final stage.

## Guided practice

Inspect the Lab 02 image ID, tag and history. Design a two-stage compiled-app build on paper; explain why this standard-library Python example does not need a compiler stage.

## Independent evidence

Explain why a small image can still contain a vulnerable dependency, and how you would identify the exact image tested.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

Tags are movable names.
