#!/usr/bin/env python3
from __future__ import annotations

import json
import textwrap


def build_batch_manifest() -> str:
    payload = {
        "items": [
            {
                "id": "B1",
                "input": "",
                "status": "pending",
                "attempts": 0,
                "notes": "",
            }
        ]
    }
    return json.dumps(payload, indent=2) + "\n"


def build_batch_contract() -> str:
    return textwrap.dedent(
        """\
        # Batch Contract

        Define:
        - how one batch is selected
        - retry policy
        - partial failure policy
        - final summary format
        - archive behavior
        """
    )


def build_codebase_patterns() -> str:
    return textwrap.dedent(
        """\
        # Codebase Patterns

        Record reusable patterns here as the harness discovers them.

        Good entries:
        - module-specific gotchas
        - tests that must be run for a given area
        - coupling rules between files
        - conventions that future passes should preserve
        """
    )


def build_current_feature_plan() -> str:
    return textwrap.dedent(
        """\
        # Current Feature Plan

        1. Pick one pending feature.
        2. Freeze the scope for this pass.
        3. Implement.
        4. Run project checks.
        5. Update feature state and progress.
        """
    )


def build_source_manifest() -> str:
    payload = {
        "sources": [
            {
                "id": "S1",
                "url": "",
                "status": "pending",
                "credibility": "",
                "notes": "",
            }
        ]
    }
    return json.dumps(payload, indent=2) + "\n"


def build_research_protocol() -> str:
    return textwrap.dedent(
        """\
        # Research Protocol

        Define:
        - target question
        - source quality rules
        - evidence format
        - contradiction handling
        - final synthesis requirements
        """
    )


def build_findings_readme() -> str:
    return textwrap.dedent(
        """\
        # Findings

        Store validated findings here.

        Prefer one file per topic or one file per completed question rather than one ever-growing scratchpad.
        """
    )


def build_ui_verdict() -> str:
    payload = {
        "status": "pending",
        "screenshots": [],
        "flows_checked": [],
        "issues": [],
        "notes": "",
    }
    return json.dumps(payload, indent=2) + "\n"


def build_ui_validation() -> str:
    return textwrap.dedent(
        """\
        # UI Validation

        Browser verification should confirm:
        - the page loads
        - the intended user path works
        - the rendered state matches the acceptance criteria
        - evidence is stored under `screenshots/`, `traces/`, or `verdicts/`
        """
    )
