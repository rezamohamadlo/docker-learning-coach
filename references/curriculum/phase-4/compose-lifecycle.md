# Recreation and persisted state

## Previous-note recap

Recall: Startup versus readiness. Connect that distinction to today’s observation.

## Mental model

A configuration change may need recreation. compose up applies the desired stack; restart reuses current containers. compose down removes the stack containers and network, retaining declared named volumes unless volume removal is requested.

## Guided practice

In Lab 05 increment twice, down, then up, and observe another increment. Record the actual volume name.

## Independent evidence

Describe a cleanup that keeps data and a separate explicitly intentional reset.

The coach should vary the assessment after guided practice. Explain your prediction before running a check; preserve actual output when runtime behavior is part of the outcome.

## Summary

A configuration change may need recreation.
