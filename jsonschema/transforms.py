"""Dataset-level transformations from DCAT-US v1.1 to v3.0.

Each public function takes a dataset dict and returns a transformed copy when a
transformation applies.
"""

import copy
import re

from convert_dcat_1_1_to_3_0 import CatalogConversionException


ACCESS_RIGHTS_BY_LEVEL = {
    "public": "public",
    "restricted public": "Access restricted. Contact the publisher to request access.",
    "non-public": "Not available for public release. Contact the publisher for more information.",
}


REPEATING_INTERVAL_REGEX = re.compile(r"^R\d*/")

# ISO 8601 date or datetime: YYYY-MM-DD, optionally followed by a time
# component (T HH:MM[:SS[.fff]]) and optionally a timezone (Z or ±HH:MM).
# Does not validate that the date itself is real (e.g. 2020-02-30 matches).
DATE_REGEX = re.compile(
    r"^\d{4}-\d{2}-\d{2}"
    r"(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?)?$"
)


# ISO 8601 duration: PnYnMnDTnHnMnS, where each component is optional but
# at least one numeric component must be present. The 'T' separator is
# required if and only if any time component (H/M/S) is present.
DURATION_REGEX = re.compile(
    r"^P"
    r"(?=\d|T\d)"                              # require at least one component
    r"(?:\d+Y)?(?:\d+M)?(?:\d+D)?"             # date part
    r"(?:T(?=\d)(?:\d+H)?(?:\d+M)?(?:\d+S)?)?" # optional time part
    r"$"
)


def propagate_license(dataset: dict) -> dict:
    """Copy dataset-level `license` down to each Distribution
    that does not already declare one.

    Does not remove the dataset-level `license`. Returns the dataset
    unchanged if there is no license on the dataset or no distributions
    to copy it to.
    """
    return dataset  # TODO: implement


def transform_access_rights(dataset: dict) -> dict:
    """Add `accessRights` based on the existing `accessLevel`.

    Does not remove `accessLevel`. Returns the dataset unchanged if
    `accessLevel` is missing or `accessRights` is already set.
    """

    if "accessRights" in dataset:
        return dataset

    access_level = dataset.get("accessLevel")
    if access_level not in ACCESS_RIGHTS_BY_LEVEL:
        return dataset

    new_dataset = copy.deepcopy(dataset)
    new_dataset["accessRights"] = ACCESS_RIGHTS_BY_LEVEL[access_level]
    return new_dataset


def transform_conforms_to(dataset: dict) -> dict:
    """Convert `conformsTo` from a URI string to an array containing a
    Standard object, on both the Dataset and each nested Distribution.

    Per the DCAT-US v3.0 migration guide's "Additional improvements"
    section. Leaves values that are already arrays alone, and leaves
    objects (non-list, non-string) alone.
    """
    new_dataset = copy.deepcopy(dataset)
    _upgrade_conforms_to(new_dataset)
    for distribution in new_dataset.get("distribution", []):
        _upgrade_conforms_to(distribution)
    return new_dataset


def transform_described_by(dataset: dict) -> dict:
    """Convert `describedBy` from a URL string to a Distribution object,
    at both the Dataset level and on each nested Distribution.

    Folds `describedByType` (v1.1) into the new Distribution's `mediaType`.
    Per the DCAT-US v3.0 migration guide's "Additional improvements"
    section. Leaves `describedBy` alone where it is absent or already an
    object.
    """
    new_dataset = copy.deepcopy(dataset)
    _upgrade_described_by(new_dataset)
    for distribution in new_dataset.get("distribution", []):
        _upgrade_described_by(distribution)
    return new_dataset


