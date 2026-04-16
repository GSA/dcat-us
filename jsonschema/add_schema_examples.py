#!/usr/bin/env python3
"""Populate schema `examples` fields from good/typical and good/complete examples.

For each class schema in definitions/:
- Schema-level `examples` is populated from `good/typical_example.json`.
- Property-level `examples` is populated from values found in both
  `good/typical_example.json` and `good/complete_example.json`.

Examples are deduplicated while preserving order. Missing example files are
reported and skipped without failing the whole run.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).parent
DEFINITIONS_DIR = SCRIPT_DIR / "definitions"
EXAMPLES_DIR = SCRIPT_DIR / "examples"


def _load_json(file_path: Path) -> Any:
    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _stable_key(value: Any) -> str:
    """Create a stable string key for JSON-like values."""
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def _dedupe(values: list[Any]) -> list[Any]:
    seen: set[str] = set()
    deduped: list[Any] = []
    for value in values:
        key = _stable_key(value)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(value)
    return deduped


def _object_examples(raw_example: Any) -> list[dict[str, Any]]:
    """Return one or more object examples from loaded JSON data."""
    if isinstance(raw_example, dict):
        return [raw_example]
    if isinstance(raw_example, list):
        return [item for item in raw_example if isinstance(item, dict)]
    return []


def _update_schema(schema_name: str, dry_run: bool = False) -> tuple[bool, str]:
    schema_path = DEFINITIONS_DIR / f"{schema_name}.json"
    typical_path = EXAMPLES_DIR / schema_name / "good" / "typical_example.json"
    complete_path = EXAMPLES_DIR / schema_name / "good" / "complete_example.json"

    if not schema_path.exists():
        return False, f"SKIP {schema_name}: schema file not found"

    if not typical_path.exists() and not complete_path.exists():
        return False, f"SKIP {schema_name}: no typical/complete example files"

    schema = _load_json(schema_path)
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        return False, f"SKIP {schema_name}: schema has no object properties"

    typical_raw = _load_json(typical_path) if typical_path.exists() else None
    complete_raw = _load_json(complete_path) if complete_path.exists() else None

    typical_objects = _object_examples(typical_raw)
    complete_objects = _object_examples(complete_raw)

    # Always recompute examples from source examples so reruns are deterministic.
    schema.pop("examples", None)

    # Class-level examples should prefer typical examples.
    class_examples = _dedupe(typical_objects)
    if class_examples:
        schema["examples"] = class_examples

    source_objects = typical_objects + complete_objects
    for prop_name, prop_def in properties.items():
        if not isinstance(prop_def, dict):
            continue

        # Clear any prior generated examples before repopulating.
        prop_def.pop("examples", None)

        prop_values: list[Any] = []
        for obj in source_objects:
            if prop_name in obj:
                prop_values.append(obj[prop_name])

        if prop_values:
            prop_def["examples"] = _dedupe(prop_values)

    if not dry_run:
        schema_path.write_text(
            json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    return True, f"UPDATED {schema_name}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Populate schema and property examples from typical/complete examples"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which schemas would be updated without writing files",
    )
    args = parser.parse_args()

    updated = 0
    skipped = 0

    for schema_path in sorted(DEFINITIONS_DIR.glob("*.json")):
        schema_name = schema_path.stem
        changed, message = _update_schema(schema_name, dry_run=args.dry_run)
        print(message)
        if changed:
            updated += 1
        else:
            skipped += 1

    print(f"\\nDone. Updated: {updated}, Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
