# Project Presets

Project presets answer a different question from loop presets.

- Loop presets answer: how should the harness run?
- Project presets answer: what kind of work is this harness for?

Use them together.

Examples:

- `--preset ralph-loop --project-preset batch-processing`
- `--preset baseline --project-preset repo-coding`

## generic

Use for task-agnostic scaffolds.

Adds:

- no extra structure beyond the baseline harness layout

## batch-processing

Use for:

- document conversion
- OCR
- content enrichment
- bulk transformation

Adds:

- `input/`
- `output/`
- `artifacts/`
- `batch-manifest.json`
- `docs/references/batch-contract.md`
- archives enabled by default

## repo-coding

Use for:

- feature-by-feature code work
- remediation loops
- long-running codebase tasks

Adds:

- `artifacts/`
- `docs/references/codebase-patterns.md`
- `docs/exec-plans/current-feature-plan.md`
- `features.json` enabled by default

## research-collection

Use for:

- source gathering
- evidence collection
- claim verification
- synthesis workflows

Adds:

- `sources/`
- `notes/`
- `findings/`
- `evidence/`
- `source-manifest.json`
- `docs/references/research-protocol.md`
- `findings/README.md`

## ui-validation

Use for:

- browser-visible feature work
- UI acceptance loops
- rendered state verification

Adds:

- `screenshots/`
- `traces/`
- `verdicts/`
- `verdicts/verdict.json`
- `docs/references/ui-validation.md`

## Selection rule

Pick the project preset that matches the dominant evidence shape of the task.

- If the task is about items moving through a pipeline, use `batch-processing`.
- If the task is about incremental code change, use `repo-coding`.
- If the task is about collecting and validating sources, use `research-collection`.
- If the task is about browser-visible behavior, use `ui-validation`.
