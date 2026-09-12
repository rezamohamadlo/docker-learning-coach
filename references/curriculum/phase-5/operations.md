# Resource limits and safer execution

## Previous-note recap

Recall: Diagnose from evidence. Connect that distinction to today’s observation.

## Mental model

Use a non-root application identity where possible and give only required filesystem writes. Read-only roots, dropped capabilities and memory limits can reduce exposure or bound resource use, but must be tested against application needs.

## Guided practice

Inspect the app USER and Compose restrictions. Observe docker stats --no-stream. Propose a memory limit, test it on your lab and explain how you would diagnose an OOM exit.

## Independent evidence

Explain why mounting the Docker socket undermines an ordinary unprivileged container boundary.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

Use a non-root application identity where possible and give only required filesystem writes.
