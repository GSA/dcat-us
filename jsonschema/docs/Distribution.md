

**Title:** Distribution

A file that distributes the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                                   | Type               | Title/Description                                                                   |
| ---------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                             | string             | -                                                                                   |
| - [@type](#@type )                                         | string             | -                                                                                   |
| - [representationTechnique](#representationTechnique )     | More than one type | representation technique                                                            |
| - [status](#status )                                       | More than one type | lifecycle status                                                                    |
| - [characterEncoding](#characterEncoding )                 | More than one type | character encoding                                                                  |
| - [accessService](#accessService )                         | More than one type | access service                                                                      |
| - [accessURL](#accessURL )                                 | More than one type | access URL                                                                          |
| - [byteSize](#byteSize )                                   | null or string     | byte size                                                                           |
| - [compressFormat](#compressFormat )                       | More than one type | compression format                                                                  |
| - [downloadURL](#downloadURL )                             | More than one type | download URL                                                                        |
| - [mediaType](#mediaType )                                 | More than one type | media type                                                                          |
| - [packageFormat](#packageFormat )                         | More than one type | packaging format                                                                    |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string     | Spatial resolution (meters)                                                         |
| - [temporalResolution](#temporalResolution )               | null or string     | termporal resolution                                                                |
| - [availability](#availability )                           | More than one type | availability                                                                        |
| - [accessRestriction](#accessRestriction )                 | More than one type | access restriction                                                                  |
| - [cuiRestriction](#cuiRestriction )                       | More than one type | CUI restriction                                                                     |
| - [describedBy](#describedBy )                             | More than one type | data dictionary                                                                     |
| - [useRestriction](#useRestriction )                       | More than one type | use restriction                                                                     |
| - [accessRights](#accessRights )                           | More than one type | access rights                                                                       |
| - [conformsTo](#conformsTo )                               | More than one type | linked schemas                                                                      |
| - [description](#description )                             | null or string     | description                                                                         |
| - [descriptionMap](#descriptionMap )                       | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [format](#format )                                       | More than one type | format                                                                              |
| - [identifier](#identifier )                               | More than one type | identifier                                                                          |
| - [issued](#issued )                                       | More than one type | release date                                                                        |
| - [language](#language )                                   | More than one type | language                                                                            |
| - [license](#license )                                     | More than one type | license                                                                             |
| - [modified](#modified )                                   | More than one type | last modified                                                                       |
| - [rights](#rights )                                       | More than one type | rights                                                                              |
| - [title](#title )                                         | null or string     | title                                                                               |
| - [titleMap](#titleMap )                                   | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | More than one type | quality measurement                                                                 |
| - [page](#page )                                           | More than one type | documentation                                                                       |
| - [image](#image )                                         | More than one type | image                                                                               |
| - [checksum](#checksum )                                   | More than one type | checksum                                                                            |

## <a name="@id"></a>Property `Distribution > @id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Distribution > @type`

|             |                  |
| ----------- | ---------------- |
| **Type**    | `string`         |
| **Default** | `"Distribution"` |

## <a name="representationTechnique"></a>Property `Distribution > representationTechnique`

**Title:** representation technique

The format in which an Distribution is released. This is different from the file format as, for example, a ZIP file (file format) could contain an XML schema (representation technique). In DCAT-US profile,  this property SHOULD be used to express the spatial representation type (grid, vector, tin), by using the URIs of the corresponding code list operated by an approved registry

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [item 0](#representationTechnique_oneOf_i0)  |
| [Concept](#representationTechnique_oneOf_i1) |
| [item 2](#representationTechnique_oneOf_i2)  |

### <a name="representationTechnique_oneOf_i0"></a>Property `Distribution > representationTechnique > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="representationTechnique_oneOf_i1"></a>Property `Distribution > representationTechnique > oneOf > Concept`

**Title:** Concept

inline description of Concept

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="representationTechnique_oneOf_i2"></a>Property `Distribution > representationTechnique > oneOf > item 2`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="status"></a>Property `Distribution > status`

**Title:** lifecycle status

The status of the distribution in the context of maturity lifecycle

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)              |
| --------------------------- |
| [item 0](#status_oneOf_i0)  |
| [Concept](#status_oneOf_i1) |
| [item 2](#status_oneOf_i2)  |

### <a name="status_oneOf_i0"></a>Property `Distribution > status > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="status_oneOf_i1"></a>Property `Distribution > status > oneOf > Concept`

**Title:** Concept

inline description of Concept

|                           |                                              |
| ------------------------- | -------------------------------------------- |
| **Type**                  | `object`                                     |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Concept](#representationTechnique_oneOf_i1) |

### <a name="status_oneOf_i2"></a>Property `Distribution > status > oneOf > item 2`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="characterEncoding"></a>Property `Distribution > characterEncoding`

**Title:** character encoding

The list of character encodings of the Distribution, by using as value the character set names in the IANA register 

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#characterEncoding_anyOf_i0) |
| [item 1](#characterEncoding_anyOf_i1) |

### <a name="characterEncoding_anyOf_i0"></a>Property `Distribution > characterEncoding > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="characterEncoding_anyOf_i1"></a>Property `Distribution > characterEncoding > anyOf > item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 1 items](#characterEncoding_anyOf_i1_items) | -           |

#### <a name="characterEncoding_anyOf_i1_items"></a>Distribution > characterEncoding > anyOf > item 1 > item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="accessService"></a>Property `Distribution > accessService`

**Title:** access service

A data service that gives access to the distribution of the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                    |
| --------------------------------- |
| [item 0](#accessService_anyOf_i0) |
| [item 1](#accessService_anyOf_i1) |

### <a name="accessService_anyOf_i0"></a>Property `Distribution > accessService > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accessService_anyOf_i1"></a>Property `Distribution > accessService > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [item 1 items](#accessService_anyOf_i1_items) | -           |

#### <a name="accessService_anyOf_i1_items"></a>Distribution > accessService > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [DataService](#accessService_anyOf_i1_items_oneOf_i0) |
| [item 1](#accessService_anyOf_i1_items_oneOf_i1)      |

##### <a name="accessService_anyOf_i1_items_oneOf_i0"></a>Property `Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService`

**Title:** DataService

inline description of DataService

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Additional properties** | Any type allowed                |
| **Defined in**            | [Dataservice](./Dataservice.md) |

##### <a name="accessService_anyOf_i1_items_oneOf_i1"></a>Property `Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of DataService

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accessURL"></a>Property `Distribution > accessURL`

**Title:** access URL

A URL that gives access to a Distribution of the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                |
| ----------------------------- |
| [item 0](#accessURL_anyOf_i0) |
| [item 1](#accessURL_anyOf_i1) |

### <a name="accessURL_anyOf_i0"></a>Property `Distribution > accessURL > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accessURL_anyOf_i1"></a>Property `Distribution > accessURL > anyOf > item 1`

reference iri of Resource

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="byteSize"></a>Property `Distribution > byteSize`

**Title:** byte size

The size of a Distribution in bytes

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="compressFormat"></a>Property `Distribution > compressFormat`

**Title:** compression format

The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#compressFormat_oneOf_i0)    |
| [MediaType](#compressFormat_oneOf_i1) |
| [item 2](#compressFormat_oneOf_i2)    |

### <a name="compressFormat_oneOf_i0"></a>Property `Distribution > compressFormat > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="compressFormat_oneOf_i1"></a>Property `Distribution > compressFormat > oneOf > MediaType`

**Title:** MediaType

inline description of MediaType

|                           |                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                                 |
| **Same definition as**    | [MediaType](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

### <a name="compressFormat_oneOf_i2"></a>Property `Distribution > compressFormat > oneOf > item 2`

reference iri of MediaType

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="downloadURL"></a>Property `Distribution > downloadURL`

**Title:** download URL

A URL that is a direct link to a downloadable file of the Distribution in a given format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                  |
| ------------------------------- |
| [item 0](#downloadURL_anyOf_i0) |
| [item 1](#downloadURL_anyOf_i1) |

### <a name="downloadURL_anyOf_i0"></a>Property `Distribution > downloadURL > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="downloadURL_anyOf_i1"></a>Property `Distribution > downloadURL > anyOf > item 1`

reference iri of Resource

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="mediaType"></a>Property `Distribution > mediaType`

**Title:** media type

The media type of the Distribution as defined in the official register of media types managed by IANA

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                   |
| -------------------------------- |
| [item 0](#mediaType_oneOf_i0)    |
| [MediaType](#mediaType_oneOf_i1) |
| [item 2](#mediaType_oneOf_i2)    |

### <a name="mediaType_oneOf_i0"></a>Property `Distribution > mediaType > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="mediaType_oneOf_i1"></a>Property `Distribution > mediaType > oneOf > MediaType`

**Title:** MediaType

inline description of MediaType

|                           |                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                                 |
| **Same definition as**    | [MediaType](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

### <a name="mediaType_oneOf_i2"></a>Property `Distribution > mediaType > oneOf > item 2`

reference iri of MediaType

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="packageFormat"></a>Property `Distribution > packageFormat`

**Title:** packaging format

The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#packageFormat_oneOf_i0)    |
| [MediaType](#packageFormat_oneOf_i1) |
| [item 2](#packageFormat_oneOf_i2)    |

### <a name="packageFormat_oneOf_i0"></a>Property `Distribution > packageFormat > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="packageFormat_oneOf_i1"></a>Property `Distribution > packageFormat > oneOf > MediaType`

**Title:** MediaType

inline description of MediaType

|                           |                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                                 |
| **Same definition as**    | [MediaType](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

### <a name="packageFormat_oneOf_i2"></a>Property `Distribution > packageFormat > oneOf > item 2`

reference iri of MediaType

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatialResolutionInMeters"></a>Property `Distribution > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

The minimum spatial separation resolvable in a dataset distribution, measured in meters

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="temporalResolution"></a>Property `Distribution > temporalResolution`

**Title:** termporal resolution

The minimum time period resolvable in the dataset distribution

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="availability"></a>Property `Distribution > availability`

**Title:** availability

An indication how long it is planned to keep the Distribution of the Dataset available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                    |
| --------------------------------- |
| [item 0](#availability_oneOf_i0)  |
| [Concept](#availability_oneOf_i1) |
| [item 2](#availability_oneOf_i2)  |

### <a name="availability_oneOf_i0"></a>Property `Distribution > availability > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="availability_oneOf_i1"></a>Property `Distribution > availability > oneOf > Concept`

**Title:** Concept

inline description of Concept

|                           |                                              |
| ------------------------- | -------------------------------------------- |
| **Type**                  | `object`                                     |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Concept](#representationTechnique_oneOf_i1) |

### <a name="availability_oneOf_i2"></a>Property `Distribution > availability > oneOf > item 2`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accessRestriction"></a>Property `Distribution > accessRestriction`

**Title:** access restriction

List of access restrictions related to the distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#accessRestriction_anyOf_i0) |
| [item 1](#accessRestriction_anyOf_i1) |

### <a name="accessRestriction_anyOf_i0"></a>Property `Distribution > accessRestriction > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accessRestriction_anyOf_i1"></a>Property `Distribution > accessRestriction > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 1 items](#accessRestriction_anyOf_i1_items) | -           |

#### <a name="accessRestriction_anyOf_i1_items"></a>Distribution > accessRestriction > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                                  |
| --------------------------------------------------------------- |
| [AccessRestriction](#accessRestriction_anyOf_i1_items_oneOf_i0) |
| [item 1](#accessRestriction_anyOf_i1_items_oneOf_i1)            |

##### <a name="accessRestriction_anyOf_i1_items_oneOf_i0"></a>Property `Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction`

**Title:** AccessRestriction

inline description of AccessRestriction

|                           |                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                   |
| **Additional properties** | Any type allowed                                                                                                                                                           |
| **Same definition as**    | [AccessRestriction](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0) |

##### <a name="accessRestriction_anyOf_i1_items_oneOf_i1"></a>Property `Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of AccessRestriction

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="cuiRestriction"></a>Property `Distribution > cuiRestriction`

**Title:** CUI restriction

Controlled Unclassified Information restriction related to the distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                             |
| ------------------------------------------ |
| [item 0](#cuiRestriction_oneOf_i0)         |
| [CUIRestriction](#cuiRestriction_oneOf_i1) |
| [item 2](#cuiRestriction_oneOf_i2)         |

### <a name="cuiRestriction_oneOf_i0"></a>Property `Distribution > cuiRestriction > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="cuiRestriction_oneOf_i1"></a>Property `Distribution > cuiRestriction > oneOf > CUIRestriction`

**Title:** CUIRestriction

inline description of CUIRestriction

|                           |                                                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                                      |
| **Same definition as**    | [CUIRestriction](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1) |

### <a name="cuiRestriction_oneOf_i2"></a>Property `Distribution > cuiRestriction > oneOf > item 2`

reference iri of CUIRestriction

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="describedBy"></a>Property `Distribution > describedBy`

**Title:** data dictionary

A distribution containing the Data Dictionary for this distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#describedBy_oneOf_i0)       |
| [Distribution](#describedBy_oneOf_i1) |
| [item 2](#describedBy_oneOf_i2)       |

### <a name="describedBy_oneOf_i0"></a>Property `Distribution > describedBy > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="describedBy_oneOf_i1"></a>Property `Distribution > describedBy > oneOf > Distribution`

**Title:** Distribution

inline description of the data dictionary

|                           |                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                            |
| **Same definition as**    | [Distribution](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0) |

### <a name="describedBy_oneOf_i2"></a>Property `Distribution > describedBy > oneOf > item 2`

reference iri of the data dictionary

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="useRestriction"></a>Property `Distribution > useRestriction`

**Title:** use restriction

Use restriction related to the distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                     |
| ---------------------------------- |
| [item 0](#useRestriction_anyOf_i0) |
| [item 1](#useRestriction_anyOf_i1) |

### <a name="useRestriction_anyOf_i0"></a>Property `Distribution > useRestriction > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="useRestriction_anyOf_i1"></a>Property `Distribution > useRestriction > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [item 1 items](#useRestriction_anyOf_i1_items) | -           |

#### <a name="useRestriction_anyOf_i1_items"></a>Distribution > useRestriction > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                            |
| --------------------------------------------------------- |
| [UseRestriction](#useRestriction_anyOf_i1_items_oneOf_i0) |
| [item 1](#useRestriction_anyOf_i1_items_oneOf_i1)         |

##### <a name="useRestriction_anyOf_i1_items_oneOf_i0"></a>Property `Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction`

**Title:** UseRestriction

inline description of UseRestriction

|                           |                                                                                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                                     |
| **Same definition as**    | [UseRestriction](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0) |

##### <a name="useRestriction_anyOf_i1_items_oneOf_i1"></a>Property `Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of UseRestriction

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accessRights"></a>Property `Distribution > accessRights`

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

### <a name="accessRights_oneOf_i0"></a>Property `Distribution > accessRights > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accessRights_oneOf_i1"></a>Property `Distribution > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="accessRights_oneOf_i2"></a>Property `Distribution > accessRights > oneOf > item 2`

reference iri of RightsStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `Distribution > conformsTo`

**Title:** linked schemas

List of established schemas or reference systems to which the described Distribution conforms

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#conformsTo_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1) |

### <a name="conformsTo_anyOf_i0"></a>Property `Distribution > conformsTo > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="conformsTo_anyOf_i1"></a>Property `Distribution > conformsTo > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#conformsTo_anyOf_i1_items) | -           |

#### <a name="conformsTo_anyOf_i1_items"></a>Distribution > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Standard](#conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i1)   |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `Distribution > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

inline description of Standard

|                           |                                                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                   |
| **Additional properties** | Any type allowed                                                                                                                                           |
| **Same definition as**    | [Standard](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `Distribution > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of Standard

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `Distribution > description`

**Title:** description

A free-text account of the Distribution

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="descriptionMap"></a>Property `Distribution > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="format"></a>Property `Distribution > format`

**Title:** format

The file format of the Distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [item 0](#format_oneOf_i0)    |
| [MediaType](#format_oneOf_i1) |
| [item 2](#format_oneOf_i2)    |

### <a name="format_oneOf_i0"></a>Property `Distribution > format > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="format_oneOf_i1"></a>Property `Distribution > format > oneOf > MediaType`

**Title:** MediaType

inline description of the format

|                           |                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                                 |
| **Same definition as**    | [MediaType](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

### <a name="format_oneOf_i2"></a>Property `Distribution > format > oneOf > item 2`

reference iri of the format

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `Distribution > identifier`

**Title:** identifier

A list of unique identifiers for the Distribution (e.g. DOI, ISBN)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Distribution > identifier > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="identifier_anyOf_i1"></a>Property `Distribution > identifier > anyOf > item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>Distribution > identifier > anyOf > item 1 > item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="issued"></a>Property `Distribution > issued`

**Title:** release date

The date of formal issuance (e.g., publication) of the Distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Distribution > issued > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="issued_anyOf_i1"></a>Property `Distribution > issued > anyOf > item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Distribution > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Distribution > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Distribution > issued > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Distribution > issued > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `Distribution > language`

**Title:** language

A language or languages used in the Distribution. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#language_anyOf_i0) |
| [item 1](#language_anyOf_i1) |
| [item 2](#language_anyOf_i2) |

### <a name="language_anyOf_i0"></a>Property `Distribution > language > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="language_anyOf_i1"></a>Property `Distribution > language > anyOf > item 1`

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `Distribution > language > anyOf > item 2`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 2 items](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>Distribution > language > anyOf > item 2 > item 2 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="license"></a>Property `Distribution > license`

**Title:** license

A license under which the Distribution is made available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#license_oneOf_i0)          |
| [LicenseDocument](#license_oneOf_i1) |
| [item 2](#license_oneOf_i2)          |

### <a name="license_oneOf_i0"></a>Property `Distribution > license > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="license_oneOf_i1"></a>Property `Distribution > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

inline description of LicenseDocument

|                           |                                                                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                        |
| **Additional properties** | Any type allowed                                                                                                                                |
| **Same definition as**    | [LicenseDocument](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

### <a name="license_oneOf_i2"></a>Property `Distribution > license > oneOf > item 2`

reference iri of LicenseDocument

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="modified"></a>Property `Distribution > modified`

**Title:** last modified

The most recent date on which the Distribution was changed or modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `Distribution > modified > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="modified_anyOf_i1"></a>Property `Distribution > modified > anyOf > item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `Distribution > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `Distribution > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `Distribution > modified > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `Distribution > modified > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="rights"></a>Property `Distribution > rights`

**Title:** rights

A statement that specifies rights associated with the Distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#rights_oneOf_i0)          |
| [RightsStatement](#rights_oneOf_i1) |
| [item 2](#rights_oneOf_i2)          |

### <a name="rights_oneOf_i0"></a>Property `Distribution > rights > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="rights_oneOf_i1"></a>Property `Distribution > rights > oneOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="rights_oneOf_i2"></a>Property `Distribution > rights > oneOf > item 2`

reference iri of RightsStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `Distribution > title`

**Title:** title

A name given to the Distribution

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="titleMap"></a>Property `Distribution > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="hasQualityMeasurement"></a>Property `Distribution > hasQualityMeasurement`

**Title:** quality measurement

A list of quality measurements for the distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#hasQualityMeasurement_anyOf_i0) |
| [item 1](#hasQualityMeasurement_anyOf_i1) |

### <a name="hasQualityMeasurement_anyOf_i0"></a>Property `Distribution > hasQualityMeasurement > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="hasQualityMeasurement_anyOf_i1"></a>Property `Distribution > hasQualityMeasurement > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [item 1 items](#hasQualityMeasurement_anyOf_i1_items) | -           |

#### <a name="hasQualityMeasurement_anyOf_i1_items"></a>Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                                       |
| -------------------------------------------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

inline description of QualityMeasurement

|                           |                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                        |
| **Additional properties** | Any type allowed                                                                                                                                                                |
| **Same definition as**    | [QualityMeasurement](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of QualityMeasurement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="page"></a>Property `Distribution > page`

**Title:** documentation

A page or document about this Distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)           |
| ------------------------ |
| [item 0](#page_anyOf_i0) |
| [item 1](#page_anyOf_i1) |

### <a name="page_anyOf_i0"></a>Property `Distribution > page > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="page_anyOf_i1"></a>Property `Distribution > page > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be      | Description |
| ------------------------------------ | ----------- |
| [item 1 items](#page_anyOf_i1_items) | -           |

#### <a name="page_anyOf_i1_items"></a>Distribution > page > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [Document](#page_anyOf_i1_items_oneOf_i0) |
| [item 1](#page_anyOf_i1_items_oneOf_i1)   |

##### <a name="page_anyOf_i1_items_oneOf_i0"></a>Property `Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document`

**Title:** Document

inline description of Document

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [Document](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

##### <a name="page_anyOf_i1_items_oneOf_i1"></a>Property `Distribution > page > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of Document

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="image"></a>Property `Distribution > image`

**Title:** image

A link to a thumbnail picture illustrating the content of the distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)            |
| ------------------------- |
| [item 0](#image_anyOf_i0) |
| [item 1](#image_anyOf_i1) |

### <a name="image_anyOf_i0"></a>Property `Distribution > image > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="image_anyOf_i1"></a>Property `Distribution > image > anyOf > item 1`

The link to the image

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="checksum"></a>Property `Distribution > checksum`

**Title:** checksum

A mechanism that can be used to verify that the contents of a distribution have not changed

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                 |
| ------------------------------ |
| [item 0](#checksum_oneOf_i0)   |
| [Checksum](#checksum_oneOf_i1) |
| [item 2](#checksum_oneOf_i2)   |

### <a name="checksum_oneOf_i0"></a>Property `Distribution > checksum > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="checksum_oneOf_i1"></a>Property `Distribution > checksum > oneOf > Checksum`

**Title:** Checksum

inline description of Checksum

|                           |                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                  |
| **Additional properties** | Any type allowed                                                                                                                          |
| **Same definition as**    | [Checksum](#accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1) |

### <a name="checksum_oneOf_i2"></a>Property `Distribution > checksum > oneOf > item 2`

reference iri of Checksum

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

