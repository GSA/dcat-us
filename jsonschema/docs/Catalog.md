

**Title:** DCAT-US 3 Catalog

The main item defined by DCAT-US 3 is the Catalog class

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                         | Type                    | Title/Description           |
| ------------------------------------------------ | ----------------------- | --------------------------- |
| - [@id](#@id )                                   | string                  | -                           |
| - [@type](#@type )                               | string                  | -                           |
| - [catalog](#catalog )                           | null or array           | Related catalogs            |
| - [contactPoint](#contactPoint )                 | null or array           | Contact points              |
| + [dataset](#dataset )                           | array                   | dataset                     |
| - [keyword](#keyword )                           | null or array of string | keyword/tag                 |
| - [record](#record )                             | null or array           | catalog record              |
| - [service](#service )                           | null or array           | service                     |
| - [theme](#theme )                               | null or array           | theme/category              |
| - [themeTaxonomy](#themeTaxonomy )               | null or array           | themes                      |
| - [accessRights](#accessRights )                 | More than one type      | access rights               |
| - [conformsTo](#conformsTo )                     | More than one type      | schema version              |
| - [creator](#creator )                           | null or array           | creator                     |
| - [description](#description )                   | null or string          | description                 |
| - [hasPart](#hasPart )                           | null or array           | has part                    |
| - [identifier](#identifier )                     | More than one type      | identifier                  |
| - [otherIdentifier](#otherIdentifier )           | null or array           | other identifier            |
| - [issued](#issued )                             | More than one type      | release date                |
| - [language](#language )                         | More than one type      | language                    |
| - [license](#license )                           | More than one type      | license                     |
| - [modified](#modified )                         | More than one type      | update/modification date    |
| - [publisher](#publisher )                       | More than one type      | publisher                   |
| - [rights](#rights )                             | null or array of string | rights                      |
| - [rightsHolder](#rightsHolder )                 | null or array           | rights holder               |
| - [spatial](#spatial )                           | null or array           | spatial/geographic coverage |
| - [subject](#subject )                           | null or array           | subject                     |
| - [temporal](#temporal )                         | null or array           | temporal coverage           |
| - [title](#title )                               | null or string          | title                       |
| - [category](#category )                         | null or array           | category                    |
| - [homepage](#homepage )                         | More than one type      | homepage                    |
| - [qualifiedAttribution](#qualifiedAttribution ) | null or array           | qualified attribution       |

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

| Each item of this array must be     | Description                                             |
| ----------------------------------- | ------------------------------------------------------- |
| [DCAT-US 3 Catalog](#catalog_items) | The main item defined by DCAT-US 3 is the Catalog class |

### <a name="catalog_items"></a>DCAT-US 3 Catalog > catalog > DCAT-US 3 Catalog

**Title:** DCAT-US 3 Catalog

The main item defined by DCAT-US 3 is the Catalog class

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

## <a name="contactPoint"></a>Property `DCAT-US 3 Catalog > contactPoint`

**Title:** Contact points

Contact information that can be used for sending comments about the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| [Kind](#contactPoint_items)     | Contact information for an individual or entity |

### <a name="contactPoint_items"></a>DCAT-US 3 Catalog > contactPoint > Kind

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

## <a name="dataset"></a>Property `DCAT-US 3 Catalog > dataset`

**Title:** dataset

List of Datasets that are part of the Catalog

| **Type**     | `array` |
| ------------ | ------- |
| **Required** | Yes     |

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#dataset_items)       | Information about a set of data |

### <a name="dataset_items"></a>DCAT-US 3 Catalog > dataset > Dataset

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

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

## <a name="record"></a>Property `DCAT-US 3 Catalog > record`

**Title:** catalog record

A record describing a single resource (e.g., a dataset, a data service) that is part of the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                             |
| ------------------------------- | ----------------------------------------------------------------------- |
| [CatalogRecord](#record_items)  | A record in a catalog, describing the registration of a single resource |

### <a name="record_items"></a>DCAT-US 3 Catalog > record > CatalogRecord

**Title:** CatalogRecord

A record in a catalog, describing the registration of a single resource

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Catalogrecord](./Catalogrecord.md) |

## <a name="service"></a>Property `DCAT-US 3 Catalog > service`

**Title:** service

List of data services that are listed in the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                   |
| ------------------------------- | --------------------------------------------- |
| [DataService](#service_items)   | A service for providing data at a URL or URLs |

### <a name="service_items"></a>DCAT-US 3 Catalog > service > DataService

**Title:** DataService

A service for providing data at a URL or URLs

| **Type**                  | `object`                                                       |
| ------------------------- | -------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                               |
| **Same definition as**    | [DataService](#dataset_items_sample_items_accessService_items) |

## <a name="theme"></a>Property `DCAT-US 3 Catalog > theme`

**Title:** theme/category

A list of categories for the Catalog. A Catalog may be associated with multiple themes

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#theme_items)         | A labeled value from an optionally specified concept scheme |

### <a name="theme_items"></a>DCAT-US 3 Catalog > theme > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                                      |
| ------------------------- | ----------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                        |
| **Same definition as**    | [Concept](#dataset_items_sample_items_representationTechnique_anyOf_i1) |

## <a name="themeTaxonomy"></a>Property `DCAT-US 3 Catalog > themeTaxonomy`

**Title:** themes

A knowledge organization system (KOS) used to classify the resources documented in the catalog (e.g., datasets and services)

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be       | Description                                                  |
| ------------------------------------- | ------------------------------------------------------------ |
| [ConceptScheme](#themeTaxonomy_items) | A system for specifying approved values for a single concept |

### <a name="themeTaxonomy_items"></a>DCAT-US 3 Catalog > themeTaxonomy > ConceptScheme

**Title:** ConceptScheme

A system for specifying approved values for a single concept

| **Type**                  | `object`                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [inScheme](#dataset_items_sample_items_representationTechnique_anyOf_i1_anyOf_i1_inScheme) |

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

### <a name="accessRights_anyOf_i0"></a>Property `DCAT-US 3 Catalog > accessRights > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessRights_anyOf_i1"></a>Property `DCAT-US 3 Catalog > accessRights > anyOf > item 1`

Text description of the access rights

| **Type** | `string` |
| -------- | -------- |

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

### <a name="conformsTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > conformsTo > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="conformsTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > conformsTo > anyOf > Standard`

**Title:** Standard

Information about a particular standard that another item conforms to

| **Type**                  | `object`                                                                     |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                             |
| **Same definition as**    | [Standard](#dataset_items_sample_items_accessService_items_conformsTo_items) |

## <a name="creator"></a>Property `DCAT-US 3 Catalog > creator`

**Title:** creator

The entity responsible for creating the resource

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Agent](#creator_items)         | An entity that could be involved with a resource |

### <a name="creator_items"></a>DCAT-US 3 Catalog > creator > Agent

**Title:** Agent

An entity that could be involved with a resource

| **Type**                  | `object`                                                               |
| ------------------------- | ---------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [Agent](#dataset_items_sample_items_accessService_items_creator_items) |

## <a name="description"></a>Property `DCAT-US 3 Catalog > description`

**Title:** description

Free-text description of the catalog (in the language indicated in the language property)

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="hasPart"></a>Property `DCAT-US 3 Catalog > hasPart`

**Title:** has part

A list of related catalogs that are part of the described catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description                                             |
| ----------------------------------- | ------------------------------------------------------- |
| [DCAT-US 3 Catalog](#hasPart_items) | The main item defined by DCAT-US 3 is the Catalog class |

### <a name="hasPart_items"></a>DCAT-US 3 Catalog > hasPart > DCAT-US 3 Catalog

**Title:** DCAT-US 3 Catalog

The main item defined by DCAT-US 3 is the Catalog class

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

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

### <a name="identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                 |
| ------------------------- | -------------------------------------------------- |
| **Additional properties** | Any type allowed                                   |
| **Same definition as**    | [Identifier](#dataset_items_otherIdentifier_items) |

## <a name="otherIdentifier"></a>Property `DCAT-US 3 Catalog > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Catalog besides the main identifier, e.g. the URI or other unique identifiers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>DCAT-US 3 Catalog > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type                                 |
| ------------------------- | -------------------------------------------------- |
| **Additional properties** | Any type allowed                                   |
| **Same definition as**    | [Identifier](#dataset_items_otherIdentifier_items) |

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

### <a name="license_anyOf_i0"></a>Property `DCAT-US 3 Catalog > license > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="license_anyOf_i1"></a>Property `DCAT-US 3 Catalog > license > anyOf > item 1`

Full text of the license

| **Type** | `string` |
| -------- | -------- |

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

### <a name="publisher_anyOf_i0"></a>Property `DCAT-US 3 Catalog > publisher > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="publisher_anyOf_i1"></a>Property `DCAT-US 3 Catalog > publisher > anyOf > Agent`

**Title:** Agent

inline description of the publisher

| **Type**                  | `object`                                                               |
| ------------------------- | ---------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [Agent](#dataset_items_sample_items_accessService_items_creator_items) |

## <a name="rights"></a>Property `DCAT-US 3 Catalog > rights`

**Title:** rights

A list of statements concerning all rights for the Catalog that may not be addressed by license or accessRights, such as copyright statements, statements about the intellectual property rights (IPR), or information regarding access or restrictions based on privacy, security, or other policies

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be | Description                        |
| ------------------------------- | ---------------------------------- |
| [rights items](#rights_items)   | Full text of a statement of rights |

### <a name="rights_items"></a>DCAT-US 3 Catalog > rights > rights items

Full text of a statement of rights

| **Type** | `string` |
| -------- | -------- |

## <a name="rightsHolder"></a>Property `DCAT-US 3 Catalog > rightsHolder`

**Title:** rights holder

List of organizations holding rights on the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description                                                                         |
| ----------------------------------- | ----------------------------------------------------------------------------------- |
| [Organization](#rightsHolder_items) | Information about an organization, including other organizations that it is part of |

### <a name="rightsHolder_items"></a>DCAT-US 3 Catalog > rightsHolder > Organization

**Title:** Organization

Information about an organization, including other organizations that it is part of

| **Type**                  | `object`                                                                       |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                               |
| **Same definition as**    | [Organization](#dataset_items_otherIdentifier_items_anyOf_i1_creator_anyOf_i1) |

## <a name="spatial"></a>Property `DCAT-US 3 Catalog > spatial`

**Title:** spatial/geographic coverage

The geographical area covered by the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Location](#spatial_items)      | Information about a specific geographic location |

### <a name="spatial_items"></a>DCAT-US 3 Catalog > spatial > Location

**Title:** Location

Information about a specific geographic location

| **Type**                  | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [Location](#dataset_items_sample_items_accessService_items_spatial_items) |

## <a name="subject"></a>Property `DCAT-US 3 Catalog > subject`

**Title:** subject

List of subjects of the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#subject_items)       | A labeled value from an optionally specified concept scheme |

### <a name="subject_items"></a>DCAT-US 3 Catalog > subject > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                                      |
| ------------------------- | ----------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                        |
| **Same definition as**    | [Concept](#dataset_items_sample_items_representationTechnique_anyOf_i1) |

## <a name="temporal"></a>Property `DCAT-US 3 Catalog > temporal`

**Title:** temporal coverage

List of temporal periods that the Catalog covers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| [PeriodOfTime](#temporal_items) | Information about a specific time period with a start- and/or end-time |

### <a name="temporal_items"></a>DCAT-US 3 Catalog > temporal > PeriodOfTime

**Title:** PeriodOfTime

Information about a specific time period with a start- and/or end-time

| **Type**                  | `object`                                                                       |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                                               |
| **Same definition as**    | [PeriodOfTime](#dataset_items_sample_items_accessService_items_temporal_items) |

## <a name="title"></a>Property `DCAT-US 3 Catalog > title`

**Title:** title

The title of the catalog in the indicated language

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="category"></a>Property `DCAT-US 3 Catalog > category`

**Title:** category

List of categories for the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#category_items)      | A labeled value from an optionally specified concept scheme |

### <a name="category_items"></a>DCAT-US 3 Catalog > category > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                                                      |
| ------------------------- | ----------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                        |
| **Same definition as**    | [Concept](#dataset_items_sample_items_representationTechnique_anyOf_i1) |

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

### <a name="homepage_anyOf_i0"></a>Property `DCAT-US 3 Catalog > homepage > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="homepage_anyOf_i1"></a>Property `DCAT-US 3 Catalog > homepage > anyOf > Document`

**Title:** Document

inline description of the home page

| **Type**                  | `object`                                           |
| ------------------------- | -------------------------------------------------- |
| **Additional properties** | Any type allowed                                   |
| **Same definition as**    | [Document](#dataset_items_sample_items_page_items) |

## <a name="qualifiedAttribution"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution`

**Title:** qualified attribution

A list of agents having some form of responsibility for the catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be            | Description                                  |
| ------------------------------------------ | -------------------------------------------- |
| [Attribution](#qualifiedAttribution_items) | An attribution that an agent plays some role |

### <a name="qualifiedAttribution_items"></a>DCAT-US 3 Catalog > qualifiedAttribution > Attribution

**Title:** Attribution

An attribution that an agent plays some role

| **Type**                  | `object`                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [Attribution](#dataset_items_sample_items_accessService_items_qualifiedAttribution_items) |

