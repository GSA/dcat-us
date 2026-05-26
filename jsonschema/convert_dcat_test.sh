#!/usr/bin/env bash

urls=(
    # Produces valid DCAT-US v3.0 data
    "https://open.gsa.gov/data.json" # (342 datasets, baseline)
    "https://www.energy.gov/data.json" # (482 datasets, contains "temporal" keys)

		# Cannot be converted to valid DCAT-US v3.0 data as-is
		"https://www.fec.gov/data.json"
    "https://www.nsf.gov/data.json"
    "https://www.treasury.gov/data.json"
		"https://www.justice.gov/data.json"

		# Contains invalid v1.1 data
    "https://www.usda.gov/data.json" # missing required field 'programCode' (requires TLS impersonation)
)

for url in "${urls[@]}"; do
    echo "Running DCAT-US v1.1 to v3.0 conversion script for: $url"
    if poetry run python convert_dcat_1_1_to_3_0.py --url="$url" --dry-run; then
        echo "success: $url"
    else
        echo "failed (exit $?): $url"
    fi
done