def transform_landing_page(dataset: dict) -> dict:
    """Convert `landingPage` from a URL string to a Document object
    with `title` and `accessURL`.

    The title is reused from the dataset's `title` field. Returns the
    dataset unchanged if `landingPage` is absent or not a string.
    """
    if "landingPage" not in dataset:
        return dataset

    value = dataset["landingPage"]
    if not isinstance(value, str):
        return dataset

    new_dataset = copy.deepcopy(dataset)
    document = {"@type": "Document", "accessURL": value}
    if "title" in new_dataset:
        document["title"] = new_dataset["title"]
    new_dataset["landingPage"] = document
    return new_dataset


def transform_language(dataset: dict) -> dict:
    """Truncate RFC 5646 language tags to two-letter ISO 639-1
    on the dataset and any nested Distribution objects.

    Returns the dataset unchanged if no `language` field is present at
    either level.

    Raises CatalogConversionException if `language` is present but not a
    list, or if any element of the list is not a string.
    """
    new_dataset = copy.deepcopy(dataset)

    if "language" in new_dataset:
        _coerce_language_list(new_dataset, "dataset")

    for i, distribution in enumerate(new_dataset.get("distribution", [])):
        if "language" in distribution:
            _coerce_language_list(distribution, f"distribution[{i}]")

    return new_dataset


def transform_modified(dataset: dict) -> dict:
    """Move ISO 8601 repeating intervals out of `modified`.

    If `dataset["modified"]` is a repeating interval (e.g. "R/P1Y"), return
    a copy with that value moved to `accrualPeriodicity` and `modified`
    replaced with a concrete date. Otherwise return the dataset unchanged.

    Raises CatalogConversionException when `modified` is a repeating
    interval and no concrete date is available to substitute.
    """
    modified = dataset.get("modified")
    if not _is_repeating_interval(modified):
        return dataset

    concrete_date = dataset.get("issued")
    if not concrete_date:
        raise CatalogConversionException(
            f"`modified` is a repeating interval ({modified!r}) and no "
            "concrete date is available to substitute."
        )

    result = copy.deepcopy(dataset)

    existing = result.get("accrualPeriodicity")
    if existing and existing != modified:
        raise CatalogConversionException(
            f"Cannot move {modified!r} from `modified` to `accrualPeriodicity`: "
            f"field already set to {existing!r}."
        )

    result["accrualPeriodicity"] = modified
    result["modified"] = concrete_date
    return result


def transform_rights(dataset: dict) -> dict:
    """Convert `rights` from a single string to an array of strings.

    Per the DCAT-US v3.0 migration guide's "Additional improvements"
    section. Returns the dataset unchanged if `rights` is absent or
    already a list.
    """
    if "rights" not in dataset:
        return dataset

    value = dataset["rights"]
    if isinstance(value, list):
        return dataset

    new_dataset = copy.deepcopy(dataset)
    new_dataset["rights"] = [value]
    return new_dataset


def transform_spatial(dataset: dict) -> dict:
    """Convert `spatial` from a plain string or bbox string to a
    list of Location objects.

    Detects bbox format ("<minLon>,<minLat>,<maxLon>,<maxLat>") and emits
    a POLYGON WKT; otherwise treats the value as a prefLabel. Returns the
    dataset unchanged if `spatial` is absent.

    Raises CatalogConversionException if `spatial` is present but not a
    string.
    """
    if "spatial" not in dataset:
        return dataset

    value = dataset["spatial"]
    if not isinstance(value, str):
        raise CatalogConversionException(
            f"`spatial` must be a string, got {type(value).__name__}."
        )

    new_dataset = copy.deepcopy(dataset)
    bbox = _parse_bbox(value)
    if bbox is not None:
        new_dataset["spatial"] = [{
            "@type": "Location",
            "bbox": _bbox_to_polygon_wkt(bbox),
        }]
    else:
        new_dataset["spatial"] = [{
            "@type": "Location",
            "prefLabel": value,
        }]
    return new_dataset


