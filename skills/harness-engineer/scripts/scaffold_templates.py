#!/usr/bin/env python3
from __future__ import annotations

import json
import textwrap


def baseline_runner_template(project_name: str, topology: str, runner: str) -> str:
    if runner == "powershell":
        return textwrap.dedent(
            f"""\
            param(
                [int]$MaxPasses = 1
            )

            Write-Host "Starting harness runner for {project_name}"
            Write-Host "Topology: {topology}"
            Write-Host "TODO: Replace this placeholder with the real loop."
            """
        )

    if runner == "bash":
        return textwrap.dedent(
            f"""\
            #!/usr/bin/env bash
            set -euo pipefail

            echo "Starting harness runner for {project_name}"
            echo "Topology: {topology}"
            echo "TODO: Replace this placeholder with the real loop."
            """
        )

    return textwrap.dedent(
        f"""\
        #!/usr/bin/env python3
        def main() -> None:
            print("Starting harness runner for {project_name}")
            print("Topology: {topology}")
            print("TODO: Replace this placeholder with the real loop.")


        if __name__ == "__main__":
            main()
        """
    )


def ralph_runner_template(project_name: str, runner: str) -> str:
    if runner == "powershell":
        return textwrap.dedent(
            f"""\
            param(
                [int]$MaxIterations = 10
            )

            Set-StrictMode -Version Latest
            $ErrorActionPreference = "Stop"

            if ($PSVersionTable.PSVersion.Major -lt 7) {{
                throw "Run this Ralph Loop scaffold with PowerShell 7."
            }}

            $projectRoot = Split-Path -Parent $PSScriptRoot
            $promptPath = Join-Path $projectRoot "PROMPT.md"
            $progressPath = Join-Path $projectRoot "progress.txt"
            $tasksPath = Join-Path $projectRoot "tasks.json"

            Write-Host "Starting Ralph Loop for {project_name}"
            Write-Host "Prompt: $promptPath"
            Write-Host "Progress: $progressPath"
            Write-Host "Tasks: $tasksPath"

            for ($iteration = 1; $iteration -le $MaxIterations; $iteration++) {{
                Write-Host "Ralph iteration $iteration / $MaxIterations"
                Write-Host "TODO: Replace this placeholder with your non-interactive agent command."
                Write-Host "Expected exit-code contract: 0=continue, 2=complete, nonzero=fail."
                break
            }}
            """
        )

    if runner == "bash":
        return textwrap.dedent(
            f"""\
            #!/usr/bin/env bash
            set -euo pipefail

            SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"
            PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
            PROMPT_PATH="$PROJECT_ROOT/PROMPT.md"
            PROGRESS_PATH="$PROJECT_ROOT/progress.txt"
            TASKS_PATH="$PROJECT_ROOT/tasks.json"
            MAX_ITERATIONS="${{1:-10}}"

            echo "Starting Ralph Loop for {project_name}"
            echo "Prompt: $PROMPT_PATH"
            echo "Progress: $PROGRESS_PATH"
            echo "Tasks: $TASKS_PATH"

            for ((iteration=1; iteration<=MAX_ITERATIONS; iteration++)); do
              echo "Ralph iteration $iteration / $MAX_ITERATIONS"
              echo "TODO: Replace this placeholder with your non-interactive agent command."
              echo "Expected exit-code contract: 0=continue, 2=complete, nonzero=fail."
              break
            done
            """
        )

    return textwrap.dedent(
        f"""\
        #!/usr/bin/env python3
        def main() -> None:
            print("Starting Ralph Loop for {project_name}")
            print("TODO: Replace this placeholder with your non-interactive agent command.")
            print("Expected exit-code contract: 0=continue, 2=complete, nonzero=fail.")


        if __name__ == "__main__":
            main()
        """
    )


def runner_template(project_name: str, topology: str, runner: str, preset: str) -> str:
    if preset == "ralph-loop":
        return ralph_runner_template(project_name, runner)
    return baseline_runner_template(project_name, topology, runner)


