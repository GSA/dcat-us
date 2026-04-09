"""Create examples with `null` in all of the not-required properties.

We want our schemas to allow the JSON value `null` for every property that is
not required. This uses the schemas themselves to generate example files that
have this structure. They have actual (quite minimal) data for the required
properties and then `null` for everything else.

We put these schema files in our `examples/` directory so that our testing
process will verify that our desired use of `null` is maintained.
"""

import json
import sys

from pathlib import Path

"""A dict with schema names for keys and a starter dict with the required fields as values."""
SCHEMA_STARTERS = {
    "AccessRestriction": {"restrictionStatus": ""},
    "Activity": {"label": ""},
    "Address": {},
    "Agent": {"name": "Agent name"},
    "Checksum": {"algorithm": "", "checksumValue": ""},
    "Concept": {"prefLabel": ""},
    "ConceptScheme": {"title": ""},
    "CUIRestriction": {"cuiBannerMarking": "", "designationIndicator": ""},
    "DataService": {
        "contactPoint": [],
        "endpointURL": [],
        "publisher": {"name": ""},
        "title": "",
    },
    "Dataset": {
        "description": "",
        "publisher": {"name": ""},
        "title": "",
        "contactPoint": {"hasEmail": "mailto:a@example.gov", "fn": ""},
    },
    "DatasetSeries": {"description": "", "title": ""},
    "Distribution": {},
    "Document": {"title": ""},
    "Identifier": {},
    "Kind": {"hasEmail": "mailto:a@example.gov", "fn": ""},
    "Location": {},
    "Metric": {"expectedDataType": "", "inDimension": "urn:example:z"},
    "Organization": {"name": ""},
    "PeriodOfTime": {},
    "QualityMeasurement": {
        "isMeasurementOf": {"expectedDataType": "", "inDimension": "urn:example:z"},
        "value": "",
    },
    "Relationship": {"hadRole": "", "relation": "urn:example:z"},
    "Standard": {},
    "UseRestriction": {"restrictionStatus": ""},
}


def main():
    for name, starter in SCHEMA_STARTERS.items():
        print(f"{name}: ", end="")
        # load schema using the name
        with open(f"definitions/{name}.json") as f:
            schema = json.load(f)

        # verify that starter has all the required properties
        assert all(prop in starter for prop in schema.get("required", []))

        # set all non-required properties to None
        non_required = [
            prop
            for prop in schema.get("properties", [])
            # exclude @id and @type from this
            if all([prop not in schema["required"], not prop.startswith("@")])
        ]
        for prop in non_required:
            starter[prop] = None

        # save the object to a file
        filename = f"examples/{name}/good/null_example.json"
        with open(filename, "w") as f:
            json.dump(starter, f, indent=2, sort_keys=True)
        print(filename)


if __name__ == "__main__":
    sys.exit(main())