def transform_sub_organization_of(dataset: dict) -> dict:
    """Wrap `publisher.subOrganizationOf` (and any nested chain of the
    same field) in arrays.

    In v1.1, `subOrganizationOf` is a single Organization object that
    can nest recursively. In v3.0, it must be an array of Organization
    objects (or null). Walks the chain and wraps each level.

    Returns the dataset unchanged if there is no publisher or no
    `subOrganizationOf` to wrap. Leaves values that are already arrays
    alone.
    """
    if "publisher" not in dataset:
        return dataset

    publisher = dataset["publisher"]
    if not isinstance(publisher, dict) or "subOrganizationOf" not in publisher:
        return dataset

    new_dataset = copy.deepcopy(dataset)
    _wrap_sub_organization_of(new_dataset["publisher"])
    return new_dataset


def transform_temporal(dataset: dict) -> dict:
    """Convert `temporal` from an ISO 8601 interval string to a
    list of PeriodOfTime objects.

    Handles three input shapes:
      - "<start>/<end>"      -> {startDate, endDate}
      - "<start>/<duration>" -> {startDate}            (duration discarded)
      - "<duration>/<end>"   -> {endDate}              (duration discarded)

    Datetime values are normalized to dates (the time component is dropped).
    Returns the dataset unchanged if `temporal` is absent.

    Raises CatalogConversionException if `temporal` is not a well-formed
    ISO 8601 interval (exactly one '/' separating two non-empty tokens,
    each token a valid ISO 8601 date/datetime or duration, with at least
    one of the two tokens being a date).
    """
    if "temporal" not in dataset:
        return dataset

    value = dataset["temporal"]
    if not isinstance(value, str):
        raise CatalogConversionException(
            f"`temporal` must be a string, got {type(value).__name__}."
        )

    parts = value.split("/")
    if len(parts) != 2 or not all(parts):
        raise CatalogConversionException(
            f"`temporal` must be an ISO 8601 interval of the form "
            f"'<start>/<end>', '<start>/<duration>', or "
            f"'<duration>/<end>'; got {value!r}."
        )
    left, right = parts

    left_kind = _classify_interval_token(left)
    right_kind = _classify_interval_token(right)

    if left_kind is None or right_kind is None:
        bad = left if left_kind is None else right
        raise CatalogConversionException(
            f"`temporal` token {bad!r} in interval {value!r} is not a "
            "valid ISO 8601 date, datetime, or duration."
        )

    if left_kind == "duration" and right_kind == "duration":
        raise CatalogConversionException(
            f"`temporal` interval {value!r} has two durations and no "
            "concrete date; cannot produce a PeriodOfTime."
        )

    period: dict = {"@type": "PeriodOfTime"}
    if left_kind == "duration":
        period["endDate"] = _normalize_to_date(right)
    elif right_kind == "duration":
        period["startDate"] = _normalize_to_date(left)
    else:
        period["startDate"] = _normalize_to_date(left)
        period["endDate"] = _normalize_to_date(right)

    new_dataset = copy.deepcopy(dataset)
    new_dataset["temporal"] = [period]
    return new_dataset


def _coerce_language_list(obj: dict, context: str) -> None:
    """Validate and normalize `obj['language']` in place.

    Raises CatalogConversionException if the value is not a list of
    strings.
    """
    value = obj["language"]
    if not isinstance(value, list):
        raise CatalogConversionException(
            f"`language` on {context} must be a list of RFC 5646 tags, "
            f"got {type(value).__name__}: {value!r}."
        )
    for i, tag in enumerate(value):
        if not isinstance(tag, str):
            raise CatalogConversionException(
                f"`language[{i}]` on {context} must be a string, "
                f"got {type(tag).__name__}: {tag!r}."
            )
    obj["language"] = [_to_iso_639_1(tag) for tag in value]


def _is_repeating_interval(value) -> bool:
    return isinstance(value, str) and bool(REPEATING_INTERVAL_REGEX.match(value))


def _is_duration(token: str) -> bool:
    """Return True if `token` is a syntactically valid ISO 8601 duration.

    Matches the grammar PnYnMnDTnHnMnS where each component is optional
    but at least one numeric component must be present. Does not accept
    fractional components or the alternative week ('PnW') / date-form
    ('P[YYYY-MM-DD]') notations.
    """
    return bool(DURATION_REGEX.match(token))


