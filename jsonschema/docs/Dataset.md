

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                                   | Type                    | Title/Description                                                                   |
| ---------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                             | string                  | -                                                                                   |
| - [@type](#@type )                                         | string                  | -                                                                                   |
| - [otherIdentifier](#otherIdentifier )                     | null or array           | other identifier                                                                    |
| - [sample](#sample )                                       | More than one type      | sample                                                                              |
| - [status](#status )                                       | More than one type      | lifecycle status                                                                    |
| - [supportedSchema](#supportedSchema )                     | More than one type      | supported schema                                                                    |
| - [versionNotes](#versionNotes )                           | null or string          | version notes                                                                       |
| + [contactPoint](#contactPoint )                           | More than one type      | contact point                                                                       |
| - [distribution](#distribution )                           | More than one type      | dataset distribution                                                                |
| - [first](#first )                                         | More than one type      | first                                                                               |
| - [hasCurrentVersion](#hasCurrentVersion )                 | More than one type      | current version                                                                     |
| - [hasVersion](#hasVersion )                               | More than one type      | has version                                                                         |
| - [inSeries](#inSeries )                                   | More than one type      | in series                                                                           |
| - [keyword](#keyword )                                     | null or array of string | keyword/tag                                                                         |
| - [keywordMap](#keywordMap )                               | null or object          | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [landingPage](#landingPage )                             | More than one type      | landing page                                                                        |
| - [previousVersion](#previousVersion )                     | More than one type      | previous version                                                                    |
| - [qualifiedRelation](#qualifiedRelation )                 | More than one type      | qualified relation                                                                  |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string          | Spatial resolution (meters)                                                         |
| - [temporalResolution](#temporalResolution )               | null or string          | temporal resolution                                                                 |
| - [theme](#theme )                                         | More than one type      | theme/category                                                                      |
| - [version](#version )                                     | null or string          | version                                                                             |
| - [describedBy](#describedBy )                             | More than one type      | data dictionary                                                                     |
| - [geographicBoundingBox](#geographicBoundingBox )         | More than one type      | geographic bounding box                                                             |
| - [liabilityStatement](#liabilityStatement )               | More than one type      | liability statement                                                                 |
| - [metadataDistribution](#metadataDistribution )           | More than one type      | metadata distribution                                                               |
| - [purpose](#purpose )                                     | null or string          | purpose                                                                             |
| - [purposeMap](#purposeMap )                               | null or object          | Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [accessRights](#accessRights )                           | More than one type      | access rights                                                                       |
| - [accrualPeriodicity](#accrualPeriodicity )               | More than one type      | frequency                                                                           |
| - [conformsTo](#conformsTo )                               | More than one type      | conforms to                                                                         |
| - [contributor](#contributor )                             | More than one type      | contributor                                                                         |
| - [created](#created )                                     | More than one type      | creation date                                                                       |
| - [creator](#creator )                                     | More than one type      | creator                                                                             |
| + [description](#description )                             | string                  | description                                                                         |
| - [descriptionMap](#descriptionMap )                       | null or object          | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#hasPart )                                     | More than one type      | has part                                                                            |
| - [identifier](#identifier )                               | More than one type      | identifier                                                                          |
| - [isReferencedBy](#isReferencedBy )                       | More than one type      | is referenced by                                                                    |
| - [issued](#issued )                                       | More than one type      | release date                                                                        |
| - [language](#language )                                   | More than one type      | language                                                                            |
| - [modified](#modified )                                   | More than one type      | last modified                                                                       |
| - [provenance](#provenance )                               | More than one type      | provenance                                                                          |
| + [publisher](#publisher )                                 | More than one type      | publisher                                                                           |
| - [relation](#relation )                                   | More than one type      | related resource                                                                    |
| - [replaces](#replaces )                                   | More than one type      | replaces                                                                            |
| - [rights](#rights )                                       | More than one type      | rights                                                                              |
| - [rightsHolder](#rightsHolder )                           | More than one type      | rights holder                                                                       |
| - [source](#source )                                       | More than one type      | data source                                                                         |
| - [spatial](#spatial )                                     | More than one type      | spatial/geographic coverage                                                         |
| - [subject](#subject )                                     | More than one type      | subject                                                                             |
| - [temporal](#temporal )                                   | More than one type      | temporal coverage                                                                   |
| + [title](#title )                                         | string                  | title                                                                               |
| - [titleMap](#titleMap )                                   | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                                   | More than one type      | category                                                                            |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | More than one type      | quality measurement                                                                 |
| - [page](#page )                                           | More than one type      | documentation                                                                       |
| - [qualifiedAttribution](#qualifiedAttribution )           | More than one type      | qualified attribution                                                               |
| - [wasAttributedTo](#wasAttributedTo )                     | More than one type      | attribution                                                                         |
| - [wasGeneratedBy](#wasGeneratedBy )                       | More than one type      | was generated by                                                                    |
| - [wasUsedBy](#wasUsedBy )                                 | More than one type      | used by                                                                             |
| - [image](#image )                                         | More than one type      | image                                                                               |
| - [scopeNote](#scopeNote )                                 | null or string          | usage note                                                                          |
| - [scopeNoteMap](#scopeNoteMap )                           | null or object          | Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `Dataset > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Dataset > @type`

| **Type**    | `string`    |
| ----------- | ----------- |
| **Default** | `"Dataset"` |

## <a name="otherIdentifier"></a>Property `Dataset > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Dataset besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [otherIdentifier items](#otherIdentifier_items) | -           |

### <a name="otherIdentifier_items"></a>Dataset > otherIdentifier > otherIdentifier items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                |
| --------------------------------------------- |
| [Identifier](#otherIdentifier_items_anyOf_i0) |
| [Link](#otherIdentifier_items_anyOf_i1)       |

#### <a name="otherIdentifier_items_anyOf_i0"></a>Property `Dataset > otherIdentifier > otherIdentifier items > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type            |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Defined in**            | [Identifier](./Identifier.md) |

#### <a name="otherIdentifier_items_anyOf_i1"></a>Property `Dataset > otherIdentifier > otherIdentifier items > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="sample"></a>Property `Dataset > sample`

**Title:** sample

List of links to samples of a Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#sample_anyOf_i0) |
| [List of samples](#sample_anyOf_i1)                |

### <a name="sample_anyOf_i0"></a>Property `Dataset > sample > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="sample_anyOf_i1"></a>Property `Dataset > sample > anyOf > List of samples`

**Title:** List of samples

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [Distribution object or link](#sample_anyOf_i1_items) | -           |

#### <a name="sample_anyOf_i1_items"></a>Dataset > sample > anyOf > List of samples > Distribution object or link

**Title:** Distribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Distribution](#sample_anyOf_i1_items_oneOf_i0) |
| [Link](#sample_anyOf_i1_items_oneOf_i1)         |

##### <a name="sample_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > sample > anyOf > List of samples > Distribution object or link > oneOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Distribution](./Distribution.md) |

##### <a name="sample_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > sample > anyOf > List of samples > Distribution object or link > oneOf > Link`

**Title:** Link

reference iri of Distribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="status"></a>Property `Dataset > status`

**Title:** lifecycle status

The status of the dataset  in the context of maturity lifecycle

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#status_oneOf_i0) |
| [Concept](#status_oneOf_i1)                        |
| [Link](#status_oneOf_i2)                           |

### <a name="status_oneOf_i0"></a>Property `Dataset > status > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_oneOf_i1"></a>Property `Dataset > status > oneOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                                    |
| ------------------------- | --------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

### <a name="status_oneOf_i2"></a>Property `Dataset > status > oneOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="supportedSchema"></a>Property `Dataset > supportedSchema`

**Title:** supported schema

supported schema for this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [Null allowed when not required](#supportedSchema_oneOf_i0) |
| [Dataset](#supportedSchema_oneOf_i1)                        |
| [Link](#supportedSchema_oneOf_i2)                           |

### <a name="supportedSchema_oneOf_i0"></a>Property `Dataset > supportedSchema > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="supportedSchema_oneOf_i1"></a>Property `Dataset > supportedSchema > oneOf > Dataset`

**Title:** Dataset

inline description of the supported schema

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="supportedSchema_oneOf_i2"></a>Property `Dataset > supportedSchema > oneOf > Link`

**Title:** Link

reference iri of the supported schema

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="versionNotes"></a>Property `Dataset > versionNotes`

**Title:** version notes

version notes for this dataset

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="contactPoint"></a>Property `Dataset > contactPoint`

**Title:** contact point

A single contact point or list of contact information that can be used for sending comments about the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| Any of(Option)                             |
| ------------------------------------------ |
| [Kind](#contactPoint_anyOf_i0)             |
| [Link](#contactPoint_anyOf_i1)             |
| [List of contacts](#contactPoint_anyOf_i2) |

### <a name="contactPoint_anyOf_i0"></a>Property `Dataset > contactPoint > anyOf > Kind`

**Title:** Kind

inline description of Kind

| **Type**                  | `object`                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                          |
| **Same definition as**    | [Kind](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0) |

### <a name="contactPoint_anyOf_i1"></a>Property `Dataset > contactPoint > anyOf > Link`

**Title:** Link

reference iri of Kind

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="contactPoint_anyOf_i2"></a>Property `Dataset > contactPoint > anyOf > List of contacts`

**Title:** List of contacts

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [Kind object or link](#contactPoint_anyOf_i2_items) | -           |

#### <a name="contactPoint_anyOf_i2_items"></a>Dataset > contactPoint > anyOf > List of contacts > Kind object or link

**Title:** Kind object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                |
| --------------------------------------------- |
| [Kind](#contactPoint_anyOf_i2_items_anyOf_i0) |
| [Link](#contactPoint_anyOf_i2_items_anyOf_i1) |

##### <a name="contactPoint_anyOf_i2_items_anyOf_i0"></a>Property `Dataset > contactPoint > anyOf > List of contacts > Kind object or link > anyOf > Kind`

**Title:** Kind

inline description of Kind

| **Type**                  | `object`                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                          |
| **Same definition as**    | [Kind](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0) |

##### <a name="contactPoint_anyOf_i2_items_anyOf_i1"></a>Property `Dataset > contactPoint > anyOf > List of contacts > Kind object or link > anyOf > Link`

**Title:** Link

reference iri of Kind

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="distribution"></a>Property `Dataset > distribution`

**Title:** dataset distribution

List of available distributions for the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#distribution_anyOf_i0) |
| [List of distributions](#distribution_anyOf_i1)          |

### <a name="distribution_anyOf_i0"></a>Property `Dataset > distribution > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="distribution_anyOf_i1"></a>Property `Dataset > distribution > anyOf > List of distributions`

**Title:** List of distributions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [Distribution object or link](#distribution_anyOf_i1_items) | -           |

#### <a name="distribution_anyOf_i1_items"></a>Dataset > distribution > anyOf > List of distributions > Distribution object or link

**Title:** Distribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Distribution](#distribution_anyOf_i1_items_oneOf_i0) |
| [Link](#distribution_anyOf_i1_items_oneOf_i1)         |

##### <a name="distribution_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > distribution > anyOf > List of distributions > Distribution object or link > oneOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                                        |
| ------------------------- | ----------------------------------------------- |
| **Additional properties** | Any type allowed                                |
| **Same definition as**    | [Distribution](#sample_anyOf_i1_items_oneOf_i0) |

##### <a name="distribution_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > distribution > anyOf > List of distributions > Distribution object or link > oneOf > Link`

**Title:** Link

reference iri of Distribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="first"></a>Property `Dataset > first`

**Title:** first

the first item of the sequence the dataset belongs to

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#first_oneOf_i0) |
| [Dataset](#first_oneOf_i1)                        |
| [Link](#first_oneOf_i2)                           |

### <a name="first_oneOf_i0"></a>Property `Dataset > first > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="first_oneOf_i1"></a>Property `Dataset > first > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="first_oneOf_i2"></a>Property `Dataset > first > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="hasCurrentVersion"></a>Property `Dataset > hasCurrentVersion`

**Title:** current version

reference to the current (latest) version of a dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [Null allowed when not required](#hasCurrentVersion_oneOf_i0) |
| [Dataset](#hasCurrentVersion_oneOf_i1)                        |
| [Link](#hasCurrentVersion_oneOf_i2)                           |

### <a name="hasCurrentVersion_oneOf_i0"></a>Property `Dataset > hasCurrentVersion > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasCurrentVersion_oneOf_i1"></a>Property `Dataset > hasCurrentVersion > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="hasCurrentVersion_oneOf_i2"></a>Property `Dataset > hasCurrentVersion > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="hasVersion"></a>Property `Dataset > hasVersion`

**Title:** has version

List of related Datasets that are a version, edition, or adaptation of the described Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [Null allowed when not required](#hasVersion_anyOf_i0)         |
| [List of other versions of this dataset](#hasVersion_anyOf_i1) |

### <a name="hasVersion_anyOf_i0"></a>Property `Dataset > hasVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasVersion_anyOf_i1"></a>Property `Dataset > hasVersion > anyOf > List of other versions of this dataset`

**Title:** List of other versions of this dataset

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [Dataset object or link](#hasVersion_anyOf_i1_items) | -           |

#### <a name="hasVersion_anyOf_i1_items"></a>Dataset > hasVersion > anyOf > List of other versions of this dataset > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                 |
| ---------------------------------------------- |
| [Dataset](#hasVersion_anyOf_i1_items_oneOf_i0) |
| [Link](#hasVersion_anyOf_i1_items_oneOf_i1)    |

##### <a name="hasVersion_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > hasVersion > anyOf > List of other versions of this dataset > Dataset object or link > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="hasVersion_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > hasVersion > anyOf > List of other versions of this dataset > Dataset object or link > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="inSeries"></a>Property `Dataset > inSeries`

**Title:** in series

List of Dataset Series this dataset belongs to

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#inSeries_anyOf_i0) |
| [List of series](#inSeries_anyOf_i1)                 |

### <a name="inSeries_anyOf_i0"></a>Property `Dataset > inSeries > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="inSeries_anyOf_i1"></a>Property `Dataset > inSeries > anyOf > List of series`

**Title:** List of series

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [DatasetSeries object or link](#inSeries_anyOf_i1_items) | -           |

#### <a name="inSeries_anyOf_i1_items"></a>Dataset > inSeries > anyOf > List of series > DatasetSeries object or link

**Title:** DatasetSeries object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                     |
| -------------------------------------------------- |
| [DatasetSeries](#inSeries_anyOf_i1_items_oneOf_i0) |
| [Link](#inSeries_anyOf_i1_items_oneOf_i1)          |

##### <a name="inSeries_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > inSeries > anyOf > List of series > DatasetSeries object or link > oneOf > DatasetSeries`

**Title:** DatasetSeries

inline description of DatasetSeries

| **Type**                  | `object`                                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                              |
| **Same definition as**    | [DatasetSeries](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0) |

##### <a name="inSeries_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > inSeries > anyOf > List of series > DatasetSeries object or link > oneOf > Link`

**Title:** Link

reference iri of DatasetSeries

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="keyword"></a>Property `Dataset > keyword`

**Title:** keyword/tag

List of keywords or tags describing the Dataset

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be    | Description |
| ---------------------------------- | ----------- |
| [Non-empty string](#keyword_items) | -           |

### <a name="keyword_items"></a>Dataset > keyword > Non-empty string

**Title:** Non-empty string

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="keywordMap"></a>Property `Dataset > keywordMap`

Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="landingPage"></a>Property `Dataset > landingPage`

**Title:** landing page

A web page that provides access to the Dataset, its Distributions and/or additional information

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#landingPage_oneOf_i0) |
| [Document](#landingPage_oneOf_i1)                       |
| [Link](#landingPage_oneOf_i2)                           |

### <a name="landingPage_oneOf_i0"></a>Property `Dataset > landingPage > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="landingPage_oneOf_i1"></a>Property `Dataset > landingPage > oneOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                                                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                             |
| **Same definition as**    | [Document](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_landingPage_oneOf_i1) |

### <a name="landingPage_oneOf_i2"></a>Property `Dataset > landingPage > oneOf > Link`

**Title:** Link

reference iri of Document

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="previousVersion"></a>Property `Dataset > previousVersion`

**Title:** previous version

reference to the previous dataset version

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [Null allowed when not required](#previousVersion_oneOf_i0) |
| [Dataset](#previousVersion_oneOf_i1)                        |
| [Link](#previousVersion_oneOf_i2)                           |

### <a name="previousVersion_oneOf_i0"></a>Property `Dataset > previousVersion > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="previousVersion_oneOf_i1"></a>Property `Dataset > previousVersion > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="previousVersion_oneOf_i2"></a>Property `Dataset > previousVersion > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="qualifiedRelation"></a>Property `Dataset > qualifiedRelation`

**Title:** qualified relation

Qualified relationship with role of the dataset with another resource

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [Null allowed when not required](#qualifiedRelation_anyOf_i0) |
| [List of relationships](#qualifiedRelation_anyOf_i1)          |

### <a name="qualifiedRelation_anyOf_i0"></a>Property `Dataset > qualifiedRelation > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="qualifiedRelation_anyOf_i1"></a>Property `Dataset > qualifiedRelation > anyOf > List of relationships`

**Title:** List of relationships

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                                  | Description |
| ---------------------------------------------------------------- | ----------- |
| [Relationship object or link](#qualifiedRelation_anyOf_i1_items) | -           |

#### <a name="qualifiedRelation_anyOf_i1_items"></a>Dataset > qualifiedRelation > anyOf > List of relationships > Relationship object or link

**Title:** Relationship object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Relationship](#qualifiedRelation_anyOf_i1_items_oneOf_i0) |
| [Link](#qualifiedRelation_anyOf_i1_items_oneOf_i1)         |

##### <a name="qualifiedRelation_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > qualifiedRelation > anyOf > List of relationships > Relationship object or link > oneOf > Relationship`

**Title:** Relationship

inline description of Relationship

| **Type**                  | `object`                                                                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                      |
| **Same definition as**    | [Relationship](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedRelation_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > qualifiedRelation > anyOf > List of relationships > Relationship object or link > oneOf > Link`

**Title:** Link

reference iri of Relationship

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="spatialResolutionInMeters"></a>Property `Dataset > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

Spatial resolution in meters

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="temporalResolution"></a>Property `Dataset > temporalResolution`

**Title:** temporal resolution

Temporal resolution using xsd:duration syntax

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="theme"></a>Property `Dataset > theme`

**Title:** theme/category

List of themes of the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#theme_anyOf_i0) |
| [List of themes](#theme_anyOf_i1)                 |

### <a name="theme_anyOf_i0"></a>Property `Dataset > theme > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="theme_anyOf_i1"></a>Property `Dataset > theme > anyOf > List of themes`

**Title:** List of themes

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [Theme or link](#theme_anyOf_i1_items) | -           |

#### <a name="theme_anyOf_i1_items"></a>Dataset > theme > anyOf > List of themes > Theme or link

**Title:** Theme or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                            |
| ----------------------------------------- |
| [Concept](#theme_anyOf_i1_items_oneOf_i0) |
| [Link](#theme_anyOf_i1_items_oneOf_i1)    |

##### <a name="theme_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > theme > anyOf > List of themes > Theme or link > oneOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                                    |
| ------------------------- | --------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="theme_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > theme > anyOf > List of themes > Theme or link > oneOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="version"></a>Property `Dataset > version`

**Title:** version

The version indicator (name or identifier) of a resource

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="describedBy"></a>Property `Dataset > describedBy`

**Title:** data dictionary

A distribution describing the Data Dictionary for this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#describedBy_oneOf_i0) |
| [Distribution](#describedBy_oneOf_i1)                   |
| [Link](#describedBy_oneOf_i2)                           |

### <a name="describedBy_oneOf_i0"></a>Property `Dataset > describedBy > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="describedBy_oneOf_i1"></a>Property `Dataset > describedBy > oneOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                                        |
| ------------------------- | ----------------------------------------------- |
| **Additional properties** | Any type allowed                                |
| **Same definition as**    | [Distribution](#sample_anyOf_i1_items_oneOf_i0) |

### <a name="describedBy_oneOf_i2"></a>Property `Dataset > describedBy > oneOf > Link`

**Title:** Link

reference iri of Distribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="geographicBoundingBox"></a>Property `Dataset > geographicBoundingBox`

**Title:** geographic bounding box

List of WGS84 Geographic Bounding Boxes for this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [Null allowed when not required](#geographicBoundingBox_anyOf_i0) |
| [List of bounding boxes](#geographicBoundingBox_anyOf_i1)         |

### <a name="geographicBoundingBox_anyOf_i0"></a>Property `Dataset > geographicBoundingBox > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="geographicBoundingBox_anyOf_i1"></a>Property `Dataset > geographicBoundingBox > anyOf > List of bounding boxes`

**Title:** List of bounding boxes

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                                      | Description |
| -------------------------------------------------------------------- | ----------- |
| [Bounding box object or link](#geographicBoundingBox_anyOf_i1_items) | -           |

#### <a name="geographicBoundingBox_anyOf_i1_items"></a>Dataset > geographicBoundingBox > anyOf > List of bounding boxes > Bounding box object or link

**Title:** Bounding box object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [GeographicBoundingBox](#geographicBoundingBox_anyOf_i1_items_oneOf_i0) |
| [Link](#geographicBoundingBox_anyOf_i1_items_oneOf_i1)                  |

##### <a name="geographicBoundingBox_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > geographicBoundingBox > anyOf > List of bounding boxes > Bounding box object or link > oneOf > GeographicBoundingBox`

**Title:** GeographicBoundingBox

inline description of GeographicBoundingBox

| **Type**                  | `object`                                                                                                                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                                   |
| **Same definition as**    | [GeographicBoundingBox](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |

##### <a name="geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > geographicBoundingBox > anyOf > List of bounding boxes > Bounding box object or link > oneOf > Link`

**Title:** Link

reference iri of GeographicBoundingBox

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="liabilityStatement"></a>Property `Dataset > liabilityStatement`

**Title:** liability statement

A liability statement about the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                                 |
| -------------------------------------------------------------- |
| [Null allowed when not required](#liabilityStatement_oneOf_i0) |
| [LiabilityStatement](#liabilityStatement_oneOf_i1)             |
| [Link](#liabilityStatement_oneOf_i2)                           |

### <a name="liabilityStatement_oneOf_i0"></a>Property `Dataset > liabilityStatement > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="liabilityStatement_oneOf_i1"></a>Property `Dataset > liabilityStatement > oneOf > LiabilityStatement`

**Title:** LiabilityStatement

inline description of LiabilityStatement

| **Type**                  | `object`                                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                              |
| **Same definition as**    | [LiabilityStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_liabilityStatement_oneOf_i1) |

### <a name="liabilityStatement_oneOf_i2"></a>Property `Dataset > liabilityStatement > oneOf > Link`

**Title:** Link

reference iri of LiabilityStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="metadataDistribution"></a>Property `Dataset > metadataDistribution`

**Title:** metadata distribution

Distribution to "original" metadata document

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Null allowed when not required](#metadataDistribution_anyOf_i0) |
| [List of distributions](#metadataDistribution_anyOf_i1)          |

### <a name="metadataDistribution_anyOf_i0"></a>Property `Dataset > metadataDistribution > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="metadataDistribution_anyOf_i1"></a>Property `Dataset > metadataDistribution > anyOf > List of distributions`

**Title:** List of distributions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [Distribution object or link](#metadataDistribution_anyOf_i1_items) | -           |

#### <a name="metadataDistribution_anyOf_i1_items"></a>Dataset > metadataDistribution > anyOf > List of distributions > Distribution object or link

**Title:** Distribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [Distribution](#metadataDistribution_anyOf_i1_items_oneOf_i0) |
| [Link](#metadataDistribution_anyOf_i1_items_oneOf_i1)         |

##### <a name="metadataDistribution_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > metadataDistribution > anyOf > List of distributions > Distribution object or link > oneOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                                        |
| ------------------------- | ----------------------------------------------- |
| **Additional properties** | Any type allowed                                |
| **Same definition as**    | [Distribution](#sample_anyOf_i1_items_oneOf_i0) |

##### <a name="metadataDistribution_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > metadataDistribution > anyOf > List of distributions > Distribution object or link > oneOf > Link`

**Title:** Link

reference iri of Distribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="purpose"></a>Property `Dataset > purpose`

**Title:** purpose

The purpose of the dataset

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="purposeMap"></a>Property `Dataset > purposeMap`

Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="accessRights"></a>Property `Dataset > accessRights`

**Title:** access rights

Information that indicates whether the Dataset is open data, has access restrictions or is public

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_oneOf_i0) |
| [RightsStatement](#accessRights_oneOf_i1)                |
| [Link](#accessRights_oneOf_i2)                           |

### <a name="accessRights_oneOf_i0"></a>Property `Dataset > accessRights > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_oneOf_i1"></a>Property `Dataset > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

| **Type**                  | `object`                                                                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="accessRights_oneOf_i2"></a>Property `Dataset > accessRights > oneOf > Link`

**Title:** Link

reference iri of RightsStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="accrualPeriodicity"></a>Property `Dataset > accrualPeriodicity`

**Title:** frequency

The frequency at which the Dataset is updated

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [Null allowed when not required](#accrualPeriodicity_anyOf_i0) |
| [item 1](#accrualPeriodicity_anyOf_i1)                         |
| [item 2](#accrualPeriodicity_anyOf_i2)                         |
| [item 3](#accrualPeriodicity_anyOf_i3)                         |

### <a name="accrualPeriodicity_anyOf_i0"></a>Property `Dataset > accrualPeriodicity > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accrualPeriodicity_anyOf_i1"></a>Property `Dataset > accrualPeriodicity > anyOf > item 1`

ISO 19115 Maintenance Frequency code, see https://infopolicy.github.io/dcat-us/#frequency-coding

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

### <a name="accrualPeriodicity_anyOf_i2"></a>Property `Dataset > accrualPeriodicity > anyOf > item 2`

ISO-8601 Maintenance Frequency code for recurring values, see https://infopolicy.github.io/dcat-us/#frequency-coding

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                   |
| --------------------------------- | ----------------------------------------------------------------- |
| **Must match regular expression** | ```^R/P.+$``` [Test](https://regex101.com/?regex=%5ER%2FP.%2B%24) |

### <a name="accrualPeriodicity_anyOf_i3"></a>Property `Dataset > accrualPeriodicity > anyOf > item 3`

Dublin Core Collection Frequency Vocabulary, see https://infopolicy.github.io/dcat-us/#frequency-coding

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

## <a name="conformsTo"></a>Property `Dataset > conformsTo`

**Title:** conforms to

List of standards to which the described Dataset conforms

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#conformsTo_anyOf_i0) |
| [List of standards](#conformsTo_anyOf_i1)              |

### <a name="conformsTo_anyOf_i0"></a>Property `Dataset > conformsTo > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="conformsTo_anyOf_i1"></a>Property `Dataset > conformsTo > anyOf > List of standards`

**Title:** List of standards

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [Standard object or link](#conformsTo_anyOf_i1_items) | -           |

#### <a name="conformsTo_anyOf_i1_items"></a>Dataset > conformsTo > anyOf > List of standards > Standard object or link

**Title:** Standard object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Standard](#conformsTo_anyOf_i1_items_oneOf_i0) |
| [Link](#conformsTo_anyOf_i1_items_oneOf_i1)     |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > conformsTo > anyOf > List of standards > Standard object or link > oneOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                                                                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                       |
| **Same definition as**    | [Standard](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_landingPage_oneOf_i1_conformsTo_items_anyOf_i0) |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > conformsTo > anyOf > List of standards > Standard object or link > oneOf > Link`

**Title:** Link

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="contributor"></a>Property `Dataset > contributor`

**Title:** contributor

List of agents contributing to the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#contributor_anyOf_i0) |
| [List of agents](#contributor_anyOf_i1)                 |

### <a name="contributor_anyOf_i0"></a>Property `Dataset > contributor > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="contributor_anyOf_i1"></a>Property `Dataset > contributor > anyOf > List of agents`

**Title:** List of agents

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [Agent object or link](#contributor_anyOf_i1_items) | -           |

#### <a name="contributor_anyOf_i1_items"></a>Dataset > contributor > anyOf > List of agents > Agent object or link

**Title:** Agent object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                |
| --------------------------------------------- |
| [Agent](#contributor_anyOf_i1_items_oneOf_i0) |
| [Link](#contributor_anyOf_i1_items_oneOf_i1)  |

##### <a name="contributor_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > contributor > anyOf > List of agents > Agent object or link > oneOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                                                         |
| **Same definition as**    | [Agent](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

##### <a name="contributor_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > contributor > anyOf > List of agents > Agent object or link > oneOf > Link`

**Title:** Link

reference iri of Agent

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="created"></a>Property `Dataset > created`

**Title:** creation date

The date on which the Dataset was first created

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#created_anyOf_i0) |
| [item 1](#created_anyOf_i1)                         |

### <a name="created_anyOf_i0"></a>Property `Dataset > created > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>Property `Dataset > created > anyOf > item 1`

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_oneOf_i0) |
| [item 1](#created_anyOf_i1_oneOf_i1) |
| [item 2](#created_anyOf_i1_oneOf_i2) |
| [item 3](#created_anyOf_i1_oneOf_i3) |

#### <a name="created_anyOf_i1_oneOf_i0"></a>Property `Dataset > created > anyOf > item 1 > oneOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="created_anyOf_i1_oneOf_i1"></a>Property `Dataset > created > anyOf > item 1 > oneOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="created_anyOf_i1_oneOf_i2"></a>Property `Dataset > created > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_oneOf_i3"></a>Property `Dataset > created > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="creator"></a>Property `Dataset > creator`

**Title:** creator

An entity responsible for producing the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#creator_oneOf_i0) |
| [Agent](#creator_oneOf_i1)                          |
| [Link](#creator_oneOf_i2)                           |

### <a name="creator_oneOf_i0"></a>Property `Dataset > creator > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="creator_oneOf_i1"></a>Property `Dataset > creator > oneOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                                                         |
| **Same definition as**    | [Agent](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

### <a name="creator_oneOf_i2"></a>Property `Dataset > creator > oneOf > Link`

**Title:** Link

reference iri of Agent

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="description"></a>Property `Dataset > description`

**Title:** description

A free-text account of the Dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="descriptionMap"></a>Property `Dataset > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="hasPart"></a>Property `Dataset > hasPart`

**Title:** has part

List of related datasets that are part of the described dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#hasPart_anyOf_i0) |
| [List of datasets](#hasPart_anyOf_i1)               |

### <a name="hasPart_anyOf_i0"></a>Property `Dataset > hasPart > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasPart_anyOf_i1"></a>Property `Dataset > hasPart > anyOf > List of datasets`

**Title:** List of datasets

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [Dataset object or link](#hasPart_anyOf_i1_items) | -           |

#### <a name="hasPart_anyOf_i1_items"></a>Dataset > hasPart > anyOf > List of datasets > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                              |
| ------------------------------------------- |
| [Dataset](#hasPart_anyOf_i1_items_oneOf_i0) |
| [Link](#hasPart_anyOf_i1_items_oneOf_i1)    |

##### <a name="hasPart_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > hasPart > anyOf > List of datasets > Dataset object or link > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="hasPart_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > hasPart > anyOf > List of datasets > Dataset object or link > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `Dataset > identifier`

**Title:** identifier

The unique identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#identifier_anyOf_i0) |
| [Identifier](#identifier_anyOf_i1)                     |
| [Link](#identifier_anyOf_i2)                           |

### <a name="identifier_anyOf_i0"></a>Property `Dataset > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Dataset > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                            |
| ------------------------- | --------------------------------------------- |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Identifier](#otherIdentifier_items_anyOf_i0) |

### <a name="identifier_anyOf_i2"></a>Property `Dataset > identifier > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="isReferencedBy"></a>Property `Dataset > isReferencedBy`

**Title:** is referenced by

List of links to related resources, such as publications, that reference, cite, or otherwise point to the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [Null allowed when not required](#isReferencedBy_anyOf_i0) |
| [List of related items](#isReferencedBy_anyOf_i1)          |

### <a name="isReferencedBy_anyOf_i0"></a>Property `Dataset > isReferencedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="isReferencedBy_anyOf_i1"></a>Property `Dataset > isReferencedBy > anyOf > List of related items`

**Title:** List of related items

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be        | Description               |
| -------------------------------------- | ------------------------- |
| [Link](#isReferencedBy_anyOf_i1_items) | reference iri of Resource |

#### <a name="isReferencedBy_anyOf_i1_items"></a>Dataset > isReferencedBy > anyOf > List of related items > Link

**Title:** Link

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="issued"></a>Property `Dataset > issued`

**Title:** release date

Date of formal issuance (e.g., publication) of the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1)                         |

### <a name="issued_anyOf_i0"></a>Property `Dataset > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Dataset > issued > anyOf > item 1`

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Dataset > issued > anyOf > item 1 > oneOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Dataset > issued > anyOf > item 1 > oneOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Dataset > issued > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Dataset > issued > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `Dataset > language`

**Title:** language

Language or languages used in the Dataset. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#language_anyOf_i0) |
| [Language code](#language_anyOf_i1)                  |
| [List of languages](#language_anyOf_i2)              |

### <a name="language_anyOf_i0"></a>Property `Dataset > language > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="language_anyOf_i1"></a>Property `Dataset > language > anyOf > Language code`

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `Dataset > language > anyOf > List of languages`

**Title:** List of languages

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Language code](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>Dataset > language > anyOf > List of languages > Language code

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="modified"></a>Property `Dataset > modified`

**Title:** last modified

The most recent date on which the Dataset was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1)                         |

### <a name="modified_anyOf_i0"></a>Property `Dataset > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `Dataset > modified > anyOf > item 1`

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `Dataset > modified > anyOf > item 1 > oneOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `Dataset > modified > anyOf > item 1 > oneOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `Dataset > modified > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `Dataset > modified > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="provenance"></a>Property `Dataset > provenance`

**Title:** provenance

List of statements about the lineage of a Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#provenance_anyOf_i0) |
| [List of provenance information](#provenance_anyOf_i1) |

### <a name="provenance_anyOf_i0"></a>Property `Dataset > provenance > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="provenance_anyOf_i1"></a>Property `Dataset > provenance > anyOf > List of provenance information`

**Title:** List of provenance information

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [ProvenanceStatement or link](#provenance_anyOf_i1_items) | -           |

#### <a name="provenance_anyOf_i1_items"></a>Dataset > provenance > anyOf > List of provenance information > ProvenanceStatement or link

**Title:** ProvenanceStatement or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [ProvenanceStatement](#provenance_anyOf_i1_items_oneOf_i0) |
| [Link](#provenance_anyOf_i1_items_oneOf_i1)                |

##### <a name="provenance_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > provenance > anyOf > List of provenance information > ProvenanceStatement or link > oneOf > ProvenanceStatement`

**Title:** ProvenanceStatement

inline description of ProvenanceStatement

| **Type**                  | `object`                                                                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                      |
| **Same definition as**    | [ProvenanceStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0) |

##### <a name="provenance_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > provenance > anyOf > List of provenance information > ProvenanceStatement or link > oneOf > Link`

**Title:** Link

reference iri of ProvenanceStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="publisher"></a>Property `Dataset > publisher`

**Title:** publisher

An organization responsible for making the Dataset available

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| One of(Option)                      |
| ----------------------------------- |
| [Organization](#publisher_oneOf_i0) |
| [Link](#publisher_oneOf_i1)         |

### <a name="publisher_oneOf_i0"></a>Property `Dataset > publisher > oneOf > Organization`

**Title:** Organization

inline description of Organization

| **Type**                  | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Organization](#otherIdentifier_items_anyOf_i0_anyOf_i1_creator_oneOf_i1) |

### <a name="publisher_oneOf_i1"></a>Property `Dataset > publisher > oneOf > Link`

**Title:** Link

reference iri of Organization

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="relation"></a>Property `Dataset > relation`

**Title:** related resource

List of references to a related resource

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#relation_anyOf_i0) |
| [List of resources](#relation_anyOf_i1)              |

### <a name="relation_anyOf_i0"></a>Property `Dataset > relation > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="relation_anyOf_i1"></a>Property `Dataset > relation > anyOf > List of resources`

**Title:** List of resources

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be  | Description               |
| -------------------------------- | ------------------------- |
| [Link](#relation_anyOf_i1_items) | reference iri of Resource |

#### <a name="relation_anyOf_i1_items"></a>Dataset > relation > anyOf > List of resources > Link

**Title:** Link

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="replaces"></a>Property `Dataset > replaces`

**Title:** replaces

List of Datasets replaced by this Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#replaces_anyOf_i0) |
| [List of replaced datasets](#replaces_anyOf_i1)      |

### <a name="replaces_anyOf_i0"></a>Property `Dataset > replaces > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="replaces_anyOf_i1"></a>Property `Dataset > replaces > anyOf > List of replaced datasets`

**Title:** List of replaced datasets

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                    | Description |
| -------------------------------------------------- | ----------- |
| [Dataset object or link](#replaces_anyOf_i1_items) | -           |

#### <a name="replaces_anyOf_i1_items"></a>Dataset > replaces > anyOf > List of replaced datasets > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                               |
| -------------------------------------------- |
| [Dataset](#replaces_anyOf_i1_items_oneOf_i0) |
| [Link](#replaces_anyOf_i1_items_oneOf_i1)    |

##### <a name="replaces_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > replaces > anyOf > List of replaced datasets > Dataset object or link > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="replaces_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > replaces > anyOf > List of replaced datasets > Dataset object or link > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rights"></a>Property `Dataset > rights`

**Title:** rights

List of statements concerning all rights for the Dataset not addressed with license or accessRights, such as copyright statements

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#rights_oneOf_i0) |
| [RightsStatement](#rights_oneOf_i1)                |
| [Link](#rights_oneOf_i2)                           |

### <a name="rights_oneOf_i0"></a>Property `Dataset > rights > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="rights_oneOf_i1"></a>Property `Dataset > rights > oneOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

| **Type**                  | `object`                                                                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="rights_oneOf_i2"></a>Property `Dataset > rights > oneOf > Link`

**Title:** Link

reference iri of RightsStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `Dataset > rightsHolder`

**Title:** rights holder

List of agents (organizations) holding rights on the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#rightsHolder_anyOf_i0) |
| [List of rights holders](#rightsHolder_anyOf_i1)         |

### <a name="rightsHolder_anyOf_i0"></a>Property `Dataset > rightsHolder > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="rightsHolder_anyOf_i1"></a>Property `Dataset > rightsHolder > anyOf > List of rights holders`

**Title:** List of rights holders

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [Organization or link](#rightsHolder_anyOf_i1_items) | -           |

#### <a name="rightsHolder_anyOf_i1_items"></a>Dataset > rightsHolder > anyOf > List of rights holders > Organization or link

**Title:** Organization or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Organization](#rightsHolder_anyOf_i1_items_oneOf_i0) |
| [Link](#rightsHolder_anyOf_i1_items_oneOf_i1)         |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > rightsHolder > anyOf > List of rights holders > Organization or link > oneOf > Organization`

**Title:** Organization

inline description of Organization

| **Type**                  | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Organization](#otherIdentifier_items_anyOf_i0_anyOf_i1_creator_oneOf_i1) |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > rightsHolder > anyOf > List of rights holders > Organization or link > oneOf > Link`

**Title:** Link

reference iri of Organization

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="source"></a>Property `Dataset > source`

**Title:** data source

List of related Datasets from which the described Dataset is derived

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#source_anyOf_i0) |
| [List of source datasets](#source_anyOf_i1)        |

### <a name="source_anyOf_i0"></a>Property `Dataset > source > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="source_anyOf_i1"></a>Property `Dataset > source > anyOf > List of source datasets`

**Title:** List of source datasets

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                  | Description |
| ------------------------------------------------ | ----------- |
| [Dataset object or link](#source_anyOf_i1_items) | -           |

#### <a name="source_anyOf_i1_items"></a>Dataset > source > anyOf > List of source datasets > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                             |
| ------------------------------------------ |
| [Dataset](#source_anyOf_i1_items_oneOf_i0) |
| [Link](#source_anyOf_i1_items_oneOf_i1)    |

##### <a name="source_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > source > anyOf > List of source datasets > Dataset object or link > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="source_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > source > anyOf > List of source datasets > Dataset object or link > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `Dataset > spatial`

**Title:** spatial/geographic coverage

A geographic region or regions that are covered by the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#spatial_oneOf_i0) |
| [Location](#spatial_oneOf_i1)                       |
| [Link](#spatial_oneOf_i2)                           |
| [List og geographic regions](#spatial_oneOf_i3)     |

### <a name="spatial_oneOf_i0"></a>Property `Dataset > spatial > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="spatial_oneOf_i1"></a>Property `Dataset > spatial > oneOf > Location`

**Title:** Location

inline description of Location

| **Type**                  | `object`                                                                                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                                         |
| **Same definition as**    | [Location](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

### <a name="spatial_oneOf_i2"></a>Property `Dataset > spatial > oneOf > Link`

**Title:** Link

reference iri of Location

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="spatial_oneOf_i3"></a>Property `Dataset > spatial > oneOf > List og geographic regions`

**Title:** List og geographic regions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [Location or link](#spatial_oneOf_i3_items) | -           |

#### <a name="spatial_oneOf_i3_items"></a>Dataset > spatial > oneOf > List og geographic regions > Location or link

**Title:** Location or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_oneOf_i3_items_oneOf_i0) |
| [Link](#spatial_oneOf_i3_items_oneOf_i1)     |

##### <a name="spatial_oneOf_i3_items_oneOf_i0"></a>Property `Dataset > spatial > oneOf > List og geographic regions > Location or link > oneOf > Location`

**Title:** Location

inline description of Location

| **Type**                  | `object`                                                                                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                                         |
| **Same definition as**    | [Location](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_oneOf_i3_items_oneOf_i1"></a>Property `Dataset > spatial > oneOf > List og geographic regions > Location or link > oneOf > Link`

**Title:** Link

reference iri of Location

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="subject"></a>Property `Dataset > subject`

**Title:** subject

List of primary subjects of the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#subject_anyOf_i0) |
| [List of subjects](#subject_anyOf_i1)               |

### <a name="subject_anyOf_i0"></a>Property `Dataset > subject > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="subject_anyOf_i1"></a>Property `Dataset > subject > anyOf > List of subjects`

**Title:** List of subjects

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [Subject or link](#subject_anyOf_i1_items) | -           |

#### <a name="subject_anyOf_i1_items"></a>Dataset > subject > anyOf > List of subjects > Subject or link

**Title:** Subject or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                              |
| ------------------------------------------- |
| [Concept](#subject_anyOf_i1_items_oneOf_i0) |
| [Link](#subject_anyOf_i1_items_oneOf_i1)    |

##### <a name="subject_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > subject > anyOf > List of subjects > Subject or link > oneOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                                    |
| ------------------------- | --------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="subject_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > subject > anyOf > List of subjects > Subject or link > oneOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `Dataset > temporal`

**Title:** temporal coverage

List of temporal periods that the dataset covers

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#temporal_anyOf_i0) |
| [List of covered time periods](#temporal_anyOf_i1)   |

### <a name="temporal_anyOf_i0"></a>Property `Dataset > temporal > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="temporal_anyOf_i1"></a>Property `Dataset > temporal > anyOf > List of covered time periods`

**Title:** List of covered time periods

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [PeriodOfTime object or link](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>Dataset > temporal > anyOf > List of covered time periods > PeriodOfTime object or link

**Title:** PeriodOfTime object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [Link](#temporal_anyOf_i1_items_oneOf_i1)         |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > temporal > anyOf > List of covered time periods > PeriodOfTime object or link > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

inline description of PeriodOfTime

| **Type**                  | `object`                                                                                                                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > temporal > anyOf > List of covered time periods > PeriodOfTime object or link > oneOf > Link`

**Title:** Link

reference iri of PeriodOfTime

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="title"></a>Property `Dataset > title`

**Title:** title

A name given to the Dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `Dataset > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="category"></a>Property `Dataset > category`

**Title:** category

List of categories of the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#category_anyOf_i0) |
| [List of categories](#category_anyOf_i1)             |

### <a name="category_anyOf_i0"></a>Property `Dataset > category > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="category_anyOf_i1"></a>Property `Dataset > category > anyOf > List of categories`

**Title:** List of categories

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [Category or link](#category_anyOf_i1_items) | -           |

#### <a name="category_anyOf_i1_items"></a>Dataset > category > anyOf > List of categories > Category or link

**Title:** Category or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                               |
| -------------------------------------------- |
| [Concept](#category_anyOf_i1_items_oneOf_i0) |
| [item 1](#category_anyOf_i1_items_oneOf_i1)  |

##### <a name="category_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > category > anyOf > List of categories > Category or link > oneOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                                    |
| ------------------------- | --------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="category_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > category > anyOf > List of categories > Category or link > oneOf > item 1`

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="hasQualityMeasurement"></a>Property `Dataset > hasQualityMeasurement`

**Title:** quality measurement

List of quality measurements for the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [Null allowed when not required](#hasQualityMeasurement_anyOf_i0) |
| [List of quality measurements](#hasQualityMeasurement_anyOf_i1)   |

### <a name="hasQualityMeasurement_anyOf_i0"></a>Property `Dataset > hasQualityMeasurement > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasQualityMeasurement_anyOf_i1"></a>Property `Dataset > hasQualityMeasurement > anyOf > List of quality measurements`

**Title:** List of quality measurements

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [QualityMeasurement or link](#hasQualityMeasurement_anyOf_i1_items) | -           |

#### <a name="hasQualityMeasurement_anyOf_i1_items"></a>Dataset > hasQualityMeasurement > anyOf > List of quality measurements > QualityMeasurement or link

**Title:** QualityMeasurement or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                                       |
| -------------------------------------------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [Link](#hasQualityMeasurement_anyOf_i1_items_oneOf_i1)               |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > hasQualityMeasurement > anyOf > List of quality measurements > QualityMeasurement or link > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

inline description of QualityMeasurement

| **Type**                  | `object`                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                                |
| **Same definition as**    | [QualityMeasurement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > hasQualityMeasurement > anyOf > List of quality measurements > QualityMeasurement or link > oneOf > Link`

**Title:** Link

reference iri of QualityMeasurement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="page"></a>Property `Dataset > page`

**Title:** documentation

List of pages or documents about this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                   |
| ------------------------------------------------ |
| [Null allowed when not required](#page_anyOf_i0) |
| [List of documents](#page_anyOf_i1)              |

### <a name="page_anyOf_i0"></a>Property `Dataset > page > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="page_anyOf_i1"></a>Property `Dataset > page > anyOf > List of documents`

**Title:** List of documents

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [Document object or link](#page_anyOf_i1_items) | -           |

#### <a name="page_anyOf_i1_items"></a>Dataset > page > anyOf > List of documents > Document object or link

**Title:** Document object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                            |
| ----------------------------------------- |
| [Document](#page_anyOf_i1_items_oneOf_i0) |
| [item 1](#page_anyOf_i1_items_oneOf_i1)   |

##### <a name="page_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > page > anyOf > List of documents > Document object or link > oneOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                                                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                             |
| **Same definition as**    | [Document](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_landingPage_oneOf_i1) |

##### <a name="page_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > page > anyOf > List of documents > Document object or link > oneOf > item 1`

reference iri of Document

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `Dataset > qualifiedAttribution`

**Title:** qualified attribution

List of agents having some form of responsibility for the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Null allowed when not required](#qualifiedAttribution_anyOf_i0) |
| [List of agents](#qualifiedAttribution_anyOf_i1)                 |

### <a name="qualifiedAttribution_anyOf_i0"></a>Property `Dataset > qualifiedAttribution > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="qualifiedAttribution_anyOf_i1"></a>Property `Dataset > qualifiedAttribution > anyOf > List of agents`

**Title:** List of agents

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [Attribution object or link](#qualifiedAttribution_anyOf_i1_items) | -           |

#### <a name="qualifiedAttribution_anyOf_i1_items"></a>Dataset > qualifiedAttribution > anyOf > List of agents > Attribution object or link

**Title:** Attribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [Attribution](#qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [Link](#qualifiedAttribution_anyOf_i1_items_oneOf_i1)        |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > qualifiedAttribution > anyOf > List of agents > Attribution object or link > oneOf > Attribution`

**Title:** Attribution

inline description of Attribution

| **Type**                  | `object`                                                                                                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                                        |
| **Same definition as**    | [Attribution](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > qualifiedAttribution > anyOf > List of agents > Attribution object or link > oneOf > Link`

**Title:** Link

reference iri of Attribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="wasAttributedTo"></a>Property `Dataset > wasAttributedTo`

**Title:** attribution

List of agents attributed to this dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [Null allowed when not required](#wasAttributedTo_anyOf_i0) |
| [List of agents](#wasAttributedTo_anyOf_i1)                 |

### <a name="wasAttributedTo_anyOf_i0"></a>Property `Dataset > wasAttributedTo > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="wasAttributedTo_anyOf_i1"></a>Property `Dataset > wasAttributedTo > anyOf > List of agents`

**Title:** List of agents

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [Agent object or link](#wasAttributedTo_anyOf_i1_items) | -           |

#### <a name="wasAttributedTo_anyOf_i1_items"></a>Dataset > wasAttributedTo > anyOf > List of agents > Agent object or link

**Title:** Agent object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                    |
| ------------------------------------------------- |
| [Agent](#wasAttributedTo_anyOf_i1_items_oneOf_i0) |
| [Link](#wasAttributedTo_anyOf_i1_items_oneOf_i1)  |

##### <a name="wasAttributedTo_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > wasAttributedTo > anyOf > List of agents > Agent object or link > oneOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                                                         |
| **Same definition as**    | [Agent](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

##### <a name="wasAttributedTo_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > wasAttributedTo > anyOf > List of agents > Agent object or link > oneOf > Link`

**Title:** Link

reference iri of Agent

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="wasGeneratedBy"></a>Property `Dataset > wasGeneratedBy`

**Title:** was generated by

List of activities that generated, or provide the business context for the creation of the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [Null allowed when not required](#wasGeneratedBy_anyOf_i0) |
| [List of activities](#wasGeneratedBy_anyOf_i1)             |

### <a name="wasGeneratedBy_anyOf_i0"></a>Property `Dataset > wasGeneratedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="wasGeneratedBy_anyOf_i1"></a>Property `Dataset > wasGeneratedBy > anyOf > List of activities`

**Title:** List of activities

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [Activity object or link](#wasGeneratedBy_anyOf_i1_items) | -           |

#### <a name="wasGeneratedBy_anyOf_i1_items"></a>Dataset > wasGeneratedBy > anyOf > List of activities > Activity object or link

**Title:** Activity object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                      |
| --------------------------------------------------- |
| [Activity](#wasGeneratedBy_anyOf_i1_items_oneOf_i0) |
| [Link](#wasGeneratedBy_anyOf_i1_items_oneOf_i1)     |

##### <a name="wasGeneratedBy_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > wasGeneratedBy > anyOf > List of activities > Activity object or link > oneOf > Activity`

**Title:** Activity

inline description of Activity

| **Type**                  | `object`                                                                                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                               |
| **Same definition as**    | [Activity](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i0) |

##### <a name="wasGeneratedBy_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > wasGeneratedBy > anyOf > List of activities > Activity object or link > oneOf > Link`

**Title:** Link

reference iri of Activity

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="wasUsedBy"></a>Property `Dataset > wasUsedBy`

**Title:** used by

List of activities that used the Dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#wasUsedBy_anyOf_i0) |
| [List of activities](#wasUsedBy_anyOf_i1)             |

### <a name="wasUsedBy_anyOf_i0"></a>Property `Dataset > wasUsedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="wasUsedBy_anyOf_i1"></a>Property `Dataset > wasUsedBy > anyOf > List of activities`

**Title:** List of activities

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [Activity object or link](#wasUsedBy_anyOf_i1_items) | -           |

#### <a name="wasUsedBy_anyOf_i1_items"></a>Dataset > wasUsedBy > anyOf > List of activities > Activity object or link

**Title:** Activity object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                 |
| ---------------------------------------------- |
| [Activity](#wasUsedBy_anyOf_i1_items_oneOf_i0) |
| [Link](#wasUsedBy_anyOf_i1_items_oneOf_i1)     |

##### <a name="wasUsedBy_anyOf_i1_items_oneOf_i0"></a>Property `Dataset > wasUsedBy > anyOf > List of activities > Activity object or link > oneOf > Activity`

**Title:** Activity

inline description of Activity

| **Type**                  | `object`                                                                                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                               |
| **Same definition as**    | [Activity](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i0) |

##### <a name="wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `Dataset > wasUsedBy > anyOf > List of activities > Activity object or link > oneOf > Link`

**Title:** Link

reference iri of Activity

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="image"></a>Property `Dataset > image`

**Title:** image

Link to a thumbnail picture illustrating the content of the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#image_anyOf_i0) |
| [Link](#image_anyOf_i1)                           |

### <a name="image_anyOf_i0"></a>Property `Dataset > image > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="image_anyOf_i1"></a>Property `Dataset > image > anyOf > Link`

**Title:** Link

The link to the image

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="scopeNote"></a>Property `Dataset > scopeNote`

**Title:** usage note

usage note for the dataset

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="scopeNoteMap"></a>Property `Dataset > scopeNoteMap`

Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

