import copy

import pytest

from convert_dcat_1_1_to_3_0 import CatalogConversionException
from transforms import (
    transform_language,
    transform_modified,
    transform_temporal,
)


class TestTransformLanguage:
    """Tests for transform_language."""

    # --- happy path: dataset-level ---

    def test_truncates_rfc_5646_tag_to_iso_639_1(self):
        dataset = {"language": ["en-US"]}
        result = transform_language(dataset)
        assert result == {"language": ["en"]}

    def test_handles_multiple_tags(self):
        dataset = {"language": ["en-US", "es-MX", "fr-CA"]}
        result = transform_language(dataset)
        assert result == {"language": ["en", "es", "fr"]}

    def test_passes_through_bare_iso_639_1_tag(self):
        dataset = {"language": ["en"]}
        result = transform_language(dataset)
        assert result == {"language": ["en"]}

    def test_lowercases_primary_subtag(self):
        dataset = {"language": ["EN-US"]}
        result = transform_language(dataset)
        assert result == {"language": ["en"]}

    def test_handles_extended_subtags(self):
        # Anything after the first '-' is dropped.
        dataset = {"language": ["zh-Hant-TW"]}
        result = transform_language(dataset)
        assert result == {"language": ["zh"]}

    def test_empty_list_left_as_empty_list(self):
        dataset = {"language": []}
        result = transform_language(dataset)
        assert result == {"language": []}

    # --- happy path: distribution-level ---

    def test_truncates_language_on_distributions(self):
        dataset = {
            "distribution": [
                {"language": ["en-US"]},
                {"language": ["es-MX", "fr-CA"]},
            ],
        }
        result = transform_language(dataset)
        assert result["distribution"][0]["language"] == ["en"]
        assert result["distribution"][1]["language"] == ["es", "fr"]

    def test_distribution_without_language_left_alone(self):
        dataset = {
            "language": ["en-US"],
            "distribution": [
                {"language": ["fr-CA"]},
                {"title": "no language here"},
            ],
        }
        result = transform_language(dataset)
        assert result["distribution"][0]["language"] == ["fr"]
        assert result["distribution"][1] == {"title": "no language here"}

    def test_transforms_dataset_and_distributions_together(self):
        dataset = {
            "language": ["en-US"],
            "distribution": [{"language": ["fr-CA"]}],
        }
        result = transform_language(dataset)
        assert result["language"] == ["en"]
        assert result["distribution"][0]["language"] == ["fr"]

    # --- passthrough ---

    def test_returns_dataset_unchanged_when_language_absent(self):
        dataset = {"title": "No language here"}
        result = transform_language(dataset)
        assert result == {"title": "No language here"}

    def test_empty_dataset_returned_as_is(self):
        assert transform_language({}) == {}

    def test_no_language_on_dataset_or_distributions(self):
        dataset = {
            "title": "Dataset",
            "distribution": [{"title": "Dist"}],
        }
        result = transform_language(dataset)
        assert result == dataset

    # --- non-mutation ---

    def test_does_not_mutate_input(self):
        dataset = {
            "language": ["en-US"],
            "distribution": [{"language": ["fr-CA"]}],
        }
        original = copy.deepcopy(dataset)
        transform_language(dataset)
        assert dataset == original

    # --- error: bad shape on dataset ---

    def test_raises_when_dataset_language_is_string(self):
        with pytest.raises(CatalogConversionException, match="dataset"):
            transform_language({"language": "en-US"})

    def test_raises_when_dataset_language_is_none(self):
        with pytest.raises(CatalogConversionException, match="dataset"):
            transform_language({"language": None})

    def test_raises_when_dataset_language_is_dict(self):
        with pytest.raises(CatalogConversionException, match="dataset"):
            transform_language({"language": {"tag": "en-US"}})

    def test_raises_when_dataset_language_contains_non_string(self):
        with pytest.raises(CatalogConversionException, match=r"language\[1\]"):
            transform_language({"language": ["en-US", None, "fr-CA"]})

    def test_raises_when_dataset_language_contains_number(self):
        with pytest.raises(CatalogConversionException, match=r"language\[0\]"):
            transform_language({"language": [42]})

    # --- error: bad shape on distribution ---

    def test_raises_when_distribution_language_is_string(self):
        dataset = {"distribution": [{"language": "en-US"}]}
        with pytest.raises(CatalogConversionException, match=r"distribution\[0\]"):
            transform_language(dataset)

    def test_error_message_identifies_which_distribution(self):
        dataset = {
            "distribution": [
                {"language": ["en-US"]},
                {"language": "fr-CA"},  # bad
            ],
        }
        with pytest.raises(CatalogConversionException, match=r"distribution\[1\]"):
            transform_language(dataset)

    def test_raises_when_distribution_language_contains_non_string(self):
        dataset = {"distribution": [{"language": ["en-US", 42]}]}
        with pytest.raises(CatalogConversionException, match=r"distribution\[0\]"):
            transform_language(dataset)


