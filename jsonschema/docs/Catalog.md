

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
| - [otherIdentifier](#otherIdentifier )           | null or array           | other identifier                                                                    |
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

| One of(Option)                               |
| -------------------------------------------- |
| [DCAT-US 3 Catalog](#catalog_items_oneOf_i0) |
| [Link](#catalog_items_oneOf_i1)              |

#### <a name="catalog_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > catalog > Catalog or a link > oneOf > DCAT-US 3 Catalog`

**Title:** DCAT-US 3 Catalog

inline description of a Catalog object

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

#### <a name="catalog_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > catalog > Catalog or a link > oneOf > Link`

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

| One of(Option)                       |
| ------------------------------------ |
| [Kind](#contactPoint_items_oneOf_i0) |
| [Link](#contactPoint_items_oneOf_i1) |

#### <a name="contactPoint_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > contactPoint > Contact point or a link > oneOf > Kind`

**Title:** Kind

inline value for contact point

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

#### <a name="contactPoint_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > contactPoint > Contact point or a link > oneOf > Link`

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

| One of(Option)                     |
| ---------------------------------- |
| [Dataset](#dataset_items_oneOf_i0) |
| [Link](#dataset_items_oneOf_i1)    |

#### <a name="dataset_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset`

**Title:** Dataset

inline description of Dataset

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

#### <a name="dataset_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Link`

**Title:** Link

reference iri of Dataset

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="keyword"></a>Property `DCAT-US 3 Catalog > keyword`

**Title:** keyword/tag

A list of keywords or tags describing the resource

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [keyword items](#keyword_items) | -           |

### <a name="keyword_items"></a>DCAT-US 3 Catalog > keyword > keyword items

| **Type** | `string` |
| -------- | -------- |

## <a name="keywordMap"></a>Property `DCAT-US 3 Catalog > keywordMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="record"></a>Property `DCAT-US 3 Catalog > record`

**Title:** catalog record

A record describing a single resource (e.g., a dataset, a data service) that is part of the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#record_anyOf_i0) |
| [Array of records](#record_anyOf_i1)               |

### <a name="record_anyOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="record_anyOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > Array of records`

**Title:** Array of records

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [Record object or Link](#record_anyOf_i1_items) | -           |

#### <a name="record_anyOf_i1_items"></a>DCAT-US 3 Catalog > record > anyOf > Array of records > Record object or Link

**Title:** Record object or Link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                   |
| ------------------------------------------------ |
| [CatalogRecord](#record_anyOf_i1_items_oneOf_i0) |
| [Link](#record_anyOf_i1_items_oneOf_i1)          |

##### <a name="record_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > Array of records > Record object or Link > oneOf > CatalogRecord`

**Title:** CatalogRecord

inline description of the record

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Catalogrecord](./Catalogrecord.md) |

##### <a name="record_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > Array of records > Record object or Link > oneOf > Link`

**Title:** Link

reference iri of the record

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="service"></a>Property `DCAT-US 3 Catalog > service`

**Title:** service

List of data services that are listed in the Catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#service_anyOf_i0) |
| [Array of data services](#service_anyOf_i1)         |

### <a name="service_anyOf_i0"></a>Property `DCAT-US 3 Catalog > service > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="service_anyOf_i1"></a>Property `DCAT-US 3 Catalog > service > anyOf > Array of data services`

**Title:** Array of data services

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [DataService object or link](#service_anyOf_i1_items) | -           |

#### <a name="service_anyOf_i1_items"></a>DCAT-US 3 Catalog > service > anyOf > Array of data services > DataService object or link

**Title:** DataService object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                  |
| ----------------------------------------------- |
| [DataService](#service_anyOf_i1_items_oneOf_i0) |
| [Link](#service_anyOf_i1_items_oneOf_i1)        |

##### <a name="service_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > service > anyOf > Array of data services > DataService object or link > oneOf > DataService`

**Title:** DataService

inline description of the service

| **Type**                  | `object`                                                                                                    |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [DataService](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0) |

##### <a name="service_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > service > anyOf > Array of data services > DataService object or link > oneOf > Link`

**Title:** Link

reference iri of the service

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="theme"></a>Property `DCAT-US 3 Catalog > theme`

**Title:** theme/category

A list of categories for the Catalog. A Catalog may be associated with multiple themes

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#theme_anyOf_i0) |
| [Array of categories](#theme_anyOf_i1)            |

### <a name="theme_anyOf_i0"></a>Property `DCAT-US 3 Catalog > theme > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="theme_anyOf_i1"></a>Property `DCAT-US 3 Catalog > theme > anyOf > Array of categories`

**Title:** Array of categories

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Category or link](#theme_anyOf_i1_items) | -           |

#### <a name="theme_anyOf_i1_items"></a>DCAT-US 3 Catalog > theme > anyOf > Array of categories > Category or link

**Title:** Category or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                            |
| ----------------------------------------- |
| [Concept](#theme_anyOf_i1_items_oneOf_i0) |
| [Link](#theme_anyOf_i1_items_oneOf_i1)    |

##### <a name="theme_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > theme > anyOf > Array of categories > Category or link > oneOf > Concept`

**Title:** Concept

inline description of the theme

| **Type**                  | `object`                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="theme_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > theme > anyOf > Array of categories > Category or link > oneOf > Link`

**Title:** Link

reference iri of the theme

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="themeTaxonomy"></a>Property `DCAT-US 3 Catalog > themeTaxonomy`

**Title:** themes

A knowledge organization system (KOS) used to classify the resources documented in the catalog (e.g., datasets and services)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [Null allowed when not required](#themeTaxonomy_anyOf_i0) |
| [Array of taxonomies](#themeTaxonomy_anyOf_i1)            |

### <a name="themeTaxonomy_anyOf_i0"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="themeTaxonomy_anyOf_i1"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > Array of taxonomies`

**Title:** Array of taxonomies

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [ConceptScheme object or link](#themeTaxonomy_anyOf_i1_items) | -           |

#### <a name="themeTaxonomy_anyOf_i1_items"></a>DCAT-US 3 Catalog > themeTaxonomy > anyOf > Array of taxonomies > ConceptScheme object or link

**Title:** ConceptScheme object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [ConceptScheme](#themeTaxonomy_anyOf_i1_items_oneOf_i0) |
| [Link](#themeTaxonomy_anyOf_i1_items_oneOf_i1)          |

##### <a name="themeTaxonomy_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > Array of taxonomies > ConceptScheme object or link > oneOf > ConceptScheme`

**Title:** ConceptScheme

inline description of ConceptScheme

| **Type**                  | `object`                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

##### <a name="themeTaxonomy_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > Array of taxonomies > ConceptScheme object or link > oneOf > Link`

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

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#accessRights_oneOf_i0) |
| [RightsStatement](#accessRights_oneOf_i1)                |
| [Link](#accessRights_oneOf_i2)                           |

### <a name="accessRights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > accessRights > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

inline description of access rights

| **Type**                  | `object`                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="accessRights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > accessRights > oneOf > Link`

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

| One of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#conformsTo_oneOf_i0) |
| [Standard](#conformsTo_oneOf_i1)                       |
| [Link](#conformsTo_oneOf_i2)                           |

### <a name="conformsTo_oneOf_i0"></a>Property `DCAT-US 3 Catalog > conformsTo > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="conformsTo_oneOf_i1"></a>Property `DCAT-US 3 Catalog > conformsTo > oneOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

### <a name="conformsTo_oneOf_i2"></a>Property `DCAT-US 3 Catalog > conformsTo > oneOf > Link`

**Title:** Link

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="creator"></a>Property `DCAT-US 3 Catalog > creator`

**Title:** creator

The entity responsible for creating the resource

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#creator_anyOf_i0) |
| [Array of creators](#creator_anyOf_i1)              |

### <a name="creator_anyOf_i0"></a>Property `DCAT-US 3 Catalog > creator > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="creator_anyOf_i1"></a>Property `DCAT-US 3 Catalog > creator > anyOf > Array of creators`

**Title:** Array of creators

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#creator_anyOf_i1_items) | -           |

#### <a name="creator_anyOf_i1_items"></a>DCAT-US 3 Catalog > creator > anyOf > Array of creators > item 1 items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                            |
| ----------------------------------------- |
| [Agent](#creator_anyOf_i1_items_oneOf_i0) |
| [Link](#creator_anyOf_i1_items_oneOf_i1)  |

##### <a name="creator_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > creator > anyOf > Array of creators > item 1 items > oneOf > Agent`

**Title:** Agent

inline description of creator

| **Type**                  | `object`                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

##### <a name="creator_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > creator > anyOf > Array of creators > item 1 items > oneOf > Link`

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

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#hasPart_anyOf_i0) |
| [Array of catalogs](#hasPart_anyOf_i1)              |

### <a name="hasPart_anyOf_i0"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="hasPart_anyOf_i1"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > Array of catalogs`

**Title:** Array of catalogs

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [Catalog object or link](#hasPart_anyOf_i1_items) | -           |

#### <a name="hasPart_anyOf_i1_items"></a>DCAT-US 3 Catalog > hasPart > anyOf > Array of catalogs > Catalog object or link

**Title:** Catalog object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [DCAT-US 3 Catalog](#hasPart_anyOf_i1_items_oneOf_i0) |
| [Link](#hasPart_anyOf_i1_items_oneOf_i1)              |

##### <a name="hasPart_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > Array of catalogs > Catalog object or link > oneOf > DCAT-US 3 Catalog`

**Title:** DCAT-US 3 Catalog

inline description of the related catalog

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

##### <a name="hasPart_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > Array of catalogs > Catalog object or link > oneOf > Link`

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
| [item 2](#identifier_anyOf_i2)                         |

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
| **Same definition as**    | [Identifier](#dataset_items_oneOf_i0_otherIdentifier_items_anyOf_i0) |

### <a name="identifier_anyOf_i2"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > item 2`

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
| [item 1](#otherIdentifier_items_anyOf_i1)     |

#### <a name="otherIdentifier_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > otherIdentifier > otherIdentifier items > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                                   |
| ------------------------- | -------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                     |
| **Same definition as**    | [Identifier](#dataset_items_oneOf_i0_otherIdentifier_items_anyOf_i0) |

#### <a name="otherIdentifier_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > otherIdentifier > otherIdentifier items > anyOf > item 1`

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

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > issued > anyOf > Date string > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

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

The license under which the Catalog can be used or reused

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#license_oneOf_i0) |
| [LicenseDocument](#license_oneOf_i1)                |
| [Link](#license_oneOf_i2)                           |

### <a name="license_oneOf_i0"></a>Property `DCAT-US 3 Catalog > license > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="license_oneOf_i1"></a>Property `DCAT-US 3 Catalog > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

inline description of the license

| **Type**                  | `object`                                                                                                                         |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [LicenseDocument](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

### <a name="license_oneOf_i2"></a>Property `DCAT-US 3 Catalog > license > oneOf > Link`

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

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > modified > anyOf > Date string > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `DCAT-US 3 Catalog > publisher`

**Title:** publisher

Agent responsible for making the catalog available

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#publisher_oneOf_i0) |
| [Agent](#publisher_oneOf_i1)                          |
| [Link](#publisher_oneOf_i2)                           |

### <a name="publisher_oneOf_i0"></a>Property `DCAT-US 3 Catalog > publisher > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="publisher_oneOf_i1"></a>Property `DCAT-US 3 Catalog > publisher > oneOf > Agent`

**Title:** Agent

inline description of the publisher

| **Type**                  | `object`                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

### <a name="publisher_oneOf_i2"></a>Property `DCAT-US 3 Catalog > publisher > oneOf > Link`

**Title:** Link

reference iri of the publisher

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rights"></a>Property `DCAT-US 3 Catalog > rights`

**Title:** rights

A statement that specifies rights associated with the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#rights_oneOf_i0) |
| [RightsStatement](#rights_oneOf_i1)                |
| [Link](#rights_oneOf_i2)                           |

### <a name="rights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > rights > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="rights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > rights > oneOf > RightsStatement`

**Title:** RightsStatement

inline description of rights

| **Type**                  | `object`                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

### <a name="rights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > rights > oneOf > Link`

**Title:** Link

reference iri of rights

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="rightsHolder"></a>Property `DCAT-US 3 Catalog > rightsHolder`

**Title:** rights holder

List of organizations holding rights on the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [Null allowed when not required](#rightsHolder_anyOf_i0) |
| [Array of rights holders](#rightsHolder_anyOf_i1)        |

### <a name="rightsHolder_anyOf_i0"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="rightsHolder_anyOf_i1"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > Array of rights holders`

**Title:** Array of rights holders

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [Organization or link](#rightsHolder_anyOf_i1_items) | -           |

#### <a name="rightsHolder_anyOf_i1_items"></a>DCAT-US 3 Catalog > rightsHolder > anyOf > Array of rights holders > Organization or link

**Title:** Organization or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Organization](#rightsHolder_anyOf_i1_items_oneOf_i0) |
| [Link](#rightsHolder_anyOf_i1_items_oneOf_i1)         |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > Array of rights holders > Organization or link > oneOf > Organization`

**Title:** Organization

inline description of rights holder

| **Type**                  | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_items_anyOf_i0_anyOf_i1_creator_oneOf_i1) |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > Array of rights holders > Organization or link > oneOf > Link`

**Title:** Link

reference iri of rights holder

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `DCAT-US 3 Catalog > spatial`

**Title:** spatial/geographic coverage

The geographical area covered by the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#spatial_anyOf_i0) |
| [Array of locations](#spatial_anyOf_i1)             |

### <a name="spatial_anyOf_i0"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="spatial_anyOf_i1"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > Array of locations`

**Title:** Array of locations

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                    | Description |
| -------------------------------------------------- | ----------- |
| [Location object or link](#spatial_anyOf_i1_items) | -           |

#### <a name="spatial_anyOf_i1_items"></a>DCAT-US 3 Catalog > spatial > anyOf > Array of locations > Location object or link

**Title:** Location object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i1_items_oneOf_i0) |
| [Link](#spatial_anyOf_i1_items_oneOf_i1)     |

##### <a name="spatial_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > Array of locations > Location object or link > oneOf > Location`

**Title:** Location

inline description of geographical coverage

| **Type**                  | `object`                                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                         |
| **Same definition as**    | [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > Array of locations > Location object or link > oneOf > Link`

**Title:** Link

reference iri of geographical coverage

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="subject"></a>Property `DCAT-US 3 Catalog > subject`

**Title:** subject

List of subjects of the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#subject_anyOf_i0) |
| [Array of subjects](#subject_anyOf_i1)              |

### <a name="subject_anyOf_i0"></a>Property `DCAT-US 3 Catalog > subject > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="subject_anyOf_i1"></a>Property `DCAT-US 3 Catalog > subject > anyOf > Array of subjects`

**Title:** Array of subjects

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [Concept or link](#subject_anyOf_i1_items) | -           |

#### <a name="subject_anyOf_i1_items"></a>DCAT-US 3 Catalog > subject > anyOf > Array of subjects > Concept or link

**Title:** Concept or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                              |
| ------------------------------------------- |
| [Concept](#subject_anyOf_i1_items_oneOf_i0) |
| [Link](#subject_anyOf_i1_items_oneOf_i1)    |

##### <a name="subject_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > subject > anyOf > Array of subjects > Concept or link > oneOf > Concept`

**Title:** Concept

inline description of the subject

| **Type**                  | `object`                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

##### <a name="subject_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > subject > anyOf > Array of subjects > Concept or link > oneOf > Link`

**Title:** Link

reference iri of the subject

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `DCAT-US 3 Catalog > temporal`

**Title:** temporal coverage

List of temporal periods that the Catalog covers

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#temporal_anyOf_i0) |
| [Array of time periods](#temporal_anyOf_i1)          |

### <a name="temporal_anyOf_i0"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="temporal_anyOf_i1"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > Array of time periods`

**Title:** Array of time periods

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [PeriodOfTime object or link](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>DCAT-US 3 Catalog > temporal > anyOf > Array of time periods > PeriodOfTime object or link

**Title:** PeriodOfTime object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [Link](#temporal_anyOf_i1_items_oneOf_i1)         |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > Array of time periods > PeriodOfTime object or link > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

inline description of the temporal coverage

| **Type**                  | `object`                                                                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > Array of time periods > PeriodOfTime object or link > oneOf > Link`

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

The category of the Catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#category_oneOf_i0) |
| [Concept](#category_oneOf_i1)                        |
| [Link](#category_oneOf_i2)                           |

### <a name="category_oneOf_i0"></a>Property `DCAT-US 3 Catalog > category > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="category_oneOf_i1"></a>Property `DCAT-US 3 Catalog > category > oneOf > Concept`

**Title:** Concept

inline description of the category

| **Type**                  | `object`                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

### <a name="category_oneOf_i2"></a>Property `DCAT-US 3 Catalog > category > oneOf > Link`

**Title:** Link

reference iri of the category

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="homepage"></a>Property `DCAT-US 3 Catalog > homepage`

**Title:** homepage

The home page of the catalog (a public Web document usually available in HTML)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                 |
| ------------------------------ |
| [item 0](#homepage_oneOf_i0)   |
| [Document](#homepage_oneOf_i1) |
| [Link](#homepage_oneOf_i2)     |

### <a name="homepage_oneOf_i0"></a>Property `DCAT-US 3 Catalog > homepage > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="homepage_oneOf_i1"></a>Property `DCAT-US 3 Catalog > homepage > oneOf > Document`

**Title:** Document

inline description of the home page

| **Type**                  | `object`                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Document](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

### <a name="homepage_oneOf_i2"></a>Property `DCAT-US 3 Catalog > homepage > oneOf > Link`

**Title:** Link

reference iri of the home page

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="qualifiedAttribution"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution`

**Title:** qualified attribution

A list of agents having some form of responsibility for the catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Null allowed when not required](#qualifiedAttribution_anyOf_i0) |
| [Array of attributions](#qualifiedAttribution_anyOf_i1)          |

### <a name="qualifiedAttribution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="qualifiedAttribution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > Array of attributions`

**Title:** Array of attributions

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [Attribution object or link](#qualifiedAttribution_anyOf_i1_items) | -           |

#### <a name="qualifiedAttribution_anyOf_i1_items"></a>DCAT-US 3 Catalog > qualifiedAttribution > anyOf > Array of attributions > Attribution object or link

**Title:** Attribution object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [Attribution](#qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [Link](#qualifiedAttribution_anyOf_i1_items_oneOf_i1)        |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > Array of attributions > Attribution object or link > oneOf > Attribution`

**Title:** Attribution

inline description of Attribution

| **Type**                  | `object`                                                                                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                                                                                         |
| **Same definition as**    | [Attribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > Array of attributions > Attribution object or link > oneOf > Link`

**Title:** Link

reference iri of Attribution

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

