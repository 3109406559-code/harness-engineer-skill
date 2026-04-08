# Roadmap

This roadmap keeps the project focused on practical harness engineering instead of feature sprawl.

## Near-term

- Improve the Ralph Loop preset with more realistic runner templates for Codex-style non-interactive runs
- Add optional project-type presets such as:
  - batch-processing
  - repo-coding
  - research-collection
  - UI-validation
- Add richer validator templates without making them default-heavy
- Improve generated `tasks.json` and feature/task manifest patterns

## Medium-term

- Add cross-platform scaffold examples for PowerShell, Bash, and Python runner styles
- Add optional evaluator and grader presets for high-risk tasks
- Add browser-verification guidance bundles for UI-focused harnesses
- Add sample generated projects under an `examples/` release artifact or separate branch

## Long-term

- Distill newer harness doctrine as model capabilities evolve
- Remove scaffolding that becomes unnecessary as base models improve
- Support narrower presets instead of growing one giant generic scaffold
- Keep the project publishable as a compact open-source skill, not a heavyweight framework

## Non-goals

- Becoming a universal agent runtime
- Replacing OpenHarness, Ralph, or upstream harness frameworks
- Defaulting every project to multi-agent orchestration
- Encoding every project-specific habit into the public skill