class TestTransformModified:
    """Tests for transform_modified."""

    # --- non-repeating values: passthrough ---

    def test_returns_dataset_unchanged_when_modified_is_concrete_date(self):
        dataset = {"modified": "2024-10-01"}
        result = transform_modified(dataset)
        assert result == {"modified": "2024-10-01"}

    def test_returns_dataset_unchanged_when_modified_absent(self):
        dataset = {"title": "No modified here"}
        result = transform_modified(dataset)
        assert result == {"title": "No modified here"}

    def test_empty_dataset_returned_as_is(self):
        assert transform_modified({}) == {}

    def test_concrete_datetime_left_untouched(self):
        # Function only acts on repeating intervals; other formats pass through.
        dataset = {"modified": "2024-10-01T12:30:00Z"}
        result = transform_modified(dataset)
        assert result == {"modified": "2024-10-01T12:30:00Z"}

    def test_non_string_modified_left_untouched(self):
        dataset = {"modified": None}
        result = transform_modified(dataset)
        assert result == {"modified": None}

    # --- repeating intervals: move to accrualPeriodicity ---

    def test_moves_repeating_interval_to_accrual_periodicity(self):
        dataset = {"modified": "R/P1Y", "issued": "2024-10-01"}
        result = transform_modified(dataset)
        assert result["accrualPeriodicity"] == "R/P1Y"

    def test_replaces_modified_with_concrete_date(self):
        dataset = {"modified": "R/P1Y", "issued": "2024-10-01"}
        result = transform_modified(dataset)
        assert result["modified"] == "2024-10-01"

    def test_preserves_other_dataset_fields(self):
        dataset = {
            "modified": "R/P1D",
            "issued": "2024-10-15",
            "title": "My Dataset",
            "identifier": "abc-123",
        }
        result = transform_modified(dataset)
        assert result["title"] == "My Dataset"
        assert result["identifier"] == "abc-123"

    def test_handles_daily_interval(self):
        dataset = {"modified": "R/P1D", "issued": "2024-10-15"}
        result = transform_modified(dataset)
        assert result["modified"] == "2024-10-15"
        assert result["accrualPeriodicity"] == "R/P1D"

    def test_handles_uncommon_interval_verbatim(self):
        # Intervals outside the common set are passed through unchanged.
        dataset = {"modified": "R/P2Y", "issued": "2024-10-01"}
        result = transform_modified(dataset)
        assert result["accrualPeriodicity"] == "R/P2Y"

    def test_handles_bounded_repeating_interval(self):
        # "R5/P1Y" means repeat 5 times — still a repeating interval.
        dataset = {"modified": "R5/P1Y", "issued": "2024-10-01"}
        result = transform_modified(dataset)
        assert result["accrualPeriodicity"] == "R5/P1Y"
        assert result["modified"] == "2024-10-01"

    # --- conflicts and missing data: raise ---

    def test_raises_when_no_concrete_date_available(self):
        dataset = {"modified": "R/P1Y"}
        with pytest.raises(CatalogConversionException):
            transform_modified(dataset)

    def test_raises_when_issued_is_empty_string(self):
        dataset = {"modified": "R/P1Y", "issued": ""}
        with pytest.raises(CatalogConversionException):
            transform_modified(dataset)

    def test_raises_when_accrual_periodicity_conflicts(self):
        dataset = {
            "modified": "R/P1Y",
            "issued": "2024-10-01",
            "accrualPeriodicity": "R/P1M",
        }
        with pytest.raises(CatalogConversionException):
            transform_modified(dataset)

    def test_does_not_raise_when_accrual_periodicity_matches(self):
        dataset = {
            "modified": "R/P1Y",
            "issued": "2024-10-01",
            "accrualPeriodicity": "R/P1Y",
        }
        result = transform_modified(dataset)
        assert result["accrualPeriodicity"] == "R/P1Y"
        assert result["modified"] == "2024-10-01"

    # --- non-mutation ---

    def test_does_not_mutate_input(self):
        dataset = {"modified": "R/P1Y", "issued": "2024-10-01"}
        original = dict(dataset)
        transform_modified(dataset)
        assert dataset == original

    def test_returns_new_object_when_transforming(self):
        dataset = {"modified": "R/P1Y", "issued": "2024-10-01"}
        result = transform_modified(dataset)
        assert result is not dataset

    def test_returns_same_object_when_no_transform_needed(self):
        # Passthrough path doesn't need a copy.
        dataset = {"modified": "2024-10-01"}
        result = transform_modified(dataset)
        assert result is dataset


