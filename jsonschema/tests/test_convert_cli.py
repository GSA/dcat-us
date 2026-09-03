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


class TestMain:

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
