#!/usr/bin/env python3
"""Check and optionally fix requirement levels against JSON Schema required fields.

Rules:
- If a property is listed in a schema's required array, requirementLevel should be Mandatory.
- If requirementLevel is Mandatory but property is not required, it is downgraded to Optional in --fix mode.
- If requirementLevel is missing, it is treated as Optional by default.

Compatibility:
- Legacy _oldDocs.requirementLevel is still read as a fallback.
"""

import argparse
import json
from pathlib import Path


def normalize_requirement_level(value: str | None) -> str:
    if not value:
        return "Optional"
    lowered = value.strip().lower()
    if lowered == "mandatory":
        return "Mandatory"
    if lowered == "recommended":
        return "Recommended"
    return "Optional"


def get_requirement_level(prop_schema: dict) -> str:
    """Read requirement level from the new location, with legacy fallback."""
    if "requirementLevel" in prop_schema:
        return normalize_requirement_level(prop_schema.get("requirementLevel"))

    old_docs = prop_schema.get("_oldDocs")
    if isinstance(old_docs, dict):
        return normalize_requirement_level(old_docs.get("requirementLevel"))

    return "Optional"


def check_schema(schema_path: Path, fix: bool = False) -> tuple[list[str], bool]:
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    required = set(schema.get("required", []))
    properties = schema.get("properties", {})
    changed = False
    findings: list[str] = []

    for prop_name, prop_schema in properties.items():
        if prop_name in {"@id", "@type"} or not isinstance(prop_schema, dict):
            continue

        current_level = get_requirement_level(prop_schema)

        is_required = prop_name in required

        if is_required and current_level != "Mandatory":
            findings.append(
                f"{schema_path.name}: '{prop_name}' is required in schema but requirementLevel is {current_level}"
            )
            if fix:
                prop_schema["requirementLevel"] = "Mandatory"
                changed = True

        if (not is_required) and current_level == "Mandatory":
            findings.append(
                f"{schema_path.name}: '{prop_name}' is not required in schema but requirementLevel is Mandatory"
            )
            if fix:
                prop_schema["requirementLevel"] = "Optional"
                changed = True

    if changed:
        with open(schema_path, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
            f.write("\n")

    return findings, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Apply fixes to schema files")
    args = parser.parse_args()

    schema_dir = Path(__file__).parent / "definitions"
    schema_files = sorted(schema_dir.glob("*.json"))

    all_findings: list[str] = []
    changed_count = 0

    for schema_path in schema_files:
        findings, changed = check_schema(schema_path, fix=args.fix)
        all_findings.extend(findings)
        if changed:
            changed_count += 1

    if all_findings:
        for line in all_findings:
            print(line)
    else:
        print("No requirement-level mismatches found.")

    if args.fix:
        print(f"Updated {changed_count} schema file(s).")

    return 1 if all_findings and not args.fix else 0


if __name__ == "__main__":
    raise SystemExit(main())
