

**Title:** Distribution

A file that distributes the dataset

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                                   | Type                    | Title/Description           |
| ---------------------------------------------------------- | ----------------------- | --------------------------- |
| - [@id](#@id )                                             | string                  | -                           |
| - [@type](#@type )                                         | string                  | -                           |
| - [representationTechnique](#representationTechnique )     | More than one type      | representation technique    |
| - [status](#status )                                       | More than one type      | lifecycle status            |
| - [characterEncoding](#characterEncoding )                 | More than one type      | character encoding          |
| - [accessService](#accessService )                         | null or array           | access service              |
| - [accessURL](#accessURL )                                 | More than one type      | access URL                  |
| - [byteSize](#byteSize )                                   | null or string          | byte size                   |
| - [compressFormat](#compressFormat )                       | null or string          | compression format          |
| - [downloadURL](#downloadURL )                             | More than one type      | download URL                |
| - [mediaType](#mediaType )                                 | null or string          | media type                  |
| - [packageFormat](#packageFormat )                         | null or string          | packaging format            |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string          | Spatial resolution (meters) |
| - [temporalResolution](#temporalResolution )               | null or string          | termporal resolution        |
| - [availability](#availability )                           | More than one type      | availability                |
| - [accessRestriction](#accessRestriction )                 | null or array           | access restriction          |
| - [cuiRestriction](#cuiRestriction )                       | More than one type      | CUI restriction             |
| - [describedBy](#describedBy )                             | More than one type      | data dictionary             |
| - [useRestriction](#useRestriction )                       | null or array           | use restriction             |
| - [accessRights](#accessRights )                           | More than one type      | access rights               |
| - [conformsTo](#conformsTo )                               | null or array           | linked schemas              |
| - [description](#description )                             | null or string          | description                 |
| - [format](#format )                                       | null or string          | format                      |
| - [identifier](#identifier )                               | More than one type      | identifier                  |
| - [otherIdentifier](#otherIdentifier )                     | null or array           | other identifier            |
| - [issued](#issued )                                       | More than one type      | release date                |
| - [language](#language )                                   | More than one type      | language                    |
| - [license](#license )                                     | More than one type      | license                     |
| - [modified](#modified )                                   | More than one type      | last modified               |
| - [rights](#rights )                                       | null or array of string | rights                      |
| - [title](#title )                                         | null or string          | title                       |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | null or array           | quality measurement         |
| - [page](#page )                                           | null or array           | documentation               |
| - [image](#image )                                         | More than one type      | image                       |
| - [checksum](#checksum )                                   | More than one type      | checksum                    |

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

### <a name="representationTechnique_anyOf_i0"></a>Property `Distribution > representationTechnique > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="representationTechnique_anyOf_i1"></a>Property `Distribution > representationTechnique > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

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

### <a name="status_anyOf_i0"></a>Property `Distribution > status > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_anyOf_i1"></a>Property `Distribution > status > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type                           |
| ------------------------- | -------------------------------------------- |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Concept](#representationTechnique_anyOf_i1) |

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

| Each item of this array must be     | Description                                   |
| ----------------------------------- | --------------------------------------------- |
| [DataService](#accessService_items) | A service for providing data at a URL or URLs |

### <a name="accessService_items"></a>Distribution > accessService > DataService

**Title:** DataService

A service for providing data at a URL or URLs

| **Type**                  | `object`                        |
| ------------------------- | ------------------------------- |
| **Additional properties** | Any type allowed                |
| **Defined in**            | [Dataservice](./Dataservice.md) |

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

| **Type** | `null or string` |
| -------- | ---------------- |

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

The media type of the Distribution as defined in the official register of media types managed by IANA: https://www.iana.org/assignments/media-types/media-types.xhtml

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="packageFormat"></a>Property `Distribution > packageFormat`

**Title:** packaging format

The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together

| **Type** | `null or string` |
| -------- | ---------------- |

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

### <a name="availability_anyOf_i0"></a>Property `Distribution > availability > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="availability_anyOf_i1"></a>Property `Distribution > availability > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type                           |
| ------------------------- | -------------------------------------------- |
| **Additional properties** | Any type allowed                             |
| **Same definition as**    | [Concept](#representationTechnique_anyOf_i1) |

## <a name="accessRestriction"></a>Property `Distribution > accessRestriction`

**Title:** access restriction

List of access restrictions related to the distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be               | Description                                         |
| --------------------------------------------- | --------------------------------------------------- |
| [AccessRestriction](#accessRestriction_items) | A restriction on the permitted access to a resource |

### <a name="accessRestriction_items"></a>Distribution > accessRestriction > AccessRestriction

**Title:** AccessRestriction

A restriction on the permitted access to a resource

| **Type**                  | `object`                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [AccessRestriction](#accessService_items_servesDataset_items_sample_items_accessRestriction_items) |

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

### <a name="cuiRestriction_anyOf_i0"></a>Property `Distribution > cuiRestriction > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="cuiRestriction_anyOf_i1"></a>Property `Distribution > cuiRestriction > anyOf > CUIRestriction`

**Title:** CUIRestriction

inline description of CUIRestriction

| **Type**                  | `object`                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [CUIRestriction](#accessService_items_servesDataset_items_sample_items_cuiRestriction_anyOf_i1) |

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

### <a name="describedBy_anyOf_i0"></a>Property `Distribution > describedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="describedBy_anyOf_i1"></a>Property `Distribution > describedBy > anyOf > Distribution`

**Title:** Distribution

inline description of the data dictionary

| **Type**                  | `object`                                                              |
| ------------------------- | --------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                      |
| **Same definition as**    | [Distribution](#accessService_items_servesDataset_items_sample_items) |

## <a name="useRestriction"></a>Property `Distribution > useRestriction`

**Title:** use restriction

Use restriction related to the distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be         | Description                            |
| --------------------------------------- | -------------------------------------- |
| [UseRestriction](#useRestriction_items) | A restriction on usage of another item |

### <a name="useRestriction_items"></a>Distribution > useRestriction > UseRestriction

**Title:** UseRestriction

A restriction on usage of another item

| **Type**                  | `object`                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                             |
| **Same definition as**    | [UseRestriction](#accessService_items_servesDataset_items_sample_items_useRestriction_items) |

## <a name="accessRights"></a>Property `Distribution > accessRights`

**Title:** access rights

Information that indicates whether the Distribution is open data, has access restrictions or is not public

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_anyOf_i0) |
| [item 1](#accessRights_anyOf_i1)                         |

### <a name="accessRights_anyOf_i0"></a>Property `Distribution > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `Distribution > accessRights > anyOf > item 1`

Text description of the access rights

| **Type** | `string` |
| -------- | -------- |

## <a name="conformsTo"></a>Property `Distribution > conformsTo`

**Title:** linked schemas

List of established schemas or reference systems to which the described Distribution conforms

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| [Standard](#conformsTo_items)   | Information about a particular standard that another item conforms to |

### <a name="conformsTo_items"></a>Distribution > conformsTo > Standard

**Title:** Standard

Information about a particular standard that another item conforms to

| **Type**                  | `object`                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                   |
| **Same definition as**    | [Standard](#accessService_items_servesDataset_items_sample_items_conformsTo_items) |

## <a name="description"></a>Property `Distribution > description`

**Title:** description

A free-text account of the Distribution

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="format"></a>Property `Distribution > format`

**Title:** format

A human-readable description of the file format of the Distribution that provides useful information that might not be apparent from mediaType

| **Type** | `null or string` |
| -------- | ---------------- |

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

### <a name="identifier_anyOf_i0"></a>Property `Distribution > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Distribution > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                                           |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                             |
| **Same definition as**    | [Identifier](#accessService_items_servesDataset_items_otherIdentifier_items) |

## <a name="otherIdentifier"></a>Property `Distribution > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Distribution besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>Distribution > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type                                                           |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                             |
| **Same definition as**    | [Identifier](#accessService_items_servesDataset_items_otherIdentifier_items) |

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

The license under which the Distribution is made available; see https://resources.data.gov/schemas/dcat-us/open-licenses for more information regarding license-free declarations and licenses

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#license_anyOf_i0) |
| [item 1](#license_anyOf_i1)                         |

### <a name="license_anyOf_i0"></a>Property `Distribution > license > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="license_anyOf_i1"></a>Property `Distribution > license > anyOf > item 1`

Full text of the license

| **Type** | `string` |
| -------- | -------- |

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

A list of statements concerning all rights for the Distribution that may not be addressed by license or accessRights, such as copyright statements, statements about the intellectual property rights (IPR), or information regarding access or restrictions based on privacy, security, or other policies

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description                        |
| ------------------------------- | ---------------------------------- |
| [rights items](#rights_items)   | Full text of a statement of rights |

### <a name="rights_items"></a>Distribution > rights > rights items

Full text of a statement of rights

| **Type** | `string` |
| -------- | -------- |

## <a name="title"></a>Property `Distribution > title`

**Title:** title

A name given to the Distribution

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="hasQualityMeasurement"></a>Property `Distribution > hasQualityMeasurement`

**Title:** quality measurement

A list of quality measurements for the distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                        |
| -------------------------------------------------- | ---------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_items) | A single measurement of one metric |

### <a name="hasQualityMeasurement_items"></a>Distribution > hasQualityMeasurement > QualityMeasurement

**Title:** QualityMeasurement

A single measurement of one metric

| **Type**                  | `object`                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [QualityMeasurement](#accessService_items_servesDataset_items_sample_items_hasQualityMeasurement_items) |

## <a name="page"></a>Property `Distribution > page`

**Title:** documentation

A page or document about this Distribution

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                       |
| ------------------------------- | --------------------------------- |
| [Document](#page_items)         | Information about a text document |

### <a name="page_items"></a>Distribution > page > Document

**Title:** Document

Information about a text document

| **Type**                  | `object`                                                                     |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                             |
| **Same definition as**    | [Document](#accessService_items_servesDataset_items_sample_items_page_items) |

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

### <a name="checksum_anyOf_i0"></a>Property `Distribution > checksum > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="checksum_anyOf_i1"></a>Property `Distribution > checksum > anyOf > Checksum`

**Title:** Checksum

inline description of Checksum

| **Type**                  | `object`                                                                            |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                    |
| **Same definition as**    | [Checksum](#accessService_items_servesDataset_items_sample_items_checksum_anyOf_i1) |

