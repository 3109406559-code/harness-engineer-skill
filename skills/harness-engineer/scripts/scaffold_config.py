#!/usr/bin/env python3
from __future__ import annotations

import os

PRESET_CHOICES = ["baseline", "ralph-loop"]
PROJECT_PRESET_CHOICES = [
    "generic",
    "batch-processing",
    "repo-coding",
    "research-collection",
    "ui-validation",
]
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


def default_runner_for_preset(preset: str) -> str:
    if preset == "ralph-loop":
        return "powershell" if os.name == "nt" else "bash"
    return "python"


def runner_filename(runner: str) -> str:
    if runner == "powershell":
        return "ralph.ps1"
    if runner == "bash":
        return "ralph.sh"
    return "runner.py"


def plan_filename_for_preset(preset: str) -> str:
    if preset == "ralph-loop":
        return "current-batch-plan.md"
    return "current-plan.md"
