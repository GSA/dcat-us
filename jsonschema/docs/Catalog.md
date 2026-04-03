

**Title:** DCAT-US 3 Catalog

The main item defined by DCAT-US 3 is the Catalog class

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                         | Type                    | Title/Description                                                                   |
| ------------------------------------------------ | ----------------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                   | string                  | -                                                                                   |
| - [@type](#@type )                               | string                  | -                                                                                   |
| - [catalog](#catalog )                           | null or array           | Related catalogs                                                                    |
| - [contactPoint](#contactPoint )                 | null or array           | Contact points                                                                      |
| + [dataset](#dataset )                           | array                   | dataset                                                                             |
| - [keyword](#keyword )                           | null or array of string | keyword/tag                                                                         |
| - [keywordMap](#keywordMap )                     | null or object          | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [record](#record )                             | null or array           | catalog record                                                                      |
| - [service](#service )                           | null or array           | service                                                                             |
| - [theme](#theme )                               | null or array           | theme/category                                                                      |
| - [themeTaxonomy](#themeTaxonomy )               | null or array           | themes                                                                              |
| - [accessRights](#accessRights )                 | More than one type      | access rights                                                                       |
| - [conformsTo](#conformsTo )                     | More than one type      | schema version                                                                      |
| - [creator](#creator )                           | null or array           | creator                                                                             |
| - [description](#description )                   | null or string          | description                                                                         |
| - [descriptionMap](#descriptionMap )             | null or object          | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#hasPart )                           | null or array           | has part                                                                            |
| - [identifier](#identifier )                     | More than one type      | identifier                                                                          |
| - [otherIdentifier](#otherIdentifier )           | null or array           | other identifier                                                                    |
| - [issued](#issued )                             | More than one type      | release date                                                                        |
| - [language](#language )                         | More than one type      | language                                                                            |
| - [license](#license )                           | More than one type      | license                                                                             |
| - [modified](#modified )                         | More than one type      | update/modification date                                                            |
| - [publisher](#publisher )                       | More than one type      | publisher                                                                           |
| - [rights](#rights )                             | null or array           | rights                                                                              |
| - [rightsHolder](#rightsHolder )                 | null or array           | rights holder                                                                       |
| - [spatial](#spatial )                           | null or array           | spatial/geographic coverage                                                         |
| - [subject](#subject )                           | null or array           | subject                                                                             |
| - [temporal](#temporal )                         | null or array           | temporal coverage                                                                   |
| - [title](#title )                               | null or string          | title                                                                               |
| - [titleMap](#titleMap )                         | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                         | null or array           | category                                                                            |
| - [homepage](#homepage )                         | More than one type      | homepage                                                                            |
| - [qualifiedAttribution](#qualifiedAttribution ) | null or array           | qualified attribution                                                               |

## <a name="@id"></a>Property `DCAT-US 3 Catalog > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `DCAT-US 3 Catalog > @type`

| **Type**    | `string`    |
| ----------- | ----------- |
| **Default** | `"Catalog"` |

## <a name="catalog"></a>Property `DCAT-US 3 Catalog > catalog`

**Title:** Related catalogs

List of related catalogs whose contents are of interest in the context of this catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [Catalog or a link](#catalog_items) | -           |

### <a name="catalog_items"></a>DCAT-US 3 Catalog > catalog > Catalog or a link

**Title:** Catalog or a link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [catalog](#catalog_items_anyOf_i0) |
| [Link](#catalog_items_anyOf_i1)    |

#### <a name="catalog_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > catalog > Catalog or a link > anyOf > catalog`

inline description of Catalog

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Catalog](./Catalog.md) |

#### <a name="catalog_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > catalog > Catalog or a link > anyOf > Link`

**Title:** Link

reference iri of Catalog

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="contactPoint"></a>Property `DCAT-US 3 Catalog > contactPoint`

**Title:** Contact points

Contact information that can be used for sending comments about the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [Contact point or a link](#contactPoint_items) | -           |

### <a name="contactPoint_items"></a>DCAT-US 3 Catalog > contactPoint > Contact point or a link

**Title:** Contact point or a link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                       |
| ------------------------------------ |
| [Kind](#contactPoint_items_anyOf_i0) |
| [Link](#contactPoint_items_anyOf_i1) |

#### <a name="contactPoint_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > contactPoint > Contact point or a link > anyOf > Kind`

**Title:** Kind

inline value for contact point

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

#### <a name="contactPoint_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > contactPoint > Contact point or a link > anyOf > Link`

**Title:** Link

reference iri of contact point

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="dataset"></a>Property `DCAT-US 3 Catalog > dataset`

**Title:** dataset

List of Datasets that are part of the Catalog

| **Type**     | `array` |
| ------------ | ------- |
| **Required** | Yes     |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [dataset items](#dataset_items) | -           |

### <a name="dataset_items"></a>DCAT-US 3 Catalog > dataset > dataset items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [Dataset](#dataset_items_anyOf_i0) |
| [Link](#dataset_items_anyOf_i1)    |

#### <a name="dataset_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > anyOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

#### <a name="dataset_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > anyOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="keyword"></a>Property `DCAT-US 3 Catalog > keyword`

**Title:** keyword/tag

List of keywords or tags describing the Catalog

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [keyword items](#keyword_items) | -           |

### <a name="keyword_items"></a>DCAT-US 3 Catalog > keyword > keyword items

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="keywordMap"></a>Property `DCAT-US 3 Catalog > keywordMap`

Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="record"></a>Property `DCAT-US 3 Catalog > record`

**Title:** catalog record

A record describing a single resource (e.g., a dataset, a data service) that is part of the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [record items](#record_items)   | -           |

### <a name="record_items"></a>DCAT-US 3 Catalog > record > record items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                          |
| --------------------------------------- |
| [CatalogRecord](#record_items_anyOf_i0) |
| [Link](#record_items_anyOf_i1)          |

#### <a name="record_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > record > record items > anyOf > CatalogRecord`

**Title:** CatalogRecord

inline description of the record

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Catalogrecord](./Catalogrecord.md) |

#### <a name="record_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > record > record items > anyOf > Link`

**Title:** Link

reference iri of the record

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="service"></a>Property `DCAT-US 3 Catalog > service`

**Title:** service

List of data services that are listed in the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [service items](#service_items) | -           |

### <a name="service_items"></a>DCAT-US 3 Catalog > service > service items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [DataService](#service_items_anyOf_i0) |
| [Link](#service_items_anyOf_i1)        |

#### <a name="service_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > service > service items > anyOf > DataService`

**Title:** DataService

inline description of the service

| **Type**                  | `object`                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [DataService](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0) |

#### <a name="service_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > service > service items > anyOf > Link`

**Title:** Link

reference iri of the service

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="theme"></a>Property `DCAT-US 3 Catalog > theme`

**Title:** theme/category

A list of categories for the Catalog. A Catalog may be associated with multiple themes

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [theme items](#theme_items)     | -           |

### <a name="theme_items"></a>DCAT-US 3 Catalog > theme > theme items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [Concept](#theme_items_anyOf_i0) |
| [Link](#theme_items_anyOf_i1)    |

#### <a name="theme_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > theme > theme items > anyOf > Concept`

**Title:** Concept

inline description of the theme

| **Type**                  | `object`                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [Concept](#dataset_items_anyOf_i0_sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

#### <a name="theme_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > theme > theme items > anyOf > Link`

**Title:** Link

reference iri of the theme

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="themeTaxonomy"></a>Property `DCAT-US 3 Catalog > themeTaxonomy`

**Title:** themes

A knowledge organization system (KOS) used to classify the resources documented in the catalog (e.g., datasets and services)

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [themeTaxonomy items](#themeTaxonomy_items) | -           |

### <a name="themeTaxonomy_items"></a>DCAT-US 3 Catalog > themeTaxonomy > themeTaxonomy items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                 |
| ---------------------------------------------- |
| [ConceptScheme](#themeTaxonomy_items_anyOf_i0) |
| [Link](#themeTaxonomy_items_anyOf_i1)          |

#### <a name="themeTaxonomy_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > themeTaxonomy items > anyOf > ConceptScheme`

**Title:** ConceptScheme

inline description of ConceptScheme

| **Type**                  | `object`                                                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                  |
| **Same definition as**    | [ConceptScheme](#dataset_items_anyOf_i0_sample_items_anyOf_i0_representationTechnique_anyOf_i1_inScheme_anyOf_i0) |

#### <a name="themeTaxonomy_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > themeTaxonomy items > anyOf > Link`

**Title:** Link

reference iri of ConceptScheme

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="accessRights"></a>Property `DCAT-US 3 Catalog > accessRights`

**Title:** access rights

Information that indicates whether the Catalog is open data, has access restrictions or is not public

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_anyOf_i0) |
| [item 1](#accessRights_anyOf_i1)                         |
| [Link](#accessRights_anyOf_i2)                           |

### <a name="accessRights_anyOf_i0"></a>Property `DCAT-US 3 Catalog > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `DCAT-US 3 Catalog > accessRights > anyOf > item 1`

Text description of the access rights

| **Type** | `string` |
| -------- | -------- |

### <a name="accessRights_anyOf_i2"></a>Property `DCAT-US 3 Catalog > accessRights > anyOf > Link`

**Title:** Link

reference iri of the access rights

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `DCAT-US 3 Catalog > conformsTo`

**Title:** schema version

An established standard to which the described catalog conforms

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#conformsTo_anyOf_i0) |
| [Standard](#conformsTo_anyOf_i1)                       |
| [Link](#conformsTo_anyOf_i2)                           |

### <a name="conformsTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > conformsTo > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="conformsTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > conformsTo > anyOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                 |
| **Same definition as**    | [Standard](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0_conformsTo_items_anyOf_i0) |

### <a name="conformsTo_anyOf_i2"></a>Property `DCAT-US 3 Catalog > conformsTo > anyOf > Link`

**Title:** Link

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="creator"></a>Property `DCAT-US 3 Catalog > creator`

**Title:** creator

The entity responsible for creating the resource

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [creator items](#creator_items) | -           |

### <a name="creator_items"></a>DCAT-US 3 Catalog > creator > creator items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [Agent](#creator_items_anyOf_i0) |
| [Link](#creator_items_anyOf_i1)  |

#### <a name="creator_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > creator > creator items > anyOf > Agent`

**Title:** Agent

inline description of creator

| **Type**                  | `object`                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                           |
| **Same definition as**    | [Agent](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0_creator_items_anyOf_i0) |

#### <a name="creator_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > creator > creator items > anyOf > Link`

**Title:** Link

reference iri of creator

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="description"></a>Property `DCAT-US 3 Catalog > description`

**Title:** description

Free-text description of the catalog (in the language indicated in the language property)

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="descriptionMap"></a>Property `DCAT-US 3 Catalog > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="hasPart"></a>Property `DCAT-US 3 Catalog > hasPart`

**Title:** has part

A list of related catalogs that are part of the described catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [hasPart items](#hasPart_items) | -           |

### <a name="hasPart_items"></a>DCAT-US 3 Catalog > hasPart > hasPart items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [DCAT-US 3 Catalog](#hasPart_items_anyOf_i0) |
| [Link](#hasPart_items_anyOf_i1)              |

#### <a name="hasPart_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > hasPart > hasPart items > anyOf > DCAT-US 3 Catalog`

**Title:** DCAT-US 3 Catalog

inline description of the related catalog

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

#### <a name="hasPart_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > hasPart > hasPart items > anyOf > Link`

**Title:** Link

reference iri of the related catalog

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `DCAT-US 3 Catalog > identifier`

**Title:** identifier

The unique identifier for the Catalog, e.g. the URI or other unique identifier

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#identifier_anyOf_i0) |
| [Identifier](#identifier_anyOf_i1)                     |
| [Link](#identifier_anyOf_i2)                           |

### <a name="identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                                   |
| ------------------------- | -------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                     |
| **Same definition as**    | [Identifier](#dataset_items_anyOf_i0_otherIdentifier_items_anyOf_i0) |

### <a name="identifier_anyOf_i2"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="otherIdentifier"></a>Property `DCAT-US 3 Catalog > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Catalog besides the main identifier, e.g. the URI or other unique identifiers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [otherIdentifier items](#otherIdentifier_items) | -           |

### <a name="otherIdentifier_items"></a>DCAT-US 3 Catalog > otherIdentifier > otherIdentifier items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                |
| --------------------------------------------- |
| [Identifier](#otherIdentifier_items_anyOf_i0) |
| [Link](#otherIdentifier_items_anyOf_i1)       |

#### <a name="otherIdentifier_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > otherIdentifier > otherIdentifier items > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                                   |
| ------------------------- | -------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                     |
| **Same definition as**    | [Identifier](#dataset_items_anyOf_i0_otherIdentifier_items_anyOf_i0) |

#### <a name="otherIdentifier_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > otherIdentifier > otherIdentifier items > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="issued"></a>Property `DCAT-US 3 Catalog > issued`

**Title:** release date

Date of formal issuance (e.g., publication) of the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string`

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

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `DCAT-US 3 Catalog > language`

**Title:** language

Language or languages used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalog. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#language_anyOf_i0) |
| [Language code](#language_anyOf_i1)                  |
| [List of language codes](#language_anyOf_i2)         |

### <a name="language_anyOf_i0"></a>Property `DCAT-US 3 Catalog > language > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="language_anyOf_i1"></a>Property `DCAT-US 3 Catalog > language > anyOf > Language code`

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `DCAT-US 3 Catalog > language > anyOf > List of language codes`

**Title:** List of language codes

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Language code](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>DCAT-US 3 Catalog > language > anyOf > List of language codes > Language code

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="license"></a>Property `DCAT-US 3 Catalog > license`

**Title:** license

The license under which the Catalog is made available; see https://resources.data.gov/schemas/dcat-us/open-licenses for more information regarding license-free declarations and licenses

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#license_anyOf_i0) |
| [item 1](#license_anyOf_i1)                         |
| [Link](#license_anyOf_i2)                           |

### <a name="license_anyOf_i0"></a>Property `DCAT-US 3 Catalog > license > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="license_anyOf_i1"></a>Property `DCAT-US 3 Catalog > license > anyOf > item 1`

Full text of the license

| **Type** | `string` |
| -------- | -------- |

### <a name="license_anyOf_i2"></a>Property `DCAT-US 3 Catalog > license > anyOf > Link`

**Title:** Link

reference iri of the license

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="modified"></a>Property `DCAT-US 3 Catalog > modified`

**Title:** update/modification date

Most recent date on which the catalog was changed, updated or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string`

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

#### <a name="modified_anyOf_i1_anyOf_i0"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `DCAT-US 3 Catalog > publisher`

**Title:** publisher

Agent responsible for making the catalog available

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#publisher_anyOf_i0) |
| [Agent](#publisher_anyOf_i1)                          |
| [Link](#publisher_anyOf_i2)                           |

### <a name="publisher_anyOf_i0"></a>Property `DCAT-US 3 Catalog > publisher > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="publisher_anyOf_i1"></a>Property `DCAT-US 3 Catalog > publisher > anyOf > Agent`

**Title:** Agent

inline description of the publisher

| **Type**                  | `object`                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                           |
| **Same definition as**    | [Agent](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0_creator_items_anyOf_i0) |

### <a name="publisher_anyOf_i2"></a>Property `DCAT-US 3 Catalog > publisher > anyOf > Link`

**Title:** Link

reference iri of the publisher

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rights"></a>Property `DCAT-US 3 Catalog > rights`

**Title:** rights

A list of statements concerning all rights for the Catalog that may not be addressed by license or accessRights, such as copyright statements, statements about the intellectual property rights (IPR), or information regarding access or restrictions based on privacy, security, or other policies

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [Rights statement text or link](#rights_items) | -           |

### <a name="rights_items"></a>DCAT-US 3 Catalog > rights > Rights statement text or link

**Title:** Rights statement text or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#rights_items_anyOf_i0) |
| [Link](#rights_items_anyOf_i1)   |

#### <a name="rights_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > rights > Rights statement text or link > anyOf > item 0`

Full text of a statement of rights

| **Type** | `string` |
| -------- | -------- |

#### <a name="rights_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > rights > Rights statement text or link > anyOf > Link`

**Title:** Link

reference iri of a statement of rights

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `DCAT-US 3 Catalog > rightsHolder`

**Title:** rights holder

List of organizations holding rights on the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [rightsHolder items](#rightsHolder_items) | -           |

### <a name="rightsHolder_items"></a>DCAT-US 3 Catalog > rightsHolder > rightsHolder items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [Organization](#rightsHolder_items_anyOf_i0) |
| [Link](#rightsHolder_items_anyOf_i1)         |

#### <a name="rightsHolder_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > rightsHolder > rightsHolder items > anyOf > Organization`

**Title:** Organization

inline description of rights holder

| **Type**                  | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_anyOf_i0_otherIdentifier_items_anyOf_i0_anyOf_i1_creator_anyOf_i1) |

#### <a name="rightsHolder_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > rightsHolder > rightsHolder items > anyOf > Link`

**Title:** Link

reference iri of rights holder

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `DCAT-US 3 Catalog > spatial`

**Title:** spatial/geographic coverage

The geographical area covered by the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [spatial items](#spatial_items) | -           |

### <a name="spatial_items"></a>DCAT-US 3 Catalog > spatial > spatial items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Location](#spatial_items_anyOf_i0) |
| [Link](#spatial_items_anyOf_i1)     |

#### <a name="spatial_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > spatial > spatial items > anyOf > Location`

**Title:** Location

inline description of geographical coverage

| **Type**                  | `object`                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                              |
| **Same definition as**    | [Location](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0_spatial_items_anyOf_i0) |

#### <a name="spatial_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > spatial > spatial items > anyOf > Link`

**Title:** Link

reference iri of geographical coverage

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="subject"></a>Property `DCAT-US 3 Catalog > subject`

**Title:** subject

List of subjects of the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [subject items](#subject_items) | -           |

### <a name="subject_items"></a>DCAT-US 3 Catalog > subject > subject items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [Concept](#subject_items_anyOf_i0) |
| [Link](#subject_items_anyOf_i1)    |

#### <a name="subject_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > subject > subject items > anyOf > Concept`

**Title:** Concept

inline description of the subject

| **Type**                  | `object`                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [Concept](#dataset_items_anyOf_i0_sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

#### <a name="subject_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > subject > subject items > anyOf > Link`

**Title:** Link

reference iri of the subject

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `DCAT-US 3 Catalog > temporal`

**Title:** temporal coverage

List of temporal periods that the Catalog covers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be   | Description |
| --------------------------------- | ----------- |
| [temporal items](#temporal_items) | -           |

### <a name="temporal_items"></a>DCAT-US 3 Catalog > temporal > temporal items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                           |
| ---------------------------------------- |
| [PeriodOfTime](#temporal_items_anyOf_i0) |
| [Link](#temporal_items_anyOf_i1)         |

#### <a name="temporal_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > temporal > temporal items > anyOf > PeriodOfTime`

**Title:** PeriodOfTime

inline description of the temporal coverage

| **Type**                  | `object`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                                   |
| **Same definition as**    | [PeriodOfTime](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0_temporal_items_anyOf_i0) |

#### <a name="temporal_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > temporal > temporal items > anyOf > Link`

**Title:** Link

reference iri of the temporal coverage

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="title"></a>Property `DCAT-US 3 Catalog > title`

**Title:** title

The title of the catalog in the indicated language

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="titleMap"></a>Property `DCAT-US 3 Catalog > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="category"></a>Property `DCAT-US 3 Catalog > category`

**Title:** category

List of categories for the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be   | Description |
| --------------------------------- | ----------- |
| [category items](#category_items) | -           |

### <a name="category_items"></a>DCAT-US 3 Catalog > category > category items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Concept](#category_items_anyOf_i0) |
| [Link](#category_items_anyOf_i1)    |

#### <a name="category_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > category > category items > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [Concept](#dataset_items_anyOf_i0_sample_items_anyOf_i0_representationTechnique_anyOf_i1) |

#### <a name="category_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > category > category items > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="homepage"></a>Property `DCAT-US 3 Catalog > homepage`

**Title:** homepage

The home page of the catalog (a public Web document usually available in HTML)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#homepage_anyOf_i0) |
| [Document](#homepage_anyOf_i1)                       |
| [Link](#homepage_anyOf_i2)                           |

### <a name="homepage_anyOf_i0"></a>Property `DCAT-US 3 Catalog > homepage > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="homepage_anyOf_i1"></a>Property `DCAT-US 3 Catalog > homepage > anyOf > Document`

**Title:** Document

inline description of the home page

| **Type**                  | `object`                                                                      |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [Document](#dataset_items_anyOf_i0_sample_items_anyOf_i0_page_items_anyOf_i0) |

### <a name="homepage_anyOf_i2"></a>Property `DCAT-US 3 Catalog > homepage > anyOf > Link`

**Title:** Link

reference iri of the home page

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution`

**Title:** qualified attribution

A list of agents having some form of responsibility for the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [qualifiedAttribution items](#qualifiedAttribution_items) | -           |

### <a name="qualifiedAttribution_items"></a>DCAT-US 3 Catalog > qualifiedAttribution > qualifiedAttribution items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Attribution](#qualifiedAttribution_items_anyOf_i0) |
| [Link](#qualifiedAttribution_items_anyOf_i1)        |

#### <a name="qualifiedAttribution_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > qualifiedAttribution items > anyOf > Attribution`

**Title:** Attribution

inline description of Attribution

| **Type**                  | `object`                                                                                                                      |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Attribution](#dataset_items_anyOf_i0_sample_items_anyOf_i0_accessService_items_anyOf_i0_qualifiedAttribution_items_anyOf_i0) |

#### <a name="qualifiedAttribution_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > qualifiedAttribution items > anyOf > Link`

**Title:** Link

reference iri of Attribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

