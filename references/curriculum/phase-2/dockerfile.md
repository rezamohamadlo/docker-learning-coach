# Dockerfile and build context

## Previous-note recap

Recall: Listening and published ports. Connect that distinction to today’s observation.

## Mental model

A Dockerfile describes a build. COPY reads from its build context; WORKDIR sets subsequent paths. CMD supplies the default runtime command and USER selects its identity. The context should contain only required build inputs.

## Guided practice

Build Lab 02, read every Dockerfile instruction, and explain the .dockerignore.

## Independent evidence

Write a Dockerfile for the provided app from memory and explain each instruction.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

A Dockerfile describes a build.
