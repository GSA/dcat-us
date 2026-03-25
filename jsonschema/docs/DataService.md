

**Title:** DataService

A service for providing data at a URL or URLs

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                                   | Type               | Title/Description                                                                    |
| ---------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------ |
| - [@id](#@id )                                             | string             | -                                                                                    |
| - [@type](#@type )                                         | string             | -                                                                                    |
| + [contactPoint](#contactPoint )                           | array              | contact point                                                                        |
| - [endpointDescription](#endpointDescription )             | More than one type | endpoint description                                                                 |
| + [endpointURL](#endpointURL )                             | array of string    | endpoint URL                                                                         |
| - [keyword](#keyword )                                     | null or string     | keyword/tag                                                                          |
| - [keywordMap](#keywordMap )                               | null or object     | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}         |
| - [servesDataset](#servesDataset )                         | More than one type | serves dataset                                                                       |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | More than one type | spatial resolution in meters                                                         |
| - [temporalResolution](#temporalResolution )               | More than one type | temporal resolution                                                                  |
| - [theme](#theme )                                         | More than one type | theme/category                                                                       |
| - [geographicBoundingBox](#geographicBoundingBox )         | More than one type | geographic bounding box                                                              |
| - [accessRights](#accessRights )                           | More than one type | access rights                                                                        |
| - [conformsTo](#conformsTo )                               | More than one type | conforms to                                                                          |
| - [created](#created )                                     | More than one type | creation date                                                                        |
| - [creator](#creator )                                     | More than one type | creator                                                                              |
| - [description](#description )                             | null or string     | description                                                                          |
| - [descriptionMap](#descriptionMap )                       | null or object     | Language map for the description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#identifier )                               | More than one type | identifier                                                                           |
| - [language](#language )                                   | More than one type | language                                                                             |
| - [license](#license )                                     | More than one type | license                                                                              |
| - [modified](#modified )                                   | More than one type | update/modification date                                                             |
| + [publisher](#publisher )                                 | More than one type | publisher                                                                            |
| - [rights](#rights )                                       | More than one type | rights                                                                               |
| - [rightsHolder](#rightsHolder )                           | More than one type | rights holder                                                                        |
| - [spatial](#spatial )                                     | More than one type | spatial/geographic coverage                                                          |
| - [temporal](#temporal )                                   | More than one type | temporal coverage                                                                    |
| + [title](#title )                                         | string             | title                                                                                |
| - [titleMap](#titleMap )                                   | null or object     | Language map for the title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#category )                                   | More than one type | category                                                                             |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | More than one type | quality measurement                                                                  |
| - [qualifiedAttribution](#qualifiedAttribution )           | More than one type | qualified attribution                                                                |
| - [wasUsedBy](#wasUsedBy )                                 | More than one type | was used by                                                                          |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                 |
| ----------- | --------------- |
| **Type**    | `string`        |
| **Default** | `"DataService"` |

## <a name="contactPoint"></a>Property `contactPoint`

**Title:** contact point

Contact information that can be used for sending comments about the Data Service

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [contactPoint items](#contactPoint_items) | -           |

### <a name="contactPoint_items"></a>contactPoint items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                         |
| -------------------------------------- |
| [Kind](#contactPoint_items_oneOf_i0)   |
| [item 1](#contactPoint_items_oneOf_i1) |

#### <a name="contactPoint_items_oneOf_i0"></a>Property `Kind`

**Title:** Kind

inline description of Kind

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

#### <a name="contactPoint_items_oneOf_i1"></a>Property `item 1`

reference iri of Kind

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="endpointDescription"></a>Property `endpointDescription`

**Title:** endpoint description

A list of descriptions of the services available via the end-points, including their operations, parameters etc

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                          |
| --------------------------------------- |
| [item 0](#endpointDescription_anyOf_i0) |
| [item 1](#endpointDescription_anyOf_i1) |

### <a name="endpointDescription_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="endpointDescription_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [item 1 items](#endpointDescription_anyOf_i1_items) | -           |

#### <a name="endpointDescription_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#endpointDescription_anyOf_i1_items_anyOf_i0) |
| [item 1](#endpointDescription_anyOf_i1_items_anyOf_i1) |

##### <a name="endpointDescription_anyOf_i1_items_anyOf_i0"></a>Property `item 0`

An in-line description of the endpoint description

|          |          |
| -------- | -------- |
| **Type** | `string` |

##### <a name="endpointDescription_anyOf_i1_items_anyOf_i1"></a>Property `item 1`

reference iri of the endpoint description

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="endpointURL"></a>Property `endpointURL`

**Title:** endpoint URL

A list of root locations or primary endpoints of the service (a Web-resolvable IRI)

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

| Each item of this array must be         | Description                                                                 |
| --------------------------------------- | --------------------------------------------------------------------------- |
| [endpointURL items](#endpointURL_items) | The root location or primary endpoint of the service (a Web-resolvable IRI) |

### <a name="endpointURL_items"></a>endpointURL items

The root location or primary endpoint of the service (a Web-resolvable IRI)

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="keyword"></a>Property `keyword`

**Title:** keyword/tag

A keyword or tag describing the Data Service

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="keywordMap"></a>Property `keywordMap`

Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="servesDataset"></a>Property `servesDataset`

**Title:** serves dataset

List of datasets that are served by this data service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                    |
| --------------------------------- |
| [item 0](#servesDataset_anyOf_i0) |
| [item 1](#servesDataset_anyOf_i1) |

### <a name="servesDataset_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="servesDataset_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [item 1 items](#servesDataset_anyOf_i1_items) | -           |

#### <a name="servesDataset_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                    |
| ------------------------------------------------- |
| [Dataset](#servesDataset_anyOf_i1_items_oneOf_i0) |
| [item 1](#servesDataset_anyOf_i1_items_oneOf_i1)  |

##### <a name="servesDataset_anyOf_i1_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

##### <a name="servesDataset_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatialResolutionInMeters"></a>Property `spatialResolutionInMeters`

**Title:** spatial resolution in meters

The minimum spatial separation resolvable in a Data Service, measured in meters

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#spatialResolutionInMeters_anyOf_i0) |
| [item 1](#spatialResolutionInMeters_anyOf_i1) |

### <a name="spatialResolutionInMeters_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="spatialResolutionInMeters_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [item 1 items](#spatialResolutionInMeters_anyOf_i1_items) | -           |

#### <a name="spatialResolutionInMeters_anyOf_i1_items"></a>item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="temporalResolution"></a>Property `temporalResolution`

**Title:** temporal resolution

The minimum time period resolvable by the Data Service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                         |
| -------------------------------------- |
| [item 0](#temporalResolution_anyOf_i0) |
| [item 1](#temporalResolution_anyOf_i1) |

### <a name="temporalResolution_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="temporalResolution_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be                    | Description |
| -------------------------------------------------- | ----------- |
| [item 1 items](#temporalResolution_anyOf_i1_items) | -           |

#### <a name="temporalResolution_anyOf_i1_items"></a>item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="theme"></a>Property `theme`

**Title:** theme/category

A list of themes of the Data Service. A Data Service may be associated with multiple themes

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)            |
| ------------------------- |
| [item 0](#theme_anyOf_i0) |
| [item 1](#theme_anyOf_i1) |

### <a name="theme_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="theme_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [item 1 items](#theme_anyOf_i1_items) | -           |

#### <a name="theme_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [Concept](#theme_anyOf_i1_items_oneOf_i0) |
| [item 1](#theme_anyOf_i1_items_oneOf_i1)  |

##### <a name="theme_anyOf_i1_items_oneOf_i0"></a>Property `Concept`

**Title:** Concept

inline description of Concept

|                           |                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                  |
| **Same definition as**    | [Concept](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="theme_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="geographicBoundingBox"></a>Property `geographicBoundingBox`

**Title:** geographic bounding box

The spatial extent of domain of application of an data service and is standardized in WGS 84 Lat/Long coordinate system

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#geographicBoundingBox_anyOf_i0) |
| [item 1](#geographicBoundingBox_anyOf_i1) |

### <a name="geographicBoundingBox_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="geographicBoundingBox_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [item 1 items](#geographicBoundingBox_anyOf_i1_items) | -           |

#### <a name="geographicBoundingBox_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [GeographicBoundingBox](#geographicBoundingBox_anyOf_i1_items_oneOf_i0) |
| [item 1](#geographicBoundingBox_anyOf_i1_items_oneOf_i1)                |

##### <a name="geographicBoundingBox_anyOf_i1_items_oneOf_i0"></a>Property `GeographicBoundingBox`

**Title:** GeographicBoundingBox

inline description of GeographicBoundingBox

|                           |                                                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                           |
| **Additional properties** | Any type allowed                                                                                                                                                                   |
| **Same definition as**    | [GeographicBoundingBox](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |

##### <a name="geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of GeographicBoundingBox

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accessRights"></a>Property `accessRights`

**Title:** access rights

Information regarding access or restrictions based on privacy, security, or other policies

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#accessRights_oneOf_i0)          |
| [RightsStatement](#accessRights_oneOf_i1) |
| [item 2](#accessRights_oneOf_i2)          |

### <a name="accessRights_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accessRights_oneOf_i1"></a>Property `RightsStatement`

**Title:** RightsStatement

inline description of access rights

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="accessRights_oneOf_i2"></a>Property `item 2`

reference iri of access rights

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `conformsTo`

**Title:** conforms to

List of general standards or specifications that the Data Service endpoints implement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#conformsTo_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1) |

### <a name="conformsTo_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="conformsTo_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#conformsTo_anyOf_i1_items) | -           |

#### <a name="conformsTo_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Standard](#conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i1)   |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `Standard`

**Title:** Standard

inline description of Standard

|                           |                                                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                   |
| **Additional properties** | Any type allowed                                                                                                                                           |
| **Same definition as**    | [Standard](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Standard

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="created"></a>Property `created`

**Title:** creation date

The date on which the Data Service has been first created

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#created_anyOf_i0) |
| [item 1](#created_anyOf_i1) |

### <a name="created_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="created_anyOf_i1"></a>Property `item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_oneOf_i0) |
| [item 1](#created_anyOf_i1_oneOf_i1) |
| [item 2](#created_anyOf_i1_oneOf_i2) |
| [item 3](#created_anyOf_i1_oneOf_i3) |

#### <a name="created_anyOf_i1_oneOf_i0"></a>Property `item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i1"></a>Property `item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i2"></a>Property `item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_oneOf_i3"></a>Property `item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="creator"></a>Property `creator`

**Title:** creator

List of agents primarily responsible for producing the Data Service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#creator_anyOf_i0) |
| [item 1](#creator_anyOf_i1) |

### <a name="creator_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="creator_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#creator_anyOf_i1_items) | -           |

#### <a name="creator_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                             |
| ------------------------------------------ |
| [Agent](#creator_anyOf_i1_items_oneOf_i0)  |
| [item 1](#creator_anyOf_i1_items_oneOf_i1) |

##### <a name="creator_anyOf_i1_items_oneOf_i0"></a>Property `Agent`

**Title:** Agent

inline description of Agent

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [Agent](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

##### <a name="creator_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Agent

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `description`

**Title:** description

A free-text account of the Data Service

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="descriptionMap"></a>Property `descriptionMap`

Language map for the description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="identifier"></a>Property `identifier`

**Title:** identifier

List of the main identifiers for the Data Service, e.g. the URI or other unique identifier in the context of the Catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="identifier_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="language"></a>Property `language`

**Title:** language

Language or languages supported by the Data Service. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#language_anyOf_i0) |
| [item 1](#language_anyOf_i1) |
| [item 2](#language_anyOf_i2) |

### <a name="language_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="language_anyOf_i1"></a>Property `item 1`

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `item 2`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 2 items](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>item 2 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="license"></a>Property `license`

**Title:** license

The license under which the Data Service is made available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#license_oneOf_i0)          |
| [LicenseDocument](#license_oneOf_i1) |
| [item 2](#license_oneOf_i2)          |

### <a name="license_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="license_oneOf_i1"></a>Property `LicenseDocument`

**Title:** LicenseDocument

inline description of LicenseDocument

|                           |                                                                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                        |
| **Additional properties** | Any type allowed                                                                                                                                |
| **Same definition as**    | [LicenseDocument](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

### <a name="license_oneOf_i2"></a>Property `item 2`

reference iri of LicenseDocument

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="modified"></a>Property `modified`

**Title:** update/modification date

The most recent date on which the Data Service was changed or modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="modified_anyOf_i1"></a>Property `item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `publisher`

**Title:** publisher

An entity (organization) responsible for making the Data Service available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [Agent](#publisher_oneOf_i0)  |
| [item 1](#publisher_oneOf_i1) |

### <a name="publisher_oneOf_i0"></a>Property `Agent`

**Title:** Agent

inline description of Agent

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [Agent](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

### <a name="publisher_oneOf_i1"></a>Property `item 1`

reference iri of Agent

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="rights"></a>Property `rights`

**Title:** rights

A list of statements concerning all rights for the Data Service not addressed with license or accessRights, such as copyright statements

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#rights_anyOf_i0) |
| [item 1](#rights_anyOf_i1) |

### <a name="rights_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="rights_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#rights_anyOf_i1_items) | -           |

#### <a name="rights_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                     |
| -------------------------------------------------- |
| [RightsStatement](#rights_anyOf_i1_items_oneOf_i0) |
| [item 1](#rights_anyOf_i1_items_oneOf_i1)          |

##### <a name="rights_anyOf_i1_items_oneOf_i0"></a>Property `RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

##### <a name="rights_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of RightsStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `rightsHolder`

**Title:** rights holder

A list of Agents (organizations) holding rights on the Data Service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#rightsHolder_anyOf_i0) |
| [item 1](#rightsHolder_anyOf_i1) |

### <a name="rightsHolder_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="rightsHolder_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#rightsHolder_anyOf_i1_items) | -           |

#### <a name="rightsHolder_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Organization](#rightsHolder_anyOf_i1_items_oneOf_i0) |
| [item 1](#rightsHolder_anyOf_i1_items_oneOf_i1)       |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `Organization`

**Title:** Organization

inline description of Organization

|                           |                                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                        |
| **Additional properties** | Any type allowed                                                                                                |
| **Same definition as**    | [Organization](#servesDataset_anyOf_i1_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Organization

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `spatial`

**Title:** spatial/geographic coverage

A geographic region that is covered by the Data Service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#spatial_anyOf_i0) |
| [item 1](#spatial_anyOf_i1) |

### <a name="spatial_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="spatial_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#spatial_anyOf_i1_items) | -           |

#### <a name="spatial_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#spatial_anyOf_i1_items_oneOf_i1)   |

##### <a name="spatial_anyOf_i1_items_oneOf_i0"></a>Property `Location`

**Title:** Location

inline description of Location

|                           |                                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                |
| **Additional properties** | Any type allowed                                                                                                                                        |
| **Same definition as**    | [Location](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Location

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `temporal`

**Title:** temporal coverage

A list of temporal periods that the DataService covers

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#temporal_anyOf_i0) |
| [item 1](#temporal_anyOf_i1) |

### <a name="temporal_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="temporal_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#temporal_anyOf_i1_items_oneOf_i1)       |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `PeriodOfTime`

**Title:** PeriodOfTime

inline description of PeriodOfTime

|                           |                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                                     |
| **Additional properties** | Any type allowed                                                                                                                                             |
| **Same definition as**    | [PeriodOfTime](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of PeriodOfTime

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `title`

**Title:** title

The title of the data service in the indicated language

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `titleMap`

Language map for the title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="category"></a>Property `category`

**Title:** category

Category of the data service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="category_oneOf_i1"></a>Property `Concept`

**Title:** Concept

inline description of Concept

|                           |                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                  |
| **Same definition as**    | [Concept](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

### <a name="category_oneOf_i2"></a>Property `item 2`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="hasQualityMeasurement"></a>Property `hasQualityMeasurement`

**Title:** quality measurement

Refers to the performed quality measurements

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#hasQualityMeasurement_anyOf_i0) |
| [item 1](#hasQualityMeasurement_anyOf_i1) |

### <a name="hasQualityMeasurement_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="hasQualityMeasurement_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [item 1 items](#hasQualityMeasurement_anyOf_i1_items) | -           |

#### <a name="hasQualityMeasurement_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                                       |
| -------------------------------------------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `QualityMeasurement`

**Title:** QualityMeasurement

inline description of QualityMeasurement

|                           |                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                        |
| **Additional properties** | Any type allowed                                                                                                                                                                |
| **Same definition as**    | [QualityMeasurement](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of QualityMeasurement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `qualifiedAttribution`

**Title:** qualified attribution

An Agent having some form of responsibility for the DataService

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                           |
| ---------------------------------------- |
| [item 0](#qualifiedAttribution_anyOf_i0) |
| [item 1](#qualifiedAttribution_anyOf_i1) |

### <a name="qualifiedAttribution_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="qualifiedAttribution_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 1 items](#qualifiedAttribution_anyOf_i1_items) | -           |

#### <a name="qualifiedAttribution_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [Attribution](#qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#qualifiedAttribution_anyOf_i1_items_oneOf_i1)      |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `Attribution`

**Title:** Attribution

inline description of Attribution

|                           |                                                                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                |
| **Additional properties** | Any type allowed                                                                                                                                                        |
| **Same definition as**    | [Attribution](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Attribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="wasUsedBy"></a>Property `wasUsedBy`

**Title:** was used by

List of activities that used the Data Service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                |
| ----------------------------- |
| [item 0](#wasUsedBy_anyOf_i0) |
| [item 1](#wasUsedBy_anyOf_i1) |

### <a name="wasUsedBy_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="wasUsedBy_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [item 1 items](#wasUsedBy_anyOf_i1_items) | -           |

#### <a name="wasUsedBy_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                 |
| ---------------------------------------------- |
| [Activity](#wasUsedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#wasUsedBy_anyOf_i1_items_oneOf_i1)   |

##### <a name="wasUsedBy_anyOf_i1_items_oneOf_i0"></a>Property `Activity`

**Title:** Activity

inline description of Activity

|                           |                                                                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                  |
| **Additional properties** | Any type allowed                                                                                                                                          |
| **Same definition as**    | [Activity](#servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |

##### <a name="wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Activity

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

