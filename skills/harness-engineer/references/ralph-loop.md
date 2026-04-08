# Ralph Loop Preset

Use the `ralph-loop` preset when the project should run as repeated, resumable passes over a queue of work.

## What the preset is for

The preset is for tasks where:

- the work naturally breaks into small, repeatable units
- each pass should advance exactly one unit or one bounded batch
- the agent may need fresh context between passes
- progress must survive interruption
- the worker should rely on files, not chat memory, to resume

Examples:

- batch enrichment or conversion jobs
- multi-feature implementation where each pass completes one feature
- long-running research collection with structured tasks
- migration or remediation work that progresses unit by unit

## What the preset creates

- a Ralph-style runner scaffold
- `PROMPT.md` for the worker contract
- `progress.txt` as resumable loop state
- `tasks.json` as mutable machine state
- `docs/exec-plans/current-batch-plan.md`
- `logs/` and `archives/` by default

## Core Ralph rules

- one pass advances one smallest verifiable unit
- the worker reads state from files first
- the loop only advances when validation passes
- completion is explicit, not guessed
- each pass leaves a clean restart surface

## Suggested state contract

- exit code `0`: unit complete, continue next pass later
- exit code `2`: all work complete
- nonzero exit: stop and inspect logs

Adjust the exact contract to the project if needed, but keep it simple and explicit.

## Task file shape

Use structured state for loop-owned tasks. A typical `tasks.json` entry includes:

- `id`
- `title`
- `status`
- `passes`
- `notes`

This lets the loop mutate task state safely without forcing the worker to rewrite large Markdown docs.

## Do not misuse the preset

- Do not use it for one-shot tasks that do not need a loop.
- Do not let one pass try to complete the whole project.
- Do not rely on the worker to remember prior chat context.
- Do not treat the prompt alone as the loop.
