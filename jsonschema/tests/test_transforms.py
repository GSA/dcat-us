import pytest

from transforms import (
    transform_language,
    transform_modified,
    transform_temporal,
)


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
            "accrualPeriodicity": "R/P1Y",
        }

    @pytest.mark.parametrize("interval", ["R/P1Y", "R/P1D", "R/P2Y", "R5/P1Y"])
    def test_handles_various_repeating_intervals(self, interval):
        result = transform_modified({"modified": interval, "issued": "2024-10-01"})
        assert result["accrualPeriodicity"] == interval
        assert result["modified"] == "2024-10-01"

    @pytest.mark.parametrize("dataset", [
        {},
        {"title": "no modified"},
        {"modified": "2024-10-01"},                # concrete date
        {"modified": "2024-10-01T12:30:00Z"},      # concrete datetime
        {"modified": None},                        # not a string
        {"modified": "R/P1Y"},                     # no issued to fall back on
        {"modified": "R/P1Y", "issued": ""},       # empty issued
    ])
    def test_noop_when_no_transform_needed(self, dataset):
        original = dict(dataset)
        assert transform_modified(dataset) == original


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