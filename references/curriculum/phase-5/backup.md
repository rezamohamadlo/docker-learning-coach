# Backup, restore, and release evidence

## Previous-note recap

Recall: Resource limits and safer execution. Connect that distinction to today’s observation.

## Mental model

Persistence is not backup. A useful backup must be restored and checked; a running database may need an application-aware consistency method. Record the image identity, configuration and data compatibility for rollback.

## Guided practice

Stop the single-container SQLite app, follow the scoped Lab 03 backup and restore steps, and verify the value on a separate restore volume.

## Independent evidence

Explain why an image rollback alone cannot reverse a database schema migration.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

Persistence is not backup.
