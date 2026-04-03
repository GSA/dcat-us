

**Title:** Distribution

A file that distributes the dataset

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                                   | Type               | Title/Description                                                                   |
| ---------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                             | string             | -                                                                                   |
| - [@type](#@type )                                         | string             | -                                                                                   |
| - [representationTechnique](#representationTechnique )     | More than one type | representation technique                                                            |
| - [status](#status )                                       | More than one type | lifecycle status                                                                    |
| - [characterEncoding](#characterEncoding )                 | More than one type | character encoding                                                                  |
| - [accessService](#accessService )                         | null or array      | access service                                                                      |
| - [accessURL](#accessURL )                                 | More than one type | access URL                                                                          |
| - [byteSize](#byteSize )                                   | null or string     | byte size                                                                           |
| - [compressFormat](#compressFormat )                       | More than one type | compression format                                                                  |
| - [downloadURL](#downloadURL )                             | More than one type | download URL                                                                        |
| - [mediaType](#mediaType )                                 | More than one type | media type                                                                          |
| - [packageFormat](#packageFormat )                         | More than one type | packaging format                                                                    |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string     | Spatial resolution (meters)                                                         |
| - [temporalResolution](#temporalResolution )               | null or string     | termporal resolution                                                                |
| - [availability](#availability )                           | More than one type | availability                                                                        |
| - [accessRestriction](#accessRestriction )                 | null or array      | access restriction                                                                  |
| - [cuiRestriction](#cuiRestriction )                       | More than one type | CUI restriction                                                                     |
| - [describedBy](#describedBy )                             | More than one type | data dictionary                                                                     |
| - [useRestriction](#useRestriction )                       | null or array      | use restriction                                                                     |
| - [accessRights](#accessRights )                           | More than one type | access rights                                                                       |
| - [conformsTo](#conformsTo )                               | null or array      | linked schemas                                                                      |
| - [description](#description )                             | null or string     | description                                                                         |
| - [descriptionMap](#descriptionMap )                       | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [format](#format )                                       | More than one type | format                                                                              |
| - [identifier](#identifier )                               | More than one type | identifier                                                                          |
| - [otherIdentifier](#otherIdentifier )                     | null or array      | other identifier                                                                    |
| - [issued](#issued )                                       | More than one type | release date                                                                        |
| - [language](#language )                                   | More than one type | language                                                                            |
| - [license](#license )                                     | More than one type | license                                                                             |
| - [modified](#modified )                                   | More than one type | last modified                                                                       |
| - [rights](#rights )                                       | More than one type | rights                                                                              |
| - [title](#title )                                         | null or string     | title                                                                               |
| - [titleMap](#titleMap )                                   | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | null or array      | quality measurement                                                                 |
| - [page](#page )                                           | null or array      | documentation                                                                       |
| - [image](#image )                                         | More than one type | image                                                                               |
| - [checksum](#checksum )                                   | More than one type | checksum                                                                            |

## <a name="@id"></a>Property `Distribution > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Distribution > @type`

| **Type**    | `string`         |
| ----------- | ---------------- |
| **Default** | `"Distribution"` |

## <a name="representationTechnique"></a>Property `Distribution > representationTechnique`

**Title:** representation technique

The format in which an Distribution is released. This is different from the file format as, for example, a ZIP file (file format) could contain an XML schema (representation technique). In DCAT-US profile,  this property SHOULD be used to express the spatial representation type (grid, vector, tin), by using the URIs of the corresponding code list operated by an approved registry

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                      |
| ------------------------------------------------------------------- |
| [Null allowed when not required](#representationTechnique_anyOf_i0) |
| [Concept](#representationTechnique_anyOf_i1)                        |
| [Link](#representationTechnique_anyOf_i2)                           |

### <a name="representationTechnique_anyOf_i0"></a>Property `Distribution > representationTechnique > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="representationTechnique_anyOf_i1"></a>Property `Distribution > representationTechnique > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="representationTechnique_anyOf_i2"></a>Property `Distribution > representationTechnique > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="status"></a>Property `Distribution > status`

**Title:** lifecycle status

The status of the distribution in the context of maturity lifecycle

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#status_anyOf_i0) |
| [Concept](#status_anyOf_i1)                        |
| [Link](#status_anyOf_i2)                           |

### <a name="status_anyOf_i0"></a>Property `Distribution > status > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_anyOf_i1"></a>Property `Distribution > status > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                     |
| ------------------------- | -------------------------------------------- |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Concept](#representationTechnique_anyOf_i1) |

### <a name="status_anyOf_i2"></a>Property `Distribution > status > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="characterEncoding"></a>Property `Distribution > characterEncoding`

**Title:** character encoding

The list of character encodings of the Distribution, by using as value the character set names in the IANA register 

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [Null allowed when not required](#characterEncoding_anyOf_i0) |
| [List of encodings](#characterEncoding_anyOf_i1)              |

### <a name="characterEncoding_anyOf_i0"></a>Property `Distribution > characterEncoding > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="characterEncoding_anyOf_i1"></a>Property `Distribution > characterEncoding > anyOf > List of encodings`

**Title:** List of encodings

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [Character encoding](#characterEncoding_anyOf_i1_items) | -           |

#### <a name="characterEncoding_anyOf_i1_items"></a>Distribution > characterEncoding > anyOf > List of encodings > Character encoding

**Title:** Character encoding

| **Type** | `string` |
| -------- | -------- |

## <a name="accessService"></a>Property `Distribution > accessService`

**Title:** access service

A data service that gives access to the distribution of the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description |
| -------------------------------------------------- | ----------- |
| [DataService object or link](#accessService_items) | -           |

### <a name="accessService_items"></a>Distribution > accessService > DataService object or link

**Title:** DataService object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [DataService](#accessService_items_anyOf_i0) |
| [Link](#accessService_items_anyOf_i1)        |

#### <a name="accessService_items_anyOf_i0"></a>Property `Distribution > accessService > DataService object or link > anyOf > DataService`

**Title:** DataService

inline description of DataService

| **Type**                  | `object`                        |
| ------------------------- | ------------------------------- |
| **Additional properties** | Any type allowed                |
| **Defined in**            | [Dataservice](./Dataservice.md) |

#### <a name="accessService_items_anyOf_i1"></a>Property `Distribution > accessService > DataService object or link > anyOf > Link`

**Title:** Link

reference iri of DataService

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="accessURL"></a>Property `Distribution > accessURL`

**Title:** access URL

A URL that gives access to a Distribution of the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#accessURL_anyOf_i0) |
| [URL](#accessURL_anyOf_i1)                            |

### <a name="accessURL_anyOf_i0"></a>Property `Distribution > accessURL > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessURL_anyOf_i1"></a>Property `Distribution > accessURL > anyOf > URL`

**Title:** URL

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="byteSize"></a>Property `Distribution > byteSize`

**Title:** byte size

The size of a Distribution in bytes

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="compressFormat"></a>Property `Distribution > compressFormat`

**Title:** compression format

The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [Null allowed when not required](#compressFormat_anyOf_i0) |
| [MediaType](#compressFormat_anyOf_i1)                      |
| [Link](#compressFormat_anyOf_i2)                           |

### <a name="compressFormat_anyOf_i0"></a>Property `Distribution > compressFormat > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="compressFormat_anyOf_i1"></a>Property `Distribution > compressFormat > anyOf > MediaType`

**Title:** MediaType

inline description of MediaType

| **Type**                  | `object`                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                      |
| **Same definition as**    | [MediaType](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_compressFormat_anyOf_i1) |

### <a name="compressFormat_anyOf_i2"></a>Property `Distribution > compressFormat > anyOf > Link`

**Title:** Link

reference iri of MediaType

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="downloadURL"></a>Property `Distribution > downloadURL`

**Title:** download URL

A URL that is a direct link to a downloadable file of the Distribution in a given format

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#downloadURL_anyOf_i0) |
| [URL](#downloadURL_anyOf_i1)                            |

### <a name="downloadURL_anyOf_i0"></a>Property `Distribution > downloadURL > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="downloadURL_anyOf_i1"></a>Property `Distribution > downloadURL > anyOf > URL`

**Title:** URL

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="mediaType"></a>Property `Distribution > mediaType`

**Title:** media type

The media type of the Distribution as defined in the official register of media types managed by IANA

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#mediaType_anyOf_i0) |
| [MediaType](#mediaType_anyOf_i1)                      |
| [Link](#mediaType_anyOf_i2)                           |

### <a name="mediaType_anyOf_i0"></a>Property `Distribution > mediaType > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="mediaType_anyOf_i1"></a>Property `Distribution > mediaType > anyOf > MediaType`

**Title:** MediaType

inline description of MediaType

| **Type**                  | `object`                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                      |
| **Same definition as**    | [MediaType](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_compressFormat_anyOf_i1) |

### <a name="mediaType_anyOf_i2"></a>Property `Distribution > mediaType > anyOf > Link`

**Title:** Link

reference iri of MediaType

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="packageFormat"></a>Property `Distribution > packageFormat`

**Title:** packaging format

The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [Null allowed when not required](#packageFormat_anyOf_i0) |
| [MediaType](#packageFormat_anyOf_i1)                      |
| [Link](#packageFormat_anyOf_i2)                           |

### <a name="packageFormat_anyOf_i0"></a>Property `Distribution > packageFormat > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="packageFormat_anyOf_i1"></a>Property `Distribution > packageFormat > anyOf > MediaType`

**Title:** MediaType

inline description of MediaType

| **Type**                  | `object`                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                      |
| **Same definition as**    | [MediaType](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_compressFormat_anyOf_i1) |

### <a name="packageFormat_anyOf_i2"></a>Property `Distribution > packageFormat > anyOf > Link`

**Title:** Link

reference iri of MediaType

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="spatialResolutionInMeters"></a>Property `Distribution > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

The minimum spatial separation resolvable in a dataset distribution, measured in meters

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="temporalResolution"></a>Property `Distribution > temporalResolution`

**Title:** termporal resolution

The minimum time period resolvable in the dataset distribution

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="availability"></a>Property `Distribution > availability`

**Title:** availability

An indication how long it is planned to keep the Distribution of the Dataset available

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#availability_anyOf_i0) |
| [Concept](#availability_anyOf_i1)                        |
| [Link](#availability_anyOf_i2)                           |

### <a name="availability_anyOf_i0"></a>Property `Distribution > availability > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="availability_anyOf_i1"></a>Property `Distribution > availability > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                     |
| ------------------------- | -------------------------------------------- |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Concept](#representationTechnique_anyOf_i1) |

### <a name="availability_anyOf_i2"></a>Property `Distribution > availability > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="accessRestriction"></a>Property `Distribution > accessRestriction`

**Title:** access restriction

List of access restrictions related to the distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                              | Description |
| ------------------------------------------------------------ | ----------- |
| [AccessRestriction object or link](#accessRestriction_items) | -           |

### <a name="accessRestriction_items"></a>Distribution > accessRestriction > AccessRestriction object or link

**Title:** AccessRestriction object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [AccessRestriction](#accessRestriction_items_anyOf_i0) |
| [Link](#accessRestriction_items_anyOf_i1)              |

#### <a name="accessRestriction_items_anyOf_i0"></a>Property `Distribution > accessRestriction > AccessRestriction object or link > anyOf > AccessRestriction`

**Title:** AccessRestriction

inline description of AccessRestriction

| **Type**                  | `object`                                                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                       |
| **Same definition as**    | [AccessRestriction](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_accessRestriction_items_anyOf_i0) |

#### <a name="accessRestriction_items_anyOf_i1"></a>Property `Distribution > accessRestriction > AccessRestriction object or link > anyOf > Link`

**Title:** Link

reference iri of AccessRestriction

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="cuiRestriction"></a>Property `Distribution > cuiRestriction`

**Title:** CUI restriction

Controlled Unclassified Information restriction related to the distribution

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [Null allowed when not required](#cuiRestriction_anyOf_i0) |
| [CUIRestriction](#cuiRestriction_anyOf_i1)                 |
| [Link](#cuiRestriction_anyOf_i2)                           |

### <a name="cuiRestriction_anyOf_i0"></a>Property `Distribution > cuiRestriction > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="cuiRestriction_anyOf_i1"></a>Property `Distribution > cuiRestriction > anyOf > CUIRestriction`

**Title:** CUIRestriction

inline description of CUIRestriction

| **Type**                  | `object`                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [CUIRestriction](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_cuiRestriction_anyOf_i1) |

### <a name="cuiRestriction_anyOf_i2"></a>Property `Distribution > cuiRestriction > anyOf > Link`

**Title:** Link

reference iri of CUIRestriction

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="describedBy"></a>Property `Distribution > describedBy`

**Title:** data dictionary

A distribution containing the Data Dictionary for this distribution

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#describedBy_anyOf_i0) |
| [Distribution](#describedBy_anyOf_i1)                   |
| [Link](#describedBy_anyOf_i2)                           |

### <a name="describedBy_anyOf_i0"></a>Property `Distribution > describedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="describedBy_anyOf_i1"></a>Property `Distribution > describedBy > anyOf > Distribution`

**Title:** Distribution

inline description of the data dictionary

| **Type**                  | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Distribution](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0) |

### <a name="describedBy_anyOf_i2"></a>Property `Distribution > describedBy > anyOf > Link`

**Title:** Link

reference iri of the data dictionary

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="useRestriction"></a>Property `Distribution > useRestriction`

**Title:** use restriction

Use restriction related to the distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [UseRestriction object or link](#useRestriction_items) | -           |

### <a name="useRestriction_items"></a>Distribution > useRestriction > UseRestriction object or link

**Title:** UseRestriction object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                   |
| ------------------------------------------------ |
| [UseRestriction](#useRestriction_items_anyOf_i0) |
| [Link](#useRestriction_items_anyOf_i1)           |

#### <a name="useRestriction_items_anyOf_i0"></a>Property `Distribution > useRestriction > UseRestriction object or link > anyOf > UseRestriction`

**Title:** UseRestriction

inline description of UseRestriction

| **Type**                  | `object`                                                                                                                         |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [UseRestriction](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_useRestriction_items_anyOf_i0) |

#### <a name="useRestriction_items_anyOf_i1"></a>Property `Distribution > useRestriction > UseRestriction object or link > anyOf > Link`

**Title:** Link

reference iri of UseRestriction

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="accessRights"></a>Property `Distribution > accessRights`

**Title:** access rights

Information regarding access or restrictions based on privacy, security, or other policies

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_anyOf_i0) |
| [RightsStatement](#accessRights_anyOf_i1)                |
| [Link](#accessRights_anyOf_i2)                           |

### <a name="accessRights_anyOf_i0"></a>Property `Distribution > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `Distribution > accessRights > anyOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

| **Type**                  | `object`                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                          |
| **Same definition as**    | [RightsStatement](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_accessRights_anyOf_i1) |

### <a name="accessRights_anyOf_i2"></a>Property `Distribution > accessRights > anyOf > Link`

**Title:** Link

reference iri of RightsStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `Distribution > conformsTo`

**Title:** linked schemas

List of established schemas or reference systems to which the described Distribution conforms

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [Standard object or link](#conformsTo_items) | -           |

### <a name="conformsTo_items"></a>Distribution > conformsTo > Standard object or link

**Title:** Standard object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [Standard](#conformsTo_items_anyOf_i0) |
| [Link](#conformsTo_items_anyOf_i1)     |

#### <a name="conformsTo_items_anyOf_i0"></a>Property `Distribution > conformsTo > Standard object or link > anyOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Standard](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_conformsTo_items_anyOf_i0) |

#### <a name="conformsTo_items_anyOf_i1"></a>Property `Distribution > conformsTo > Standard object or link > anyOf > Link`

**Title:** Link

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="description"></a>Property `Distribution > description`

**Title:** description

A free-text account of the Distribution

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="descriptionMap"></a>Property `Distribution > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="format"></a>Property `Distribution > format`

**Title:** format

The file format of the Distribution

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#format_anyOf_i0) |
| [MediaType](#format_anyOf_i1)                      |
| [Link](#format_anyOf_i2)                           |

### <a name="format_anyOf_i0"></a>Property `Distribution > format > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="format_anyOf_i1"></a>Property `Distribution > format > anyOf > MediaType`

**Title:** MediaType

inline description of the format

| **Type**                  | `object`                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                      |
| **Same definition as**    | [MediaType](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_compressFormat_anyOf_i1) |

### <a name="format_anyOf_i2"></a>Property `Distribution > format > anyOf > Link`

**Title:** Link

reference iri of the format

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `Distribution > identifier`

**Title:** identifier

The unique identifier for the Distribution (e.g. DOI, ISBN)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#identifier_anyOf_i0) |
| [Identifier](#identifier_anyOf_i1)                     |
| [Link](#identifier_anyOf_i2)                           |

### <a name="identifier_anyOf_i0"></a>Property `Distribution > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Distribution > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [Identifier](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_otherIdentifier_items_anyOf_i0) |

### <a name="identifier_anyOf_i2"></a>Property `Distribution > identifier > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="otherIdentifier"></a>Property `Distribution > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Distribution besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [Identifier object or link](#otherIdentifier_items) | -           |

### <a name="otherIdentifier_items"></a>Distribution > otherIdentifier > Identifier object or link

**Title:** Identifier object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                |
| --------------------------------------------- |
| [Identifier](#otherIdentifier_items_anyOf_i0) |
| [Link](#otherIdentifier_items_anyOf_i1)       |

#### <a name="otherIdentifier_items_anyOf_i0"></a>Property `Distribution > otherIdentifier > Identifier object or link > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [Identifier](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_otherIdentifier_items_anyOf_i0) |

#### <a name="otherIdentifier_items_anyOf_i1"></a>Property `Distribution > otherIdentifier > Identifier object or link > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="issued"></a>Property `Distribution > issued`

**Title:** release date

The date of formal issuance (e.g., publication) of the Distribution

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>Property `Distribution > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Distribution > issued > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_anyOf_i0) |
| [item 1](#issued_anyOf_i1_anyOf_i1) |
| [item 2](#issued_anyOf_i1_anyOf_i2) |
| [item 3](#issued_anyOf_i1_anyOf_i3) |

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `Distribution > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `Distribution > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `Distribution > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `Distribution > issued > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `Distribution > language`

**Title:** language

A language or languages used in the Distribution. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#language_anyOf_i0) |
| [Language code](#language_anyOf_i1)                  |
| [List of languages](#language_anyOf_i2)              |

### <a name="language_anyOf_i0"></a>Property `Distribution > language > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="language_anyOf_i1"></a>Property `Distribution > language > anyOf > Language code`

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `Distribution > language > anyOf > List of languages`

**Title:** List of languages

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Language code](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>Distribution > language > anyOf > List of languages > Language code

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="license"></a>Property `Distribution > license`

**Title:** license

A license under which the Distribution is made available

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#license_anyOf_i0) |
| [LicenseDocument](#license_anyOf_i1)                |
| [Link](#license_anyOf_i2)                           |

### <a name="license_anyOf_i0"></a>Property `Distribution > license > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="license_anyOf_i1"></a>Property `Distribution > license > anyOf > LicenseDocument`

**Title:** LicenseDocument

inline description of LicenseDocument

| **Type**                  | `object`                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                     |
| **Same definition as**    | [LicenseDocument](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_license_anyOf_i1) |

### <a name="license_anyOf_i2"></a>Property `Distribution > license > anyOf > Link`

**Title:** Link

reference iri of LicenseDocument

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="modified"></a>Property `Distribution > modified`

**Title:** last modified

The most recent date on which the Distribution was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `Distribution > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `Distribution > modified > anyOf > Date string`

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

#### <a name="modified_anyOf_i1_anyOf_i0"></a>Property `Distribution > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>Property `Distribution > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>Property `Distribution > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>Property `Distribution > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="rights"></a>Property `Distribution > rights`

**Title:** rights

A statement that specifies rights associated with the Distribution

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#rights_anyOf_i0) |
| [RightsStatement](#rights_anyOf_i1)                |
| [Link](#rights_anyOf_i2)                           |

### <a name="rights_anyOf_i0"></a>Property `Distribution > rights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="rights_anyOf_i1"></a>Property `Distribution > rights > anyOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

| **Type**                  | `object`                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                          |
| **Same definition as**    | [RightsStatement](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_accessRights_anyOf_i1) |

### <a name="rights_anyOf_i2"></a>Property `Distribution > rights > anyOf > Link`

**Title:** Link

reference iri of RightsStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="title"></a>Property `Distribution > title`

**Title:** title

A name given to the Distribution

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="titleMap"></a>Property `Distribution > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="hasQualityMeasurement"></a>Property `Distribution > hasQualityMeasurement`

**Title:** quality measurement

A list of quality measurements for the distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [QualityMeasurement object or link](#hasQualityMeasurement_items) | -           |

### <a name="hasQualityMeasurement_items"></a>Distribution > hasQualityMeasurement > QualityMeasurement object or link

**Title:** QualityMeasurement object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_items_anyOf_i0) |
| [Link](#hasQualityMeasurement_items_anyOf_i1)               |

#### <a name="hasQualityMeasurement_items_anyOf_i0"></a>Property `Distribution > hasQualityMeasurement > QualityMeasurement object or link > anyOf > QualityMeasurement`

**Title:** QualityMeasurement

inline description of QualityMeasurement

| **Type**                  | `object`                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [QualityMeasurement](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_hasQualityMeasurement_items_anyOf_i0) |

#### <a name="hasQualityMeasurement_items_anyOf_i1"></a>Property `Distribution > hasQualityMeasurement > QualityMeasurement object or link > anyOf > Link`

**Title:** Link

reference iri of QualityMeasurement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="page"></a>Property `Distribution > page`

**Title:** documentation

A page or document about this Distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [Document object or link](#page_items) | -           |

### <a name="page_items"></a>Distribution > page > Document object or link

**Title:** Document object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [Document](#page_items_anyOf_i0) |
| [Link](#page_items_anyOf_i1)     |

#### <a name="page_items_anyOf_i0"></a>Property `Distribution > page > Document object or link > anyOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                 |
| **Same definition as**    | [Document](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_page_items_anyOf_i0) |

#### <a name="page_items_anyOf_i1"></a>Property `Distribution > page > Document object or link > anyOf > Link`

**Title:** Link

reference iri of Document

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="image"></a>Property `Distribution > image`

**Title:** image

A link to a thumbnail picture illustrating the content of the distribution

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#image_anyOf_i0) |
| [Link](#image_anyOf_i1)                           |

### <a name="image_anyOf_i0"></a>Property `Distribution > image > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="image_anyOf_i1"></a>Property `Distribution > image > anyOf > Link`

**Title:** Link

The link to the image

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="checksum"></a>Property `Distribution > checksum`

**Title:** checksum

A mechanism that can be used to verify that the contents of a distribution have not changed

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#checksum_anyOf_i0) |
| [Checksum](#checksum_anyOf_i1)                       |
| [Link](#checksum_anyOf_i2)                           |

### <a name="checksum_anyOf_i0"></a>Property `Distribution > checksum > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="checksum_anyOf_i1"></a>Property `Distribution > checksum > anyOf > Checksum`

**Title:** Checksum

inline description of Checksum

| **Type**                  | `object`                                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                               |
| **Same definition as**    | [Checksum](#accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_sample_items_anyOf_i0_checksum_anyOf_i1) |

### <a name="checksum_anyOf_i2"></a>Property `Distribution > checksum > anyOf > Link`

**Title:** Link

reference iri of Checksum

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