def _is_date(token: str) -> bool:
    """Return True if `token` matches the ISO 8601 date or datetime
    grammar (YYYY-MM-DD with optional time/timezone). Does not validate
    that the date is a real calendar date.
    """
    return bool(DATE_REGEX.match(token))


def _classify_interval_token(token: str) -> str | None:
    """Classify one side of an ISO 8601 interval. Returns 'date',
    'duration', or None if the token matches neither grammar.
    """
    if _is_date(token):
        return "date"
    if _is_duration(token):
        return "duration"
    return None


def _normalize_to_date(token: str) -> str:
    """Strip any time component from an ISO 8601 datetime, returning
    just the date portion. '2000-01-15T00:00:00Z' -> '2000-01-15'.
    Leaves date-only strings unchanged.
    """
    return token.split("T", 1)[0]


def _upgrade_described_by(obj: dict) -> None:
    """Upgrade `describedBy` in place from a URL string to a Distribution
    object, consuming `describedByType` (removed from `obj`, folded into
    the new Distribution's `mediaType`).
    """
    if "describedBy" not in obj:
        return
    value = obj["describedBy"]
    if not isinstance(value, str):
        return
    distribution = {"accessURL": value}
    if "describedByType" in obj:
        distribution["mediaType"] = obj.pop("describedByType")
    obj["describedBy"] = distribution


def _upgrade_conforms_to(obj: dict) -> None:
    """Upgrade `conformsTo` on `obj` in place from a URI string to an
    array containing a Standard object."""
    if "conformsTo" not in obj:
        return
    value = obj["conformsTo"]
    if isinstance(value, list):
        return
    if not isinstance(value, str):
        return
    obj["conformsTo"] = [{"@type": "Standard", "identifier": value}]


def _wrap_sub_organization_of(organization: dict) -> None:
    """Recursively wrap `subOrganizationOf` in arrays, in place.

    Assumes `organization` is a v1.1-shaped Organization where
    `subOrganizationOf`, if present, is a single Organization object.
    Walks the chain and wraps each level.
    """
    if "subOrganizationOf" not in organization:
        return
    parent = organization["subOrganizationOf"]
    if isinstance(parent, list):
        # Already an array (recurse into each element in case any
        # element still has an unwrapped subOrganizationOf).
        for element in parent:
            if isinstance(element, dict):
                _wrap_sub_organization_of(element)
        return
    if not isinstance(parent, dict):
        return
    _wrap_sub_organization_of(parent)
    organization["subOrganizationOf"] = [parent]


def _to_iso_639_1(tag: str) -> str:
    """Reduce an RFC 5646 language tag (e.g. 'en-US') to its ISO 639-1
    primary subtag ('en'). Lowercases the result."""
    return tag.split("-", 1)[0].lower()


def _parse_bbox(value: str) -> tuple[float, float, float, float] | None:
    """Return (minLon, minLat, maxLon, maxLat) if `value` is a comma-
    separated bbox string, otherwise None."""
    parts = [p.strip() for p in value.split(",")]
    if len(parts) != 4:
        return None
    try:
        nums = tuple(float(p) for p in parts)
    except ValueError:
        return None
    return nums  # type: ignore[return-value]


def _bbox_to_polygon_wkt(bbox: tuple[float, float, float, float]) -> str:
    """Convert (minLon, minLat, maxLon, maxLat) to a closed POLYGON WKT
    string. The ring is traversed counter-clockwise and closes by
    repeating the first vertex."""
    min_lon, min_lat, max_lon, max_lat = bbox
    return (
        f"POLYGON(({min_lon} {min_lat}, "
        f"{max_lon} {min_lat}, "
        f"{max_lon} {max_lat}, "
        f"{min_lon} {max_lat}, "
        f"{min_lon} {min_lat}))"
    )
