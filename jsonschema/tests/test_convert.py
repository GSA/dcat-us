import csv
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

CONVERT_SCRIPT = Path(__file__).parent.parent / "convert_dcat_1_1_to_3_0.py"
URL_CSV = Path(__file__).parent / "harvest_source_urls.csv"
OUTPUT_CSV = Path(__file__).parent / "test_convert_results.csv"

FIELD_ERROR_RE = re.compile(r"dataset\[\d+\](?:\.\w+(?:\[\d+\])?)*\.(\w+):")
COUNTS_RE = re.compile(r"^COUNTS:(\{.+\})$", re.MULTILINE)


def load_urls():
    with open(URL_CSV) as f:
        reader = csv.DictReader(f)
        return [row["url"] for row in reader]


def run_conversion(url):
    result = subprocess.run(
        [sys.executable, str(CONVERT_SCRIPT), "--url", url, "--dry-run"],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def parse_counts(stdout):
    """Extract the COUNTS JSON line from stdout. Returns a dict or None."""
    match = COUNTS_RE.search(stdout)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    return None


def categorize_failure(stderr):
    if "There was an error fetching" in stderr:
        if "DNSError" in stderr:
            return "fetch_error:dns", []
        if "not valid JSON" in stderr:
            return "fetch_error:not_json", []
        return "fetch_error:other", []
    if "v3.0 validation failed" in stderr:
        fields = FIELD_ERROR_RE.findall(stderr)
        return "validation_failed", fields
    return "unknown_error", []


def main():
    urls = load_urls()
    results = []

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        returncode, stdout, stderr = run_conversion(url)
        status = "OK" if returncode == 0 else "FAIL"
        print(f"  {status}")
        if returncode != 0:
            lines = stderr.splitlines()
            if lines:
                print(f"  {lines[0]}")

        counts = parse_counts(stdout) or {
            "valid_v1_1": 0,
            "invalid_v1_1": 0,
            "valid_v3_0": 0,
            "invalid_v3_0": 0,
            "errors": 0,
        }

        results.append({
            "url": url,
            "status": status,
            "stderr": stderr,
            "counts": counts,
        })

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "harvest source URL",
            "valid 1.1 record counts",
            "invalid 1.1 record counts",
            "valid 3.0 record counts",
            "invalid 3.0 record counts",
            "errors",
        ])
        writer.writeheader()
        for r in results:
            c = r["counts"]
            writer.writerow({
                "harvest source URL": r["url"],
                "valid 1.1 record counts": c["valid_v1_1"],
                "invalid 1.1 record counts": c["invalid_v1_1"],
                "valid 3.0 record counts": c["valid_v3_0"],
                "invalid 3.0 record counts": c["invalid_v3_0"],
                "errors": c["errors"],
            })
    print(f"\nWrote {OUTPUT_CSV}")

    ok = sum(1 for r in results if r["status"] == "OK")
    fail = sum(1 for r in results if r["status"] == "FAIL")
    print(f"\n{'='*50}")
    print(f"Results: {ok} OK, {fail} FAIL out of {len(results)}")

    failure_categories = Counter()
    field_errors = Counter()
    urls_per_field = defaultdict(set)

    for r in results:
        if r["status"] == "FAIL":
            category, fields = categorize_failure(r["stderr"])
            failure_categories[category] += 1
            for field in fields:
                field_errors[field] += 1
                urls_per_field[field].add(r["url"])

    if failure_categories:
        print(f"\n--- Failure categories ---")
        for category, count in failure_categories.most_common():
            print(f"  {category:<30} {count} URL(s)")

    if field_errors:
        print(f"\n--- Field errors (by frequency across all datasets) ---")
        for field, count in field_errors.most_common():
            url_count = len(urls_per_field[field])
            print(f"  {field:<30} {count:>6} dataset(s) across {url_count} URL(s)")


if __name__ == "__main__":
    main()