

**Title:** DCAT-US 3 Catalog

The main item defined by DCAT-US 3 is the Catalog class

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                         | Type                    | Title/Description                                                                   |
| ------------------------------------------------ | ----------------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                   | string                  | -                                                                                   |
| - [@type](#@type )                               | string                  | -                                                                                   |
| - [catalog](#catalog )                           | More than one type      | catalog                                                                             |
| - [contactPoint](#contactPoint )                 | More than one type      | contact point                                                                       |
| + [dataset](#dataset )                           | array                   | dataset                                                                             |
| - [keyword](#keyword )                           | null or array of string | keyword/tag                                                                         |
| - [keywordMap](#keywordMap )                     | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [record](#record )                             | More than one type      | catalog record                                                                      |
| - [service](#service )                           | More than one type      | service                                                                             |
| - [theme](#theme )                               | More than one type      | theme/category                                                                      |
| - [themeTaxonomy](#themeTaxonomy )               | More than one type      | themes                                                                              |
| - [accessRights](#accessRights )                 | More than one type      | access rights                                                                       |
| - [conformsTo](#conformsTo )                     | More than one type      | schema version                                                                      |
| - [creator](#creator )                           | More than one type      | creator                                                                             |
| - [description](#description )                   | null or string          | description                                                                         |
| - [descriptionMap](#descriptionMap )             | null or object          | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#hasPart )                           | More than one type      | has part                                                                            |
| - [identifier](#identifier )                     | More than one type      | identifier                                                                          |
| - [issued](#issued )                             | More than one type      | release date                                                                        |
| - [language](#language )                         | More than one type      | language                                                                            |
| - [license](#license )                           | More than one type      | license                                                                             |
| - [modified](#modified )                         | More than one type      | update/modification date                                                            |
| - [publisher](#publisher )                       | More than one type      | publisher                                                                           |
| - [rights](#rights )                             | More than one type      | rights                                                                              |
| - [rightsHolder](#rightsHolder )                 | More than one type      | rights holder                                                                       |
| - [spatial](#spatial )                           | More than one type      | spatial/geographic coverage                                                         |
| - [subject](#subject )                           | More than one type      | subject                                                                             |
| - [temporal](#temporal )                         | More than one type      | temporal coverage                                                                   |
| - [title](#title )                               | null or string          | title                                                                               |
| - [titleMap](#titleMap )                         | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                         | More than one type      | category                                                                            |
| - [homepage](#homepage )                         | More than one type      | homepage                                                                            |
| - [qualifiedAttribution](#qualifiedAttribution ) | More than one type      | qualified attribution                                                               |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |             |
| ----------- | ----------- |
| **Type**    | `string`    |
| **Default** | `"Catalog"` |

## <a name="catalog"></a>Property `catalog`

**Title:** catalog

List of related catalogs whose contents are of interest in the context of this catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#catalog_anyOf_i0) |
| [item 1](#catalog_anyOf_i1) |

### <a name="catalog_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="catalog_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#catalog_anyOf_i1_items) | -           |

#### <a name="catalog_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                              |
| ------------------------------------------- |
| [catalog](#catalog_anyOf_i1_items_oneOf_i0) |
| [item 1](#catalog_anyOf_i1_items_oneOf_i1)  |

##### <a name="catalog_anyOf_i1_items_oneOf_i0"></a>Property `catalog`

inline description of Catalog

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Catalog](./Catalog.md) |

##### <a name="catalog_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Catalog

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="contactPoint"></a>Property `contactPoint`

**Title:** contact point

Contact information that can be used for sending comments about the Catalog

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

inline value for contact point

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of contact point

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="dataset"></a>Property `dataset`

**Title:** dataset

List of Datasets that are part of the Catalog

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [dataset items](#dataset_items) | -           |

### <a name="dataset_items"></a>dataset items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                     |
| ---------------------------------- |
| [Dataset](#dataset_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i1)  |

#### <a name="dataset_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of Dataset

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

#### <a name="dataset_items_oneOf_i1"></a>Property `item 1`

reference iri of Dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="keyword"></a>Property `keyword`

**Title:** keyword/tag

A list of keywords or tags describing the resource

|          |                           |
| -------- | ------------------------- |
| **Type** | `null or array of string` |

## <a name="keywordMap"></a>Property `keywordMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="record"></a>Property `record`

**Title:** catalog record

A record describing a single resource (e.g., a dataset, a data service) that is part of the catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#record_anyOf_i0) |
| [item 1](#record_anyOf_i1) |

### <a name="record_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="record_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#record_anyOf_i1_items) | -           |

#### <a name="record_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [CatalogRecord](#record_anyOf_i1_items_oneOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i1)        |

##### <a name="record_anyOf_i1_items_oneOf_i0"></a>Property `CatalogRecord`

**Title:** CatalogRecord

inline description of the record

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Catalogrecord](./Catalogrecord.md) |

##### <a name="record_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the record

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="service"></a>Property `service`

**Title:** service

List of data services that are listed in the Catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#service_anyOf_i0) |
| [item 1](#service_anyOf_i1) |

### <a name="service_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="service_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#service_anyOf_i1_items) | -           |

#### <a name="service_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [DataService](#service_anyOf_i1_items_oneOf_i0) |
| [item 1](#service_anyOf_i1_items_oneOf_i1)      |

##### <a name="service_anyOf_i1_items_oneOf_i0"></a>Property `DataService`

**Title:** DataService

inline description of the service

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [DataService](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0) |

##### <a name="service_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the service

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="theme"></a>Property `theme`

**Title:** theme/category

A list of categories for the Catalog. A Catalog may be associated with multiple themes

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

inline description of the theme

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="theme_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the theme

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="themeTaxonomy"></a>Property `themeTaxonomy`

**Title:** themes

A knowledge organization system (KOS) used to classify the resources documented in the catalog (e.g., datasets and services)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                    |
| --------------------------------- |
| [item 0](#themeTaxonomy_anyOf_i0) |
| [item 1](#themeTaxonomy_anyOf_i1) |

### <a name="themeTaxonomy_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="themeTaxonomy_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [item 1 items](#themeTaxonomy_anyOf_i1_items) | -           |

#### <a name="themeTaxonomy_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [ConceptScheme](#themeTaxonomy_anyOf_i1_items_oneOf_i0) |
| [item 1](#themeTaxonomy_anyOf_i1_items_oneOf_i1)        |

##### <a name="themeTaxonomy_anyOf_i1_items_oneOf_i0"></a>Property `ConceptScheme`

**Title:** ConceptScheme

inline description of ConceptScheme

|                           |                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                   |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

##### <a name="themeTaxonomy_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of ConceptScheme

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accessRights"></a>Property `accessRights`

**Title:** access rights

Information that indicates whether the Catalog is open data, has access restrictions or is not public

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

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="accessRights_oneOf_i2"></a>Property `item 2`

reference iri of the access rights

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `conformsTo`

**Title:** schema version

An established standard to which the described catalog conforms

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                   |
| -------------------------------- |
| [item 0](#conformsTo_oneOf_i0)   |
| [Standard](#conformsTo_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i2)   |

### <a name="conformsTo_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="conformsTo_oneOf_i1"></a>Property `Standard`

**Title:** Standard

inline description of Standard

|                           |                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

### <a name="conformsTo_oneOf_i2"></a>Property `item 2`

reference iri of Standard

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="creator"></a>Property `creator`

**Title:** creator

The entity responsible for creating the resource

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

inline description of creator

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

##### <a name="creator_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of creator

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `description`

**Title:** description

Free-text description of the catalog (in the language indicated in the language property)

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="descriptionMap"></a>Property `descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="hasPart"></a>Property `hasPart`

**Title:** has part

A list of related catalogs that are part of the described catalog

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

| One of(Option)                                        |
| ----------------------------------------------------- |
| [DCAT-US 3 Catalog](#hasPart_anyOf_i1_items_oneOf_i0) |
| [item 1](#hasPart_anyOf_i1_items_oneOf_i1)            |

##### <a name="hasPart_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog`

**Title:** DCAT-US 3 Catalog

inline description of the related catalog

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

##### <a name="hasPart_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the related catalog

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `identifier`

**Title:** identifier

List of identifiers for the Catalog, e.g. the URI or other unique identifier

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

## <a name="issued"></a>Property `issued`

**Title:** release date

Date of formal issuance (e.g., publication) of the catalog

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

Language or languages used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalog. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

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

The license under which the Catalog can be used or reused

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

inline description of the license

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [LicenseDocument](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

### <a name="license_oneOf_i2"></a>Property `item 2`

reference iri of the license

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="modified"></a>Property `modified`

**Title:** update/modification date

Most recent date on which the catalog was changed, updated or modified

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

Agent responsible for making the catalog available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [item 0](#publisher_oneOf_i0) |
| [Agent](#publisher_oneOf_i1)  |
| [item 2](#publisher_oneOf_i2) |

### <a name="publisher_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="publisher_oneOf_i1"></a>Property `Agent`

**Title:** Agent

inline description of the publisher

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

### <a name="publisher_oneOf_i2"></a>Property `item 2`

reference iri of the publisher

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="rights"></a>Property `rights`

**Title:** rights

A statement that specifies rights associated with the catalog

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

inline description of rights

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="rights_oneOf_i2"></a>Property `item 2`

reference iri of rights

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `rightsHolder`

**Title:** rights holder

List of organizations holding rights on the catalog

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

inline description of rights holder

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of rights holder

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `spatial`

**Title:** spatial/geographic coverage

The geographical area covered by the catalog

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

inline description of geographical coverage

|                           |                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                         |
| **Same definition as**    | [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of geographical coverage

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="subject"></a>Property `subject`

**Title:** subject

List of subjects of the catalog

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

inline description of the subject

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="subject_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the subject

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `temporal`

**Title:** temporal coverage

List of temporal periods that the Catalog covers

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

inline description of the temporal coverage

|                           |                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the temporal coverage

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `title`

**Title:** title

The title of the catalog in the indicated language

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="titleMap"></a>Property `titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="category"></a>Property `category`

**Title:** category

The category of the Catalog

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

inline description of the category

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

### <a name="category_oneOf_i2"></a>Property `item 2`

reference iri of the category

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="homepage"></a>Property `homepage`

**Title:** homepage

The home page of the catalog (a public Web document usually available in HTML)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                 |
| ------------------------------ |
| [item 0](#homepage_oneOf_i0)   |
| [Document](#homepage_oneOf_i1) |
| [item 2](#homepage_oneOf_i2)   |

### <a name="homepage_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="homepage_oneOf_i1"></a>Property `Document`

**Title:** Document

inline description of the home page

|                           |                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                        |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Document](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

### <a name="homepage_oneOf_i2"></a>Property `item 2`

reference iri of the home page

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `qualifiedAttribution`

**Title:** qualified attribution

A list of agents having some form of responsibility for the catalog

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

|                           |                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                                         |
| **Same definition as**    | [Attribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Attribution

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

