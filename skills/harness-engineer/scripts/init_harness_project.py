#!/usr/bin/env python3
"""
Create a baseline harness project skeleton.

Supports both a generic baseline scaffold and a Ralph Loop preset for resumable,
multi-pass agent projects.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from scaffold_builder import create_scaffold
from scaffold_config import (
    PRESET_CHOICES,
    PROJECT_PRESET_CHOICES,
    RUNNER_CHOICES,
    TOPOLOGY_CHOICES,
    default_runner_for_preset,
    slugify,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a baseline harness project scaffold.")
    parser.add_argument("output_dir", help="Directory where the project scaffold will be created")
    parser.add_argument("--project-name", required=True, help="Human-readable project name")
    parser.add_argument(
        "--preset",
        choices=PRESET_CHOICES,
        default="baseline",
        help="Scaffold profile to generate",
    )
    parser.add_argument(
        "--project-preset",
        choices=PROJECT_PRESET_CHOICES,
        default="generic",
        help="Task-oriented scaffold flavor to generate",
    )
    parser.add_argument(
        "--topology",
        choices=TOPOLOGY_CHOICES,
        default="runner-worker-validator",
        help="Harness topology to scaffold",
    )
    parser.add_argument(
        "--runner",
        choices=RUNNER_CHOICES,
        default=None,
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

    runner = args.runner or default_runner_for_preset(args.preset)

    create_scaffold(
        output_dir=output_dir,
        project_name=args.project_name,
        preset=args.preset,
        project_preset=args.project_preset,
        topology=args.topology,
        runner=runner,
        batch_size=args.batch_size,
        with_features_file=args.with_features_file,
        with_failure_log=args.with_failure_log,
        with_archives=args.with_archives,
    )
    print(f"Created harness scaffold at {output_dir}")


if __name__ == "__main__":
    main()
