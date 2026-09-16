import json
import unittest.mock as mock

import pytest
from click.testing import CliRunner

import convert_dcat_1_1_to_3_0 as convert


@pytest.fixture
def sample_v1_1_catalog():
    return {
        "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
        "dataset": [
            {
                "title": "Widget Inventory",
                "description": "Every widget the agency owns.",
                "keyword": ["widgets"],
                "modified": "2025-01-15",
                "publisher": {"name": "Agency of Widgets"},
                "contactPoint": {
                    "fn": "Widget Desk",
                    "hasEmail": "mailto:widgets@agency.gov",
                },
                "identifier": "widget-001",
                "accessLevel": "public",
            }
        ],
    }


@pytest.fixture
def sample_v1_1_series_catalog():
    return {
        "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
        "dataset": [
            {
                "title": "Annual Widget Releases",
                "description": "Series container for annual widget datasets.",
                "keyword": ["widgets"],
                "modified": "2025-01-15",
                "publisher": {"name": "Agency of Widgets"},
                "contactPoint": {
                    "fn": "Widget Desk",
                    "hasEmail": "mailto:widgets@agency.gov",
                },
                "identifier": "https://example.gov/series/widget-series",
                "accessLevel": "public",
            },
            {
                "title": "Widget Inventory 2024",
                "description": "Widget inventory for 2024.",
                "keyword": ["widgets"],
                "modified": "2025-01-16",
                "publisher": {"name": "Agency of Widgets"},
                "contactPoint": {
                    "fn": "Widget Desk",
                    "hasEmail": "mailto:widgets@agency.gov",
                },
                "identifier": "widget-2024",
                "accessLevel": "public",
                "distribution": [
                    {
                        "downloadURL": "https://example.gov/widgets-2024.csv",
                        "mediaType": "text/csv"
                    }
                ],
                "isPartOf": "https://example.gov/series/widget-series"
            },
            {
                "title": "Widget Inventory 2025",
                "description": "Widget inventory for 2025.",
                "keyword": ["widgets"],
                "modified": "2025-01-17",
                "publisher": {"name": "Agency of Widgets"},
                "contactPoint": {
                    "fn": "Widget Desk",
                    "hasEmail": "mailto:widgets@agency.gov",
                },
                "identifier": "widget-2025",
                "accessLevel": "public",
                "distribution": [
                    {
                        "downloadURL": "https://example.gov/widgets-2025.csv",
                        "mediaType": "text/csv"
                    }
                ],
                "isPartOf": "https://example.gov/series/widget-series"
            }
        ]
    }


class TestMain:

    def test_convert_promotes_legacy_is_part_of_to_dataset_series(self, sample_v1_1_series_catalog):
        converted = convert.convert_dcat_catalog(sample_v1_1_series_catalog)

        assert converted["dataset"] == []
        assert len(converted["datasetSeries"]) == 1

        series = converted["datasetSeries"][0]
        assert series["@type"] == "DatasetSeries"
        assert series["@id"] == "https://example.gov/series/widget-series"
        assert "identifier" not in series
        assert isinstance(series["contactPoint"], list)
        assert "first" not in series
        assert "last" not in series
        assert [member["identifier"] for member in series["seriesMember"]] == [
            "widget-2024",
            "widget-2025",
        ]
        assert all("isPartOf" not in member for member in series["seriesMember"])

    def test_writes_catalog_on_success(self, sample_v1_1_catalog, tmp_path):
        output_dir = tmp_path / "out"
        with mock.patch.object(
            convert, "fetch_dcat_catalog", return_value=sample_v1_1_catalog
        ):
            result = CliRunner().invoke(
                convert.main,
                ["-u", "https://example.gov/data.json", "-o", str(output_dir)],
            )

        assert result.exit_code == 0, result.output
        assert "Could not convert." not in result.output

        output_file = output_dir / "catalog.json"
        assert output_file.exists()
        written = json.loads(output_file.read_text(encoding="utf-8"))
        assert written["conformsTo"]["title"] == "DCAT-US 3.0"

    def test_cli_reports_success_for_dataset_series_conversion(self, sample_v1_1_series_catalog, tmp_path):
        output_dir = tmp_path / "out"
        with mock.patch.object(
            convert, "fetch_dcat_catalog", return_value=sample_v1_1_series_catalog
        ):
            result = CliRunner().invoke(
                convert.main,
                ["-u", "https://example.gov/data.json", "-o", str(output_dir)],
            )

        assert result.exit_code == 0, result.output
        assert '"conversion_successful": true' in result.output

        output_file = output_dir / "catalog.json"
        assert output_file.exists()
        written = json.loads(output_file.read_text(encoding="utf-8"))
        assert written["dataset"] == []
        assert len(written["datasetSeries"]) == 1

    def test_dry_run_does_not_write(self, sample_v1_1_catalog, tmp_path):
        output_dir = tmp_path / "out"
        with mock.patch.object(
            convert, "fetch_dcat_catalog", return_value=sample_v1_1_catalog
        ):
            result = CliRunner().invoke(
                convert.main,
                [
                    "--dry-run",
                    "-u", "https://example.gov/data.json",
                    "-o", str(output_dir),
                ],
            )

        assert result.exit_code == 0, result.output
        assert "Dry run complete." in result.output
        assert not (output_dir / "catalog.json").exists()

    def test_exits_nonzero_on_fetch_failure(self, tmp_path):
        output_dir = tmp_path / "out"
        with mock.patch.object(
            convert,
            "fetch_dcat_catalog",
            side_effect=convert.CatalogFetchException("boom"),
        ):
            result = CliRunner().invoke(
                convert.main,
                ["-u", "https://example.gov/data.json", "-o", str(output_dir)],
            )

        assert result.exit_code == 1
        assert not (output_dir / "catalog.json").exists()
