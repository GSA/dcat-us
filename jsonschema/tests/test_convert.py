import csv
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

CONVERT_SCRIPT = Path(__file__).parent.parent / 'convert_dcat_1_1_to_3_0.py'
URL_CSV = Path(__file__).parent / 'harvest_source_urls.csv'

# Matches the field name from lines like:
#   dataset[27].contactPoint: does not match ...
#   dataset[533].distribution[28].downloadURL: field is not null ...
#   dataset[56].temporal: expected type ...
FIELD_ERROR_RE = re.compile(r'dataset\[\d+\](?:\.\w+(?:\[\d+\])?)*\.(\w+):')


def load_urls():
    with open(URL_CSV) as f:
        reader = csv.DictReader(f)
        urls = [row['url'] for row in reader]
        return urls


def run_conversion(url):
    result = subprocess.run(
        [sys.executable, str(CONVERT_SCRIPT), '--url', url, '--dry-run'],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def categorize_failure(stderr):
    """Return a top-level failure category and a list of field-level error types."""
    if 'There was an error fetching' in stderr:
        if 'DNSError' in stderr:
            return 'fetch_error:dns', []
        if 'not valid JSON' in stderr:
            return 'fetch_error:not_json', []
        return 'fetch_error:other', []
    if 'v3.0 validation failed' in stderr:
        fields = FIELD_ERROR_RE.findall(stderr)
        return 'validation_failed', fields
    if 'v1.1 validation failed' in stderr:
        return 'input_invalid_v1_1', []
    return 'unknown_error', []


def main():
    urls = load_urls()
    results = []

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        returncode, stdout, stderr = run_conversion(url)
        status = "OK" if returncode == 0 else "FAIL"
        print(f"  {status}")
        if returncode != 0:
            print(f"  {stderr.splitlines()[0]}")

        results.append({
            "url": url,
            "status": status,
            "stderr": stderr,
        })

    # --- Summary ---
    ok = sum(1 for r in results if r['status'] == 'OK')
    fail = sum(1 for r in results if r['status'] == 'FAIL')
    print(f"\n{'='*50}")
    print(f"Results: {ok} OK, {fail} FAIL out of {len(results)}")

    # Top-level failure categories
    failure_categories = Counter()
    field_errors = Counter()  # which fields fail most across all URLs
    urls_per_field = defaultdict(set)  # which URLs are affected by each field

    for r in results:
        if r['status'] == 'FAIL':
            category, fields = categorize_failure(r['stderr'])
            failure_categories[category] += 1
            for field in fields:
                field_errors[field] += 1
                urls_per_field[field].add(r['url'])

    if failure_categories:
        print(f"\n--- Failure categories ---")
        for category, count in failure_categories.most_common():
            print(f"  {category:<30} {count} URL(s)")

    if field_errors:
        print(f"\n--- Field errors (by frequency across all datasets) ---")
        for field, count in field_errors.most_common():
            url_count = len(urls_per_field[field])
            print(f"  {field:<30} {count:>6} dataset(s) across {url_count} URL(s)")


if __name__ == '__main__':
    main()
