# Topology Selection

Choose the smallest topology that can enforce the task safely.

## Default topology

### `runner + worker + validator`

Use this by default when:

- the task is well-scoped
- the acceptance criteria are concrete
- the environment is stable
- one agent can do the work if the harness is well-structured

Typical examples:

- batch file enrichment
- deterministic content transformation
- code changes with clear test coverage
- structured research collection with fixed output format

## Add an initializer

### `initializer + runner + worker + validator`

Add an initializer when the environment must be put into a known-good state before each pass.

Signals:

- dev server or dataset must be started or checked
- auth/session/bootstrap work is required before the worker can start
- health checks must run at the start of every loop
- the worker should not spend tokens rediscovering environment setup

## Add a planner

### `planner + worker + validator`

Add a planner when the worker is likely to fail because the task is underspecified or too large.

Signals:

- scope is ambiguous
- many files or subsystems are involved
- the user’s request hides multiple phases
- the worker would otherwise spend too much effort deciding task boundaries

Keep the planner output structured and short. It should freeze the contract, not become a second encyclopedia.

## Add an evaluator

### `planner + worker + evaluator`

Add an evaluator when the worker’s own “looks done” judgment is not trustworthy enough.

Signals:

- acceptance includes subjective quality
- the worker often passes obvious defects
- the system needs an independent judgment before state advances

Use the evaluator to grade or reject work; do not let it rewrite the project architecture by itself.

## Add a grader

### `planner + worker + evaluator + grader`

Reserve this for high-stakes or multi-axis acceptance.

Signals:

- correctness and presentation quality both matter
- you need a strict pass/fail gate plus a richer diagnostic pass
- there are multiple independent acceptance surfaces

Examples:

- productized UI work
- compliance-heavy output
- large research artifacts that need both factual and structural review

## Add browser verification

Browser verification is required when the task changes actual user-visible web behavior.

Do this even if unit tests pass when:

- the task changes UI
- the task touches navigation or interaction flows
- acceptance depends on rendered output

## Choose Ralph Loop as execution policy

Use a Ralph-style loop when the topology is stable but the work repeats over many passes.

Signals:

- one pass should advance one task, one feature, or one batch
- the agent may restart from fresh context between passes
- progress must be externalized in files
- the loop needs a simple explicit stop signal

Ralph Loop is not a separate harness topology. It is an execution policy layered on top of a topology such as `runner + worker + validator`.

## Anti-patterns

- Do not default every harness to the heaviest topology.
- Do not use “multi-agent” as a badge of seriousness.
- Do not create a planner if the execution contract is already obvious.
- Do not create an evaluator when a simple deterministic validator is sufficient.
- Do not keep legacy scaffolding forever if the current model no longer needs it.
