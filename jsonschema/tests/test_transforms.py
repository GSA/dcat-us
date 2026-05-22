from transforms import transform_temporal


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

    def test_mutates_in_place_and_returns_same_object(self):
        dataset = {"temporal": "2020-01-01/2020-12-31"}
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
