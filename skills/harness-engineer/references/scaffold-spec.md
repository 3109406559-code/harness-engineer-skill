# Scaffold Spec

This reference defines the baseline project skeleton the skill should produce or adapt.

## Required files

### `AGENTS.md`

Use as:

- entry map
- directory map
- behavior contract

Do not use as:

- exhaustive knowledge base
- long design document
- mutable run log

### `docs/`

Recommended subdirectories:

- `docs/product-specs/`
- `docs/design-docs/`
- `docs/exec-plans/`
- `docs/references/`

Purpose:

- product specs define what should exist
- design docs define how the harness is shaped
- exec plans define the current plan or batch
- references store durable doctrine and domain knowledge

### `progress.txt`

The operator-visible state file.

Must answer:

- where the loop is
- what has been completed
- what failed
- what remains
- when the last successful step happened

For Ralph-style loops, it should also answer:

- current iteration or current batch
- current task file in play
- last failure summary

### `config.yaml` or `config.json`

Use for stable configuration:

- paths
- batch size
- retry limits
- topology choice
- model or runtime hints

### `scripts/`

Minimum expectation:

- one runner entrypoint
- one validator entrypoint or validator module

Optional:

- initializer
- summarizer
- helper scripts

### `logs/`

Use for append-only operational evidence:

- run logs
- failure logs
- verdict artifacts
- browser traces or request snapshots when relevant

## Optional files

### `features.json` or `tasks.json`

Use when the loop advances across many discrete units.

Prefer structured state here when:

- items are machine-mutated
- pass/fail status changes over time
- dependency order matters

For Ralph-style loops, prefer `tasks.json` when the loop will mutate task status on every pass.

### `archives/`

Use when outputs should be snapshotted or preserved separately from the active workspace.

### `summary.txt`

Use when the harness should emit a final rollup after completion or fatal stop.

## File-role split

Use prose for:

- architecture
- rationale
- instructions
- stable knowledge

Use structured files for:

- mutable state
- checklists
- feature pass/fail fields
- manifests

## Scaffold defaults

Good defaults:

- `runner + worker + validator`
- progress file at repo root
- `docs/` with four subdirectories
- logs directory present from day one
- no evaluator unless justified

Ralph-specific defaults:

- `tasks.json` present from day one
- `PROMPT.md` dedicated to the worker
- `docs/exec-plans/current-batch-plan.md` instead of a generic current-plan file
- logs and archives enabled by default

## Minimum acceptance for a generated harness

The scaffold is not “done” unless:

- the directory tree exists
- the role of each generated file is clear
- the runner has a defined stop condition
- the progress file has an initial schema
- the validator has a place in the flow
- the project can be resumed from a fresh session without hidden memory
