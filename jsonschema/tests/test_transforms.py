import copy
import pytest

from transforms import (
    propagate_license,
    transform_access_rights,
    transform_language,
    transform_modified,
    transform_temporal,
)


class TestPropagateLicense:

    def test_copies_to_all_distributions(self):
        result = propagate_license({
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "distribution": [
                {"title": "CSV", "downloadURL": "https://agency.gov/data.csv"},
                {"title": "JSON", "downloadURL": "https://agency.gov/data.json"},
            ],
        })
        assert result["distribution"][0]["license"] == "https://creativecommons.org/publicdomain/zero/1.0/"
        assert result["distribution"][1]["license"] == "https://creativecommons.org/publicdomain/zero/1.0/"

    def test_preserves_existing_distribution_license(self):
        result = propagate_license({
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "distribution": [
                {"title": "CSV", "license": "https://opensource.org/licenses/MIT"},
                {"title": "JSON"},
            ],
        })
        # First distribution keeps its own license.
        assert result["distribution"][0]["license"] == "https://opensource.org/licenses/MIT"
        # Second distribution gets the dataset-level one.
        assert result["distribution"][1]["license"] == "https://creativecommons.org/publicdomain/zero/1.0/"

    def test_does_not_remove_dataset_level_license(self):
        result = propagate_license({
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "distribution": [{"title": "CSV"}],
        })
        assert result["license"] == "https://creativecommons.org/publicdomain/zero/1.0/"


class TestTransformAccessRights:

    @pytest.mark.parametrize("access_level, expected_rights", [
        ("public",            "public"),
        ("restricted public", "Access restricted. Contact the publisher to request access."),
        ("non-public",        "Not available for public release. Contact the publisher for more information."),
    ])
    def test_adds_access_rights_for_known_levels(self, access_level, expected_rights):
        result = transform_access_rights({"accessLevel": access_level})
        assert result["accessRights"] == expected_rights

    def test_does_not_remove_access_level(self):
        result = transform_access_rights({"accessLevel": "public"})
        assert result["accessLevel"] == "public"

    def test_preserves_existing_access_rights(self):
        result = transform_access_rights({
            "accessLevel": "public",
            "accessRights": "Access restricted. Contact the publisher to request access.",
        })
        assert result["accessRights"] == "Access restricted. Contact the publisher to request access."
        assert result["accessLevel"] == "public"


class TestTransformLanguage:

    @pytest.mark.parametrize("tags, expected", [
        (["en-US"],                ["en"]),
        (["en-US", "es-MX"],       ["en", "es"]),
        (["en"],                   ["en"]),
        (["EN-US"],                ["en"]),
        (["zh-Hant-TW"],           ["zh"]),
        ([],                       []),
    ])
    def test_truncates_tags(self, tags, expected):
        assert transform_language({"language": tags})["language"] == expected

    def test_truncates_on_distributions(self):
        result = transform_language({
            "language": ["en-US"],
            "distribution": [{"language": ["fr-CA"]}, {"title": "no lang"}],
        })
        assert result["language"] == ["en"]
        assert result["distribution"][0]["language"] == ["fr"]
        assert result["distribution"][1] == {"title": "no lang"}

    @pytest.mark.parametrize("dataset", [
        {},
        {"title": "no language"},
        {"language": "en-US"},        # not a list: leave alone
        {"language": None},           # not a list: leave alone
        {"language": {"tag": "en"}},  # not a list: leave alone
    ])
    def test_noop_when_shape_unexpected(self, dataset):
        original = dict(dataset)
        assert transform_language(dataset) == original

    def test_drops_non_string_tags(self):
        # Permissive: skip the bad entries rather than raising.
        result = transform_language({"language": ["en-US", 42, "fr-CA"]})
        assert result["language"] == ["en", "fr"]


class TestTransformModified:

    def test_moves_repeating_interval_to_accrual_periodicity(self):
        result = transform_modified({"modified": "R/P1Y", "issued": "2024-10-01"})
        assert result == {
            "modified": "2024-10-01",
            "issued": "2024-10-01",
            "accrualPeriodicity": "annually",
        }

    @pytest.mark.parametrize("interval, expected_periodicity", [
        ("R/P1D", "daily"),
        ("R/P1W", "weekly"),
        ("R/P1M", "monthly"),
        ("R/P3M", "quarterly"),
        ("R/P1Y", "annually"),
        ("R/P2Y", "R/P2Y"),    # unmapped -> passthrough
        ("R5/P1Y", "R5/P1Y"),  # unmapped -> passthrough
    ])
    def test_handles_various_repeating_intervals(self, interval, expected_periodicity):
        result = transform_modified({"modified": interval, "issued": "2024-10-01"})
        assert result["accrualPeriodicity"] == expected_periodicity
        assert result["modified"] == "2024-10-01"

    @pytest.mark.parametrize("dataset", [
        {},
        {"title": "no modified"},
        {"modified": "2024-10-01"},                # concrete date
        {"modified": "2024-10-01T12:30:00Z"},      # concrete Zulu datetime (preserved)
        {"modified": None},                        # not a string
        {"modified": "R/P1Y"},                     # no issued to fall back on
        {"modified": "R/P1Y", "issued": ""},       # empty issued
    ])
    def test_noop_when_no_transform_needed(self, dataset):
        original = dict(dataset)
        assert transform_modified(dataset) == original

    def test_truncates_non_zulu_datetime(self):
        result = transform_modified({"modified": "2024-10-01T12:30:00"})
        assert result == {"modified": "2024-10-01"}


class TestTransformTemporal:

    @pytest.mark.parametrize("temporal, expected", [
        # start/end
        ("2020-01-01/2020-12-31",
            {"@type": "PeriodOfTime", "startDate": "2020-01-01", "endDate": "2020-12-31"}),
        # start/end with datetimes — time component is dropped
        ("2000-01-15T00:00:00+00:00/2010-01-15T00:00:00+00:00",
            {"@type": "PeriodOfTime", "startDate": "2000-01-15", "endDate": "2010-01-15"}),
        # start/duration — duration side doesn't parse as a date, so it's dropped
        ("2020-01-01/P1Y",
            {"@type": "PeriodOfTime", "startDate": "2020-01-01"}),
        # duration/end
        ("P1Y/2020-12-31",
            {"@type": "PeriodOfTime", "endDate": "2020-12-31"}),
    ])
    def test_converts_interval(self, temporal, expected):
        result = transform_temporal({"temporal": temporal})
        assert result["temporal"] == [expected]

    @pytest.mark.parametrize("dataset", [
        {},
        {"title": "no temporal"},
        {"temporal": None},                          # not a string
        {"temporal": ["2020-01-01/2020-12-31"]},     # not a string
        {"temporal": "2020-01-01"},                  # no slash
        {"temporal": "2020-01-01/2020-12-31/extra"}, # too many slashes
        {"temporal": "P1Y/P2Y"},                     # neither side is a date
        {"temporal": "Potato/Pineapple"},            # neither side is a date
    ])
    def test_noop_when_shape_unexpected(self, dataset):
        original = dict(dataset)
        # We allow the function to mutate `dataset["temporal"]` only when
        # at least one side parses — none of these cases should change.
        assert transform_temporal(dataset) == original
