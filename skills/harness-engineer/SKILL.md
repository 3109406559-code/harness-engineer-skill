---
name: "harness-engineer"
description: "Harness engineering for long-running or repeatable agent projects. Use when Codex needs to turn a recurring workflow, research loop, coding loop, batch-processing job, or high-stakes agent task into a durable harness project: clarify requirements first, choose a runner/worker/validator topology, scaffold AGENTS.md plus docs plus scripts plus progress and logs, refactor a prompt-only loop into a recoverable harness, or upgrade an existing harness with better observability, validation, and failure handling."
---

# Harness Engineer

Build harness projects that are recoverable, observable, and mechanically enforceable.

## Workflow

1. Decide whether the task should be harnessed at all.
   - Use this skill for long-running, repeatable, multi-step, high-stakes, or team-shared agent work.
   - Do not over-harness simple one-off tasks.

2. Clarify the execution contract before scaffolding.
   - Ask concise questions until these are clear: goal, inputs, outputs, success criteria, smallest unit of work, failure definition, validation method, runtime environment, human checkpoints, and whether the task is batch-oriented or feature-oriented.
   - Do not start creating files until the contract is specific enough that a validator could reject bad output.

3. Read the core references.
   - Read [references/principles.md](./references/principles.md) before making architecture decisions.
   - Read [references/topology-selection.md](./references/topology-selection.md) if the loop structure is unclear.
   - Read [references/scaffold-spec.md](./references/scaffold-spec.md) before creating the project skeleton.
   - Read [references/ralph-loop.md](./references/ralph-loop.md) when the user wants a Ralph-style long-running loop.
   - Read [references/project-presets.md](./references/project-presets.md) when the task shape matters more than the loop shape.
   - Read [references/upgrade-guide.md](./references/upgrade-guide.md) when evolving this skill or when the generated harness should be easy to extend or open-source.

4. Choose the smallest topology that can safely do the job.
   - Default to `runner + worker + validator`.
   - Add an initializer when environment bootstrapping or health checks are required before every run.
   - Add a planner when the task is too ambiguous or large to hand directly to a worker.
   - Add an evaluator or grader only when acceptance is subjective, high-risk, or clearly beyond a solo worker.
   - Require browser verification for UI or real web-flow tasks.

5. Scaffold the project.
   - Prefer running [scripts/init_harness_project.py](./scripts/init_harness_project.py) to create the baseline directory tree and placeholder files.
   - Use `--preset ralph-loop` when the project should advance by repeated loop passes with resumable state and a dedicated worker prompt.
   - Use `--project-preset` to bias the scaffold toward the task family: batch processing, repo coding, research collection, or UI validation.
   - After generation, replace placeholders with task-specific content instead of piling everything into `AGENTS.md`.
   - Keep `AGENTS.md` as a directory map and behavior contract, not a dumping ground.
   - Put durable knowledge in `docs/`, machine-written state in JSON or YAML when mutation matters, and operator-visible status in `progress.txt`.

6. Convert soft rules into mechanical checks.
   - Define what "done" means in ways a validator can test.
   - Add failure logs, retry limits, and clear stop conditions.
   - Prefer structured task files for mutable state (`features.json`, `tasks.json`, manifests) over prose-only state.
   - If the harness will run for many iterations, ensure each iteration ends in a clean restart state.

7. Validate the scaffold before handing it off.
   - Run the scaffolder on a temp directory.
   - Check that the expected files and directories exist.
   - Check that the generated files match the chosen topology.
   - If the harness includes validators or runners, smoke-test them immediately.

8. Leave upgrade room.
   - Keep doctrine in `references/` so future insights can be added without bloating this file.
   - Prefer replaceable components over deeply entangled automation.
   - Do not hardcode model-specific assumptions unless the task explicitly requires them.

## Core Rules

- Treat `progress.txt` or its equivalent as agent-readable state, not just a status report for humans.
- Treat every failure as design feedback: missing tool, missing doc, missing constraint, missing validator, or wrong task split.
- Keep the loop small: one feature, one batch, or one smallest verifiable unit per pass.
- Require a handoff artifact between sessions; never rely on conversational memory alone.
- Prefer explicit topology over magical prompts.
- Reduce harness complexity when newer model behavior makes a scaffold unnecessary.

## Script

Use the bundled scaffolder when you want a baseline project quickly:

```powershell
python /path/to/harness-engineer/scripts/init_harness_project.py <output-dir> --project-name "Example Harness"
```

Useful flags include:

- `--preset`
- `--project-preset`
- `--topology`
- `--runner`
- `--with-features-file`
- `--with-failure-log`
- `--with-archives`
- `--batch-size`

## References

- [references/principles.md](./references/principles.md): synthesized design doctrine from the source material
- [references/topology-selection.md](./references/topology-selection.md): choose runner and agent shape
- [references/scaffold-spec.md](./references/scaffold-spec.md): baseline project structure and file roles
- [references/ralph-loop.md](./references/ralph-loop.md): how and when to scaffold a Ralph-style loop
- [references/project-presets.md](./references/project-presets.md): task-family presets and what they add to the scaffold
- [references/upgrade-guide.md](./references/upgrade-guide.md): how to extend the skill and generated harnesses without breaking the core design
