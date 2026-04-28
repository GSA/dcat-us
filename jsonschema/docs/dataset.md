<a name="root"></a>

Information about a dataset, including identifiers, contacts, coverage, distributions, and related resources.

**Title:** Dataset

A collection of data published or curated by one provider

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Dataset",
    "title": "Daily Climate Observations 2024",
    "description": "Daily temperature, precipitation, and wind measurements from monitoring stations across the United States.",
    "identifier": "https://example.gov/datasets/climate-observations-2024",
    "contactPoint": {
        "fn": "Climate Data Support",
        "hasEmail": "mailto:climate@example.gov"
    },
    "publisher": {
        "name": "National Climate Data Center"
    },
    "keyword": [
        "climate",
        "weather",
        "temperature",
        "precipitation"
    ],
    "issued": "2024-01-15",
    "modified": "2024-06-01",
    "accrualPeriodicity": "daily",
    "accessRights": "public",
    "landingPage": {
        "@id": "https://example.gov/climate-data",
        "@type": "Document",
        "title": "Climate Data Landing Page"
    },
    "describedBy": {
        "@id": "https://example.gov/climate-data/data-dictionary",
        "@type": "Distribution",
        "title": "Data Dictionary",
        "mediaType": "application/pdf"
    },
    "spatial": {
        "@type": "Location",
        "bbox": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -125.0,
                        24.0
                    ],
                    [
                        -66.0,
                        24.0
                    ],
                    [
                        -66.0,
                        50.0
                    ],
                    [
                        -125.0,
                        50.0
                    ],
                    [
                        -125.0,
                        24.0
                    ]
                ]
            ]
        }
    },
    "theme": [
        "Climate Science"
    ],
    "distribution": [
        {
            "title": "Climate Data CSV",
            "downloadURL": "https://example.gov/downloads/climate-2024.csv",
            "mediaType": "text/csv"
        }
    ],
    "rights": [
        "Data is provided as-is without warranty. Please cite the National Climate Data Center when using this data."
    ],
    "temporal": [
        {
            "@type": "PeriodOfTime",
            "startDate": "2024-01-01",
            "endDate": "2024-12-31"
        }
    ]
}
```

| Property                                                 | Type                    | Requirement Level | Title/Description           |
| -------------------------------------------------------- | ----------------------- | ----------------- | --------------------------- |
| [@id](#@id)                                             | string                  | Optional          | -                           |
| [@type](#@type)                                         | string                  | Optional          | -                           |
| [otherIdentifier](#otherIdentifier)                     | null or array           | Optional          | other identifier            |
| [sample](#sample)                                       | null or array           | Optional          | sample                      |
| [status](#status)                                       | More than one type      | Optional          | lifecycle status            |
| [supportedSchema](#supportedSchema)                     | More than one type      | Optional          | supported schema            |
| [versionNotes](#versionNotes)                           | null or string          | Optional          | version notes               |
| [contactPoint](#contactPoint)                           | More than one type      | Mandatory         | contact point               |
| [distribution](#distribution)                           | null or array           | Recommended       | dataset distribution        |
| [first](#first)                                         | More than one type      | Optional          | first                       |
| [hasCurrentVersion](#hasCurrentVersion)                 | More than one type      | Optional          | current version             |
| [hasVersion](#hasVersion)                               | null or array           | Optional          | has version                 |
| [inSeries](#inSeries)                                   | null or array           | Optional          | in series                   |
| [keyword](#keyword)                                     | null or array of string | Recommended       | keyword/tag                 |
| [landingPage](#landingPage)                             | More than one type      | Recommended       | landing page                |
| [previousVersion](#previousVersion)                     | More than one type      | Optional          | previous version            |
| [qualifiedRelation](#qualifiedRelation)                 | null or array           | Optional          | qualified relation          |
| [spatialResolutionInMeters](#spatialResolutionInMeters) | null or string          | Optional          | Spatial resolution (meters) |
| [temporalResolution](#temporalResolution)               | null or string          | Optional          | temporal resolution         |
| [theme](#theme)                                         | null or array           | Recommended       | theme/category              |
| [version](#version)                                     | null or string          | Optional          | version                     |
| [describedBy](#describedBy)                             | More than one type      | Recommended       | data dictionary             |
| [liabilityStatement](#liabilityStatement)               | More than one type      | Optional          | liability statement         |
| [metadataDistribution](#metadataDistribution)           | null or array           | Optional          | metadata distribution       |
| [purpose](#purpose)                                     | null or string          | Optional          | purpose                     |
| [accessRights](#accessRights)                           | More than one type      | Optional          | access rights               |
| [accrualPeriodicity](#accrualPeriodicity)               | More than one type      | Optional          | frequency                   |
| [conformsTo](#conformsTo)                               | null or array           | Optional          | conforms to                 |
| [contributor](#contributor)                             | null or array           | Optional          | contributor                 |
| [created](#created)                                     | More than one type      | Optional          | creation date               |
| [creator](#creator)                                     | More than one type      | Optional          | creator                     |
| [description](#description)                             | string                  | Mandatory         | description                 |
| [hasPart](#hasPart)                                     | null or array           | Optional          | has part                    |
| [identifier](#identifier)                               | More than one type      | Mandatory         | identifier                  |
| [isReferencedBy](#isReferencedBy)                       | null or array of string | Optional          | is referenced by            |
| [issued](#issued)                                       | More than one type      | Optional          | release date                |
| [language](#language)                                   | More than one type      | Optional          | language                    |
| [modified](#modified)                                   | More than one type      | Recommended       | last modified               |
| [provenance](#provenance)                               | null or array of string | Optional          | provenance                  |
| [publisher](#publisher)                                 | object                  | Mandatory         | publisher                   |
| [relation](#relation)                                   | null or array of string | Optional          | related resource            |
| [replaces](#replaces)                                   | null or array           | Optional          | replaces                    |
| [rights](#rights)                                       | null or array of string | Recommended       | rights                      |
| [rightsHolder](#rightsHolder)                           | null or array           | Optional          | rights holder               |
| [source](#source)                                       | null or array           | Optional          | data source                 |
| [spatial](#spatial)                                     | More than one type      | Recommended       | spatial/geographic coverage |
| [subject](#subject)                                     | null or array           | Optional          | subject                     |
| [temporal](#temporal)                                   | null or array           | Recommended       | temporal coverage           |
| [title](#title)                                         | string                  | Mandatory         | title                       |
| [category](#category)                                   | null or array           | Optional          | category                    |
| [hasQualityMeasurement](#hasQualityMeasurement)         | null or array           | Optional          | quality measurement         |
| [page](#page)                                           | null or array           | Optional          | documentation               |
| [qualifiedAttribution](#qualifiedAttribution)           | null or array           | Optional          | qualified attribution       |
| [wasAttributedTo](#wasAttributedTo)                     | null or array           | Optional          | attribution                 |
| [wasGeneratedBy](#wasGeneratedBy)                       | null or array           | Optional          | was generated by            |
| [wasUsedBy](#wasUsedBy)                                 | null or array           | Optional          | used by                     |
| [image](#image)                                         | More than one type      | Optional          | image                       |
| [scopeNote](#scopeNote)                                 | null or string          | Optional          | usage note                  |

## <a name="@id"></a>`Dataset > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/datasets/national-climate-observations-2024"
```

## <a name="@type"></a>`Dataset > @type`

**Requirement:** Optional

| **Type**    | `string`    |
| ----------- | ----------- |
| **Default** | `"Dataset"` |

## <a name="otherIdentifier"></a>`Dataset > otherIdentifier`

**Title:** other identifier

**Requirement:** Optional

Additional identifiers for the dataset besides the main identifier, such as a DOI or other persistent ID

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                             | Description                                                                   |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [Identifier](./identifiers-and-relationships.md#identifier) | A unique identifier and optionally it's scheme and other relevant information |

## <a name="sample"></a>`Dataset > sample`

**Title:** sample

**Requirement:** Optional

List of sample distributions for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be        | Description                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------- |
| [Distribution](./distribution.md#root) | A specific representation of a dataset, such as a file, feed, or API response |

## <a name="status"></a>`Dataset > status`

**Title:** lifecycle status

**Requirement:** Optional

Lifecycle status of the dataset, such as completed, deprecated, under development, or withdrawn

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                             |
| -------------------------------------------------- |
| [Null allowed when not required](#status_anyOf_i0) |
| [Concept](#status_anyOf_i1)                        |

### <a name="status_anyOf_i0"></a>`Dataset > status > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_anyOf_i1"></a>`Dataset > status > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type                                    |
| ------------------------- | ----------------------------------------------------- |
| **Additional properties** | Any type allowed                                      |
| **Same definition as**    | [Concept](./identifiers-and-relationships.md#concept) |

## <a name="supportedSchema"></a>`Dataset > supportedSchema`

**Title:** supported schema

**Requirement:** Optional

supported schema for this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                                      |
| ----------------------------------------------------------- |
| [Null allowed when not required](#supportedSchema_anyOf_i0) |
| [Dataset](#supportedSchema_anyOf_i1)                        |

### <a name="supportedSchema_anyOf_i0"></a>`Dataset > supportedSchema > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="supportedSchema_anyOf_i1"></a>`Dataset > supportedSchema > anyOf > Dataset`

**Title:** Dataset

inline description of the supported schema

| **Type**                  | `object`                     |
| ------------------------- | ---------------------------- |
| **Additional properties** | Any type allowed             |
| **Same definition as**    | [Dataset](./dataset.md#root) |

---
**See Also:** (related supporting classes)

## <a name="versionNotes"></a>`Dataset > versionNotes`

**Title:** version notes

**Requirement:** Optional

Notes describing how this version differs from earlier versions of the dataset

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Initial release of 2024 climate observations data."
```

## <a name="contactPoint"></a>`Dataset > contactPoint`

**Title:** contact point

**Requirement:** Mandatory

A contact point for questions about the Dataset (single contact or list). Include an email address that is continuously monitored

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| Any of                                     |
| ------------------------------------------ |
| [Kind](#contactPoint_anyOf_i0)             |
| [List of contacts](#contactPoint_anyOf_i1) |

### <a name="contactPoint_anyOf_i0"></a>`Dataset > contactPoint > anyOf > Kind`

**Title:** Kind

inline description of Kind

| **Type**                  | `object`                 |
| ------------------------- | ------------------------ |
| **Additional properties** | Any type allowed         |
| **Same definition as**    | [Kind](./agents.md#kind) |

### <a name="contactPoint_anyOf_i1"></a>`Dataset > contactPoint > anyOf > List of contacts`

**Title:** List of contacts

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| [Kind](./agents.md#kind)        | Contact information for an individual or entity |

## <a name="distribution"></a>`Dataset > distribution`

**Title:** dataset distribution

**Requirement:** Recommended

List of available distributions for the dataset. This can be omitted when no distribution is available yet.

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be        | Description                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------- |
| [Distribution](./distribution.md#root) | A specific representation of a dataset, such as a file, feed, or API response |

## <a name="first"></a>`Dataset > first`

**Title:** first

**Requirement:** Optional

the first item of the sequence the dataset belongs to

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                            |
| ------------------------------------------------- |
| [Null allowed when not required](#first_anyOf_i0) |
| [Dataset](#first_anyOf_i1)                        |

### <a name="first_anyOf_i0"></a>`Dataset > first > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="first_anyOf_i1"></a>`Dataset > first > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                     |
| ------------------------- | ---------------------------- |
| **Additional properties** | Any type allowed             |
| **Same definition as**    | [Dataset](./dataset.md#root) |

---
**See Also:** (related supporting classes)

## <a name="hasCurrentVersion"></a>`Dataset > hasCurrentVersion`

**Title:** current version

**Requirement:** Optional

reference to the current (latest) version of a dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                                        |
| ------------------------------------------------------------- |
| [Null allowed when not required](#hasCurrentVersion_anyOf_i0) |
| [Dataset](#hasCurrentVersion_anyOf_i1)                        |

### <a name="hasCurrentVersion_anyOf_i0"></a>`Dataset > hasCurrentVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasCurrentVersion_anyOf_i1"></a>`Dataset > hasCurrentVersion > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                     |
| ------------------------- | ---------------------------- |
| **Additional properties** | Any type allowed             |
| **Same definition as**    | [Dataset](./dataset.md#root) |

---
**See Also:** (related supporting classes)

## <a name="hasVersion"></a>`Dataset > hasVersion`

**Title:** has version

**Requirement:** Optional

List of related Datasets that are a version, edition, or adaptation of the described Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| [Dataset](./dataset.md#root)    | A collection of data published or curated by one provider |

## <a name="inSeries"></a>`Dataset > inSeries`

**Title:** in series

**Requirement:** Optional

Dataset series this dataset belongs to

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be           | Description                                               |
| ----------------------------------------- | --------------------------------------------------------- |
| [DatasetSeries](./dataset-series.md#root) | A group of related datasets that are published separately |

## <a name="keyword"></a>`Dataset > keyword`

**Title:** keyword/tag

**Requirement:** Recommended

List of keywords or tags describing the dataset

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Examples:**

```json
[
    "climate",
    "weather",
    "temperature",
    "precipitation"
]
```

```json
[
    "climate",
    "weather",
    "temperature",
    "precipitation",
    "humidity",
    "wind",
    "meteorology"
]
```

| Each item of this array must be    | Description |
| ---------------------------------- | ----------- |
| [Non-empty string](#keyword_items) | -           |

### <a name="keyword_items"></a>Non-empty string

**Title:** Non-empty string

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="landingPage"></a>`Dataset > landingPage`

**Title:** landing page

**Requirement:** Recommended

A web page from the original data provider that gives access to the Dataset, its Distributions, and related information

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                                  |
| ------------------------------------------------------- |
| [Null allowed when not required](#landingPage_anyOf_i0) |
| [Document](#landingPage_anyOf_i1)                       |

### <a name="landingPage_anyOf_i0"></a>`Dataset > landingPage > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="landingPage_anyOf_i1"></a>`Dataset > landingPage > anyOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                     |
| ------------------------- | -------------------------------------------- |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Document](./quality-governance.md#document) |

## <a name="previousVersion"></a>`Dataset > previousVersion`

**Title:** previous version

**Requirement:** Optional

reference to the previous dataset version

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                                      |
| ----------------------------------------------------------- |
| [Null allowed when not required](#previousVersion_anyOf_i0) |
| [Dataset](#previousVersion_anyOf_i1)                        |

### <a name="previousVersion_anyOf_i0"></a>`Dataset > previousVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="previousVersion_anyOf_i1"></a>`Dataset > previousVersion > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                     |
| ------------------------- | ---------------------------- |
| **Additional properties** | Any type allowed             |
| **Same definition as**    | [Dataset](./dataset.md#root) |

---
**See Also:** (related supporting classes)

## <a name="qualifiedRelation"></a>`Dataset > qualifiedRelation`

**Title:** qualified relation

**Requirement:** Optional

Detailed relationship between the dataset and another resource, including the role of that relationship

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                                 | Description                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------- |
| [Relationship](./identifiers-and-relationships.md#relationship) | Additional information about how one resource is related to another |

## <a name="spatialResolutionInMeters"></a>`Dataset > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

**Requirement:** Optional

Smallest spatial distance between data points, in meters, represented as a single value

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"1000"
```

## <a name="temporalResolution"></a>`Dataset > temporalResolution`

**Title:** temporal resolution

**Requirement:** Optional

Smallest time interval between data points, using xsd:duration format (for example, P1D)

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"P1D"
```

## <a name="theme"></a>`Dataset > theme`

**Title:** theme/category

**Requirement:** Recommended

List of themes or categories for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                       | Description                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------ |
| [Concept](./identifiers-and-relationships.md#concept) | A controlled term or label, optionally drawn from a concept scheme |

## <a name="version"></a>`Dataset > version`

**Title:** version

**Requirement:** Optional

The version indicator (name or identifier) of a resource

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"2024.1"
```

## <a name="describedBy"></a>`Dataset > describedBy`

**Title:** data dictionary

**Requirement:** Recommended

A distribution describing the Data Dictionary for this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                                  |
| ------------------------------------------------------- |
| [Null allowed when not required](#describedBy_anyOf_i0) |
| [Distribution](#describedBy_anyOf_i1)                   |

### <a name="describedBy_anyOf_i0"></a>`Dataset > describedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="describedBy_anyOf_i1"></a>`Dataset > describedBy > anyOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                               |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Distribution](./distribution.md#root) |

---
**See Also:** (related supporting classes)

## <a name="liabilityStatement"></a>`Dataset > liabilityStatement`

**Title:** liability statement

**Requirement:** Optional

A liability statement about the dataset that may clarify limitations of responsibility, qualifications on the accuracy, reliability, and completeness of the data, or absence of endorsement by the data publisher or provider, among other considerations

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"This dataset is provided as-is without warranty of any kind. Users are responsible for determining fitness for their intended use."
```

| Any of                                                         |
| -------------------------------------------------------------- |
| [Null allowed when not required](#liabilityStatement_anyOf_i0) |
| [item 1](#liabilityStatement_anyOf_i1)                         |

### <a name="liabilityStatement_anyOf_i0"></a>`Dataset > liabilityStatement > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="liabilityStatement_anyOf_i1"></a>`Dataset > liabilityStatement > anyOf > item 1`

Full text of the liability statement

| **Type** | `string` |
| -------- | -------- |

## <a name="metadataDistribution"></a>`Dataset > metadataDistribution`

**Title:** metadata distribution

**Requirement:** Optional

Distribution of the original metadata document this dataset was derived from

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be        | Description                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------- |
| [Distribution](./distribution.md#root) | A specific representation of a dataset, such as a file, feed, or API response |

## <a name="purpose"></a>`Dataset > purpose`

**Title:** purpose

**Requirement:** Optional

The purpose of the dataset

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"To provide comprehensive, high-quality climate observations for research, planning, and decision-making related to weather and climate."
```

## <a name="accessRights"></a>`Dataset > accessRights`

**Title:** access rights

**Requirement:** Optional

Information about whether the dataset is publicly accessible, restricted, or not public

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"public"
```

```json
"Public access with no restrictions. Data is freely available for download and use."
```

| Any of                                                   |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_anyOf_i0) |
| [item 1](#accessRights_anyOf_i1)                         |

### <a name="accessRights_anyOf_i0"></a>`Dataset > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>`Dataset > accessRights > anyOf > item 1`

Text description of the access rights

| **Type** | `string` |
| -------- | -------- |

## <a name="accrualPeriodicity"></a>`Dataset > accrualPeriodicity`

**Title:** frequency

**Requirement:** Optional

The frequency at which the Dataset is updated

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"daily"
```

| Any of                                                         |
| -------------------------------------------------------------- |
| [Null allowed when not required](#accrualPeriodicity_anyOf_i0) |
| [item 1](#accrualPeriodicity_anyOf_i1)                         |
| [item 2](#accrualPeriodicity_anyOf_i2)                         |
| [item 3](#accrualPeriodicity_anyOf_i3)                         |

### <a name="accrualPeriodicity_anyOf_i0"></a>`Dataset > accrualPeriodicity > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accrualPeriodicity_anyOf_i1"></a>`Dataset > accrualPeriodicity > anyOf > item 1`

ISO 19115 Maintenance Frequency code

| **Type** | `enum (of string)` |
| -------- | ------------------ |

Must be one of:
* "continual"
* "daily"
* "weekly"
* "fortnightly"
* "monthly"
* "quarterly"
* "biannually"
* "annually"
* "asNeeded"
* "irregular"
* "notPlanned"
* "unknown"

### <a name="accrualPeriodicity_anyOf_i2"></a>`Dataset > accrualPeriodicity > anyOf > item 2`

ISO-8601 Maintenance Frequency code for recurring values, see https://www.iso.org/standard/70907.html

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                   |
| --------------------------------- | ----------------------------------------------------------------- |
| **Must match regular expression** | ```^R/P.+$``` [Test](https://regex101.com/?regex=%5ER%2FP.%2B%24) |

### <a name="accrualPeriodicity_anyOf_i3"></a>`Dataset > accrualPeriodicity > anyOf > item 3`

Dublin Core Collection Frequency Vocabulary, see https://www.dublincore.org/specifications/dublin-core/collection-description/frequency/#vocabulary-terms

| **Type** | `enum (of string)` |
| -------- | ------------------ |

Must be one of:
* "continuous"
* "daily"
* "weekly"
* "biweekly"
* "monthly"
* "quarterly"
* "semiannual"
* "annual"
* "irregular"
* "triennial"
* "biennial"
* "threeTimesAYear"
* "bimonthly"
* "semimonthly"
* "threeTimesAMonth"
* "semiweekly"
* "threeTimesAWeek"

## <a name="conformsTo"></a>`Dataset > conformsTo`

**Title:** conforms to

**Requirement:** Optional

List of standards, schemas, or profiles the dataset follows

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be              | Description                                                   |
| -------------------------------------------- | ------------------------------------------------------------- |
| [Standard](./quality-governance.md#standard) | A standard or specification that another resource conforms to |

## <a name="contributor"></a>`Dataset > contributor`

**Title:** contributor

**Requirement:** Optional

List of agents contributing to the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------- |
| [Agent](./agents.md#agent)      | A person, organization, software agent, or other entity involved with a resource |

## <a name="created"></a>`Dataset > created`

**Title:** creation date

**Requirement:** Optional

The date on which the Dataset was first created

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-01-01"
```

```json
"2024-01-15T10:30:00Z"
```

```json
"2024"
```

```json
"2024-01"
```

| Any of                                              |
| --------------------------------------------------- |
| [Null allowed when not required](#created_anyOf_i0) |
| [Date string](#created_anyOf_i1)                    |

### <a name="created_anyOf_i0"></a>`Dataset > created > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>`Dataset > created > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                               |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_anyOf_i0) |
| [item 1](#created_anyOf_i1_anyOf_i1) |
| [item 2](#created_anyOf_i1_anyOf_i2) |
| [item 3](#created_anyOf_i1_anyOf_i3) |

#### <a name="created_anyOf_i1_anyOf_i0"></a>`Dataset > created > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="created_anyOf_i1_anyOf_i1"></a>`Dataset > created > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="created_anyOf_i1_anyOf_i2"></a>`Dataset > created > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_anyOf_i3"></a>`Dataset > created > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="creator"></a>`Dataset > creator`

**Title:** creator

**Requirement:** Optional

Person or organization responsible for creating the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                              |
| --------------------------------------------------- |
| [Null allowed when not required](#creator_anyOf_i0) |
| [Agent](#creator_anyOf_i1)                          |

### <a name="creator_anyOf_i0"></a>`Dataset > creator > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="creator_anyOf_i1"></a>`Dataset > creator > anyOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Agent](./agents.md#agent) |

## <a name="description"></a>`Dataset > description`

**Title:** description

**Requirement:** Mandatory

Plain-language summary of the dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"Daily temperature, precipitation, and wind measurements from monitoring stations across the United States."
```

```json
"Comprehensive daily climate observations collected from monitoring stations across the United States, including temperature, precipitation, humidity, and wind measurements."
```

## <a name="hasPart"></a>`Dataset > hasPart`

**Title:** has part

**Requirement:** Optional

List of related datasets that are part of the described dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| [Dataset](./dataset.md#root)    | A collection of data published or curated by one provider |

## <a name="identifier"></a>`Dataset > identifier`

**Title:** identifier

**Requirement:** Mandatory

The unique identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| Any of                                                 |
| ------------------------------------------------------ |
| [Null allowed when not required](#identifier_anyOf_i0) |
| [Identifier](#identifier_anyOf_i1)                     |

### <a name="identifier_anyOf_i0"></a>`Dataset > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>`Dataset > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                          |
| ------------------------- | ----------------------------------------------------------- |
| **Additional properties** | Any type allowed                                            |
| **Same definition as**    | [Identifier](./identifiers-and-relationships.md#identifier) |

## <a name="isReferencedBy"></a>`Dataset > isReferencedBy`

**Title:** is referenced by

**Requirement:** Optional

List of links to related resources, such as publications, that reference, cite, or otherwise point to the Dataset

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "https://example.gov/publications/climate-trends-2024"
]
```

| Each item of this array must be | Description               |
| ------------------------------- | ------------------------- |
| [Link](#isReferencedBy_items)   | reference iri of Resource |

### <a name="isReferencedBy_items"></a>Link

**Title:** Link

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="issued"></a>`Dataset > issued`

**Title:** release date

**Requirement:** Optional

Date when the dataset was first published. If the exact publication date is unknown, use the date it was first referenced in the catalog.

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-01-15"
```

```json
"2024-01-15T10:30:00Z"
```

```json
"2024"
```

```json
"2024-01"
```

| Any of                                             |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>`Dataset > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>`Dataset > issued > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                              |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_anyOf_i0) |
| [item 1](#issued_anyOf_i1_anyOf_i1) |
| [item 2](#issued_anyOf_i1_anyOf_i2) |
| [item 3](#issued_anyOf_i1_anyOf_i3) |

#### <a name="issued_anyOf_i1_anyOf_i0"></a>`Dataset > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>`Dataset > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>`Dataset > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>`Dataset > issued > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>`Dataset > language`

**Title:** language

**Requirement:** Optional

ISO 639-1 language code values used in the dataset text or metadata, such as en or es, full list can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
[
    "en"
]
```

| Any of                                               |
| ---------------------------------------------------- |
| [Null allowed when not required](#language_anyOf_i0) |
| [Language code](#language_anyOf_i1)                  |
| [List of languages](#language_anyOf_i2)              |

### <a name="language_anyOf_i0"></a>`Dataset > language > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="language_anyOf_i1"></a>`Dataset > language > anyOf > Language code`

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>`Dataset > language > anyOf > List of languages`

**Title:** List of languages

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Language code](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>Language code

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="modified"></a>`Dataset > modified`

**Title:** last modified

**Requirement:** Recommended

Most recent date when the dataset's actual data changed, not just metadata

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-06-01"
```

```json
"2024-01-15T10:30:00Z"
```

```json
"2024"
```

```json
"2024-01"
```

| Any of                                               |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>`Dataset > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>`Dataset > modified > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_anyOf_i0) |
| [item 1](#modified_anyOf_i1_anyOf_i1) |
| [item 2](#modified_anyOf_i1_anyOf_i2) |
| [item 3](#modified_anyOf_i1_anyOf_i3) |

#### <a name="modified_anyOf_i1_anyOf_i0"></a>`Dataset > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>`Dataset > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>`Dataset > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>`Dataset > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="provenance"></a>`Dataset > provenance`

**Title:** provenance

**Requirement:** Optional

List of statements about the lineage of a Dataset, including any changes in its ownership or custody since its creation that may be significant for its authenticity, integrity, or interpretation

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "Data collected from automated weather stations deployed at 2,500 locations across the continental United States.",
    "Quality control procedures applied according to WMO guidelines."
]
```

| Each item of this array must be       | Description                           |
| ------------------------------------- | ------------------------------------- |
| [provenance items](#provenance_items) | Full text of the provenance statement |

### <a name="provenance_items"></a>Array Item

Full text of the provenance statement

| **Type** | `string` |
| -------- | -------- |

## <a name="publisher"></a>`Dataset > publisher`

**Title:** publisher

**Requirement:** Mandatory

Organization responsible for publishing and making the dataset available

| **Type**                  | `object`                                 |
| ------------------------- | ---------------------------------------- |
| **Required**              | Yes                                      |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | [Organization](./agents.md#organization) |

## <a name="relation"></a>`Dataset > relation`

**Title:** related resource

**Requirement:** Optional

List of links to related resources when the relationship is not otherwise specified

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "https://example.gov/datasets/historical-climate-averages"
]
```

| Each item of this array must be | Description               |
| ------------------------------- | ------------------------- |
| [Link](#relation_items)         | reference iri of Resource |

### <a name="relation_items"></a>Link

**Title:** Link

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="replaces"></a>`Dataset > replaces`

**Title:** replaces

**Requirement:** Optional

List of Datasets replaced by this Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| [Dataset](./dataset.md#root)    | A collection of data published or curated by one provider |

## <a name="rights"></a>`Dataset > rights`

**Title:** rights

**Requirement:** Recommended

Rights statements not already covered by license or accessRights, such as copyright or policy restrictions

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Examples:**

```json
[
    "Data is provided as-is without warranty. Please cite the National Climate Data Center when using this data."
]
```

```json
[
    "This data is in the public domain and may be used without restriction."
]
```

| Each item of this array must be | Description                        |
| ------------------------------- | ---------------------------------- |
| [rights items](#rights_items)   | Full text of a statement of rights |

### <a name="rights_items"></a>Array Item

Full text of a statement of rights

| **Type** | `string` |
| -------- | -------- |

## <a name="rightsHolder"></a>`Dataset > rightsHolder`

**Title:** rights holder

**Requirement:** Optional

List of agents (organizations) holding rights on the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be          | Description                                                                       |
| ---------------------------------------- | --------------------------------------------------------------------------------- |
| [Organization](./agents.md#organization) | An organization involved with a resource, including parent or child organizations |

## <a name="source"></a>`Dataset > source`

**Title:** data source

**Requirement:** Optional

List of related Datasets from which the described Dataset is derived

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| [Dataset](./dataset.md#root)    | A collection of data published or curated by one provider |

## <a name="spatial"></a>`Dataset > spatial`

**Title:** spatial/geographic coverage

**Requirement:** Recommended

A geographic region or regions that are covered by the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                              |
| --------------------------------------------------- |
| [Null allowed when not required](#spatial_anyOf_i0) |
| [Location](#spatial_anyOf_i1)                       |
| [List of geographic regions](#spatial_anyOf_i2)     |

### <a name="spatial_anyOf_i0"></a>`Dataset > spatial > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="spatial_anyOf_i1"></a>`Dataset > spatial > anyOf > Location`

**Title:** Location

inline description of Location

| **Type**                  | `object`                                           |
| ------------------------- | -------------------------------------------------- |
| **Additional properties** | Any type allowed                                   |
| **Same definition as**    | [Location](./temporal-spatial-metrics.md#location) |

### <a name="spatial_anyOf_i2"></a>`Dataset > spatial > anyOf > List of geographic regions`

**Title:** List of geographic regions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                    | Description                      |
| -------------------------------------------------- | -------------------------------- |
| [Location](./temporal-spatial-metrics.md#location) | A named place or geographic area |

## <a name="subject"></a>`Dataset > subject`

**Title:** subject

**Requirement:** Optional

List of primary subjects for the dataset, usually narrower than broad theme categories

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                       | Description                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------ |
| [Concept](./identifiers-and-relationships.md#concept) | A controlled term or label, optionally drawn from a concept scheme |

## <a name="temporal"></a>`Dataset > temporal`

**Title:** temporal coverage

**Requirement:** Recommended

Time periods covered by the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                              | Description                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------------- |
| [PeriodOfTime](./temporal-spatial-metrics.md#period-of-time) | Information about a specific time period with a start- and/or end-time |

## <a name="title"></a>`Dataset > title`

**Title:** title

**Requirement:** Mandatory

Human-readable title of the dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"Daily Climate Observations 2024"
```

```json
"National Climate Observations 2024"
```

## <a name="category"></a>`Dataset > category`

**Title:** category

**Requirement:** Optional

List of high-level categories for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                       | Description                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------ |
| [Concept](./identifiers-and-relationships.md#concept) | A controlled term or label, optionally drawn from a concept scheme |

## <a name="hasQualityMeasurement"></a>`Dataset > hasQualityMeasurement`

**Title:** quality measurement

**Requirement:** Optional

List of quality measurements for the dataset (for example, completeness, accuracy, or timeliness) beyond spatial or temporal resolution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                                         | Description                                                   |
| ----------------------------------------------------------------------- | ------------------------------------------------------------- |
| [QualityMeasurement](./temporal-spatial-metrics.md#quality-measurement) | A measurement of a resource against a specific quality metric |

## <a name="page"></a>`Dataset > page`

**Title:** documentation

**Requirement:** Optional

List of pages or documents about this dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be              | Description                                           |
| -------------------------------------------- | ----------------------------------------------------- |
| [Document](./quality-governance.md#document) | A publication or other document related to a resource |

## <a name="qualifiedAttribution"></a>`Dataset > qualifiedAttribution`

**Title:** qualified attribution

**Requirement:** Optional

List of agents with specific responsibilities for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                                       |
| -------------------------------------------------- | ------------------------------------------------- |
| [Attribution](./quality-governance.md#attribution) | A responsibility that an agent has for a resource |

## <a name="wasAttributedTo"></a>`Dataset > wasAttributedTo`

**Title:** attribution

**Requirement:** Optional

List of agents attributed to this dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------- |
| [Agent](./agents.md#agent)      | A person, organization, software agent, or other entity involved with a resource |

## <a name="wasGeneratedBy"></a>`Dataset > wasGeneratedBy`

**Title:** was generated by

**Requirement:** Optional

List of activities that generated, or provide the business context for the creation of the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                                                    |
| -------------------------------------------------- | -------------------------------------------------------------- |
| [Activity](./temporal-spatial-metrics.md#activity) | An activity related to creating, changing, or using a resource |

## <a name="wasUsedBy"></a>`Dataset > wasUsedBy`

**Title:** used by

**Requirement:** Optional

List of activities that used the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                                                    |
| -------------------------------------------------- | -------------------------------------------------------------- |
| [Activity](./temporal-spatial-metrics.md#activity) | An activity related to creating, changing, or using a resource |

## <a name="image"></a>`Dataset > image`

**Title:** image

**Requirement:** Optional

Thumbnail image illustrating the dataset, especially useful for visual data such as maps, photos, or video

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of                                            |
| ------------------------------------------------- |
| [Null allowed when not required](#image_anyOf_i0) |
| [Link](#image_anyOf_i1)                           |

### <a name="image_anyOf_i0"></a>`Dataset > image > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="image_anyOf_i1"></a>`Dataset > image > anyOf > Link`

**Title:** Link

The link to the image

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="scopeNote"></a>`Dataset > scopeNote`

**Title:** usage note

**Requirement:** Optional

usage note for the dataset

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"This dataset contains raw observational data. For derived products such as monthly averages or climate normals, see related datasets."
```

---
**See Also:** (related supporting classes)
