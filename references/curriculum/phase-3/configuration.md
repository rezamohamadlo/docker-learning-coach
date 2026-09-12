# Runtime configuration and secrets

## Previous-note recap

Recall: Bridge networks and DNS. Connect that distinction to today’s observation.

## Mental model

Environment variables configure runtime behavior. Build ARG and runtime environment are different mechanisms. Secrets placed in an image or its history can persist; .env is a convenience file, not encryption.

## Guided practice

Set GREETING for Lab 02 at run time; recreate to change it. Explain the Compose environment section without putting credentials in reports.

## Independent evidence

Describe how you would supply a credential without committing it or baking it into an image.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

Environment variables configure runtime behavior.
