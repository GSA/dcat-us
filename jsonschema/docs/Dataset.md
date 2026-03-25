

**Title:** Dataset

Information about a set of data

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                                   | Type               | Title/Description                                                                   |
| ---------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                             | string             | -                                                                                   |
| - [@type](#@type )                                         | string             | -                                                                                   |
| - [otherIdentifier](#otherIdentifier )                     | More than one type | other identifier                                                                    |
| - [sample](#sample )                                       | More than one type | sample                                                                              |
| - [status](#status )                                       | More than one type | lifecycle status                                                                    |
| - [supportedSchema](#supportedSchema )                     | More than one type | supported schema                                                                    |
| - [versionNotes](#versionNotes )                           | null or string     | version notes                                                                       |
| - [contactPoint](#contactPoint )                           | More than one type | contact point                                                                       |
| - [distribution](#distribution )                           | More than one type | dataset distribution                                                                |
| - [first](#first )                                         | More than one type | first                                                                               |
| - [hasCurrentVersion](#hasCurrentVersion )                 | More than one type | current version                                                                     |
| - [hasVersion](#hasVersion )                               | More than one type | has version                                                                         |
| - [inSeries](#inSeries )                                   | More than one type | in series                                                                           |
| - [keyword](#keyword )                                     | More than one type | keyword/tag                                                                         |
| - [keywordMap](#keywordMap )                               | null or object     | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [landingPage](#landingPage )                             | More than one type | landing page                                                                        |
| - [previousVersion](#previousVersion )                     | More than one type | previous version                                                                    |
| - [qualifiedRelation](#qualifiedRelation )                 | More than one type | qualified relation                                                                  |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string     | Spatial resolution (meters)                                                         |
| - [temporalResolution](#temporalResolution )               | null or string     | temporal resolution                                                                 |
| - [theme](#theme )                                         | More than one type | theme/category                                                                      |
| - [version](#version )                                     | null or string     | version                                                                             |
| - [describedBy](#describedBy )                             | More than one type | data dictionary                                                                     |
| - [geographicBoundingBox](#geographicBoundingBox )         | More than one type | geographic bounding box                                                             |
| - [liabilityStatement](#liabilityStatement )               | More than one type | liability statement                                                                 |
| - [metadataDistribution](#metadataDistribution )           | More than one type | metadata distribution                                                               |
| - [purpose](#purpose )                                     | null or string     | purpose                                                                             |
| - [purposeMap](#purposeMap )                               | null or object     | Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [accessRights](#accessRights )                           | More than one type | access rights                                                                       |
| - [accrualPeriodicity](#accrualPeriodicity )               | More than one type | frequency                                                                           |
| - [conformsTo](#conformsTo )                               | More than one type | conforms to                                                                         |
| - [contributor](#contributor )                             | More than one type | contributor                                                                         |
| - [created](#created )                                     | More than one type | creation date                                                                       |
| - [creator](#creator )                                     | More than one type | creator                                                                             |
| + [description](#description )                             | string             | description                                                                         |
| - [descriptionMap](#descriptionMap )                       | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#hasPart )                                     | More than one type | has part                                                                            |
| - [identifier](#identifier )                               | null or string     | identifier                                                                          |
| - [isReferencedBy](#isReferencedBy )                       | More than one type | is referenced by                                                                    |
| - [issued](#issued )                                       | More than one type | release date                                                                        |
| - [language](#language )                                   | More than one type | language                                                                            |
| - [modified](#modified )                                   | More than one type | last modified                                                                       |
| - [provenance](#provenance )                               | More than one type | provenance                                                                          |
| + [publisher](#publisher )                                 | More than one type | publisher                                                                           |
| - [relation](#relation )                                   | More than one type | related resource                                                                    |
| - [replaces](#replaces )                                   | More than one type | replaces                                                                            |
| - [rights](#rights )                                       | More than one type | rights                                                                              |
| - [rightsHolder](#rightsHolder )                           | More than one type | rights holder                                                                       |
| - [source](#source )                                       | More than one type | data source                                                                         |
| - [spatial](#spatial )                                     | More than one type | spatial/geographic coverage                                                         |
| - [subject](#subject )                                     | More than one type | subject                                                                             |
| - [temporal](#temporal )                                   | More than one type | temporal coverage                                                                   |
| + [title](#title )                                         | string             | title                                                                               |
| - [titleMap](#titleMap )                                   | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                                   | More than one type | category                                                                            |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | More than one type | quality measurement                                                                 |
| - [page](#page )                                           | More than one type | documentation                                                                       |
| - [qualifiedAttribution](#qualifiedAttribution )           | More than one type | qualified attribution                                                               |
| - [wasAttributedTo](#wasAttributedTo )                     | More than one type | attribution                                                                         |
| - [wasGeneratedBy](#wasGeneratedBy )                       | More than one type | was generated by                                                                    |
| - [wasUsedBy](#wasUsedBy )                                 | More than one type | used by                                                                             |
| - [image](#image )                                         | More than one type | image                                                                               |
| - [scopeNote](#scopeNote )                                 | null or string     | usage note                                                                          |
| - [scopeNoteMap](#scopeNoteMap )                           | null or object     | Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |             |
| ----------- | ----------- |
| **Type**    | `string`    |
| **Default** | `"Dataset"` |

## <a name="otherIdentifier"></a>Property `otherIdentifier`

**Title:** other identifier

List of structure identifiers

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#otherIdentifier_anyOf_i0) |
| [item 1](#otherIdentifier_anyOf_i1) |

### <a name="otherIdentifier_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="otherIdentifier_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [item 1 items](#otherIdentifier_anyOf_i1_items) | -           |

#### <a name="otherIdentifier_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                         |
| ------------------------------------------------------ |
| [Identifier](#otherIdentifier_anyOf_i1_items_oneOf_i0) |
| [item 1](#otherIdentifier_anyOf_i1_items_oneOf_i1)     |

##### <a name="otherIdentifier_anyOf_i1_items_oneOf_i0"></a>Property `Identifier`

**Title:** Identifier

inline description of other identifier

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Additional properties** | Any type allowed              |
| **Defined in**            | [Identifier](./Identifier.md) |

##### <a name="otherIdentifier_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of other identifier

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="sample"></a>Property `sample`

**Title:** sample

List of links to samples of a Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#sample_anyOf_i0) |
| [item 1](#sample_anyOf_i1) |

### <a name="sample_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="sample_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#sample_anyOf_i1_items) | -           |

#### <a name="sample_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Distribution](#sample_anyOf_i1_items_oneOf_i0) |
| [item 1](#sample_anyOf_i1_items_oneOf_i1)       |

##### <a name="sample_anyOf_i1_items_oneOf_i0"></a>Property `Distribution`

**Title:** Distribution

inline description of Distribution

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Distribution](./Distribution.md) |

##### <a name="sample_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Distribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="status"></a>Property `status`

**Title:** lifecycle status

The status of the dataset  in the context of maturity lifecycle

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)              |
| --------------------------- |
| [item 0](#status_oneOf_i0)  |
| [Concept](#status_oneOf_i1) |
| [item 2](#status_oneOf_i2)  |

### <a name="status_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="status_oneOf_i1"></a>Property `Concept`

**Title:** Concept

inline description of Concept

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

### <a name="status_oneOf_i2"></a>Property `item 2`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="supportedSchema"></a>Property `supportedSchema`

**Title:** supported schema

supported schema for this dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#supportedSchema_oneOf_i0)  |
| [Dataset](#supportedSchema_oneOf_i1) |
| [item 2](#supportedSchema_oneOf_i2)  |

### <a name="supportedSchema_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="supportedSchema_oneOf_i1"></a>Property `Dataset`

**Title:** Dataset

inline description of the supported schema

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="supportedSchema_oneOf_i2"></a>Property `item 2`

reference iri of the supported schema

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="versionNotes"></a>Property `versionNotes`

**Title:** version notes

version notes for this dataset

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="contactPoint"></a>Property `contactPoint`

**Title:** contact point

List of contact information that can be used for sending comments about the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#contactPoint_anyOf_i0) |
| [item 1](#contactPoint_anyOf_i1) |

### <a name="contactPoint_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="contactPoint_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items) | -           |

#### <a name="contactPoint_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Kind](#contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i1) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `Kind`

**Title:** Kind

inline description of Kind

|                           |                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                  |
| **Additional properties** | Any type allowed                                                                                          |
| **Same definition as**    | [Kind](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Kind

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="distribution"></a>Property `distribution`

**Title:** dataset distribution

List of available distributions for the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#distribution_anyOf_i0) |
| [item 1](#distribution_anyOf_i1) |

### <a name="distribution_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="distribution_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#distribution_anyOf_i1_items) | -           |

#### <a name="distribution_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Distribution](#distribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#distribution_anyOf_i1_items_oneOf_i1)       |

##### <a name="distribution_anyOf_i1_items_oneOf_i0"></a>Property `Distribution`

**Title:** Distribution

inline description of Distribution

|                           |                                                 |
| ------------------------- | ----------------------------------------------- |
| **Type**                  | `object`                                        |
| **Additional properties** | Any type allowed                                |
| **Same definition as**    | [Distribution](#sample_anyOf_i1_items_oneOf_i0) |

##### <a name="distribution_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Distribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="first"></a>Property `first`

**Title:** first

the first item of the sequence the dataset belongs to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)             |
| -------------------------- |
| [item 0](#first_oneOf_i0)  |
| [Dataset](#first_oneOf_i1) |
| [item 2](#first_oneOf_i2)  |

### <a name="first_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="first_oneOf_i1"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="first_oneOf_i2"></a>Property `item 2`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="hasCurrentVersion"></a>Property `hasCurrentVersion`

**Title:** current version

reference to the current (latest) version of a dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                         |
| -------------------------------------- |
| [item 0](#hasCurrentVersion_oneOf_i0)  |
| [Dataset](#hasCurrentVersion_oneOf_i1) |
| [item 2](#hasCurrentVersion_oneOf_i2)  |

### <a name="hasCurrentVersion_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="hasCurrentVersion_oneOf_i1"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="hasCurrentVersion_oneOf_i2"></a>Property `item 2`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="hasVersion"></a>Property `hasVersion`

**Title:** has version

List of related Datasets that are a version, edition, or adaptation of the described Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#hasVersion_anyOf_i0) |
| [item 1](#hasVersion_anyOf_i1) |

### <a name="hasVersion_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="hasVersion_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#hasVersion_anyOf_i1_items) | -           |

#### <a name="hasVersion_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                 |
| ---------------------------------------------- |
| [Dataset](#hasVersion_anyOf_i1_items_oneOf_i0) |
| [item 1](#hasVersion_anyOf_i1_items_oneOf_i1)  |

##### <a name="hasVersion_anyOf_i1_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="hasVersion_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="inSeries"></a>Property `inSeries`

**Title:** in series

List of Dataset Series this dataset belongs to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#inSeries_anyOf_i0) |
| [item 1](#inSeries_anyOf_i1) |

### <a name="inSeries_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="inSeries_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#inSeries_anyOf_i1_items) | -           |

#### <a name="inSeries_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                     |
| -------------------------------------------------- |
| [DatasetSeries](#inSeries_anyOf_i1_items_oneOf_i0) |
| [item 1](#inSeries_anyOf_i1_items_oneOf_i1)        |

##### <a name="inSeries_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries`

**Title:** DatasetSeries

inline description of DatasetSeries

|                           |                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                                                              |
| **Same definition as**    | [DatasetSeries](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0) |

##### <a name="inSeries_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of DatasetSeries

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="keyword"></a>Property `keyword`

**Title:** keyword/tag

List of keywords or tags describing the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#keyword_anyOf_i0) |
| [item 1](#keyword_anyOf_i1) |

### <a name="keyword_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="keyword_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#keyword_anyOf_i1_items) | -           |

#### <a name="keyword_anyOf_i1_items"></a>item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="keywordMap"></a>Property `keywordMap`

Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="landingPage"></a>Property `landingPage`

**Title:** landing page

A web page that provides access to the Dataset, its Distributions and/or additional information

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                    |
| --------------------------------- |
| [item 0](#landingPage_oneOf_i0)   |
| [Document](#landingPage_oneOf_i1) |
| [item 2](#landingPage_oneOf_i2)   |

### <a name="landingPage_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="landingPage_oneOf_i1"></a>Property `Document`

**Title:** Document

inline description of Document

|                           |                                                                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                     |
| **Additional properties** | Any type allowed                                                                                                                             |
| **Same definition as**    | [Document](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_landingPage_oneOf_i1) |

### <a name="landingPage_oneOf_i2"></a>Property `item 2`

reference iri of Document

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="previousVersion"></a>Property `previousVersion`

**Title:** previous version

reference to the previous dataset version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#previousVersion_oneOf_i0)  |
| [Dataset](#previousVersion_oneOf_i1) |
| [item 2](#previousVersion_oneOf_i2)  |

### <a name="previousVersion_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="previousVersion_oneOf_i1"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

### <a name="previousVersion_oneOf_i2"></a>Property `item 2`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="qualifiedRelation"></a>Property `qualifiedRelation`

**Title:** qualified relation

Qualified relationship with role of the dataset with another resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#qualifiedRelation_anyOf_i0) |
| [item 1](#qualifiedRelation_anyOf_i1) |

### <a name="qualifiedRelation_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="qualifiedRelation_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 1 items](#qualifiedRelation_anyOf_i1_items) | -           |

#### <a name="qualifiedRelation_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Relationship](#qualifiedRelation_anyOf_i1_items_oneOf_i0) |
| [item 1](#qualifiedRelation_anyOf_i1_items_oneOf_i1)       |

##### <a name="qualifiedRelation_anyOf_i1_items_oneOf_i0"></a>Property `Relationship`

**Title:** Relationship

inline description of Relationship

|                           |                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                                                      |
| **Same definition as**    | [Relationship](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedRelation_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Relationship

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatialResolutionInMeters"></a>Property `spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

Spatial resolution in meters

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="temporalResolution"></a>Property `temporalResolution`

**Title:** temporal resolution

Temporal resolution using xsd:duration syntax

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="theme"></a>Property `theme`

**Title:** theme/category

List of themes of the dataset

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

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="theme_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="version"></a>Property `version`

**Title:** version

The version indicator (name or identifier) of a resource

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="describedBy"></a>Property `describedBy`

**Title:** data dictionary

A distribution describing the Data Dictionary for this dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#describedBy_oneOf_i0)       |
| [Distribution](#describedBy_oneOf_i1) |
| [item 2](#describedBy_oneOf_i2)       |

### <a name="describedBy_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="describedBy_oneOf_i1"></a>Property `Distribution`

**Title:** Distribution

inline description of Distribution

|                           |                                                 |
| ------------------------- | ----------------------------------------------- |
| **Type**                  | `object`                                        |
| **Additional properties** | Any type allowed                                |
| **Same definition as**    | [Distribution](#sample_anyOf_i1_items_oneOf_i0) |

### <a name="describedBy_oneOf_i2"></a>Property `item 2`

reference iri of Distribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="geographicBoundingBox"></a>Property `geographicBoundingBox`

**Title:** geographic bounding box

List of WGS84 Geographic Bounding Boxes for this dataset

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
| **Same definition as**    | [GeographicBoundingBox](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |

##### <a name="geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of GeographicBoundingBox

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="liabilityStatement"></a>Property `liabilityStatement`

**Title:** liability statement

A liability statement about the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#liabilityStatement_oneOf_i0)             |
| [LiabilityStatement](#liabilityStatement_oneOf_i1) |
| [item 2](#liabilityStatement_oneOf_i2)             |

### <a name="liabilityStatement_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="liabilityStatement_oneOf_i1"></a>Property `LiabilityStatement`

**Title:** LiabilityStatement

inline description of LiabilityStatement

|                           |                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                                                              |
| **Same definition as**    | [LiabilityStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_liabilityStatement_oneOf_i1) |

### <a name="liabilityStatement_oneOf_i2"></a>Property `item 2`

reference iri of LiabilityStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="metadataDistribution"></a>Property `metadataDistribution`

**Title:** metadata distribution

Distribution to "original" metadata document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                           |
| ---------------------------------------- |
| [item 0](#metadataDistribution_anyOf_i0) |
| [item 1](#metadataDistribution_anyOf_i1) |

### <a name="metadataDistribution_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="metadataDistribution_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 1 items](#metadataDistribution_anyOf_i1_items) | -           |

#### <a name="metadataDistribution_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [Distribution](#metadataDistribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#metadataDistribution_anyOf_i1_items_oneOf_i1)       |

##### <a name="metadataDistribution_anyOf_i1_items_oneOf_i0"></a>Property `Distribution`

**Title:** Distribution

inline description of Distribution

|                           |                                                 |
| ------------------------- | ----------------------------------------------- |
| **Type**                  | `object`                                        |
| **Additional properties** | Any type allowed                                |
| **Same definition as**    | [Distribution](#sample_anyOf_i1_items_oneOf_i0) |

##### <a name="metadataDistribution_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Distribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="purpose"></a>Property `purpose`

**Title:** purpose

The purpose of the dataset

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="purposeMap"></a>Property `purposeMap`

Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="accessRights"></a>Property `accessRights`

**Title:** access rights

Information that indicates whether the Dataset is open data, has access restrictions or is public

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

inline description of RightsStatement

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="accessRights_oneOf_i2"></a>Property `item 2`

reference iri of RightsStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accrualPeriodicity"></a>Property `accrualPeriodicity`

**Title:** frequency

The frequency at which the Dataset is updated

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#accrualPeriodicity_oneOf_i0)    |
| [frequency](#accrualPeriodicity_oneOf_i1) |
| [item 2](#accrualPeriodicity_oneOf_i2)    |

### <a name="accrualPeriodicity_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accrualPeriodicity_oneOf_i1"></a>Property `frequency`

inline description of Frequency

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Additional properties** | Any type allowed            |
| **Defined in**            | [Frequency](./Frequency.md) |

### <a name="accrualPeriodicity_oneOf_i2"></a>Property `item 2`

reference iri of Frequency

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `conformsTo`

**Title:** conforms to

List of standards to which the described Dataset conforms

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

|                           |                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                        |
| **Additional properties** | Any type allowed                                                                                                                                                                |
| **Same definition as**    | [Standard](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_landingPage_oneOf_i1_conformsTo_anyOf_i1_items_oneOf_i0) |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Standard

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="contributor"></a>Property `contributor`

**Title:** contributor

List of agents contributing to the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                  |
| ------------------------------- |
| [item 0](#contributor_anyOf_i0) |
| [item 1](#contributor_anyOf_i1) |

### <a name="contributor_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="contributor_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [item 1 items](#contributor_anyOf_i1_items) | -           |

#### <a name="contributor_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                 |
| ---------------------------------------------- |
| [Agent](#contributor_anyOf_i1_items_oneOf_i0)  |
| [item 1](#contributor_anyOf_i1_items_oneOf_i1) |

##### <a name="contributor_anyOf_i1_items_oneOf_i0"></a>Property `Agent`

**Title:** Agent

inline description of Agent

|                           |                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                                                         |
| **Same definition as**    | [Agent](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

##### <a name="contributor_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Agent

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="created"></a>Property `created`

**Title:** creation date

The date on which the Dataset was first created

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

An entity responsible for producing the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)              |
| --------------------------- |
| [item 0](#creator_oneOf_i0) |
| [Agent](#creator_oneOf_i1)  |
| [item 2](#creator_oneOf_i2) |

### <a name="creator_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="creator_oneOf_i1"></a>Property `Agent`

**Title:** Agent

inline description of Agent

|                           |                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                                                         |
| **Same definition as**    | [Agent](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

### <a name="creator_oneOf_i2"></a>Property `item 2`

reference iri of Agent

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `description`

**Title:** description

A free-text account of the Dataset

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="descriptionMap"></a>Property `descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="hasPart"></a>Property `hasPart`

**Title:** has part

List of related datasets that are part of the described dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#hasPart_anyOf_i0) |
| [item 1](#hasPart_anyOf_i1) |

### <a name="hasPart_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="hasPart_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#hasPart_anyOf_i1_items) | -           |

#### <a name="hasPart_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                              |
| ------------------------------------------- |
| [Dataset](#hasPart_anyOf_i1_items_oneOf_i0) |
| [item 1](#hasPart_anyOf_i1_items_oneOf_i1)  |

##### <a name="hasPart_anyOf_i1_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="hasPart_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `identifier`

**Title:** identifier

The unique identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalog

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="isReferencedBy"></a>Property `isReferencedBy`

**Title:** is referenced by

List of links to related resources, such as publications, that reference, cite, or otherwise point to the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                     |
| ---------------------------------- |
| [item 0](#isReferencedBy_anyOf_i0) |
| [item 1](#isReferencedBy_anyOf_i1) |

### <a name="isReferencedBy_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="isReferencedBy_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be                | Description               |
| ---------------------------------------------- | ------------------------- |
| [item 1 items](#isReferencedBy_anyOf_i1_items) | reference iri of Resource |

#### <a name="isReferencedBy_anyOf_i1_items"></a>item 1 items

reference iri of Resource

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="issued"></a>Property `issued`

**Title:** release date

Date of formal issuance (e.g., publication) of the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="issued_anyOf_i1"></a>Property `item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `language`

**Title:** language

Language or languages used in the Dataset. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

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

## <a name="modified"></a>Property `modified`

**Title:** last modified

The most recent date on which the Dataset was changed or modified

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

## <a name="provenance"></a>Property `provenance`

**Title:** provenance

List of statements about the lineage of a Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#provenance_anyOf_i0) |
| [item 1](#provenance_anyOf_i1) |

### <a name="provenance_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="provenance_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#provenance_anyOf_i1_items) | -           |

#### <a name="provenance_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [ProvenanceStatement](#provenance_anyOf_i1_items_oneOf_i0) |
| [item 1](#provenance_anyOf_i1_items_oneOf_i1)              |

##### <a name="provenance_anyOf_i1_items_oneOf_i0"></a>Property `ProvenanceStatement`

**Title:** ProvenanceStatement

inline description of ProvenanceStatement

|                           |                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                                                      |
| **Same definition as**    | [ProvenanceStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0) |

##### <a name="provenance_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of ProvenanceStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="publisher"></a>Property `publisher`

**Title:** publisher

An organization responsible for making the Dataset available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                      |
| ----------------------------------- |
| [Organization](#publisher_oneOf_i0) |
| [item 1](#publisher_oneOf_i1)       |

### <a name="publisher_oneOf_i0"></a>Property `Organization`

**Title:** Organization

inline description of Organization

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Organization](#otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

### <a name="publisher_oneOf_i1"></a>Property `item 1`

reference iri of Organization

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="relation"></a>Property `relation`

**Title:** related resource

List of references to a related resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#relation_anyOf_i0) |
| [item 1](#relation_anyOf_i1) |

### <a name="relation_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="relation_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be          | Description               |
| ---------------------------------------- | ------------------------- |
| [item 1 items](#relation_anyOf_i1_items) | reference iri of Resource |

#### <a name="relation_anyOf_i1_items"></a>item 1 items

reference iri of Resource

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="replaces"></a>Property `replaces`

**Title:** replaces

List of Datasets replaced by this Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#replaces_anyOf_i0) |
| [item 1](#replaces_anyOf_i1) |

### <a name="replaces_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="replaces_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#replaces_anyOf_i1_items) | -           |

#### <a name="replaces_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Dataset](#replaces_anyOf_i1_items_oneOf_i0) |
| [item 1](#replaces_anyOf_i1_items_oneOf_i1)  |

##### <a name="replaces_anyOf_i1_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="replaces_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="rights"></a>Property `rights`

**Title:** rights

List of statements concerning all rights for the Dataset not addressed with license or accessRights, such as copyright statements

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#rights_oneOf_i0)          |
| [RightsStatement](#rights_oneOf_i1) |
| [item 2](#rights_oneOf_i2)          |

### <a name="rights_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="rights_oneOf_i1"></a>Property `RightsStatement`

**Title:** RightsStatement

inline description of RightsStatement

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | Any type allowed                                                                                                                                     |
| **Same definition as**    | [RightsStatement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="rights_oneOf_i2"></a>Property `item 2`

reference iri of RightsStatement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `rightsHolder`

**Title:** rights holder

List of agents (organizations) holding rights on the Dataset

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

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Organization](#otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Organization

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="source"></a>Property `source`

**Title:** data source

List of related Datasets from which the described Dataset is derived

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#source_anyOf_i0) |
| [item 1](#source_anyOf_i1) |

### <a name="source_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="source_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#source_anyOf_i1_items) | -           |

#### <a name="source_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                             |
| ------------------------------------------ |
| [Dataset](#source_anyOf_i1_items_oneOf_i0) |
| [item 1](#source_anyOf_i1_items_oneOf_i1)  |

##### <a name="source_anyOf_i1_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                       |
| **Same definition as**    | [Dataset](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |

##### <a name="source_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `spatial`

**Title:** spatial/geographic coverage

A geographic region or regions that are covered by the Dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [item 0](#spatial_oneOf_i0)   |
| [Location](#spatial_oneOf_i1) |
| [item 2](#spatial_oneOf_i2)   |
| [item 3](#spatial_oneOf_i3)   |

### <a name="spatial_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="spatial_oneOf_i1"></a>Property `Location`

**Title:** Location

inline description of Location

|                           |                                                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                                                                         |
| **Same definition as**    | [Location](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

### <a name="spatial_oneOf_i2"></a>Property `item 2`

reference iri of Location

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

### <a name="spatial_oneOf_i3"></a>Property `item 3`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 3 items](#spatial_oneOf_i3_items) | -           |

#### <a name="spatial_oneOf_i3_items"></a>item 3 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_oneOf_i3_items_oneOf_i0) |
| [item 1](#spatial_oneOf_i3_items_oneOf_i1)   |

##### <a name="spatial_oneOf_i3_items_oneOf_i0"></a>Property `Location`

**Title:** Location

inline description of Location

|                           |                                                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                                                                         |
| **Same definition as**    | [Location](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_oneOf_i3_items_oneOf_i1"></a>Property `item 1`

reference iri of Location

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="subject"></a>Property `subject`

**Title:** subject

List of primary subjects of the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#subject_anyOf_i0) |
| [item 1](#subject_anyOf_i1) |

### <a name="subject_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="subject_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#subject_anyOf_i1_items) | -           |

#### <a name="subject_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                              |
| ------------------------------------------- |
| [Concept](#subject_anyOf_i1_items_oneOf_i0) |
| [item 1](#subject_anyOf_i1_items_oneOf_i1)  |

##### <a name="subject_anyOf_i1_items_oneOf_i0"></a>Property `Concept`

**Title:** Concept

inline description of Concept

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="subject_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `temporal`

**Title:** temporal coverage

List of temporal periods that the dataset covers

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

|                           |                                                                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of PeriodOfTime

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `title`

**Title:** title

A name given to the Dataset

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="category"></a>Property `category`

**Title:** category

List of categories of the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#category_anyOf_i0) |
| [item 1](#category_anyOf_i1) |

### <a name="category_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="category_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#category_anyOf_i1_items) | -           |

#### <a name="category_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Concept](#category_anyOf_i1_items_oneOf_i0) |
| [item 1](#category_anyOf_i1_items_oneOf_i1)  |

##### <a name="category_anyOf_i1_items_oneOf_i0"></a>Property `Concept`

**Title:** Concept

inline description of Concept

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | Any type allowed                                                            |
| **Same definition as**    | [Concept](#sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="category_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="hasQualityMeasurement"></a>Property `hasQualityMeasurement`

**Title:** quality measurement

List of quality measurements for the dataset

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
| **Same definition as**    | [QualityMeasurement](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

##### <a name="hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of QualityMeasurement

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="page"></a>Property `page`

**Title:** documentation

List of pages or documents about this dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)           |
| ------------------------ |
| [item 0](#page_anyOf_i0) |
| [item 1](#page_anyOf_i1) |

### <a name="page_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="page_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be      | Description |
| ------------------------------------ | ----------- |
| [item 1 items](#page_anyOf_i1_items) | -           |

#### <a name="page_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [Document](#page_anyOf_i1_items_oneOf_i0) |
| [item 1](#page_anyOf_i1_items_oneOf_i1)   |

##### <a name="page_anyOf_i1_items_oneOf_i0"></a>Property `Document`

**Title:** Document

inline description of Document

|                           |                                                                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                     |
| **Additional properties** | Any type allowed                                                                                                                             |
| **Same definition as**    | [Document](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_landingPage_oneOf_i1) |

##### <a name="page_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Document

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `qualifiedAttribution`

**Title:** qualified attribution

List of agents having some form of responsibility for the dataset

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
| **Same definition as**    | [Attribution](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Attribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="wasAttributedTo"></a>Property `wasAttributedTo`

**Title:** attribution

List of agents attributed to this dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#wasAttributedTo_anyOf_i0) |
| [item 1](#wasAttributedTo_anyOf_i1) |

### <a name="wasAttributedTo_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="wasAttributedTo_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [item 1 items](#wasAttributedTo_anyOf_i1_items) | -           |

#### <a name="wasAttributedTo_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                     |
| -------------------------------------------------- |
| [Agent](#wasAttributedTo_anyOf_i1_items_oneOf_i0)  |
| [item 1](#wasAttributedTo_anyOf_i1_items_oneOf_i1) |

##### <a name="wasAttributedTo_anyOf_i1_items_oneOf_i0"></a>Property `Agent`

**Title:** Agent

inline description of Agent

|                           |                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                                                         |
| **Same definition as**    | [Agent](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

##### <a name="wasAttributedTo_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Agent

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="wasGeneratedBy"></a>Property `wasGeneratedBy`

**Title:** was generated by

List of activities that generated, or provide the business context for the creation of the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                     |
| ---------------------------------- |
| [item 0](#wasGeneratedBy_anyOf_i0) |
| [item 1](#wasGeneratedBy_anyOf_i1) |

### <a name="wasGeneratedBy_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="wasGeneratedBy_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [item 1 items](#wasGeneratedBy_anyOf_i1_items) | -           |

#### <a name="wasGeneratedBy_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                      |
| --------------------------------------------------- |
| [Activity](#wasGeneratedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#wasGeneratedBy_anyOf_i1_items_oneOf_i1)   |

##### <a name="wasGeneratedBy_anyOf_i1_items_oneOf_i0"></a>Property `Activity`

**Title:** Activity

inline description of Activity

|                           |                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                                               |
| **Same definition as**    | [Activity](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i0) |

##### <a name="wasGeneratedBy_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Activity

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="wasUsedBy"></a>Property `wasUsedBy`

**Title:** used by

List of activities that used the Dataset

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

|                           |                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                                               |
| **Same definition as**    | [Activity](#sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i0) |

##### <a name="wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Activity

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="image"></a>Property `image`

**Title:** image

Link to a thumbnail picture illustrating the content of the dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)            |
| ------------------------- |
| [item 0](#image_anyOf_i0) |
| [item 1](#image_anyOf_i1) |

### <a name="image_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="image_anyOf_i1"></a>Property `item 1`

The link to the image

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="scopeNote"></a>Property `scopeNote`

**Title:** usage note

usage note for the dataset

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="scopeNoteMap"></a>Property `scopeNoteMap`

Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

