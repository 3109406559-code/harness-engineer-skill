# Harness Engineer

<p align="center">
  <img src="./assets/banner.svg" alt="Harness Engineer banner" width="100%">
</p>

<p align="center">
  <a href="./README.zh-CN.md"><strong>简体中文</strong></a>
</p>

<p align="center">
  <img alt="Type" src="https://img.shields.io/badge/Type-Codex%20Skill-0A7EA4">
  <img alt="Focus" src="https://img.shields.io/badge/Focus-Harness%20Engineering-1F9D55">
  <img alt="Ralph Loop" src="https://img.shields.io/badge/Ralph%20Loop-Preset%20Included-7C3AED">
  <img alt="Project Presets" src="https://img.shields.io/badge/Project%20Presets-4%20Families-F97316">
  <img alt="Built with Codex" src="https://img.shields.io/badge/Built%20with-Codex-10B981">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-EAB308">
</p>

<p align="center">
  <strong>Turn prompt-heavy workflows into recoverable, validator-first harness projects with loop presets, task-family presets, and upgrade-friendly doctrine.</strong>
</p>

<p align="center">
  <a href="#why-it-matters">Why it matters</a> ·
  <a href="#what-you-get">What you get</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#decision-model">Decision model</a> ·
  <a href="./CONTRIBUTING.md">Contributing</a> ·
  <a href="./ROADMAP.md">Roadmap</a> ·
  <a href="./RELEASING.md">Releasing</a>
</p>

## Why it matters

Most agent failures are not model failures. They are harness failures.

What breaks in practice:

- the task is too vague
- state lives only in chat memory
- the loop tries to do too much in one pass
- validation is weak or missing
- the scaffold is too generic to fit the actual work

`harness-engineer` exists to solve exactly that problem. It helps Codex design a harness before it starts improvising one.

## What you get

<table>
  <tr>
    <td width="25%">
      <strong>Doctrine Layer</strong><br>
      Practical harness engineering principles distilled from OpenAI, Anthropic, Ralph, OpenHarness, and hands-on local practice.
    </td>
    <td width="25%">
      <strong>Loop Presets</strong><br>
      Choose how the system runs: <code>baseline</code> for straightforward harnesses, <code>ralph-loop</code> for resumable multi-pass execution.
    </td>
    <td width="25%">
      <strong>Project Presets</strong><br>
      Choose what the work looks like: batch processing, repo coding, research collection, or UI validation.
    </td>
    <td width="25%">
      <strong>Scaffold Engine</strong><br>
      A modular Python generator that produces docs, progress state, manifests, validators, and runner placeholders.
    </td>
  </tr>
</table>

## Architecture poster

<p align="center">
  <img src="./assets/architecture-poster.svg" alt="Harness Engineer architecture poster" width="100%">
</p>

## Project status

