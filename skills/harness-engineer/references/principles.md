# Harness Engineering Principles

This file captures the stable doctrine behind the skill. Update this file first when new ideas arrive; only update `SKILL.md` when trigger logic or core workflow changes.

## 1. Harness and loop are different things

- The harness is the surrounding system: tools, files, permissions, logs, memory, validators, and scaffolding.
- The loop is the execution policy layered on top: Ralph-style iteration, batch progression, feature progression, or any other repeatable run cycle.
- Do not confuse a repeated prompt with a harness.

## 2. Start with the smallest enforceable system

- Do not begin with the heaviest multi-agent layout.
- A good `AGENTS.md`, progress file, validator, and runner are usually more valuable than a giant orchestration layer.
- Add components only when a concrete failure mode justifies them.

## 3. AGENTS.md is a map, not an encyclopedia

- Keep `AGENTS.md` short enough to act as an entry map.
- Store durable detail in `docs/`.
- Use `AGENTS.md` to point at the system, not to become the system.

## 4. Progress files are cross-session context

- Long-running agents must recover from a fresh context window.
- Use `progress.txt`, structured task files, git history, and logs as the handoff surface.
- Every iteration should leave behind enough state that the next iteration can restart without guessing.

## 5. Mechanical constraints beat polite reminders

- “Please follow the architecture” is weak.
- Validators, structure tests, linters, and explicit file contracts are strong.
- Convert important rules into checks whenever possible.

## 6. Done must be machine-checkable

- “Looks good” is not enough.
- Good harnesses define output artifacts, acceptance tests, invariants, and stop conditions.
- The validator should be able to reject incomplete work without human intuition.

## 7. Failure logs are design input

- Each failure should answer: what was missing?
- Common buckets: missing tool, missing documentation, missing constraint, bad task split, bad validator, environment issue.
- Use failures to harden the harness rather than repeating the same prompt.

## 8. Observability is for the agent too

- Logs, traces, diffs, manifests, screenshots, and verdict artifacts help the agent self-locate and self-correct.
- If the agent cannot see what happened, it cannot repair the system intelligently.

## 9. Fresh-context loops need clean boundaries

- One pass should advance one smallest verifiable unit: a single feature, a single batch, or a single scoped change.
- Each pass should end cleanly: write progress, update the mutable task file, and leave the environment restartable.

## 10. Use structured state when mutation matters

- Mutable plans and task lists are often safer in JSON or YAML than prose because the harness can read and patch them deterministically.
- Use Markdown for human-facing design docs and durable knowledge; use structured files for mutable state.

## 11. Independent review is optional, not default

- Add a planner when the worker cannot reliably infer the contract.
- Add an evaluator or grader when acceptance is subjective, high-risk, or consistently beyond a solo worker.
- Do not pay multi-agent complexity unless the task earns it.

## 12. Build for evolution

- Keep the harness replaceable.
- Keep doctrine separated from implementation.
- Prune scaffolding as models improve; do not turn temporary compensation into permanent ceremony.
