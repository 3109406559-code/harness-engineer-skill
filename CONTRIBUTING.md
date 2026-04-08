# Contributing

Thanks for contributing to `harness-engineer`.

This project is small on purpose. Contributions should make the skill sharper, more durable, or easier to maintain without turning it into an overbuilt framework.

## What to contribute

Good contribution areas:

- better doctrine distilled from real harness practice
- improvements to the scaffold script
- clearer topology guidance
- stronger Ralph Loop defaults
- additional validation coverage
- README or bilingual documentation improvements

Avoid contributions that:

- add ceremony without evidence
- turn `AGENTS.md` guidance back into a giant handbook
- bake one project’s local quirks into universal doctrine
- add multi-agent complexity by default

## Repository structure

- `skills/harness-engineer/` is the current public skill
- `snapshots/` contains historical rollback points
- `README*.md` are repository-facing docs
- `versions.json` tracks the published current version and snapshots

## Preferred change order

When changing the skill, update in this order when possible:

1. doctrine in `references/`
2. scaffold logic in `scripts/init_harness_project.py`
3. skill workflow or trigger text in `SKILL.md`
4. repository docs

This keeps the core reasoning stable and avoids bloating the top-level skill file.

## Validation before opening a PR

Run these checks:

```powershell
python C:\Users\Seven\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\skills\harness-engineer
python C:\Users\Seven\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\snapshots\harness-engineer-backup-20260408-161519
python -m py_compile .\skills\harness-engineer\scripts\init_harness_project.py
```

Then smoke-test the scaffold script at least once for the path you changed:

- baseline scaffold
- Ralph Loop scaffold if the preset or loop docs changed

## Pull request guidance

Keep PRs narrow and explicit. Good PR summaries answer:

- what changed
- why it changed
- what was validated
- whether the current snapshot should remain unchanged

## Snapshot policy

Do not replace existing snapshots.

If a change meaningfully alters behavior, create a new snapshot rather than mutating an old one. Snapshots are part rollback point and part historical record.

## Attribution

README-level attribution for Codex is intentional. Do not remove it without a specific project decision.