- Current release: [`v0.1.3`](https://github.com/3109406559-code/harness-engineer-skill/releases/tag/v0.1.3)
- Stability: validated across loop presets, runner variants, and all current project presets
- Scope: one current skill, one historical snapshot, one modular scaffold engine
- Evolution model: doctrine first, scaffold second, trigger text last

## Quick start

### 1. Install the skill

<details>
<summary><strong>Windows PowerShell</strong></summary>

```powershell
Copy-Item -LiteralPath .\skills\harness-engineer -Destination "$HOME\.codex\skills\harness-engineer" -Recurse -Force
```

</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/harness-engineer ~/.codex/skills/harness-engineer
```

</details>

### 2. Invoke the skill explicitly

```text
Use $harness-engineer to clarify requirements and scaffold a robust harness project.
```

Typical prompts:

- `Use $harness-engineer to design a harness for a batch document-processing pipeline.`
- `Use $harness-engineer to refactor this prompt-only workflow into a recoverable harness.`
- `Use $harness-engineer to scaffold a Ralph Loop project for a multi-pass remediation task.`

## The decision model

The skill has two independent control surfaces.

### 1. Loop preset

This answers: **How should the harness run?**

| Loop preset | Use it when | Typical result |
|---|---|---|
| `baseline` | One scaffolded harness is enough and no repeated loop policy is needed yet | simple runner, validator, docs, progress file |
| `ralph-loop` | Work advances in repeated passes and must survive fresh-context restarts | `PROMPT.md`, `tasks.json`, batch plan, Ralph runner, loop contract |

### 2. Project preset

This answers: **What shape should this work take?**

| Project preset | Best for | Adds |
|---|---|---|
| `generic` | task-agnostic scaffolds | no extra overlays |
| `batch-processing` | OCR, conversion, enrichment, bulk transforms | `input/`, `output/`, `artifacts/`, batch manifest, batch contract |
| `repo-coding` | incremental codebase work | `features.json`, codebase patterns, current feature plan |
| `research-collection` | source gathering and evidence synthesis | `sources/`, `notes/`, `findings/`, `evidence/`, source manifest |
| `ui-validation` | browser-visible work | `screenshots/`, `traces/`, `verdicts/`, UI verdict template |

## Scaffold script

The skill ships with a modular scaffold engine:

[`skills/harness-engineer/scripts/init_harness_project.py`](./skills/harness-engineer/scripts/init_harness_project.py)

### Example: baseline

```powershell
python .\skills\harness-engineer\scripts\init_harness_project.py .\output --project-name "Example Harness"
```

### Example: Ralph Loop + batch processing

```powershell
python .\skills\harness-engineer\scripts\init_harness_project.py .\output --project-name "Example Ralph Batch" --preset ralph-loop --project-preset batch-processing --batch-size 5
```

### Useful flags

- `--preset baseline|ralph-loop`
- `--project-preset generic|batch-processing|repo-coding|research-collection|ui-validation`
- `--topology`
- `--runner`
- `--batch-size`
- `--with-features-file`
- `--with-failure-log`
- `--with-archives`

## What gets generated

### Baseline scaffold

- `AGENTS.md`
- `config.yaml`
- `progress.txt`
- `docs/`
- `scripts/`
- validator placeholder
- summary placeholder

### Ralph Loop scaffold

- baseline scaffold
- `PROMPT.md`
- `tasks.json`
- `docs/exec-plans/current-batch-plan.md`
- `logs/failure-log.jsonl`
- `archives/`
- Ralph-style runner placeholder

### Task-family overlays

- `batch-processing`: batch manifest, pipeline dirs, archive bias
- `repo-coding`: feature state, codebase patterns, current feature plan
- `research-collection`: source manifest, evidence dirs, findings docs
- `ui-validation`: verdict template, screenshot and trace dirs

## Repository anatomy

```text
harness-engineer-skill/
├── assets/                 # visual landing-page resources
├── skills/
│   └── harness-engineer/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/     # doctrine and decision rules
│       └── scripts/        # modular scaffold generator
├── snapshots/              # rollback and historical comparison
├── README.md
├── README.zh-CN.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── RELEASING.md
└── versions.json
```

## Included versions

| Version | Path | Notes |
|---|---|---|
| Current | [`skills/harness-engineer/`](./skills/harness-engineer/) | Active release with Ralph Loop and project presets |
| Snapshot | [`snapshots/harness-engineer-backup-20260408-161519/`](./snapshots/harness-engineer-backup-20260408-161519/) | Backup from before the Ralph preset upgrade |

## Design lineage

This repository is an original synthesis shaped by:

- OpenAI harness engineering ideas
- Anthropic articles on long-running harnesses
- `snarktank/ralph`
- `HKUDS/OpenHarness`
- distilled practitioner notes from real local use

It is not an official upstream release of any of those projects.

## Core thesis

> Better prompts help. Better harnesses survive.

The skill assumes:

- state should live in files, not chat memory
- validators matter more than optimistic self-reporting
- topology should stay as small as possible
- scaffolding should stay replaceable as models improve

## Validation

The current skill has been validated with:

- `quick_validate.py` against the skill itself
- Python compile checks for every scaffold module
- smoke tests for:
  - baseline scaffold generation
  - Ralph Loop scaffold generation
  - generated validator execution
  - generated Python, PowerShell, and Bash runners
  - all current project preset overlays

## Attribution

- Human project owner and curator: repository maintainer
- AI implementation and packaging support: OpenAI Codex

This repository uses explicit README attribution for Codex. If you also want Codex-like attribution inside commit metadata, use a dedicated co-author trailer or bot/account identity in future commits.

## Project maintenance

- Contribution guide: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Roadmap: [ROADMAP.md](./ROADMAP.md)
- Release process: [RELEASING.md](./RELEASING.md)

## License

MIT. See [LICENSE](./LICENSE).
