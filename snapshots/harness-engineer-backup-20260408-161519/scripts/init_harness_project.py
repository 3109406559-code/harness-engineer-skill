#!/usr/bin/env python3
"""
Create a baseline harness project skeleton.

This script creates a minimal, upgrade-friendly harness layout with the files that
long-running agent projects usually need: AGENTS.md, docs/, scripts/, progress.txt,
config, and optional structured task files and failure logs.
"""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path


TOPOLOGY_CHOICES = [
    "runner-worker-validator",
    "initializer-runner-worker-validator",
    "planner-worker-validator",
    "planner-worker-evaluator",
    "planner-worker-evaluator-grader",
]

RUNNER_CHOICES = ["python", "powershell", "bash"]


def slugify(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value.strip())
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-") or "harness-project"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def runner_filename(runner: str) -> str:
    if runner == "powershell":
        return "ralph.ps1"
    if runner == "bash":
        return "ralph.sh"
    return "runner.py"


def runner_template(project_name: str, topology: str, runner: str) -> str:
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


def validator_template(project_name: str) -> str:
    return textwrap.dedent(
        f"""\
        #!/usr/bin/env python3
        from __future__ import annotations

        from pathlib import Path


        def main() -> None:
            root = Path(__file__).resolve().parents[1]
            required = [
                root / "AGENTS.md",
                root / "config.yaml",
                root / "progress.txt",
                root / "docs" / "design-docs" / "architecture.md",
            ]
            missing = [str(path) for path in required if not path.exists()]
            if missing:
                raise SystemExit("Missing required scaffold files: " + ", ".join(missing))
            print("{project_name} scaffold basic validation passed")


        if __name__ == "__main__":
            main()
        """
    )


def build_agents_md(project_name: str, topology: str, runner: str) -> str:
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

        ## Rules
        - Keep this file short and navigational.
        - Put detailed design and plans in `docs/`.
        - Treat `progress.txt` as resumable agent state.
        - Advance the loop only when validator checks pass.

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
        """
    )


def build_config(project_name: str, topology: str, runner: str, batch_size: int | None) -> str:
    batch_line = f"batch_size: {batch_size}\n" if batch_size else ""
    return textwrap.dedent(
        f"""\
        project_name: "{project_name}"
        topology: "{topology}"
        runner: "{runner}"
        {batch_line}progress_file: "progress.txt"
        logs_dir: "logs"
        docs_dir: "docs"
        """
    )


def build_progress() -> str:
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


def build_prd(project_name: str) -> str:
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
        """
    )


def build_architecture(project_name: str, topology: str, runner: str) -> str:
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

        ## Upgrade notes
        - Keep `AGENTS.md` short.
        - Use `docs/` for durable detail.
        - Add structured task files if mutable multi-unit state appears.
        """
    )


def build_current_plan(topology: str) -> str:
    return textwrap.dedent(
        f"""\
        # Current Plan

        ## Topology
        `{topology}`

        ## Immediate next steps
        1. Finalize the execution contract.
        2. Replace placeholder runner and validator logic.
        3. Define the smallest verifiable unit.
        4. Add any task or feature manifest if the work is multi-unit.
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


def build_failure_log_stub() -> str:
    return ""


def create_scaffold(
    output_dir: Path,
    project_name: str,
    topology: str,
    runner: str,
    batch_size: int | None,
    with_features_file: bool,
    with_failure_log: bool,
    with_archives: bool,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "docs" / "product-specs").mkdir(parents=True, exist_ok=True)
    (output_dir / "docs" / "design-docs").mkdir(parents=True, exist_ok=True)
    (output_dir / "docs" / "exec-plans").mkdir(parents=True, exist_ok=True)
    (output_dir / "docs" / "references").mkdir(parents=True, exist_ok=True)
    (output_dir / "scripts").mkdir(parents=True, exist_ok=True)
    (output_dir / "logs").mkdir(parents=True, exist_ok=True)
    if with_archives:
        (output_dir / "archives").mkdir(parents=True, exist_ok=True)

    write_text(output_dir / "AGENTS.md", build_agents_md(project_name, topology, runner))
    write_text(output_dir / "config.yaml", build_config(project_name, topology, runner, batch_size))
    write_text(output_dir / "progress.txt", build_progress())
    write_text(output_dir / "summary.txt", "# summary.txt\n\nPopulate this when the harness completes.\n")
    write_text(output_dir / "PROMPT.md", "# Worker Prompt\n\nReplace this placeholder with the real worker instructions.\n")
    write_text(output_dir / "docs" / "product-specs" / "PRD.md", build_prd(project_name))
    write_text(output_dir / "docs" / "design-docs" / "architecture.md", build_architecture(project_name, topology, runner))
    write_text(output_dir / "docs" / "exec-plans" / "current-plan.md", build_current_plan(topology))
    write_text(output_dir / "docs" / "references" / "upgrade-notes.md", build_upgrade_notes())
    write_text(output_dir / "scripts" / runner_filename(runner), runner_template(project_name, topology, runner))
    write_text(output_dir / "scripts" / "validate.py", validator_template(project_name))

    if with_features_file:
        write_text(output_dir / "features.json", build_features_json())
    if with_failure_log:
        write_text(output_dir / "logs" / "failure-log.jsonl", build_failure_log_stub())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a baseline harness project scaffold.")
    parser.add_argument("output_dir", help="Directory where the project scaffold will be created")
    parser.add_argument("--project-name", required=True, help="Human-readable project name")
    parser.add_argument(
        "--topology",
        choices=TOPOLOGY_CHOICES,
        default="runner-worker-validator",
        help="Harness topology to scaffold",
    )
    parser.add_argument(
        "--runner",
        choices=RUNNER_CHOICES,
        default="python",
        help="Runner implementation style to scaffold",
    )
    parser.add_argument("--batch-size", type=int, default=None, help="Optional initial batch size")
    parser.add_argument(
        "--with-features-file",
        action="store_true",
        help="Create a structured features.json file",
    )
    parser.add_argument(
        "--with-failure-log",
        action="store_true",
        help="Create logs/failure-log.jsonl",
    )
    parser.add_argument(
        "--with-archives",
        action="store_true",
        help="Create an archives/ directory",
    )
    parser.add_argument(
        "--slug",
        default=None,
        help="Optional explicit directory name; defaults to a slugified project name",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    slug = args.slug or slugify(args.project_name)
    output_dir = Path(args.output_dir).resolve() / slug
    if output_dir.exists() and any(output_dir.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty directory: {output_dir}")

    create_scaffold(
        output_dir=output_dir,
        project_name=args.project_name,
        topology=args.topology,
        runner=args.runner,
        batch_size=args.batch_size,
        with_features_file=args.with_features_file,
        with_failure_log=args.with_failure_log,
        with_archives=args.with_archives,
    )
    print(f"Created harness scaffold at {output_dir}")


if __name__ == "__main__":
    main()
