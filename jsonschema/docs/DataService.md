

**Title:** DataService

A service that provides access to data or data processing functions

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "DataService",
    "title": "Climate Data API",
    "description": "RESTful API providing access to historical climate observations.",
    "endpointURL": [
        "https://api.example.gov/climate/v1"
    ],
    "endpointDescription": [
        "https://api.example.gov/climate/v1/openapi.json"
    ],
    "contactPoint": [
        {
            "fn": "API Support Team",
            "hasEmail": "mailto:api-support@example.gov"
        }
    ],
    "publisher": {
        "name": "National Climate Data Center"
    },
    "keyword": [
        "climate",
        "weather",
        "API"
    ],
    "license": "https://creativecommons.org/publicdomain/zero/1.0/",
    "servesDataset": [
        {
            "@id": "https://example.gov/datasets/climate-observations-2024",
            "@type": "Dataset",
            "title": "Climate Observations 2024",
            "description": "Annual climate observation data.",
            "contactPoint": {
                "fn": "Climate Support",
                "hasEmail": "mailto:climate@example.gov"
            },
            "publisher": {
                "name": "National Climate Data Center"
            },
            "identifier": "https://example.gov/datasets/climate-observations-2024"
        }
    ],
    "identifier": "https://example.gov/services/climate-api"
}
```

| Property                                                   | Type                    | Title/Description            |
| ---------------------------------------------------------- | ----------------------- | ---------------------------- |
| - [@id](#@id )                                             | string                  | -                            |
| - [@type](#@type )                                         | string                  | -                            |
| + [contactPoint](#contactPoint )                           | array                   | contact point                |
| - [endpointDescription](#endpointDescription )             | null or array of string | endpoint description         |
| + [endpointURL](#endpointURL )                             | array of string         | endpoint URL                 |
| - [keyword](#keyword )                                     | null or array of string | keyword/tag                  |
| - [servesDataset](#servesDataset )                         | null or array           | serves dataset               |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string          | spatial resolution in meters |
| - [temporalResolution](#temporalResolution )               | null or string          | temporal resolution          |
| - [theme](#theme )                                         | null or array           | theme/category               |
| - [accessRights](#accessRights )                           | More than one type      | access rights                |
| - [conformsTo](#conformsTo )                               | null or array           | conforms to                  |
| - [created](#created )                                     | More than one type      | creation date                |
| - [creator](#creator )                                     | null or array           | creator                      |
| - [description](#description )                             | null or string          | description                  |
| - [identifier](#identifier )                               | More than one type      | identifier                   |
| - [otherIdentifier](#otherIdentifier )                     | null or array           | other identifier             |
| - [language](#language )                                   | More than one type      | language                     |
| - [license](#license )                                     | More than one type      | license                      |
| - [modified](#modified )                                   | More than one type      | update/modification date     |
| + [publisher](#publisher )                                 | object                  | publisher                    |
| - [rights](#rights )                                       | null or array of string | rights                       |
| - [rightsHolder](#rightsHolder )                           | null or array           | rights holder                |
| - [spatial](#spatial )                                     | null or array           | spatial/geographic coverage  |
| - [temporal](#temporal )                                   | null or array           | temporal coverage            |
| + [title](#title )                                         | string                  | title                        |
| - [category](#category )                                   | null or array           | category                     |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | null or array           | quality measurement          |
| - [qualifiedAttribution](#qualifiedAttribution )           | null or array           | qualified attribution        |
| - [wasUsedBy](#wasUsedBy )                                 | null or array           | was used by                  |

## <a name="@id"></a>[Optional] Property `DataService > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/data-services/climate-api-001"
```

## <a name="@type"></a>[Optional] Property `DataService > @type`

**Requirement:** Optional

| **Type**    | `string`        |
| ----------- | --------------- |
| **Default** | `"DataService"` |

## <a name="contactPoint"></a>[Mandatory] Property `DataService > contactPoint`

**Title:** contact point

**Requirement:** Mandatory

Contact information for questions about the Data Service. Include an email address that is continuously monitored

| **Type**     | `array` |
| ------------ | ------- |
| **Required** | Yes     |

| Each item of this array must be | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| [Kind](#contactPoint_items)     | Contact information for an individual or entity |

### <a name="contactPoint_items"></a>DataService > contactPoint > Kind

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

## <a name="endpointDescription"></a>[Recommended] Property `DataService > endpointDescription`

**Title:** endpoint description

**Requirement:** Recommended

List of endpoint descriptions with operations and parameters (for example, OpenAPI or similar service documentation)

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Examples:**

```json
[
    "https://api.example.gov/climate/v1/openapi.json"
]
```

```json
[
    "https://api.example.gov/climate/docs/openapi.json"
]
```

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [endpointDescription items](#endpointDescription_items) | -           |

### <a name="endpointDescription_items"></a>DataService > endpointDescription > endpointDescription items

| **Type** | `string` |
| -------- | -------- |

## <a name="endpointURL"></a>[Mandatory] Property `DataService > endpointURL`

**Title:** endpoint URL

**Requirement:** Mandatory

A list of root locations or primary endpoints of the service (a Web-resolvable IRI)

| **Type**     | `array of string` |
| ------------ | ----------------- |
| **Required** | Yes               |

**Examples:**

```json
[
    "https://api.example.gov/climate/v1"
]
```

```json
[
    "https://api.example.gov/climate/v1",
    "https://api.example.gov/climate/v2"
]
```

| Each item of this array must be | Description                                                                 |
| ------------------------------- | --------------------------------------------------------------------------- |
| [URLs](#endpointURL_items)      | The root location or primary endpoint of the service (a Web-resolvable IRI) |

### <a name="endpointURL_items"></a>DataService > endpointURL > URLs

**Title:** URLs

The root location or primary endpoint of the service (a Web-resolvable IRI)

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="keyword"></a>[Optional] Property `DataService > keyword`

**Title:** keyword/tag

**Requirement:** Optional

List of keywords or tags describing the data service

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Examples:**

```json
[
    "climate",
    "weather",
    "API"
]
```

```json
[
    "climate",
    "weather",
    "temperature",
    "API",
    "REST"
]
```

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [Non-empty strings](#keyword_items) | -           |

### <a name="keyword_items"></a>DataService > keyword > Non-empty strings

**Title:** Non-empty strings

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="servesDataset"></a>[Recommended] Property `DataService > servesDataset`

**Title:** serves dataset

**Requirement:** Recommended

List of datasets this service provides access to

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| [Dataset](#servesDataset_items) | A collection of data published or curated by one provider |

### <a name="servesDataset_items"></a>DataService > servesDataset > Dataset

**Title:** Dataset

A collection of data published or curated by one provider

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

## <a name="spatialResolutionInMeters"></a>[Optional] Property `DataService > spatialResolutionInMeters`

**Title:** spatial resolution in meters

**Requirement:** Optional

The minimum spatial separation resolvable in a Data Service, measured in meters

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"1000"
```

