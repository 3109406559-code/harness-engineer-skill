# Harness Engineer

<p align="center">
  <strong>A Codex skill for designing and scaffolding durable agent harness projects.</strong>
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img alt="Skill" src="https://img.shields.io/badge/Type-Codex%20Skill-0A7EA4">
  <img alt="Focus" src="https://img.shields.io/badge/Focus-Harness%20Engineering-1F9D55">
  <img alt="Loop" src="https://img.shields.io/badge/Ralph%20Preset-Included-7C3AED">
  <img alt="Built with Codex" src="https://img.shields.io/badge/Built%20with-Codex-10B981">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-EAB308">
</p>

## Why This Exists

`harness-engineer` is a reusable skill for turning long-running, repeatable, or high-stakes agent work into a real harness project.

Instead of relying on one giant prompt, it helps Codex:

- clarify the execution contract first
- choose the smallest safe topology
- scaffold a recoverable project structure
- separate durable docs from mutable machine state
- build validator-first loops
- generate Ralph-style loop skeletons when repeated passes are needed

This repository contains:

- the current `harness-engineer` skill
- an earlier backup snapshot from before the Ralph Loop preset was added

## What the Skill Covers

### Core harness engineering

- `AGENTS.md` as a directory map, not an encyclopedia
- `docs/` as the durable system of record
- `progress.txt` as resumable agent-readable state
- structured mutable state via `tasks.json` or `features.json`
- validators and mechanical checks over soft reminders
- upgrade-friendly scaffold design

### Ralph Loop support

The current skill includes an explicit `ralph-loop` preset that scaffolds:

- `PROMPT.md`
- `progress.txt`
- `tasks.json`
- `docs/exec-plans/current-batch-plan.md`
- `logs/failure-log.jsonl`
- `archives/`
- a Ralph-style runner template
- a matching validator

## Repository Layout

```text
harness-engineer-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── versions.json
├── skills/
│   └── harness-engineer/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── scripts/init_harness_project.py
└── snapshots/
    └── harness-engineer-backup-20260408-161519/
```

## Included Versions

| Version | Location | Notes |
|---|---|---|
| Current | [`skills/harness-engineer/`](./skills/harness-engineer/) | Includes the Ralph Loop preset |
| Snapshot | [`snapshots/harness-engineer-backup-20260408-161519/`](./snapshots/harness-engineer-backup-20260408-161519/) | Backup from before the Ralph Loop preset upgrade |

## Installation

Copy the current skill into your Codex skills directory.

### Windows PowerShell

```powershell
Copy-Item -LiteralPath .\skills\harness-engineer -Destination "$HOME\.codex\skills\harness-engineer" -Recurse -Force
```

### macOS / Linux

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/harness-engineer ~/.codex/skills/harness-engineer
```

## Quick Start

Once installed, invoke the skill explicitly when you want Codex to design a harness project:

```text
Use $harness-engineer to clarify requirements and scaffold a robust harness project.
```

Typical requests:

- “Use $harness-engineer to design a harness for a batch document-processing pipeline.”
- “Use $harness-engineer to refactor this prompt-only agent workflow into a recoverable harness.”
- “Use $harness-engineer to scaffold a Ralph Loop project for a multi-pass remediation task.”

## Scaffold Script

The skill includes a helper script:

[`skills/harness-engineer/scripts/init_harness_project.py`](./skills/harness-engineer/scripts/init_harness_project.py)

### Baseline scaffold

```powershell
python .\skills\harness-engineer\scripts\init_harness_project.py .\output --project-name "Example Harness"
```

### Ralph Loop scaffold

```powershell
python .\skills\harness-engineer\scripts\init_harness_project.py .\output --project-name "Example Ralph Harness" --preset ralph-loop
```

Useful flags:

- `--preset baseline|ralph-loop`
- `--topology`
- `--runner`
- `--batch-size`
- `--with-features-file`
- `--with-failure-log`
- `--with-archives`

## Design Sources

This skill was shaped by a synthesis of:

- OpenAI’s harness engineering article
- Anthropic’s long-running harness articles
- `snarktank/ralph`
- `HKUDS/OpenHarness`
- additional practitioner notes and distilled local doctrine

This repository is an original synthesis layer, not an official upstream release.

## Philosophy

> Better prompts help. Better harnesses survive.

The skill assumes:

- loops need externalized state
- validators matter more than optimistic self-reporting
- topology should stay as small as possible
- scaffolding should remain replaceable as models improve

## Attribution

- Human project owner and curator: repository maintainer
- AI implementation and packaging support: OpenAI Codex

This repository uses explicit README attribution for Codex. If you also want Codex-like attribution inside commit metadata, use a dedicated co-author trailer or bot/account identity in future commits.

## Validation

The current skill was validated with:

- `quick_validate.py` against `SKILL.md`
- Python compile checks for the scaffold script
- smoke tests for both:
  - baseline scaffold generation
  - Ralph Loop scaffold generation

## License

MIT. See [LICENSE](./LICENSE).
