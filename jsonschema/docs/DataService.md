

**Title:** DataService

A service for providing data at a URL or URLs

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

**Example:**

```json
"DataService"
```

## <a name="contactPoint"></a>[Mandatory] Property `DataService > contactPoint`

**Title:** contact point

**Requirement:** Mandatory

Contact information that can be used for sending comments about the Data Service

| **Type**     | `array` |
| ------------ | ------- |
| **Required** | Yes     |

**Examples:**

```json
[
    {
        "fn": "API Support Team",
        "hasEmail": "mailto:api-support@example.gov"
    }
]
```

```json
[
    {
        "@id": "https://example.gov/contacts/climate-team-001",
        "@type": "Kind",
        "fn": "Climate Data Support Team",
        "hasEmail": "mailto:climate-support@example.gov",
        "organization-name": "National Climate Data Center",
        "tel": "+1-555-123-4567",
        "address": [
            {
                "@id": "https://example.gov/addresses/climate-office-001",
                "country-name": "United States",
                "locality": "Asheville",
                "postal-code": "28801",
                "region": "NC",
                "street-address": "151 Patton Ave"
            }
        ]
    }
]
```

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

A list of descriptions of the services available via the end-points, including their operations, parameters etc

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

List of keywords or tags describing the Data Service

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

List of datasets that are served by this data service

| **Type** | `null or array` |
| -------- | --------------- |

**Examples:**

```json
[
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
]
```

```json
[
    {
        "@id": "https://example.gov/datasets/daily-climate-obs",
        "@type": "Dataset",
        "title": "Daily Climate Observations",
        "description": "Daily observations of temperature, precipitation, and other climate variables.",
        "contactPoint": [
            {
                "fn": "Climate Data Team",
                "hasEmail": "mailto:climate-data@example.gov"
            }
        ],
        "publisher": {
            "name": "National Climate Data Center"
        },
        "identifier": "https://example.gov/datasets/served-dataset-001"
    }
]
```

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#servesDataset_items) | Information about a set of data |

### <a name="servesDataset_items"></a>DataService > servesDataset > Dataset

**Title:** Dataset

Information about a set of data

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

A list of themes of the Data Service. A Data Service may be associated with multiple themes

| **Type** | `null or array` |
| -------- | --------------- |

**Example:**

```json
[
    {
        "@id": "https://example.gov/concepts/climate-science",
        "@type": "Concept",
        "prefLabel": "Climate Science",
        "definition": "The scientific study of climate and climate change.",
        "inScheme": {
            "@id": "https://example.gov/concept-schemes/science-domains",
            "@type": "ConceptScheme",
            "title": "Science Domains"
        }
    }
]
```

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#theme_items)         | A labeled value from an optionally specified concept scheme |

### <a name="theme_items"></a>DataService > theme > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                                            |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [Concept](#servesDataset_items_sample_items_representationTechnique_anyOf_i1) |

## <a name="accessRights"></a>[Optional] Property `DataService > accessRights`

**Title:** access rights

**Requirement:** Optional

Information that indicates whether the Data Service is open data, has access restrictions or is public

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

**Example:**

```json
[
    {
        "@id": "https://example.gov/standards/ogc-api-features",
        "@type": "Standard",
        "title": "OGC API - Features",
        "description": "OGC standard for accessing geospatial features via a Web API."
    }
]
```

