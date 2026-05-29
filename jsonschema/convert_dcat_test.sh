#!/usr/bin/env bash

urls=(
    # Produces valid DCAT-US v3.0 data
    "https://open.gsa.gov/data.json"
    "https://www.energy.gov/data.json" # contains `temporal` keys
		"https://data.cms.gov/data.json"
		"https://www.opm.gov/data.json"
		"https://www.state.gov/data.json"
		"https://www.dol.gov/data.json"
		"https://www.energy.gov/data.json"
		"https://www.fec.gov/data.json"
    "https://www.nsf.gov/data.json"
		"https://nsf-gov-resources.nsf.gov/files/data.json"
    "https://www.treasury.gov/data.json"
		"https://www.justice.gov/data.json"
		"https://www.treasury.gov/jsonfiles/data.json"
		"https://www.dhs.gov/xlibrary/assets/digital-strategy/data.json" # has `rights` set to null
    "https://www.fdic.gov/data.json"
		"https://www.loc.gov/data.json"
		"https://openei.org/data.json"
		"https://ddi.doi.gov/boem-data.json"
		"https://ddi.doi.gov/blm-data.json"
		"https://ddi.doi.gov/bia-data.json"
		"https://www.archive.arm.gov/metadata/data.json"
		"https://www.ftc.gov/data.json"
		"https://www.usitc.gov/data.json"
		"https://www.huduser.gov/data/data.json"
		"https://www.federalreserve.gov/PDC/data.json"
    "https://www.nist.gov/sites/default/files/data.json" # `replaces` set to both passing iri and non-iri in datasets
		"https://www.archives.gov/files/data.json" # temporal contains yyyy-mm/yyyy-mm dates
)

for url in "${urls[@]}"; do
    echo "Running DCAT-US v1.1 to v3.0 conversion script for: $url"
    if poetry run python convert_dcat_1_1_to_3_0.py --url="$url" --dry-run 2>/dev/null; then
        echo "success: $url"
    else
        echo "failed (exit $?): $url"
    fi
done