class TestTransformTemporal:
    """Tests for transform_temporal."""

    # --- "<start>/<end>" ---

    def test_converts_start_end_interval(self):
        dataset = {"temporal": "2020-01-01/2020-12-31"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "startDate": "2020-01-01",
            "endDate": "2020-12-31",
        }]

    def test_returns_list_wrapping_single_period(self):
        result = transform_temporal({"temporal": "2020-01-01/2020-12-31"})
        assert isinstance(result["temporal"], list)
        assert len(result["temporal"]) == 1

    def test_preserves_other_dataset_fields(self):
        dataset = {
            "temporal": "2020-01-01/2020-12-31",
            "title": "My Dataset",
            "identifier": "abc-123",
        }
        result = transform_temporal(dataset)
        assert result["title"] == "My Dataset"
        assert result["identifier"] == "abc-123"

    def test_returns_dataset_unchanged_when_temporal_absent(self):
        dataset = {"title": "No temporal here"}
        result = transform_temporal(dataset)
        assert result == {"title": "No temporal here"}

    def test_empty_dataset_returned_as_is(self):
        assert transform_temporal({}) == {}

    def test_does_not_mutate_input(self):
        dataset = {"temporal": "2020-01-01/2020-12-31"}
        original = copy.deepcopy(dataset)
        transform_temporal(dataset)
        assert dataset == original

    def test_returns_new_object_when_transforming(self):
        dataset = {"temporal": "2020-01-01/2020-12-31"}
        result = transform_temporal(dataset)
        assert result is not dataset

    def test_returns_same_object_when_no_transform_needed(self):
        dataset = {"title": "No temporal here"}
        result = transform_temporal(dataset)
        assert result is dataset

    def test_normalizes_datetime_to_date_for_start_end(self):
        dataset = {"temporal": "2000-01-15T00:00:00Z/2010-01-15T00:00:00Z"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "startDate": "2000-01-15",
            "endDate": "2010-01-15",
        }]

    # --- "<start>/<duration>" ---

    def test_converts_start_duration_to_start_only(self):
        dataset = {"temporal": "2020-01-01/P1Y"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "startDate": "2020-01-01",
        }]

    def test_start_duration_omits_end_date(self):
        result = transform_temporal({"temporal": "2020-01-01/P6M"})
        assert "endDate" not in result["temporal"][0]

    def test_start_duration_normalizes_datetime(self):
        dataset = {"temporal": "2020-01-01T00:00:00Z/P1Y"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "startDate": "2020-01-01",
        }]

    def test_start_duration_handles_complex_duration(self):
        # Duration component is discarded regardless of its complexity.
        dataset = {"temporal": "2020-01-01/P1Y2M10DT5H"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "startDate": "2020-01-01",
        }]

    # --- "<duration>/<end>" ---

    def test_converts_duration_end_to_end_only(self):
        dataset = {"temporal": "P1Y/2020-12-31"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "endDate": "2020-12-31",
        }]

    def test_duration_end_omits_start_date(self):
        result = transform_temporal({"temporal": "P1Y/2020-12-31"})
        assert "startDate" not in result["temporal"][0]

    def test_duration_end_normalizes_datetime(self):
        dataset = {"temporal": "P1Y/2020-12-31T23:59:59Z"}
        result = transform_temporal(dataset)
        assert result["temporal"] == [{
            "@type": "PeriodOfTime",
            "endDate": "2020-12-31",
        }]

    def test_raises_on_missing_slash(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "2020-01-01"})

    def test_raises_on_multiple_slashes(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "2020-01-01/2020-12-31/extra"})

    def test_raises_on_empty_string(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": ""})

    def test_raises_on_empty_side(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "2020-01-01/"})
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "/2020-12-31"})

    def test_raises_on_non_string_temporal(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": None})
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": ["2020-01-01/2020-12-31"]})

    def test_raises_on_duration_duration_interval(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "P1Y/P2Y"})

    def test_raises_on_garbage_left_side(self):
        with pytest.raises(CatalogConversionException, match="Potato"):
            transform_temporal({"temporal": "Potato/2020-12-31"})

    def test_raises_on_garbage_right_side(self):
        with pytest.raises(CatalogConversionException, match="Pineapple"):
            transform_temporal({"temporal": "2020-01-01/Pineapple"})

    def test_raises_on_bare_p_duration(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "2020-01-01/P"})

    def test_raises_on_garbage_both_sides(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "garbage/junk"})

    def test_raises_on_incomplete_date(self):
        with pytest.raises(CatalogConversionException):
            transform_temporal({"temporal": "2020-01/2020-12"})