| Each item of this array must be | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| [Standard](#conformsTo_items)   | Information about a particular standard that another item conforms to |

### <a name="conformsTo_items"></a>DataService > conformsTo > Standard

**Title:** Standard

Information about a particular standard that another item conforms to

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

**Example:**

```json
[
    {
        "@id": "https://example.gov/agents/ncdc-team",
        "@type": "Agent",
        "name": "NCDC Development Team"
    }
]
```

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Agent](#creator_items)         | An entity that could be involved with a resource |

### <a name="creator_items"></a>DataService > creator > Agent

**Title:** Agent

An entity that could be involved with a resource

| **Type**                  | `object`                                                                     |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                             |
| **Same definition as**    | [Agent](#servesDataset_items_sample_items_accessService_items_creator_items) |

## <a name="description"></a>[Optional] Property `DataService > description`

**Title:** description

**Requirement:** Optional

A free-text account of the Data Service

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

**Examples:**

```json
"https://example.gov/services/climate-api"
```

```json
{
    "@type": "Identifier",
    "schemaAgency": "example.gov",
    "notation": "CLIMATE-API-001"
}
```

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

**Example:**

```json
[
    {
        "@type": "Identifier",
        "schemaAgency": "DOI",
        "notation": "10.12345/climate-api"
    }
]
```

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

Language or languages supported by the Data Service. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

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

The license under which the Data Service is made available; see https://resources.data.gov/schemas/dcat-us/open-licenses for more information regarding license-free declarations and licenses

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

An entity (organization) responsible for making the Data Service available

| **Type**                  | `object`            |
| ------------------------- | ------------------- |
| **Required**              | Yes                 |
| **Additional properties** | Any type allowed    |
| **Defined in**            | [Agent](./Agent.md) |

**Examples:**

```json
{
    "name": "National Climate Data Center"
}
```

```json
{
    "@id": "https://example.gov/agents/ncdc-001",
    "@type": "Agent",
    "name": "National Climate Data Center",
    "category": [
        {
            "@id": "https://example.gov/concepts/federal-agency",
            "@type": "Concept",
            "prefLabel": "Federal Agency",
            "definition": "An agency of the federal government of the United States.",
            "inScheme": {
                "@id": "https://example.gov/concept-schemes/organization-types",
                "@type": "ConceptScheme",
                "title": "Organization Types"
            }
        }
    ]
}
```

## <a name="rights"></a>[Optional] Property `DataService > rights`

**Title:** rights

**Requirement:** Optional

A list of statements concerning all rights for the Data Service that may not be addressed by license or accessRights, such as copyright statements, statements about the intellectual property rights (IPR), or information regarding access or restrictions based on privacy, security, or other policies

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

**Example:**

```json
[
    {
        "@id": "https://example.gov/organizations/noaa",
        "@type": "Organization",
        "name": "National Oceanic and Atmospheric Administration"
    }
]
```

| Each item of this array must be     | Description                                                                         |
| ----------------------------------- | ----------------------------------------------------------------------------------- |
| [Organization](#rightsHolder_items) | Information about an organization, including other organizations that it is part of |

### <a name="rightsHolder_items"></a>DataService > rightsHolder > Organization

**Title:** Organization

Information about an organization, including other organizations that it is part of

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

**Example:**

```json
[
    {
        "@id": "https://example.gov/locations/usa",
        "@type": "Location",
        "geometry": "POLYGON((-125 24, -66 24, -66 50, -125 50, -125 24))"
    }
]
```

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Location](#spatial_items)      | Information about a specific geographic location |

### <a name="spatial_items"></a>DataService > spatial > Location

**Title:** Location

Information about a specific geographic location

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [Location](#servesDataset_items_sample_items_accessService_items_spatial_items) |

## <a name="temporal"></a>[Optional] Property `DataService > temporal`

**Title:** temporal coverage

**Requirement:** Optional

A list of temporal periods that the DataService covers

| **Type** | `null or array` |
| -------- | --------------- |

**Example:**

```json
[
    {
        "@id": "https://example.gov/periods/1950-present",
        "@type": "PeriodOfTime",
        "startDate": "1950-01-01",
        "endDate": "2024-12-31"
    }
]
```

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

The title of the data service in the indicated language

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

List of categories for the Data Service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#category_items)      | A labeled value from an optionally specified concept scheme |

### <a name="category_items"></a>DataService > category > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                                            |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [Concept](#servesDataset_items_sample_items_representationTechnique_anyOf_i1) |

## <a name="hasQualityMeasurement"></a>[Optional] Property `DataService > hasQualityMeasurement`

**Title:** quality measurement

**Requirement:** Optional

Refers to the performed quality measurements

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                        |
| -------------------------------------------------- | ---------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_items) | A single measurement of one metric |

### <a name="hasQualityMeasurement_items"></a>DataService > hasQualityMeasurement > QualityMeasurement

**Title:** QualityMeasurement

A single measurement of one metric

| **Type**                  | `object`                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [QualityMeasurement](#servesDataset_items_sample_items_accessService_items_hasQualityMeasurement_items) |

## <a name="qualifiedAttribution"></a>[Optional] Property `DataService > qualifiedAttribution`

**Title:** qualified attribution

**Requirement:** Optional

List of agents having some form of responsibility for the Data Service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be            | Description                                  |
| ------------------------------------------ | -------------------------------------------- |
| [Attribution](#qualifiedAttribution_items) | An attribution that an agent plays some role |

### <a name="qualifiedAttribution_items"></a>DataService > qualifiedAttribution > Attribution

**Title:** Attribution

An attribution that an agent plays some role

| **Type**                  | `object`                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Attribution](#servesDataset_items_sample_items_accessService_items_qualifiedAttribution_items) |

## <a name="wasUsedBy"></a>[Optional] Property `DataService > wasUsedBy`

**Title:** was used by

**Requirement:** Optional

List of activities that used the Data Service

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Activity](#wasUsedBy_items)    | An activity which a resource could be related to |

### <a name="wasUsedBy_items"></a>DataService > wasUsedBy > Activity

**Title:** Activity

An activity which a resource could be related to

| **Type**                  | `object`                                                                          |
| ------------------------- | --------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                  |
| **Same definition as**    | [Activity](#servesDataset_items_sample_items_accessService_items_wasUsedBy_items) |

