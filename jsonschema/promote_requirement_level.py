#!/usr/bin/env python3
"""Promote _oldDocs.requirementLevel to sibling requirementLevel in schema fields.

By default, runs as a dry run and reports how many changes would be made.
Use --write to apply updates in place.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFINITIONS_DIR = Path(__file__).parent / "definitions"


def promote_requirement_level(node: Any) -> int:
    """Recursively promote _oldDocs.requirementLevel on dict nodes.

    Returns the number of dict nodes updated.
    """
    updates = 0

    if isinstance(node, dict):
        old_docs = node.get("_oldDocs")
        if isinstance(old_docs, dict) and "requirementLevel" in old_docs:
            old_level = old_docs.pop("requirementLevel")
            if node.get("requirementLevel") != old_level:
                node["requirementLevel"] = old_level
            if not old_docs:
                node.pop("_oldDocs", None)
            updates += 1

        for value in node.values():
            updates += promote_requirement_level(value)

    elif isinstance(node, list):
        for item in node:
            updates += promote_requirement_level(item)

    return updates


def process_file(path: Path, write: bool) -> tuple[int, bool]:
    with open(path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    updates = promote_requirement_level(schema)
    changed = updates > 0

    if changed and write:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
            f.write("\n")

    return updates, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to files. Without this flag, only report what would change.",
    )
    parser.add_argument(
        "--definitions-dir",
        type=Path,
        default=DEFINITIONS_DIR,
        help=f"Schema definitions directory (default: {DEFINITIONS_DIR})",
    )
    args = parser.parse_args()

    schema_files = sorted(args.definitions_dir.glob("*.json"))
    if not schema_files:
        print(f"No schema files found in {args.definitions_dir}")
        return 1

    total_updates = 0
    changed_files = 0

    for schema_file in schema_files:
        updates, changed = process_file(schema_file, write=args.write)
        total_updates += updates
        if changed:
            changed_files += 1
            mode = "Updated" if args.write else "Would update"
            print(f"{mode} {schema_file.name}: {updates} field(s)")

    if changed_files == 0:
        print("No changes needed.")
    else:
        print(
            f"{('Updated' if args.write else 'Would update')} "
            f"{changed_files} file(s), {total_updates} field(s) total."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