def validator_template(project_name: str, preset: str, plan_filename: str) -> str:
    required = [
        'root / "AGENTS.md"',
        'root / "config.yaml"',
        'root / "progress.txt"',
        'root / "docs" / "design-docs" / "architecture.md"',
        f'root / "docs" / "exec-plans" / "{plan_filename}"',
    ]
    if preset == "ralph-loop":
        required.extend(
            [
                'root / "PROMPT.md"',
                'root / "tasks.json"',
                'root / "docs" / "exec-plans" / "current-batch-plan.md"',
            ]
        )

    required_block = "\n".join(f"        {line}," for line in required)
    return (
        "#!/usr/bin/env python3\n"
        "from __future__ import annotations\n\n"
        "from pathlib import Path\n\n\n"
        "def main() -> None:\n"
        "    root = Path(__file__).resolve().parents[1]\n"
        "    required = [\n"
        f"{required_block}\n"
        "    ]\n"
        "    missing = [str(path) for path in required if not path.exists()]\n"
        '    if missing:\n'
        '        raise SystemExit("Missing required scaffold files: " + ", ".join(missing))\n'
        f'    print("{project_name} scaffold basic validation passed")\n\n\n'
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def build_agents_md(project_name: str, topology: str, runner: str, preset: str) -> str:
    preset_lines = ""
    directory_lines = ""
    if preset == "ralph-loop":
        preset_lines = textwrap.dedent(
            """\
            ## Ralph Loop Rules
            - Each pass should advance exactly one smallest verifiable unit.
            - The worker should read `tasks.json`, `progress.txt`, and `PROMPT.md` before acting.
            - The loop should only advance when validation passes.
            - Completion should be explicit, not implied.
            """
        )
        directory_lines = textwrap.dedent(
            """\
            - `PROMPT.md` -> worker prompt for one Ralph pass
            - `tasks.json` -> mutable machine-readable task state
            - `docs/exec-plans/current-batch-plan.md` -> current pass or batch plan
            """
        )

    return textwrap.dedent(
        f"""\
        # AGENTS.md

        ## Project
        {project_name}

        ## Purpose
        This repository is a harness project scaffold.

        ## Topology
        - Selected topology: `{topology}`
        - Runner type: `{runner}`
        - Preset: `{preset}`

        ## Rules
        - Keep this file short and navigational.
        - Put detailed design and plans in `docs/`.
        - Treat `progress.txt` as resumable agent state.
        - Advance the loop only when validator checks pass.

        {preset_lines.rstrip()}

        ## Directory Map
        - `AGENTS.md` -> project map and high-level behavior rules
        - `config.yaml` -> stable configuration
        - `progress.txt` -> observable run state
        - `docs/product-specs/` -> product contract
        - `docs/design-docs/` -> architecture and topology
        - `docs/exec-plans/` -> current plan or batch
        - `docs/references/` -> durable doctrine and source notes
        - `scripts/` -> runner and validator entrypoints
        - `logs/` -> operational logs and failure artifacts
        {directory_lines.rstrip()}
        """
    )


def build_config(project_name: str, topology: str, runner: str, preset: str, batch_size: int | None) -> str:
    lines = [
        f'project_name: "{project_name}"',
        f'topology: "{topology}"',
        f'runner: "{runner}"',
        f'preset: "{preset}"',
    ]
    if batch_size:
        lines.append(f"batch_size: {batch_size}")
    lines.extend(
        [
            'progress_file: "progress.txt"',
            'logs_dir: "logs"',
            'docs_dir: "docs"',
        ]
    )
    if preset == "ralph-loop":
        lines.extend(
            [
                'tasks_file: "tasks.json"',
                'prompt_file: "PROMPT.md"',
                'summary_file: "summary.txt"',
            ]
        )
    return "\n".join(lines) + "\n"


def build_progress(preset: str) -> str:
    if preset == "ralph-loop":
        return textwrap.dedent(
            """\
            # progress.txt

            status: not-started
            current_iteration: 0
            current_unit: none
            completed_units: 0
            failed_units: 0
            last_success_at: N/A
            last_failure: none
            notes: each Ralph pass should update this file before exit
            """
        )

    return textwrap.dedent(
        """\
        # progress.txt

        status: not-started
        current_unit: none
        completed_units: 0
        failed_units: 0
        last_success_at: N/A
        notes: initialize the loop contract before first run
        """
    )


def build_prd(project_name: str, preset: str) -> str:
    preset_lines = ""
    if preset == "ralph-loop":
        preset_lines = textwrap.dedent(
            """\
            ## Ralph Loop Unit
            [Define the smallest verifiable unit that one pass is allowed to advance.]

            ## Loop Stop Condition
            [Define what makes the worker emit completion and what should stop the loop with failure.]
            """
        )

    return textwrap.dedent(
        f"""\
        # PRD

        ## Project
        {project_name}

        ## Goal
        [Describe the end-state in concrete, verifiable terms.]

        ## Inputs
        [List the inputs, sources, permissions, and environment assumptions.]

        ## Outputs
        [List the artifacts the harness must produce.]

        ## Success Criteria
        [Define what the validator must be able to prove.]

        {preset_lines.rstrip()}
        """
    )


def build_architecture(project_name: str, topology: str, runner: str, preset: str) -> str:
    preset_lines = ""
    if preset == "ralph-loop":
        preset_lines = textwrap.dedent(
            """\
            ## Ralph Loop Execution Policy
            - The loop is the execution policy layered on top of the topology.
            - One pass should advance one task, one feature, or one bounded batch.
            - The next pass should be able to restart from files alone.
            - Use explicit exit codes or explicit completion markers.
            """
        )

    return textwrap.dedent(
        f"""\
        # Architecture

        ## Project
        {project_name}

        ## Selected topology
        `{topology}`

        ## Responsibilities
        - Runner: owns loop progression and stop conditions.
        - Worker: owns one smallest verifiable unit of work.
        - Validator: decides whether the loop may advance.
        - Optional planner/evaluator/grader: add only if justified by the task.

        ## Runner type
        `{runner}`

        ## Preset
        `{preset}`

        {preset_lines.rstrip()}

        ## Upgrade notes
        - Keep `AGENTS.md` short.
        - Use `docs/` for durable detail.
        - Add structured task files if mutable multi-unit state appears.
        """
    )


def build_current_plan(topology: str, preset: str) -> str:
    heading = "Current Batch Plan" if preset == "ralph-loop" else "Current Plan"
    line4 = (
        "4. Ensure the pass contract is one smallest verifiable unit."
        if preset == "ralph-loop"
        else "4. Add any task or feature manifest if the work is multi-unit."
    )
    return textwrap.dedent(
        f"""\
        # {heading}

        ## Topology
        `{topology}`

        ## Immediate next steps
        1. Finalize the execution contract.
        2. Replace placeholder runner and validator logic.
        3. Define the smallest verifiable unit.
        {line4}
        """
    )


def build_upgrade_notes() -> str:
    return textwrap.dedent(
        """\
        # Upgrade Notes

        Record new harness lessons here before changing the scaffold.

        Suggested questions:
        - Did a repeated failure reveal a missing validator?
        - Did the task need a different topology?
        - Can any current scaffold component be simplified or removed?
        - Which rules should become mechanical checks?
        """
    )


def build_features_json() -> str:
    payload = {
        "features": [
            {
                "id": "F1",
                "title": "replace scaffold placeholders",
                "status": "pending",
                "passes": False,
                "notes": "",
            }
        ]
    }
    return json.dumps(payload, indent=2) + "\n"


def build_tasks_json() -> str:
    payload = {
        "tasks": [
            {
                "id": "T1",
                "title": "replace scaffold placeholders",
                "status": "pending",
                "passes": False,
                "notes": "Define the smallest verifiable unit before real execution.",
            }
        ]
    }
    return json.dumps(payload, indent=2) + "\n"


def build_failure_log_stub() -> str:
    return ""


def build_prompt(project_name: str, preset: str) -> str:
    if preset == "ralph-loop":
        return textwrap.dedent(
            f"""\
            # Ralph Worker Prompt

            You are the worker inside a Ralph-style harness for {project_name}.

            ## Required inputs
            1. Read `docs/product-specs/PRD.md`.
            2. Read `tasks.json`.
            3. Read `progress.txt`.
            4. Read the current execution plan in `docs/exec-plans/current-batch-plan.md`.

            ## Required behavior
            1. Pick exactly one pending task or one bounded batch.
            2. Do not attempt the whole project in one pass.
            3. Run the project validator before marking progress.
            4. Update `tasks.json` and `progress.txt`.
            5. Append useful evidence to `logs/`.
            6. If all tasks pass, emit an explicit completion signal such as `<promise>DONE</promise>`.

            ## Guardrails
            - Use file state, not chat memory, as the source of truth.
            - Leave the project in a clean restartable state before exiting.
            - Stop if validation fails or if the task contract is unclear.
            """
        )

    return "# Worker Prompt\n\nReplace this placeholder with the real worker instructions.\n"