## <a name="temporalResolution"></a>[Optional] Property `DataService > temporalResolution`

**Title:** temporal resolution

**Requirement:** Optional

The minimum time period resolvable by the Data Service

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"P1D"
```

## <a name="theme"></a>[Optional] Property `DataService > theme`

**Title:** theme/category

**Requirement:** Optional

List of themes or categories for the data service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| [Concept](#theme_items)         | A controlled term or label, optionally drawn from a concept scheme |

### <a name="theme_items"></a>DataService > theme > Concept

**Title:** Concept

A controlled term or label, optionally drawn from a concept scheme

| **Type**                  | More than one type                                                            |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [Concept](#servesDataset_items_sample_items_representationTechnique_anyOf_i1) |

## <a name="accessRights"></a>[Optional] Property `DataService > accessRights`

**Title:** access rights

**Requirement:** Optional

Information about whether the data service is publicly accessible, restricted, or not public

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"Public access with no restrictions"
```

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#accessRights_anyOf_i0) |
| [item 1](#accessRights_anyOf_i1) |

### <a name="accessRights_anyOf_i0"></a>Property `DataService > accessRights > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `DataService > accessRights > anyOf > item 1`

Text description of the access rights

| **Type** | `string` |
| -------- | -------- |

## <a name="conformsTo"></a>[Optional] Property `DataService > conformsTo`

**Title:** conforms to

**Requirement:** Optional

List of general standards or specifications that the Data Service endpoints implement

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| [Standard](#conformsTo_items)   | A standard or specification that another resource conforms to |

### <a name="conformsTo_items"></a>DataService > conformsTo > Standard

**Title:** Standard

A standard or specification that another resource conforms to

| **Type**                  | `object`                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                   |
| **Same definition as**    | [Standard](#servesDataset_items_sample_items_accessService_items_conformsTo_items) |

## <a name="created"></a>[Optional] Property `DataService > created`

**Title:** creation date

**Requirement:** Optional

The date on which the Data Service was first created

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"2020-01-15"
```

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#created_anyOf_i0)      |
| [Date string](#created_anyOf_i1) |

### <a name="created_anyOf_i0"></a>Property `DataService > created > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>Property `DataService > created > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_anyOf_i0) |
| [item 1](#created_anyOf_i1_anyOf_i1) |
| [item 2](#created_anyOf_i1_anyOf_i2) |
| [item 3](#created_anyOf_i1_anyOf_i3) |

#### <a name="created_anyOf_i1_anyOf_i0"></a>Property `DataService > created > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="created_anyOf_i1_anyOf_i1"></a>Property `DataService > created > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="created_anyOf_i1_anyOf_i2"></a>Property `DataService > created > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_anyOf_i3"></a>Property `DataService > created > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="creator"></a>[Optional] Property `DataService > creator`

**Title:** creator

**Requirement:** Optional

List of agents primarily responsible for producing the Data Service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------- |
| [Agent](#creator_items)         | A person, organization, software agent, or other entity involved with a resource |

### <a name="creator_items"></a>DataService > creator > Agent

**Title:** Agent

A person, organization, software agent, or other entity involved with a resource

| **Type**                  | `object`                                                                     |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                             |
| **Same definition as**    | [Agent](#servesDataset_items_sample_items_accessService_items_creator_items) |

## <a name="description"></a>[Optional] Property `DataService > description`

**Title:** description

**Requirement:** Optional

Plain-language summary of the data service

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"RESTful API providing access to historical climate observations."
```

```json
"A RESTful API providing access to historical and real-time climate data including temperature, precipitation, and atmospheric conditions."
```

## <a name="identifier"></a>[Optional] Property `DataService > identifier`

**Title:** identifier

**Requirement:** Optional

The unique identifier for the Data Service, e.g. the URI or other unique identifier in the context of the Catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [item 0](#identifier_anyOf_i0)     |
| [Identifier](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `DataService > identifier > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `DataService > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                       |
| ------------------------- | -------------------------------------------------------- |
| **Additional properties** | Any type allowed                                         |
| **Same definition as**    | [Identifier](#servesDataset_items_otherIdentifier_items) |

## <a name="otherIdentifier"></a>[Optional] Property `DataService > otherIdentifier`

**Title:** other identifier

**Requirement:** Optional

A list of identifiers for the Data Service besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>DataService > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type                                       |
| ------------------------- | -------------------------------------------------------- |
| **Additional properties** | Any type allowed                                         |
| **Same definition as**    | [Identifier](#servesDataset_items_otherIdentifier_items) |

## <a name="language"></a>[Optional] Property `DataService > language`

**Title:** language

**Requirement:** Optional

ISO 639-1 language code values supported by the data service, such as en or es

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
[
    "en",
    "es"
]
```

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#language_anyOf_i0) |
| [Language code](#language_anyOf_i1)                  |
| [List of lanuages](#language_anyOf_i2)               |

### <a name="language_anyOf_i0"></a>Property `DataService > language > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="language_anyOf_i1"></a>Property `DataService > language > anyOf > Language code`

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `DataService > language > anyOf > List of lanuages`

**Title:** List of lanuages

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Language code](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>DataService > language > anyOf > List of lanuages > Language code

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="license"></a>[Recommended] Property `DataService > license`

**Title:** license

**Requirement:** Recommended

License that governs how the data service can be used or reused

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"https://creativecommons.org/publicdomain/zero/1.0/"
```

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#license_anyOf_i0) |
| [item 1](#license_anyOf_i1)                         |

### <a name="license_anyOf_i0"></a>Property `DataService > license > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="license_anyOf_i1"></a>Property `DataService > license > anyOf > item 1`

Full text of the license

| **Type** | `string` |
| -------- | -------- |

## <a name="modified"></a>[Optional] Property `DataService > modified`

**Title:** update/modification date

**Requirement:** Optional

The most recent date on which the Data Service was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"2024-03-20"
```

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `DataService > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `DataService > modified > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_anyOf_i0) |
| [item 1](#modified_anyOf_i1_anyOf_i1) |
| [item 2](#modified_anyOf_i1_anyOf_i2) |
| [item 3](#modified_anyOf_i1_anyOf_i3) |

#### <a name="modified_anyOf_i1_anyOf_i0"></a>Property `DataService > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>Property `DataService > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>Property `DataService > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>Property `DataService > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>[Mandatory] Property `DataService > publisher`

**Title:** publisher

**Requirement:** Mandatory

Person or organization responsible for publishing and making the data service available

| **Type**                  | `object`            |
| ------------------------- | ------------------- |
| **Required**              | Yes                 |
| **Additional properties** | Any type allowed    |
| **Defined in**            | [Agent](./Agent.md) |

## <a name="rights"></a>[Optional] Property `DataService > rights`

**Title:** rights

**Requirement:** Optional

Rights statements not already covered by license or accessRights, such as copyright or policy restrictions

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "Data provided by the National Climate Data Center is in the public domain."
]
```

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [rights items](#rights_items)   | -           |

### <a name="rights_items"></a>DataService > rights > rights items

| **Type** | `string` |
| -------- | -------- |

## <a name="rightsHolder"></a>[Optional] Property `DataService > rightsHolder`

**Title:** rights holder

**Requirement:** Optional

A list of Agents (organizations) holding rights on the Data Service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description                                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------- |
| [Organization](#rightsHolder_items) | An organization involved with a resource, including parent or child organizations |

### <a name="rightsHolder_items"></a>DataService > rightsHolder > Organization

**Title:** Organization

An organization involved with a resource, including parent or child organizations

| **Type**                  | `object`                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                     |
| **Same definition as**    | [Organization](#servesDataset_items_otherIdentifier_items_anyOf_i1_creator_anyOf_i1) |

## <a name="spatial"></a>[Optional] Property `DataService > spatial`

**Title:** spatial/geographic coverage

**Requirement:** Optional

A geographic region that is covered by the Data Service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                      |
| ------------------------------- | -------------------------------- |
| [Location](#spatial_items)      | A named place or geographic area |

### <a name="spatial_items"></a>DataService > spatial > Location

**Title:** Location

A named place or geographic area

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [Location](#servesDataset_items_sample_items_accessService_items_spatial_items) |

## <a name="temporal"></a>[Optional] Property `DataService > temporal`

**Title:** temporal coverage

**Requirement:** Optional

Time periods covered by the data service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| [PeriodOfTime](#temporal_items) | Information about a specific time period with a start- and/or end-time |

### <a name="temporal_items"></a>DataService > temporal > PeriodOfTime

**Title:** PeriodOfTime

Information about a specific time period with a start- and/or end-time

| **Type**                  | More than one type                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                     |
| **Same definition as**    | [PeriodOfTime](#servesDataset_items_sample_items_accessService_items_temporal_items) |

## <a name="title"></a>[Mandatory] Property `DataService > title`

**Title:** title

**Requirement:** Mandatory

Human-readable title of the data service

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"Climate Data API"
```

```json
"Climate Data REST API"
```

## <a name="category"></a>[Optional] Property `DataService > category`

**Title:** category

**Requirement:** Optional

List of high-level categories for the data service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| [Concept](#category_items)      | A controlled term or label, optionally drawn from a concept scheme |

### <a name="category_items"></a>DataService > category > Concept

**Title:** Concept

A controlled term or label, optionally drawn from a concept scheme

| **Type**                  | More than one type                                                            |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [Concept](#servesDataset_items_sample_items_representationTechnique_anyOf_i1) |

## <a name="hasQualityMeasurement"></a>[Optional] Property `DataService > hasQualityMeasurement`

**Title:** quality measurement

**Requirement:** Optional

Quality measurements for the data service (for example, availability, response time, or reliability)

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                                                   |
| -------------------------------------------------- | ------------------------------------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_items) | A measurement of a resource against a specific quality metric |

### <a name="hasQualityMeasurement_items"></a>DataService > hasQualityMeasurement > QualityMeasurement

**Title:** QualityMeasurement

A measurement of a resource against a specific quality metric

| **Type**                  | `object`                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [QualityMeasurement](#servesDataset_items_sample_items_accessService_items_hasQualityMeasurement_items) |

## <a name="qualifiedAttribution"></a>[Optional] Property `DataService > qualifiedAttribution`

**Title:** qualified attribution

**Requirement:** Optional

List of agents with specific responsibilities for the data service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be            | Description                                       |
| ------------------------------------------ | ------------------------------------------------- |
| [Attribution](#qualifiedAttribution_items) | A responsibility that an agent has for a resource |

### <a name="qualifiedAttribution_items"></a>DataService > qualifiedAttribution > Attribution

**Title:** Attribution

A responsibility that an agent has for a resource

| **Type**                  | `object`                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Attribution](#servesDataset_items_sample_items_accessService_items_qualifiedAttribution_items) |

## <a name="wasUsedBy"></a>[Optional] Property `DataService > wasUsedBy`

**Title:** was used by

**Requirement:** Optional

List of activities that used or tested the data service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                    |
| ------------------------------- | -------------------------------------------------------------- |
| [Activity](#wasUsedBy_items)    | An activity related to creating, changing, or using a resource |

### <a name="wasUsedBy_items"></a>DataService > wasUsedBy > Activity

**Title:** Activity

An activity related to creating, changing, or using a resource

| **Type**                  | `object`                                                                          |
| ------------------------- | --------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                  |
| **Same definition as**    | [Activity](#servesDataset_items_sample_items_accessService_items_wasUsedBy_items) |

