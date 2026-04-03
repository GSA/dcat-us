

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
| - [sample](#sample )                                       | null or array           | sample                                                                              |
| - [status](#status )                                       | More than one type      | lifecycle status                                                                    |
| - [supportedSchema](#supportedSchema )                     | More than one type      | supported schema                                                                    |
| - [versionNotes](#versionNotes )                           | null or string          | version notes                                                                       |
| + [contactPoint](#contactPoint )                           | More than one type      | contact point                                                                       |
| - [distribution](#distribution )                           | null or array           | dataset distribution                                                                |
| - [first](#first )                                         | More than one type      | first                                                                               |
| - [hasCurrentVersion](#hasCurrentVersion )                 | More than one type      | current version                                                                     |
| - [hasVersion](#hasVersion )                               | null or array           | has version                                                                         |
| - [inSeries](#inSeries )                                   | null or array           | in series                                                                           |
| - [keyword](#keyword )                                     | null or array of string | keyword/tag                                                                         |
| - [keywordMap](#keywordMap )                               | null or object          | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [landingPage](#landingPage )                             | More than one type      | landing page                                                                        |
| - [previousVersion](#previousVersion )                     | More than one type      | previous version                                                                    |
| - [qualifiedRelation](#qualifiedRelation )                 | null or array           | qualified relation                                                                  |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string          | Spatial resolution (meters)                                                         |
| - [temporalResolution](#temporalResolution )               | null or string          | temporal resolution                                                                 |
| - [theme](#theme )                                         | null or array           | theme/category                                                                      |
| - [version](#version )                                     | null or string          | version                                                                             |
| - [describedBy](#describedBy )                             | More than one type      | data dictionary                                                                     |
| - [liabilityStatement](#liabilityStatement )               | More than one type      | liability statement                                                                 |
| - [metadataDistribution](#metadataDistribution )           | null or array           | metadata distribution                                                               |
| - [purpose](#purpose )                                     | null or string          | purpose                                                                             |
| - [purposeMap](#purposeMap )                               | null or object          | Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [accessRights](#accessRights )                           | More than one type      | access rights                                                                       |
| - [accrualPeriodicity](#accrualPeriodicity )               | More than one type      | frequency                                                                           |
| - [conformsTo](#conformsTo )                               | null or array           | conforms to                                                                         |
| - [contributor](#contributor )                             | null or array           | contributor                                                                         |
| - [created](#created )                                     | More than one type      | creation date                                                                       |
| - [creator](#creator )                                     | More than one type      | creator                                                                             |
| + [description](#description )                             | string                  | description                                                                         |
| - [descriptionMap](#descriptionMap )                       | null or object          | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#hasPart )                                     | null or array           | has part                                                                            |
| - [identifier](#identifier )                               | More than one type      | identifier                                                                          |
| - [isReferencedBy](#isReferencedBy )                       | null or array of string | is referenced by                                                                    |
| - [issued](#issued )                                       | More than one type      | release date                                                                        |
| - [language](#language )                                   | More than one type      | language                                                                            |
| - [modified](#modified )                                   | More than one type      | last modified                                                                       |
| - [provenance](#provenance )                               | null or array           | provenance                                                                          |
| + [publisher](#publisher )                                 | More than one type      | publisher                                                                           |
| - [relation](#relation )                                   | null or array of string | related resource                                                                    |
| - [replaces](#replaces )                                   | null or array           | replaces                                                                            |
| - [rights](#rights )                                       | More than one type      | rights                                                                              |
| - [rightsHolder](#rightsHolder )                           | null or array           | rights holder                                                                       |
| - [source](#source )                                       | null or array           | data source                                                                         |
| - [spatial](#spatial )                                     | More than one type      | spatial/geographic coverage                                                         |
| - [subject](#subject )                                     | null or array           | subject                                                                             |
| - [temporal](#temporal )                                   | null or array           | temporal coverage                                                                   |
| + [title](#title )                                         | string                  | title                                                                               |
| - [titleMap](#titleMap )                                   | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                                   | null or array           | category                                                                            |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | null or array           | quality measurement                                                                 |
| - [page](#page )                                           | null or array           | documentation                                                                       |
| - [qualifiedAttribution](#qualifiedAttribution )           | null or array           | qualified attribution                                                               |
| - [wasAttributedTo](#wasAttributedTo )                     | null or array           | attribution                                                                         |
| - [wasGeneratedBy](#wasGeneratedBy )                       | null or array           | was generated by                                                                    |
| - [wasUsedBy](#wasUsedBy )                                 | null or array           | used by                                                                             |
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

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [Distribution object or link](#sample_items) | -           |

### <a name="sample_items"></a>Dataset > sample > Distribution object or link

**Title:** Distribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [Distribution](#sample_items_anyOf_i0) |
| [Link](#sample_items_anyOf_i1)         |

#### <a name="sample_items_anyOf_i0"></a>Property `Dataset > sample > Distribution object or link > anyOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Distribution](./Distribution.md) |

#### <a name="sample_items_anyOf_i1"></a>Property `Dataset > sample > Distribution object or link > anyOf > Link`

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

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#status_anyOf_i0) |
| [Concept](#status_anyOf_i1)                        |
| [Link](#status_anyOf_i2)                           |

### <a name="status_anyOf_i0"></a>Property `Dataset > status > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_anyOf_i1"></a>Property `Dataset > status > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                           |
| ------------------------- | ------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                   |
| **Same definition as**    | [Concept](#sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

### <a name="status_anyOf_i2"></a>Property `Dataset > status > anyOf > Link`

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

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [Null allowed when not required](#supportedSchema_anyOf_i0) |
| [Dataset](#supportedSchema_anyOf_i1)                        |
| [Link](#supportedSchema_anyOf_i2)                           |

### <a name="supportedSchema_anyOf_i0"></a>Property `Dataset > supportedSchema > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="supportedSchema_anyOf_i1"></a>Property `Dataset > supportedSchema > anyOf > Dataset`

**Title:** Dataset

inline description of the supported schema

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

### <a name="supportedSchema_anyOf_i2"></a>Property `Dataset > supportedSchema > anyOf > Link`

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

| **Type**                  | `object`                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                        |
| **Same definition as**    | [Kind](#sample_items_anyOf_i0_accessService_items_anyOf_i0_contactPoint_items_anyOf_i0) |

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

| **Type**                  | `object`                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                        |
| **Same definition as**    | [Kind](#sample_items_anyOf_i0_accessService_items_anyOf_i0_contactPoint_items_anyOf_i0) |

##### <a name="contactPoint_anyOf_i2_items_anyOf_i1"></a>Property `Dataset > contactPoint > anyOf > List of contacts > Kind object or link > anyOf > Link`

**Title:** Link

reference iri of Kind

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="distribution"></a>Property `Dataset > distribution`

**Title:** dataset distribution

List of available distributions for the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description |
| -------------------------------------------------- | ----------- |
| [Distribution object or link](#distribution_items) | -           |

### <a name="distribution_items"></a>Dataset > distribution > Distribution object or link

**Title:** Distribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [Distribution](#distribution_items_anyOf_i0) |
| [Link](#distribution_items_anyOf_i1)         |

#### <a name="distribution_items_anyOf_i0"></a>Property `Dataset > distribution > Distribution object or link > anyOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                               |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Distribution](#sample_items_anyOf_i0) |

#### <a name="distribution_items_anyOf_i1"></a>Property `Dataset > distribution > Distribution object or link > anyOf > Link`

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

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#first_anyOf_i0) |
| [Dataset](#first_anyOf_i1)                        |
| [Link](#first_anyOf_i2)                           |

### <a name="first_anyOf_i0"></a>Property `Dataset > first > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="first_anyOf_i1"></a>Property `Dataset > first > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

### <a name="first_anyOf_i2"></a>Property `Dataset > first > anyOf > Link`

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

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [Null allowed when not required](#hasCurrentVersion_anyOf_i0) |
| [Dataset](#hasCurrentVersion_anyOf_i1)                        |
| [Link](#hasCurrentVersion_anyOf_i2)                           |

### <a name="hasCurrentVersion_anyOf_i0"></a>Property `Dataset > hasCurrentVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasCurrentVersion_anyOf_i1"></a>Property `Dataset > hasCurrentVersion > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

### <a name="hasCurrentVersion_anyOf_i2"></a>Property `Dataset > hasCurrentVersion > anyOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="hasVersion"></a>Property `Dataset > hasVersion`

**Title:** has version

List of related Datasets that are a version, edition, or adaptation of the described Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [Dataset object or link](#hasVersion_items) | -           |

### <a name="hasVersion_items"></a>Dataset > hasVersion > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                        |
| ------------------------------------- |
| [Dataset](#hasVersion_items_anyOf_i0) |
| [Link](#hasVersion_items_anyOf_i1)    |

#### <a name="hasVersion_items_anyOf_i0"></a>Property `Dataset > hasVersion > Dataset object or link > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

#### <a name="hasVersion_items_anyOf_i1"></a>Property `Dataset > hasVersion > Dataset object or link > anyOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="inSeries"></a>Property `Dataset > inSeries`

**Title:** in series

List of Dataset Series this dataset belongs to

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [DatasetSeries object or link](#inSeries_items) | -           |

### <a name="inSeries_items"></a>Dataset > inSeries > DatasetSeries object or link

**Title:** DatasetSeries object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                            |
| ----------------------------------------- |
| [DatasetSeries](#inSeries_items_anyOf_i0) |
| [Link](#inSeries_items_anyOf_i1)          |

#### <a name="inSeries_items_anyOf_i0"></a>Property `Dataset > inSeries > DatasetSeries object or link > anyOf > DatasetSeries`

**Title:** DatasetSeries

inline description of DatasetSeries

| **Type**                  | `object`                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                          |
| **Same definition as**    | [DatasetSeries](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0) |

#### <a name="inSeries_items_anyOf_i1"></a>Property `Dataset > inSeries > DatasetSeries object or link > anyOf > Link`

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

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#landingPage_anyOf_i0) |
| [Document](#landingPage_anyOf_i1)                       |
| [Link](#landingPage_anyOf_i2)                           |

### <a name="landingPage_anyOf_i0"></a>Property `Dataset > landingPage > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="landingPage_anyOf_i1"></a>Property `Dataset > landingPage > anyOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                  |
| **Same definition as**    | [Document](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_landingPage_anyOf_i1) |

### <a name="landingPage_anyOf_i2"></a>Property `Dataset > landingPage > anyOf > Link`

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

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [Null allowed when not required](#previousVersion_anyOf_i0) |
| [Dataset](#previousVersion_anyOf_i1)                        |
| [Link](#previousVersion_anyOf_i2)                           |

### <a name="previousVersion_anyOf_i0"></a>Property `Dataset > previousVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="previousVersion_anyOf_i1"></a>Property `Dataset > previousVersion > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

### <a name="previousVersion_anyOf_i2"></a>Property `Dataset > previousVersion > anyOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="qualifiedRelation"></a>Property `Dataset > qualifiedRelation`

**Title:** qualified relation

Qualified relationship with role of the dataset with another resource

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [Relationship object or link](#qualifiedRelation_items) | -           |

### <a name="qualifiedRelation_items"></a>Dataset > qualifiedRelation > Relationship object or link

**Title:** Relationship object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Relationship](#qualifiedRelation_items_anyOf_i0) |
| [Link](#qualifiedRelation_items_anyOf_i1)         |

#### <a name="qualifiedRelation_items_anyOf_i0"></a>Property `Dataset > qualifiedRelation > Relationship object or link > anyOf > Relationship`

**Title:** Relationship

inline description of Relationship

| **Type**                  | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                  |
| **Same definition as**    | [Relationship](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_qualifiedRelation_items_anyOf_i0) |

#### <a name="qualifiedRelation_items_anyOf_i1"></a>Property `Dataset > qualifiedRelation > Relationship object or link > anyOf > Link`

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

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [Theme or link](#theme_items)   | -           |

### <a name="theme_items"></a>Dataset > theme > Theme or link

**Title:** Theme or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [Concept](#theme_items_anyOf_i0) |
| [Link](#theme_items_anyOf_i1)    |

#### <a name="theme_items_anyOf_i0"></a>Property `Dataset > theme > Theme or link > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                           |
| ------------------------- | ------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                   |
| **Same definition as**    | [Concept](#sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

#### <a name="theme_items_anyOf_i1"></a>Property `Dataset > theme > Theme or link > anyOf > Link`

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

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#describedBy_anyOf_i0) |
| [Distribution](#describedBy_anyOf_i1)                   |
| [Link](#describedBy_anyOf_i2)                           |

### <a name="describedBy_anyOf_i0"></a>Property `Dataset > describedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="describedBy_anyOf_i1"></a>Property `Dataset > describedBy > anyOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                               |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Distribution](#sample_items_anyOf_i0) |

### <a name="describedBy_anyOf_i2"></a>Property `Dataset > describedBy > anyOf > Link`

**Title:** Link

reference iri of Distribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="liabilityStatement"></a>Property `Dataset > liabilityStatement`

**Title:** liability statement

A liability statement about the dataset

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [Null allowed when not required](#liabilityStatement_anyOf_i0) |
| [LiabilityStatement](#liabilityStatement_anyOf_i1)             |
| [Link](#liabilityStatement_anyOf_i2)                           |

### <a name="liabilityStatement_anyOf_i0"></a>Property `Dataset > liabilityStatement > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="liabilityStatement_anyOf_i1"></a>Property `Dataset > liabilityStatement > anyOf > LiabilityStatement`

**Title:** LiabilityStatement

inline description of LiabilityStatement

| **Type**                  | `object`                                                                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                   |
| **Same definition as**    | [LiabilityStatement](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_liabilityStatement_anyOf_i1) |

### <a name="liabilityStatement_anyOf_i2"></a>Property `Dataset > liabilityStatement > anyOf > Link`

**Title:** Link

reference iri of LiabilityStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="metadataDistribution"></a>Property `Dataset > metadataDistribution`

**Title:** metadata distribution

Distribution to "original" metadata document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                            | Description |
| ---------------------------------------------------------- | ----------- |
| [Distribution object or link](#metadataDistribution_items) | -           |

### <a name="metadataDistribution_items"></a>Dataset > metadataDistribution > Distribution object or link

**Title:** Distribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Distribution](#metadataDistribution_items_anyOf_i0) |
| [Link](#metadataDistribution_items_anyOf_i1)         |

#### <a name="metadataDistribution_items_anyOf_i0"></a>Property `Dataset > metadataDistribution > Distribution object or link > anyOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                               |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Distribution](#sample_items_anyOf_i0) |

#### <a name="metadataDistribution_items_anyOf_i1"></a>Property `Dataset > metadataDistribution > Distribution object or link > anyOf > Link`

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

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_anyOf_i0) |
| [RightsStatement](#accessRights_anyOf_i1)                |
| [Link](#accessRights_anyOf_i2)                           |

### <a name="accessRights_anyOf_i0"></a>Property `Dataset > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `Dataset > accessRights > anyOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

| **Type**                  | `object`                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                          |
| **Same definition as**    | [RightsStatement](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_accessRights_anyOf_i1) |

### <a name="accessRights_anyOf_i2"></a>Property `Dataset > accessRights > anyOf > Link`

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

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [Standard object or link](#conformsTo_items) | -           |

### <a name="conformsTo_items"></a>Dataset > conformsTo > Standard object or link

**Title:** Standard object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [Standard](#conformsTo_items_anyOf_i0) |
| [Link](#conformsTo_items_anyOf_i1)     |

#### <a name="conformsTo_items_anyOf_i0"></a>Property `Dataset > conformsTo > Standard object or link > anyOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_landingPage_anyOf_i1_conformsTo_items_anyOf_i0) |

#### <a name="conformsTo_items_anyOf_i1"></a>Property `Dataset > conformsTo > Standard object or link > anyOf > Link`

**Title:** Link

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="contributor"></a>Property `Dataset > contributor`

**Title:** contributor

List of agents contributing to the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [Agent object or link](#contributor_items) | -           |

### <a name="contributor_items"></a>Dataset > contributor > Agent object or link

**Title:** Agent object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                       |
| ------------------------------------ |
| [Agent](#contributor_items_anyOf_i0) |
| [Link](#contributor_items_anyOf_i1)  |

#### <a name="contributor_items_anyOf_i0"></a>Property `Dataset > contributor > Agent object or link > anyOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                     |
| **Same definition as**    | [Agent](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0_publisher_anyOf_i1) |

#### <a name="contributor_items_anyOf_i1"></a>Property `Dataset > contributor > Agent object or link > anyOf > Link`

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
| [Date string](#created_anyOf_i1)                    |

### <a name="created_anyOf_i0"></a>Property `Dataset > created > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>Property `Dataset > created > anyOf > Date string`

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

#### <a name="created_anyOf_i1_anyOf_i0"></a>Property `Dataset > created > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="created_anyOf_i1_anyOf_i1"></a>Property `Dataset > created > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="created_anyOf_i1_anyOf_i2"></a>Property `Dataset > created > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_anyOf_i3"></a>Property `Dataset > created > anyOf > Date string > anyOf > item 3`

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

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#creator_anyOf_i0) |
| [Agent](#creator_anyOf_i1)                          |
| [Link](#creator_anyOf_i2)                           |

### <a name="creator_anyOf_i0"></a>Property `Dataset > creator > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="creator_anyOf_i1"></a>Property `Dataset > creator > anyOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                     |
| **Same definition as**    | [Agent](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0_publisher_anyOf_i1) |

### <a name="creator_anyOf_i2"></a>Property `Dataset > creator > anyOf > Link`

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

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [Dataset object or link](#hasPart_items) | -           |

### <a name="hasPart_items"></a>Dataset > hasPart > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [Dataset](#hasPart_items_anyOf_i0) |
| [Link](#hasPart_items_anyOf_i1)    |

#### <a name="hasPart_items_anyOf_i0"></a>Property `Dataset > hasPart > Dataset object or link > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

#### <a name="hasPart_items_anyOf_i1"></a>Property `Dataset > hasPart > Dataset object or link > anyOf > Link`

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

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description               |
| ------------------------------- | ------------------------- |
| [Link](#isReferencedBy_items)   | reference iri of Resource |

### <a name="isReferencedBy_items"></a>Dataset > isReferencedBy > Link

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
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>Property `Dataset > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Dataset > issued > anyOf > Date string`

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

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `Dataset > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `Dataset > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `Dataset > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `Dataset > issued > anyOf > Date string > anyOf > item 3`

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
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `Dataset > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `Dataset > modified > anyOf > Date string`

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

#### <a name="modified_anyOf_i1_anyOf_i0"></a>Property `Dataset > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>Property `Dataset > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>Property `Dataset > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>Property `Dataset > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="provenance"></a>Property `Dataset > provenance`

**Title:** provenance

List of statements about the lineage of a Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                  | Description |
| ------------------------------------------------ | ----------- |
| [ProvenanceStatement or link](#provenance_items) | -           |

### <a name="provenance_items"></a>Dataset > provenance > ProvenanceStatement or link

**Title:** ProvenanceStatement or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [ProvenanceStatement](#provenance_items_anyOf_i0) |
| [Link](#provenance_items_anyOf_i1)                |

#### <a name="provenance_items_anyOf_i0"></a>Property `Dataset > provenance > ProvenanceStatement or link > anyOf > ProvenanceStatement`

**Title:** ProvenanceStatement

inline description of ProvenanceStatement

| **Type**                  | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                  |
| **Same definition as**    | [ProvenanceStatement](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_provenance_items_anyOf_i0) |

#### <a name="provenance_items_anyOf_i1"></a>Property `Dataset > provenance > ProvenanceStatement or link > anyOf > Link`

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

| Any of(Option)                      |
| ----------------------------------- |
| [Organization](#publisher_anyOf_i0) |
| [Link](#publisher_anyOf_i1)         |

### <a name="publisher_anyOf_i0"></a>Property `Dataset > publisher > anyOf > Organization`

**Title:** Organization

inline description of Organization

| **Type**                  | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Organization](#otherIdentifier_items_anyOf_i0_anyOf_i1_creator_anyOf_i1) |

### <a name="publisher_anyOf_i1"></a>Property `Dataset > publisher > anyOf > Link`

**Title:** Link

reference iri of Organization

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="relation"></a>Property `Dataset > relation`

**Title:** related resource

List of references to a related resource

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description               |
| ------------------------------- | ------------------------- |
| [Link](#relation_items)         | reference iri of Resource |

### <a name="relation_items"></a>Dataset > relation > Link

**Title:** Link

reference iri of Resource

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="replaces"></a>Property `Dataset > replaces`

**Title:** replaces

List of Datasets replaced by this Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Dataset object or link](#replaces_items) | -           |

### <a name="replaces_items"></a>Dataset > replaces > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Dataset](#replaces_items_anyOf_i0) |
| [Link](#replaces_items_anyOf_i1)    |

#### <a name="replaces_items_anyOf_i0"></a>Property `Dataset > replaces > Dataset object or link > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

#### <a name="replaces_items_anyOf_i1"></a>Property `Dataset > replaces > Dataset object or link > anyOf > Link`

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

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#rights_anyOf_i0) |
| [RightsStatement](#rights_anyOf_i1)                |
| [Link](#rights_anyOf_i2)                           |

### <a name="rights_anyOf_i0"></a>Property `Dataset > rights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="rights_anyOf_i1"></a>Property `Dataset > rights > anyOf > RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

| **Type**                  | `object`                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                          |
| **Same definition as**    | [RightsStatement](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_accessRights_anyOf_i1) |

### <a name="rights_anyOf_i2"></a>Property `Dataset > rights > anyOf > Link`

**Title:** Link

reference iri of RightsStatement

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `Dataset > rightsHolder`

**Title:** rights holder

List of agents (organizations) holding rights on the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [Organization or link](#rightsHolder_items) | -           |

### <a name="rightsHolder_items"></a>Dataset > rightsHolder > Organization or link

**Title:** Organization or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [Organization](#rightsHolder_items_anyOf_i0) |
| [Link](#rightsHolder_items_anyOf_i1)         |

#### <a name="rightsHolder_items_anyOf_i0"></a>Property `Dataset > rightsHolder > Organization or link > anyOf > Organization`

**Title:** Organization

inline description of Organization

| **Type**                  | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Organization](#otherIdentifier_items_anyOf_i0_anyOf_i1_creator_anyOf_i1) |

#### <a name="rightsHolder_items_anyOf_i1"></a>Property `Dataset > rightsHolder > Organization or link > anyOf > Link`

**Title:** Link

reference iri of Organization

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="source"></a>Property `Dataset > source`

**Title:** data source

List of related Datasets from which the described Dataset is derived

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [Dataset object or link](#source_items) | -           |

### <a name="source_items"></a>Dataset > source > Dataset object or link

**Title:** Dataset object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                    |
| --------------------------------- |
| [Dataset](#source_items_anyOf_i0) |
| [Link](#source_items_anyOf_i1)    |

#### <a name="source_items_anyOf_i0"></a>Property `Dataset > source > Dataset object or link > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [Dataset](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0) |

#### <a name="source_items_anyOf_i1"></a>Property `Dataset > source > Dataset object or link > anyOf > Link`

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

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#spatial_anyOf_i0) |
| [Location](#spatial_anyOf_i1)                       |
| [Link](#spatial_anyOf_i2)                           |
| [List og geographic regions](#spatial_anyOf_i3)     |

### <a name="spatial_anyOf_i0"></a>Property `Dataset > spatial > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="spatial_anyOf_i1"></a>Property `Dataset > spatial > anyOf > Location`

**Title:** Location

inline description of Location

| **Type**                  | `object`                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Location](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0_spatial_items_anyOf_i0) |

### <a name="spatial_anyOf_i2"></a>Property `Dataset > spatial > anyOf > Link`

**Title:** Link

reference iri of Location

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="spatial_anyOf_i3"></a>Property `Dataset > spatial > anyOf > List og geographic regions`

**Title:** List og geographic regions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [Location or link](#spatial_anyOf_i3_items) | -           |

#### <a name="spatial_anyOf_i3_items"></a>Dataset > spatial > anyOf > List og geographic regions > Location or link

**Title:** Location or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i3_items_anyOf_i0) |
| [Link](#spatial_anyOf_i3_items_anyOf_i1)     |

##### <a name="spatial_anyOf_i3_items_anyOf_i0"></a>Property `Dataset > spatial > anyOf > List og geographic regions > Location or link > anyOf > Location`

**Title:** Location

inline description of Location

| **Type**                  | `object`                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Location](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0_spatial_items_anyOf_i0) |

##### <a name="spatial_anyOf_i3_items_anyOf_i1"></a>Property `Dataset > spatial > anyOf > List og geographic regions > Location or link > anyOf > Link`

**Title:** Link

reference iri of Location

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="subject"></a>Property `Dataset > subject`

**Title:** subject

List of primary subjects of the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be   | Description |
| --------------------------------- | ----------- |
| [Subject or link](#subject_items) | -           |

### <a name="subject_items"></a>Dataset > subject > Subject or link

**Title:** Subject or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [Concept](#subject_items_anyOf_i0) |
| [Link](#subject_items_anyOf_i1)    |

#### <a name="subject_items_anyOf_i0"></a>Property `Dataset > subject > Subject or link > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                           |
| ------------------------- | ------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                   |
| **Same definition as**    | [Concept](#sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

#### <a name="subject_items_anyOf_i1"></a>Property `Dataset > subject > Subject or link > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `Dataset > temporal`

**Title:** temporal coverage

List of temporal periods that the dataset covers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [PeriodOfTime object or link](#temporal_items) | -           |

### <a name="temporal_items"></a>Dataset > temporal > PeriodOfTime object or link

**Title:** PeriodOfTime object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                           |
| ---------------------------------------- |
| [PeriodOfTime](#temporal_items_anyOf_i0) |
| [Link](#temporal_items_anyOf_i1)         |

#### <a name="temporal_items_anyOf_i0"></a>Property `Dataset > temporal > PeriodOfTime object or link > anyOf > PeriodOfTime`

**Title:** PeriodOfTime

inline description of PeriodOfTime

| **Type**                  | `object`                                                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                                 |
| **Same definition as**    | [PeriodOfTime](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0_temporal_items_anyOf_i0) |

#### <a name="temporal_items_anyOf_i1"></a>Property `Dataset > temporal > PeriodOfTime object or link > anyOf > Link`

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

List of categories for the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [Category or link](#category_items) | -           |

### <a name="category_items"></a>Dataset > category > Category or link

**Title:** Category or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Concept](#category_items_anyOf_i0) |
| [Link](#category_items_anyOf_i1)    |

#### <a name="category_items_anyOf_i0"></a>Property `Dataset > category > Category or link > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                           |
| ------------------------- | ------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                   |
| **Same definition as**    | [Concept](#sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

#### <a name="category_items_anyOf_i1"></a>Property `Dataset > category > Category or link > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="hasQualityMeasurement"></a>Property `Dataset > hasQualityMeasurement`

**Title:** quality measurement

List of quality measurements for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                            | Description |
| ---------------------------------------------------------- | ----------- |
| [QualityMeasurement or link](#hasQualityMeasurement_items) | -           |

### <a name="hasQualityMeasurement_items"></a>Dataset > hasQualityMeasurement > QualityMeasurement or link

**Title:** QualityMeasurement or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_items_anyOf_i0) |
| [Link](#hasQualityMeasurement_items_anyOf_i1)               |

#### <a name="hasQualityMeasurement_items_anyOf_i0"></a>Property `Dataset > hasQualityMeasurement > QualityMeasurement or link > anyOf > QualityMeasurement`

**Title:** QualityMeasurement

inline description of QualityMeasurement

| **Type**                  | `object`                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [QualityMeasurement](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_hasQualityMeasurement_items_anyOf_i0) |

#### <a name="hasQualityMeasurement_items_anyOf_i1"></a>Property `Dataset > hasQualityMeasurement > QualityMeasurement or link > anyOf > Link`

**Title:** Link

reference iri of QualityMeasurement

| **Type** | `string` |
| -------- | -------- |

## <a name="page"></a>Property `Dataset > page`

**Title:** documentation

List of pages or documents about this dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [Document object or link](#page_items) | -           |

### <a name="page_items"></a>Dataset > page > Document object or link

**Title:** Document object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [Document](#page_items_anyOf_i0) |
| [Link](#page_items_anyOf_i1)     |

#### <a name="page_items_anyOf_i0"></a>Property `Dataset > page > Document object or link > anyOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                  |
| **Same definition as**    | [Document](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_landingPage_anyOf_i1) |

#### <a name="page_items_anyOf_i1"></a>Property `Dataset > page > Document object or link > anyOf > Link`

**Title:** Link

reference iri of Document

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `Dataset > qualifiedAttribution`

**Title:** qualified attribution

List of agents having some form of responsibility for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [Attribution object or link](#qualifiedAttribution_items) | -           |

### <a name="qualifiedAttribution_items"></a>Dataset > qualifiedAttribution > Attribution object or link

**Title:** Attribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Attribution](#qualifiedAttribution_items_anyOf_i0) |
| [Link](#qualifiedAttribution_items_anyOf_i1)        |

#### <a name="qualifiedAttribution_items_anyOf_i0"></a>Property `Dataset > qualifiedAttribution > Attribution object or link > anyOf > Attribution`

**Title:** Attribution

inline description of Attribution

| **Type**                  | `object`                                                                                                                            |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                    |
| **Same definition as**    | [Attribution](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_qualifiedAttribution_items_anyOf_i0) |

#### <a name="qualifiedAttribution_items_anyOf_i1"></a>Property `Dataset > qualifiedAttribution > Attribution object or link > anyOf > Link`

**Title:** Link

reference iri of Attribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="wasAttributedTo"></a>Property `Dataset > wasAttributedTo`

**Title:** attribution

List of agents attributed to this dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [Agent object or link](#wasAttributedTo_items) | -           |

### <a name="wasAttributedTo_items"></a>Dataset > wasAttributedTo > Agent object or link

**Title:** Agent object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                           |
| ---------------------------------------- |
| [Agent](#wasAttributedTo_items_anyOf_i0) |
| [Link](#wasAttributedTo_items_anyOf_i1)  |

#### <a name="wasAttributedTo_items_anyOf_i0"></a>Property `Dataset > wasAttributedTo > Agent object or link > anyOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                                     |
| **Same definition as**    | [Agent](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_inSeries_items_anyOf_i0_publisher_anyOf_i1) |

#### <a name="wasAttributedTo_items_anyOf_i1"></a>Property `Dataset > wasAttributedTo > Agent object or link > anyOf > Link`

**Title:** Link

reference iri of Agent

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="wasGeneratedBy"></a>Property `Dataset > wasGeneratedBy`

**Title:** was generated by

List of activities that generated, or provide the business context for the creation of the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                  | Description |
| ------------------------------------------------ | ----------- |
| [Activity object or link](#wasGeneratedBy_items) | -           |

### <a name="wasGeneratedBy_items"></a>Dataset > wasGeneratedBy > Activity object or link

**Title:** Activity object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                             |
| ------------------------------------------ |
| [Activity](#wasGeneratedBy_items_anyOf_i0) |
| [Link](#wasGeneratedBy_items_anyOf_i1)     |

#### <a name="wasGeneratedBy_items_anyOf_i0"></a>Property `Dataset > wasGeneratedBy > Activity object or link > anyOf > Activity`

**Title:** Activity

inline description of Activity

| **Type**                  | `object`                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [Activity](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_wasGeneratedBy_items_anyOf_i0) |

#### <a name="wasGeneratedBy_items_anyOf_i1"></a>Property `Dataset > wasGeneratedBy > Activity object or link > anyOf > Link`

**Title:** Link

reference iri of Activity

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="wasUsedBy"></a>Property `Dataset > wasUsedBy`

**Title:** used by

List of activities that used the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [Activity object or link](#wasUsedBy_items) | -           |

### <a name="wasUsedBy_items"></a>Dataset > wasUsedBy > Activity object or link

**Title:** Activity object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                        |
| ------------------------------------- |
| [Activity](#wasUsedBy_items_anyOf_i0) |
| [Link](#wasUsedBy_items_anyOf_i1)     |

#### <a name="wasUsedBy_items_anyOf_i0"></a>Property `Dataset > wasUsedBy > Activity object or link > anyOf > Activity`

**Title:** Activity

inline description of Activity

| **Type**                  | `object`                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [Activity](#sample_items_anyOf_i0_accessService_items_anyOf_i0_servesDataset_items_anyOf_i0_wasGeneratedBy_items_anyOf_i0) |

#### <a name="wasUsedBy_items_anyOf_i1"></a>Property `Dataset > wasUsedBy > Activity object or link > anyOf > Link`

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

