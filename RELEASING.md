# Releasing

This repository uses lightweight, explicit releases.

## Release principles

- Prefer small, intelligible releases over large rewrites
- Keep snapshots immutable once published
- Update doctrine before changing public workflow claims
- Release only after both baseline and Ralph Loop paths still validate

## Versioning

Use simple semantic-ish tags:

- `v0.x.y` while the project is still evolving quickly
- bump:
  - patch for doc or small scaffold fixes
  - minor for meaningful scaffold or doctrine improvements
  - major only if the skill’s public behavior changes in a breaking way

## Release checklist

1. Validate the current skill:

```powershell
python C:\Users\Seven\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\skills\harness-engineer
```

2. Validate any included snapshots that remain public.
3. Compile-check the scaffold script.
4. Smoke-test:
   - baseline scaffold
   - Ralph Loop scaffold if the preset or runner logic changed
5. Update:
   - `README.md`
   - `README.zh-CN.md`
   - `versions.json`
   - `ROADMAP.md` if priorities changed
6. Create a release note that explains:
   - what changed
   - whether doctrine, scaffold logic, or both changed
   - whether a new snapshot was added

## When to cut a snapshot

Create a new snapshot when:

- the scaffold behavior changes materially
- the Ralph Loop preset meaningfully changes shape
- a rollback point would be useful for users or maintainers

Do not create snapshots for every tiny README edit.

## GitHub metadata

Keep these areas in sync with the actual repository:

- description
- homepage
- topics
- latest release notes

Recommended topics:

- `codex`
- `codex-skill`
- `harness-engineering`
- `ai-agents`
- `ralph-loop`
- `scaffolding`
- `long-running-agents`
