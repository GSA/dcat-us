

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                                   | Type                    | Title/Description           |
| ---------------------------------------------------------- | ----------------------- | --------------------------- |
| - [@id](#@id )                                             | string                  | -                           |
| - [@type](#@type )                                         | string                  | -                           |
| - [otherIdentifier](#otherIdentifier )                     | null or array           | other identifier            |
| - [sample](#sample )                                       | null or array           | sample                      |
| - [status](#status )                                       | More than one type      | lifecycle status            |
| - [supportedSchema](#supportedSchema )                     | More than one type      | supported schema            |
| - [versionNotes](#versionNotes )                           | null or string          | version notes               |
| + [contactPoint](#contactPoint )                           | More than one type      | contact point               |
| - [distribution](#distribution )                           | null or array           | dataset distribution        |
| - [first](#first )                                         | More than one type      | first                       |
| - [hasCurrentVersion](#hasCurrentVersion )                 | More than one type      | current version             |
| - [hasVersion](#hasVersion )                               | null or array           | has version                 |
| - [inSeries](#inSeries )                                   | null or array           | in series                   |
| - [keyword](#keyword )                                     | null or array of string | keyword/tag                 |
| - [landingPage](#landingPage )                             | More than one type      | landing page                |
| - [previousVersion](#previousVersion )                     | More than one type      | previous version            |
| - [qualifiedRelation](#qualifiedRelation )                 | null or array           | qualified relation          |
| - [spatialResolutionInMeters](#spatialResolutionInMeters ) | null or string          | Spatial resolution (meters) |
| - [temporalResolution](#temporalResolution )               | null or string          | temporal resolution         |
| - [theme](#theme )                                         | null or array           | theme/category              |
| - [version](#version )                                     | null or string          | version                     |
| - [describedBy](#describedBy )                             | More than one type      | data dictionary             |
| - [liabilityStatement](#liabilityStatement )               | More than one type      | liability statement         |
| - [metadataDistribution](#metadataDistribution )           | null or array           | metadata distribution       |
| - [purpose](#purpose )                                     | null or string          | purpose                     |
| - [accessRights](#accessRights )                           | More than one type      | access rights               |
| - [accrualPeriodicity](#accrualPeriodicity )               | More than one type      | frequency                   |
| - [conformsTo](#conformsTo )                               | null or array           | conforms to                 |
| - [contributor](#contributor )                             | null or array           | contributor                 |
| - [created](#created )                                     | More than one type      | creation date               |
| - [creator](#creator )                                     | More than one type      | creator                     |
| + [description](#description )                             | string                  | description                 |
| - [hasPart](#hasPart )                                     | null or array           | has part                    |
| - [identifier](#identifier )                               | More than one type      | identifier                  |
| - [isReferencedBy](#isReferencedBy )                       | null or array of string | is referenced by            |
| - [issued](#issued )                                       | More than one type      | release date                |
| - [language](#language )                                   | More than one type      | language                    |
| - [modified](#modified )                                   | More than one type      | last modified               |
| - [provenance](#provenance )                               | null or array of string | provenance                  |
| + [publisher](#publisher )                                 | object                  | publisher                   |
| - [relation](#relation )                                   | null or array of string | related resource            |
| - [replaces](#replaces )                                   | null or array           | replaces                    |
| - [rights](#rights )                                       | null or array of string | rights                      |
| - [rightsHolder](#rightsHolder )                           | null or array           | rights holder               |
| - [source](#source )                                       | null or array           | data source                 |
| - [spatial](#spatial )                                     | More than one type      | spatial/geographic coverage |
| - [subject](#subject )                                     | null or array           | subject                     |
| - [temporal](#temporal )                                   | null or array           | temporal coverage           |
| + [title](#title )                                         | string                  | title                       |
| - [category](#category )                                   | null or array           | category                    |
| - [hasQualityMeasurement](#hasQualityMeasurement )         | null or array           | quality measurement         |
| - [page](#page )                                           | null or array           | documentation               |
| - [qualifiedAttribution](#qualifiedAttribution )           | null or array           | qualified attribution       |
| - [wasAttributedTo](#wasAttributedTo )                     | null or array           | attribution                 |
| - [wasGeneratedBy](#wasGeneratedBy )                       | null or array           | was generated by            |
| - [wasUsedBy](#wasUsedBy )                                 | null or array           | used by                     |
| - [image](#image )                                         | More than one type      | image                       |
| - [scopeNote](#scopeNote )                                 | null or string          | usage note                  |

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

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>Dataset > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type            |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Defined in**            | [Identifier](./Identifier.md) |

## <a name="sample"></a>Property `Dataset > sample`

**Title:** sample

List of links to samples of a Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                         |
| ------------------------------- | ----------------------------------- |
| [Distribution](#sample_items)   | A file that distributes the dataset |

### <a name="sample_items"></a>Dataset > sample > Distribution

**Title:** Distribution

A file that distributes the dataset

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Distribution](./Distribution.md) |

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

### <a name="status_anyOf_i0"></a>Property `Dataset > status > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_anyOf_i1"></a>Property `Dataset > status > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type                                        |
| ------------------------- | --------------------------------------------------------- |
| **Additional properties** | Any type allowed                                          |
| **Same definition as**    | [Concept](#sample_items_representationTechnique_anyOf_i1) |

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

### <a name="supportedSchema_anyOf_i0"></a>Property `Dataset > supportedSchema > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="supportedSchema_anyOf_i1"></a>Property `Dataset > supportedSchema > anyOf > Dataset`

**Title:** Dataset

inline description of the supported schema

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

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
| [List of contacts](#contactPoint_anyOf_i1) |

### <a name="contactPoint_anyOf_i0"></a>Property `Dataset > contactPoint > anyOf > Kind`

**Title:** Kind

inline description of Kind

| **Type**                  | `object`                                                     |
| ------------------------- | ------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                             |
| **Same definition as**    | [Kind](#sample_items_accessService_items_contactPoint_items) |

### <a name="contactPoint_anyOf_i1"></a>Property `Dataset > contactPoint > anyOf > List of contacts`

**Title:** List of contacts

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be      | Description                                     |
| ------------------------------------ | ----------------------------------------------- |
| [Kind](#contactPoint_anyOf_i1_items) | Contact information for an individual or entity |

#### <a name="contactPoint_anyOf_i1_items"></a>Dataset > contactPoint > anyOf > List of contacts > Kind

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`                                                     |
| ------------------------- | ------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                             |
| **Same definition as**    | [Kind](#sample_items_accessService_items_contactPoint_items) |

## <a name="distribution"></a>Property `Dataset > distribution`

**Title:** dataset distribution

List of available distributions for the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description                         |
| ----------------------------------- | ----------------------------------- |
| [Distribution](#distribution_items) | A file that distributes the dataset |

### <a name="distribution_items"></a>Dataset > distribution > Distribution

**Title:** Distribution

A file that distributes the dataset

| **Type**                  | `object`                      |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Same definition as**    | [Distribution](#sample_items) |

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

### <a name="first_anyOf_i0"></a>Property `Dataset > first > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="first_anyOf_i1"></a>Property `Dataset > first > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

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

### <a name="hasCurrentVersion_anyOf_i0"></a>Property `Dataset > hasCurrentVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasCurrentVersion_anyOf_i1"></a>Property `Dataset > hasCurrentVersion > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

## <a name="hasVersion"></a>Property `Dataset > hasVersion`

**Title:** has version

List of related Datasets that are a version, edition, or adaptation of the described Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#hasVersion_items)    | Information about a set of data |

### <a name="hasVersion_items"></a>Dataset > hasVersion > Dataset

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

## <a name="inSeries"></a>Property `Dataset > inSeries`

**Title:** in series

List of Dataset Series this dataset belongs to

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be  | Description                   |
| -------------------------------- | ----------------------------- |
| [DatasetSeries](#inSeries_items) | An ordered series of datasets |

### <a name="inSeries_items"></a>Dataset > inSeries > DatasetSeries

**Title:** DatasetSeries

An ordered series of datasets

| **Type**                  | `object`                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                      |
| **Same definition as**    | [DatasetSeries](#sample_items_accessService_items_servesDataset_items_inSeries_items) |

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

### <a name="landingPage_anyOf_i0"></a>Property `Dataset > landingPage > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="landingPage_anyOf_i1"></a>Property `Dataset > landingPage > anyOf > Document`

**Title:** Document

inline description of Document

| **Type**                  | `object`                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                       |
| **Same definition as**    | [Document](#sample_items_accessService_items_servesDataset_items_landingPage_anyOf_i1) |

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

### <a name="previousVersion_anyOf_i0"></a>Property `Dataset > previousVersion > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="previousVersion_anyOf_i1"></a>Property `Dataset > previousVersion > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

## <a name="qualifiedRelation"></a>Property `Dataset > qualifiedRelation`

**Title:** qualified relation

Qualified relationship with role of the dataset with another resource

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be          | Description                                                                                                    |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Relationship](#qualifiedRelation_items) | Information about an item or entity that has some relationship to a dataset and the nature of the relationship |

### <a name="qualifiedRelation_items"></a>Dataset > qualifiedRelation > Relationship

**Title:** Relationship

Information about an item or entity that has some relationship to a dataset and the nature of the relationship

| **Type**                  | `object`                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                              |
| **Same definition as**    | [Relationship](#sample_items_accessService_items_servesDataset_items_qualifiedRelation_items) |

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

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#theme_items)         | A labeled value from an optionally specified concept scheme |

### <a name="theme_items"></a>Dataset > theme > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                        |
| ------------------------- | --------------------------------------------------------- |
| **Additional properties** | Any type allowed                                          |
| **Same definition as**    | [Concept](#sample_items_representationTechnique_anyOf_i1) |

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

### <a name="describedBy_anyOf_i0"></a>Property `Dataset > describedBy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="describedBy_anyOf_i1"></a>Property `Dataset > describedBy > anyOf > Distribution`

**Title:** Distribution

inline description of Distribution

| **Type**                  | `object`                      |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Same definition as**    | [Distribution](#sample_items) |

## <a name="liabilityStatement"></a>Property `Dataset > liabilityStatement`

**Title:** liability statement

A liability statement about the dataset that may clarify limitations of responsibility, qualifications on the accuracy, reliability, and completeness of the data, or absence of endorsement by the data publisher or provider, among other considerations

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [Null allowed when not required](#liabilityStatement_anyOf_i0) |
| [item 1](#liabilityStatement_anyOf_i1)                         |

### <a name="liabilityStatement_anyOf_i0"></a>Property `Dataset > liabilityStatement > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="liabilityStatement_anyOf_i1"></a>Property `Dataset > liabilityStatement > anyOf > item 1`

Full text of the liability statement

| **Type** | `string` |
| -------- | -------- |

## <a name="metadataDistribution"></a>Property `Dataset > metadataDistribution`

**Title:** metadata distribution

Distribution to "original" metadata document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be             | Description                         |
| ------------------------------------------- | ----------------------------------- |
| [Distribution](#metadataDistribution_items) | A file that distributes the dataset |

### <a name="metadataDistribution_items"></a>Dataset > metadataDistribution > Distribution

**Title:** Distribution

A file that distributes the dataset

| **Type**                  | `object`                      |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Same definition as**    | [Distribution](#sample_items) |

## <a name="purpose"></a>Property `Dataset > purpose`

**Title:** purpose

The purpose of the dataset

| **Type** | `null or string` |
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
| [item 1](#accessRights_anyOf_i1)                         |

### <a name="accessRights_anyOf_i0"></a>Property `Dataset > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `Dataset > accessRights > anyOf > item 1`

Text description of the access rights

| **Type** | `string` |
| -------- | -------- |

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

| Each item of this array must be | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| [Standard](#conformsTo_items)   | Information about a particular standard that another item conforms to |

### <a name="conformsTo_items"></a>Dataset > conformsTo > Standard

**Title:** Standard

Information about a particular standard that another item conforms to

| **Type**                  | `object`                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [Standard](#sample_items_accessService_items_servesDataset_items_landingPage_anyOf_i1_conformsTo_items) |

## <a name="contributor"></a>Property `Dataset > contributor`

**Title:** contributor

List of agents contributing to the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Agent](#contributor_items)     | An entity that could be involved with a resource |

### <a name="contributor_items"></a>Dataset > contributor > Agent

**Title:** Agent

An entity that could be involved with a resource

| **Type**                  | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Agent](#sample_items_accessService_items_servesDataset_items_inSeries_items_publisher_anyOf_i1) |

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

### <a name="creator_anyOf_i0"></a>Property `Dataset > creator > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="creator_anyOf_i1"></a>Property `Dataset > creator > anyOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Agent](#sample_items_accessService_items_servesDataset_items_inSeries_items_publisher_anyOf_i1) |

## <a name="description"></a>Property `Dataset > description`

**Title:** description

A free-text account of the Dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="hasPart"></a>Property `Dataset > hasPart`

**Title:** has part

List of related datasets that are part of the described dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#hasPart_items)       | Information about a set of data |

### <a name="hasPart_items"></a>Dataset > hasPart > Dataset

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

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

### <a name="identifier_anyOf_i0"></a>Property `Dataset > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Dataset > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                   |
| ------------------------- | ------------------------------------ |
| **Additional properties** | Any type allowed                     |
| **Same definition as**    | [Identifier](#otherIdentifier_items) |

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

List of statements about the lineage of a Dataset, including any changes in its ownership or custody since its creation that may be significant for its authenticity, integrity, or interpretation

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be       | Description                           |
| ------------------------------------- | ------------------------------------- |
| [provenance items](#provenance_items) | Full text of the provenance statement |

### <a name="provenance_items"></a>Dataset > provenance > provenance items

Full text of the provenance statement

| **Type** | `string` |
| -------- | -------- |

## <a name="publisher"></a>Property `Dataset > publisher`

**Title:** publisher

An organization responsible for making the Dataset available

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Required**              | Yes                               |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Organization](./Organization.md) |

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

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#replaces_items)      | Information about a set of data |

### <a name="replaces_items"></a>Dataset > replaces > Dataset

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

## <a name="rights"></a>Property `Dataset > rights`

**Title:** rights

A list of statements concerning all rights for the Dataset that may not be addressed by license or accessRights, such as copyright statements, statements about the intellectual property rights (IPR), or information regarding access or restrictions based on privacy, security, or other policies

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description                        |
| ------------------------------- | ---------------------------------- |
| [rights items](#rights_items)   | Full text of a statement of rights |

### <a name="rights_items"></a>Dataset > rights > rights items

Full text of a statement of rights

| **Type** | `string` |
| -------- | -------- |

## <a name="rightsHolder"></a>Property `Dataset > rightsHolder`

**Title:** rights holder

List of agents (organizations) holding rights on the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description                                                                         |
| ----------------------------------- | ----------------------------------------------------------------------------------- |
| [Organization](#rightsHolder_items) | Information about an organization, including other organizations that it is part of |

### <a name="rightsHolder_items"></a>Dataset > rightsHolder > Organization

**Title:** Organization

Information about an organization, including other organizations that it is part of

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Organization](#otherIdentifier_items_anyOf_i1_creator_anyOf_i1) |

## <a name="source"></a>Property `Dataset > source`

**Title:** data source

List of related Datasets from which the described Dataset is derived

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#source_items)        | Information about a set of data |

### <a name="source_items"></a>Dataset > source > Dataset

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Dataset](#sample_items_accessService_items_servesDataset_items) |

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
| [List of geographic regions](#spatial_anyOf_i2)     |

### <a name="spatial_anyOf_i0"></a>Property `Dataset > spatial > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="spatial_anyOf_i1"></a>Property `Dataset > spatial > anyOf > Location`

**Title:** Location

inline description of Location

| **Type**                  | `object`                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                               |
| **Same definition as**    | [Location](#sample_items_accessService_items_servesDataset_items_inSeries_items_spatial_items) |

### <a name="spatial_anyOf_i2"></a>Property `Dataset > spatial > anyOf > List of geographic regions`

**Title:** List of geographic regions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be     | Description                                      |
| ----------------------------------- | ------------------------------------------------ |
| [Location](#spatial_anyOf_i2_items) | Information about a specific geographic location |

#### <a name="spatial_anyOf_i2_items"></a>Dataset > spatial > anyOf > List of geographic regions > Location

**Title:** Location

Information about a specific geographic location

| **Type**                  | `object`                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                               |
| **Same definition as**    | [Location](#sample_items_accessService_items_servesDataset_items_inSeries_items_spatial_items) |

## <a name="subject"></a>Property `Dataset > subject`

**Title:** subject

List of primary subjects of the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#subject_items)       | A labeled value from an optionally specified concept scheme |

### <a name="subject_items"></a>Dataset > subject > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                        |
| ------------------------- | --------------------------------------------------------- |
| **Additional properties** | Any type allowed                                          |
| **Same definition as**    | [Concept](#sample_items_representationTechnique_anyOf_i1) |

## <a name="temporal"></a>Property `Dataset > temporal`

**Title:** temporal coverage

List of temporal periods that the dataset covers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| [PeriodOfTime](#temporal_items) | Information about a specific time period with a start- and/or end-time |

### <a name="temporal_items"></a>Dataset > temporal > PeriodOfTime

**Title:** PeriodOfTime

Information about a specific time period with a start- and/or end-time

| **Type**                  | `object`                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                    |
| **Same definition as**    | [PeriodOfTime](#sample_items_accessService_items_servesDataset_items_inSeries_items_temporal_items) |

## <a name="title"></a>Property `Dataset > title`

**Title:** title

A name given to the Dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="category"></a>Property `Dataset > category`

**Title:** category

List of categories for the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#category_items)      | A labeled value from an optionally specified concept scheme |

### <a name="category_items"></a>Dataset > category > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                        |
| ------------------------- | --------------------------------------------------------- |
| **Additional properties** | Any type allowed                                          |
| **Same definition as**    | [Concept](#sample_items_representationTechnique_anyOf_i1) |

## <a name="hasQualityMeasurement"></a>Property `Dataset > hasQualityMeasurement`

**Title:** quality measurement

List of quality measurements for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                    | Description                        |
| -------------------------------------------------- | ---------------------------------- |
| [QualityMeasurement](#hasQualityMeasurement_items) | A single measurement of one metric |

### <a name="hasQualityMeasurement_items"></a>Dataset > hasQualityMeasurement > QualityMeasurement

**Title:** QualityMeasurement

A single measurement of one metric

| **Type**                  | `object`                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [QualityMeasurement](#sample_items_accessService_items_servesDataset_items_hasQualityMeasurement_items) |

## <a name="page"></a>Property `Dataset > page`

**Title:** documentation

List of pages or documents about this dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                       |
| ------------------------------- | --------------------------------- |
| [Document](#page_items)         | Information about a text document |

### <a name="page_items"></a>Dataset > page > Document

**Title:** Document

Information about a text document

| **Type**                  | `object`                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                       |
| **Same definition as**    | [Document](#sample_items_accessService_items_servesDataset_items_landingPage_anyOf_i1) |

## <a name="qualifiedAttribution"></a>Property `Dataset > qualifiedAttribution`

**Title:** qualified attribution

List of agents having some form of responsibility for the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be            | Description                                  |
| ------------------------------------------ | -------------------------------------------- |
| [Attribution](#qualifiedAttribution_items) | An attribution that an agent plays some role |

### <a name="qualifiedAttribution_items"></a>Dataset > qualifiedAttribution > Attribution

**Title:** Attribution

An attribution that an agent plays some role

| **Type**                  | `object`                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Attribution](#sample_items_accessService_items_servesDataset_items_qualifiedAttribution_items) |

## <a name="wasAttributedTo"></a>Property `Dataset > wasAttributedTo`

**Title:** attribution

List of agents attributed to this dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Agent](#wasAttributedTo_items) | An entity that could be involved with a resource |

### <a name="wasAttributedTo_items"></a>Dataset > wasAttributedTo > Agent

**Title:** Agent

An entity that could be involved with a resource

| **Type**                  | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Agent](#sample_items_accessService_items_servesDataset_items_inSeries_items_publisher_anyOf_i1) |

## <a name="wasGeneratedBy"></a>Property `Dataset > wasGeneratedBy`

**Title:** was generated by

List of activities that generated, or provide the business context for the creation of the dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be   | Description                                      |
| --------------------------------- | ------------------------------------------------ |
| [Activity](#wasGeneratedBy_items) | An activity which a resource could be related to |

### <a name="wasGeneratedBy_items"></a>Dataset > wasGeneratedBy > Activity

**Title:** Activity

An activity which a resource could be related to

| **Type**                  | `object`                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                       |
| **Same definition as**    | [Activity](#sample_items_accessService_items_servesDataset_items_wasGeneratedBy_items) |

## <a name="wasUsedBy"></a>Property `Dataset > wasUsedBy`

**Title:** used by

List of activities that used the Dataset

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Activity](#wasUsedBy_items)    | An activity which a resource could be related to |

### <a name="wasUsedBy_items"></a>Dataset > wasUsedBy > Activity

**Title:** Activity

An activity which a resource could be related to

| **Type**                  | `object`                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                       |
| **Same definition as**    | [Activity](#sample_items_accessService_items_servesDataset_items_wasGeneratedBy_items) |

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

