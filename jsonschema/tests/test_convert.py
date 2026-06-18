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
RESULTS_RE = re.compile(r"^RESULTS:(\{.+\})$", re.MULTILINE)
COUNTS_RE = re.compile(r"^COUNTS:(\{.+\})$", re.MULTILINE)

DEFAULT_RESULTS = {
    "error": False,
    "conversion_successful": False,
}

DEFAULT_COUNTS = {
    "datasets": 0,
    "valid_v1_1": 0,
    "invalid_v1_1": 0,
    "validation_errors_v1_1": 0,
    "valid_v3_0": 0,
    "invalid_v3_0": 0,
    "validation_errors_v3_0": 0,
}


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


def parse_tagged_json(stdout, pattern):
    """Extract a tagged JSON line (e.g. RESULTS:{...}) from stdout. Returns a dict or None."""
    match = pattern.search(stdout)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    return None


def determine_status(results):
    if results["error"]:
        return "ERROR"
    if results["conversion_successful"]:
        return "CONVERSION SUCCESSFUL"
    return "CONVERSION FAILED"


def categorize_failure(stderr, counts):
    if "There was an error fetching" in stderr:
        if "DNSError" in stderr:
            return "fetch_error:dns", []
        if "not valid JSON" in stderr:
            return "fetch_error:not_json", []
        if "Expected a JSON object at the catalog root" in stderr:
            return "fetch_error:bad_shape", []
        return "fetch_error:other", []
    if "v3.0 validation failed" in stderr:
        fields = FIELD_ERROR_RE.findall(stderr)
        return "validation_failed", fields
    if "There was an error converting" in stderr:
        return "conversion_exception", []
    # No exception was raised and stderr doesn't match a known crash pattern--
    # most likely some datasets simply came out invalid without the script
    # erroring. Categorize using the counts themselves rather than guessing
    # from stderr.
    if counts.get("invalid_v3_0", 0) > 0 or counts.get("invalid_v1_1", 0) > 0:
        return "invalid_datasets", []
    return "unknown_error", []


def main():
    urls = load_urls()
    runs = []

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        returncode, stdout, stderr = run_conversion(url)

        results = parse_tagged_json(stdout, RESULTS_RE) or dict(DEFAULT_RESULTS)
        counts = parse_tagged_json(stdout, COUNTS_RE) or dict(DEFAULT_COUNTS)
        status = determine_status(results)

        print(f"  {status}")
        if status != "CONVERSION SUCCESSFUL":
            lines = stderr.splitlines()
            if lines:
                print(f"  {lines[0]}")

        runs.append({
            "url": url,
            "status": status,
            "stderr": stderr,
            "results": results,
            "counts": counts,
        })

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "harvest source URL",
            "datasets",
            "valid 1.1",
            "invalid 1.1",
            "validation error count 1.1",
            "valid 3.0",
            "invalid 3.0",
            "validation error count 3.0",
            "conversion successful",
            "error",
        ])
        writer.writeheader()
        for r in runs:
            c = r["counts"]
            res = r["results"]
            writer.writerow({
                "harvest source URL": r["url"],
                "datasets": c["datasets"],
                "valid 1.1": c["valid_v1_1"],
                "invalid 1.1": c["invalid_v1_1"],
                "validation error count 1.1": c["validation_errors_v1_1"],
                "valid 3.0": c["valid_v3_0"],
                "invalid 3.0": c["invalid_v3_0"],
                "validation error count 3.0": c["validation_errors_v3_0"],
                "conversion successful": res["conversion_successful"],
                "error": res["error"],
            })
    print(f"\nWrote {OUTPUT_CSV}")

    status_counts = Counter(r["status"] for r in runs)
    print(f"\n{'='*50}")
    print(f"Results out of {len(runs)}:")
    for status in ("CONVERSION SUCCESSFUL", "CONVERSION FAILED", "ERROR"):
        print(f"  {status:<24} {status_counts.get(status, 0)}")

    failure_categories = Counter()
    field_errors = Counter()
    urls_per_field = defaultdict(set)

    for r in runs:
        if r["status"] != "CONVERSION SUCCESSFUL":
            category, fields = categorize_failure(r["stderr"], r["counts"])
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
