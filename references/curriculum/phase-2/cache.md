# Layers and cache

## Previous-note recap

Recall: Dockerfile and build context. Connect that distinction to today’s observation.

## Mental model

Build steps can reuse cached results when their inputs have not changed. A change invalidates dependent work. Building an image does not update a container already created from the old image.

## Guided practice

Rebuild Lab 02 twice, change the greeting default in app.py, rebuild, and recreate the container. Save actual cached/rebuilt steps.

## Independent evidence

Explain why changing app source should not require reinstalling unchanged dependencies in a larger project.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

Build steps can reuse cached results when their inputs have not changed.
