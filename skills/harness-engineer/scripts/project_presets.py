#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass

from project_preset_templates import (
    build_batch_contract,
    build_batch_manifest,
    build_codebase_patterns,
    build_current_feature_plan,
    build_findings_readme,
    build_research_protocol,
    build_source_manifest,
    build_ui_validation,
    build_ui_verdict,
)


@dataclass(frozen=True)
class ProjectPresetSpec:
    name: str
    description: str
    extra_dirs: tuple[str, ...] = ()
    extra_files: tuple[tuple[str, str], ...] = ()
    force_archives: bool = False
    force_features_file: bool = False


PROJECT_PRESETS: dict[str, ProjectPresetSpec] = {
    "generic": ProjectPresetSpec(
        name="generic",
        description="Minimal task-agnostic harness scaffold.",
    ),
    "batch-processing": ProjectPresetSpec(
        name="batch-processing",
        description="Batch-oriented pipelines such as conversions, enrichment, OCR, or content processing.",
        extra_dirs=("input", "output", "artifacts"),
        extra_files=(
            ("batch-manifest.json", "batch_manifest"),
            ("docs/references/batch-contract.md", "batch_contract"),
        ),
        force_archives=True,
    ),
    "repo-coding": ProjectPresetSpec(
        name="repo-coding",
        description="Feature-by-feature or remediation-oriented codebase work.",
        extra_dirs=("artifacts",),
        extra_files=(
            ("docs/references/codebase-patterns.md", "codebase_patterns"),
            ("docs/exec-plans/current-feature-plan.md", "current_feature_plan"),
        ),
        force_features_file=True,
    ),
    "research-collection": ProjectPresetSpec(
        name="research-collection",
        description="Source gathering, evidence tracking, and structured synthesis work.",
        extra_dirs=("sources", "notes", "findings", "evidence"),
        extra_files=(
            ("source-manifest.json", "source_manifest"),
            ("docs/references/research-protocol.md", "research_protocol"),
            ("findings/README.md", "findings_readme"),
        ),
    ),
    "ui-validation": ProjectPresetSpec(
        name="ui-validation",
        description="Frontend or browser-flow work where rendered evidence matters.",
        extra_dirs=("screenshots", "traces", "verdicts"),
        extra_files=(
            ("verdicts/verdict.json", "ui_verdict"),
            ("docs/references/ui-validation.md", "ui_validation"),
        ),
    ),
}


PROJECT_PRESET_BUILDERS = {
    "batch_manifest": build_batch_manifest,
    "batch_contract": build_batch_contract,
    "codebase_patterns": build_codebase_patterns,
    "current_feature_plan": build_current_feature_plan,
    "source_manifest": build_source_manifest,
    "research_protocol": build_research_protocol,
    "findings_readme": build_findings_readme,
    "ui_verdict": build_ui_verdict,
    "ui_validation": build_ui_validation,
}


def get_project_preset(name: str) -> ProjectPresetSpec:
    return PROJECT_PRESETS[name]
