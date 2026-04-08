#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from scaffold_config import plan_filename_for_preset, runner_filename
from scaffold_templates import (
    build_agents_md,
    build_architecture,
    build_config,
    build_current_plan,
    build_failure_log_stub,
    build_features_json,
    build_prd,
    build_progress,
    build_prompt,
    build_tasks_json,
    build_upgrade_notes,
    runner_template,
    validator_template,
)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_scaffold(
    output_dir: Path,
    project_name: str,
    preset: str,
    topology: str,
    runner: str,
    batch_size: int | None,
    with_features_file: bool,
    with_failure_log: bool,
    with_archives: bool,
) -> None:
    with_failure_log = with_failure_log or preset == "ralph-loop"
    with_archives = with_archives or preset == "ralph-loop"

    output_dir.mkdir(parents=True, exist_ok=True)
    for subdir in [
        "docs/product-specs",
        "docs/design-docs",
        "docs/exec-plans",
        "docs/references",
        "scripts",
        "logs",
    ]:
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)
    if with_archives:
        (output_dir / "archives").mkdir(parents=True, exist_ok=True)

    plan_filename = plan_filename_for_preset(preset)

    write_text(output_dir / "AGENTS.md", build_agents_md(project_name, topology, runner, preset))
    write_text(output_dir / "config.yaml", build_config(project_name, topology, runner, preset, batch_size))
    write_text(output_dir / "progress.txt", build_progress(preset))
    write_text(output_dir / "summary.txt", "# summary.txt\n\nPopulate this when the harness completes.\n")
    write_text(output_dir / "PROMPT.md", build_prompt(project_name, preset))
    write_text(output_dir / "docs" / "product-specs" / "PRD.md", build_prd(project_name, preset))
    write_text(output_dir / "docs" / "design-docs" / "architecture.md", build_architecture(project_name, topology, runner, preset))
    write_text(output_dir / "docs" / "exec-plans" / plan_filename, build_current_plan(topology, preset))
    write_text(output_dir / "docs" / "references" / "upgrade-notes.md", build_upgrade_notes())
    write_text(output_dir / "scripts" / runner_filename(runner), runner_template(project_name, topology, runner, preset))
    write_text(output_dir / "scripts" / "validate.py", validator_template(project_name, preset, plan_filename))

    if with_features_file:
        write_text(output_dir / "features.json", build_features_json())
    if preset == "ralph-loop":
        write_text(output_dir / "tasks.json", build_tasks_json())
    if with_failure_log:
        write_text(output_dir / "logs" / "failure-log.jsonl", build_failure_log_stub())
