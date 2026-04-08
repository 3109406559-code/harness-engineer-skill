# Upgrade Guide

Use this file when the skill or a generated harness needs to evolve.

## Update order

When new doctrine arrives, update in this order:

1. `references/principles.md` if the new idea changes stable design doctrine
2. `references/topology-selection.md` if it changes when to add or remove components
3. `references/scaffold-spec.md` if it changes baseline file layout
4. `scripts/init_harness_project.py` if the scaffolder should create different defaults
5. `SKILL.md` only if trigger logic or workflow guidance changes

This keeps the surface area stable and avoids bloating the main skill file.

## Open-source discipline

- Avoid machine-specific paths in the skill body.
- Keep generated file names generic and portable.
- Avoid overfitting to one model provider unless the skill explicitly targets that provider.
- Prefer extension points over rigid dogma.

## Good upgrade reasons

- a repeated failure mode suggests a missing validator
- a new source shows a simpler or stronger topology rule
- generated projects are consistently missing a critical file
- a model improvement makes part of the scaffold unnecessary

## Bad upgrade reasons

- adding ceremony without evidence
- encoding a one-off project quirk as universal doctrine
- expanding `AGENTS.md` back into a giant handbook
- adding multi-agent complexity “just in case”

## Extension slots

Future versions can add:

- alternative scaffold profiles
- richer validators
- browser or app-specific verification bundles
- project-type presets
- structured manifests for more loop styles

Keep these as additive options instead of mutating the default minimal workflow unless the default is proven wrong.
