

**Title:** Document

Information about a text document

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                           | Type               | Title/Description                                                                   |
| -------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                     | string             | -                                                                                   |
| - [@type](#@type )                                 | string             | -                                                                                   |
| - [accessURL](#accessURL )                         | More than one type | access URL                                                                          |
| - [downloadURL](#downloadURL )                     | More than one type | download URL                                                                        |
| - [creator](#creator )                             | null or array      | author                                                                              |
| - [mediaType](#mediaType )                         | More than one type | media type                                                                          |
| - [abstract](#abstract )                           | null or string     | abstract                                                                            |
| - [abstractMap](#abstractMap )                     | null or object     | Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [bibliographicCitation](#bibliographicCitation ) | null or string     | bibliographic citation                                                              |
| - [conformsTo](#conformsTo )                       | null or array      | conforms to                                                                         |
| - [corporateCreator](#corporateCreator )           | null or array      | corporate author                                                                    |
| - [description](#description )                     | null or string     | description                                                                         |
| - [descriptionMap](#descriptionMap )               | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [identifier](#identifier )                       | More than one type | identifier                                                                          |
| - [otherIdentifier](#otherIdentifier )             | null or array      | other identifier                                                                    |
| - [issued](#issued )                               | More than one type | publication date                                                                    |
| - [publisher](#publisher )                         | null or array      | publisher                                                                           |
| + [title](#title )                                 | string             | title                                                                               |
| - [titleMap](#titleMap )                           | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                           | More than one type | category                                                                            |

## <a name="@id"></a>Property `Document > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Document > @type`

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Document"` |

## <a name="accessURL"></a>Property `Document > accessURL`

**Title:** access URL

A URL that gives access to the Document

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                |
| ----------------------------- |
| [item 0](#accessURL_anyOf_i0) |
| [item 1](#accessURL_anyOf_i1) |

### <a name="accessURL_anyOf_i0"></a>Property `Document > accessURL > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="accessURL_anyOf_i1"></a>Property `Document > accessURL > anyOf > item 1`

reference iri of Document

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="downloadURL"></a>Property `Document > downloadURL`

**Title:** download URL

A URL that is a direct link to a downloadable file of the Document in a given format

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                  |
| ------------------------------- |
| [item 0](#downloadURL_anyOf_i0) |
| [item 1](#downloadURL_anyOf_i1) |

### <a name="downloadURL_anyOf_i0"></a>Property `Document > downloadURL > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="downloadURL_anyOf_i1"></a>Property `Document > downloadURL > anyOf > item 1`

reference iri of Document

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="creator"></a>Property `Document > creator`

**Title:** author

The individual(s) responsible for creating the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [creator items](#creator_items) | -           |

### <a name="creator_items"></a>Document > creator > creator items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                    |
| --------------------------------- |
| [Kind](#creator_items_anyOf_i0)   |
| [item 1](#creator_items_anyOf_i1) |

#### <a name="creator_items_anyOf_i0"></a>Property `Document > creator > creator items > anyOf > Kind`

**Title:** Kind

inline description of author

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

#### <a name="creator_items_anyOf_i1"></a>Property `Document > creator > creator items > anyOf > item 1`

reference iri of Person

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="mediaType"></a>Property `Document > mediaType`

**Title:** media type

The file format of the Document as defined in the official register of media types managed by IANA

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#mediaType_anyOf_i0)    |
| [MediaType](#mediaType_anyOf_i1) |
| [item 2](#mediaType_anyOf_i2)    |

### <a name="mediaType_anyOf_i0"></a>Property `Document > mediaType > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="mediaType_anyOf_i1"></a>Property `Document > mediaType > anyOf > MediaType`

**Title:** MediaType

inline description of MediaType

| **Type**                  | `object`                    |
| ------------------------- | --------------------------- |
| **Additional properties** | Any type allowed            |
| **Defined in**            | [Mediatype](./Mediatype.md) |

### <a name="mediaType_anyOf_i2"></a>Property `Document > mediaType > anyOf > item 2`

reference iri of MediaType

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="abstract"></a>Property `Document > abstract`

**Title:** abstract

Text abstract of the Document

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="abstractMap"></a>Property `Document > abstractMap`

Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="bibliographicCitation"></a>Property `Document > bibliographicCitation`

**Title:** bibliographic citation

Bibliographic citation as text

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="conformsTo"></a>Property `Document > conformsTo`

**Title:** conforms to

List of standards that the Document conforms to

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [conformsTo items](#conformsTo_items) | -           |

### <a name="conformsTo_items"></a>Document > conformsTo > conformsTo items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [Standard](#conformsTo_items_anyOf_i0) |
| [item 1](#conformsTo_items_anyOf_i1)   |

#### <a name="conformsTo_items_anyOf_i0"></a>Property `Document > conformsTo > conformsTo items > anyOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                  |
| ------------------------- | ------------------------- |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

#### <a name="conformsTo_items_anyOf_i1"></a>Property `Document > conformsTo > conformsTo items > anyOf > item 1`

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="corporateCreator"></a>Property `Document > corporateCreator`

**Title:** corporate author

The corporate organization(s) responsible for creating the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [corporateCreator items](#corporateCreator_items) | -           |

### <a name="corporateCreator_items"></a>Document > corporateCreator > corporateCreator items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                   |
| ------------------------------------------------ |
| [Organization](#corporateCreator_items_anyOf_i0) |
| [item 1](#corporateCreator_items_anyOf_i1)       |

#### <a name="corporateCreator_items_anyOf_i0"></a>Property `Document > corporateCreator > corporateCreator items > anyOf > Organization`

**Title:** Organization

inline description of corporate author

| **Type**                  | `object`                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#conformsTo_items_anyOf_i0_identifier_anyOf_i1_anyOf_i1_creator_oneOf_i1) |

#### <a name="corporateCreator_items_anyOf_i1"></a>Property `Document > corporateCreator > corporateCreator items > anyOf > item 1`

reference iri of corporate author

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="description"></a>Property `Document > description`

**Title:** description

A free-text account of the Document

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="descriptionMap"></a>Property `Document > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="identifier"></a>Property `Document > identifier`

**Title:** identifier

The unique identifier for the Document (e.g. DOI, ISBN)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [item 0](#identifier_anyOf_i0)     |
| [Identifier](#identifier_anyOf_i1) |
| [item 2](#identifier_anyOf_i2)     |

### <a name="identifier_anyOf_i0"></a>Property `Document > identifier > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Document > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                           |
| ------------------------- | ------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                             |
| **Same definition as**    | [Identifier](#conformsTo_items_anyOf_i0_identifier_anyOf_i1) |

### <a name="identifier_anyOf_i2"></a>Property `Document > identifier > anyOf > item 2`

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="otherIdentifier"></a>Property `Document > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Document besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [otherIdentifier items](#otherIdentifier_items) | -           |

### <a name="otherIdentifier_items"></a>Document > otherIdentifier > otherIdentifier items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                |
| --------------------------------------------- |
| [Identifier](#otherIdentifier_items_anyOf_i0) |
| [item 1](#otherIdentifier_items_anyOf_i1)     |

#### <a name="otherIdentifier_items_anyOf_i0"></a>Property `Document > otherIdentifier > otherIdentifier items > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                           |
| ------------------------- | ------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                             |
| **Same definition as**    | [Identifier](#conformsTo_items_anyOf_i0_identifier_anyOf_i1) |

#### <a name="otherIdentifier_items_anyOf_i1"></a>Property `Document > otherIdentifier > otherIdentifier items > anyOf > item 1`

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="issued"></a>Property `Document > issued`

**Title:** publication date

Publication date of the Document

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Document > issued > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Document > issued > anyOf > item 1`

| **Type** | More than one type |
| -------- | ------------------ |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_anyOf_i0) |
| [item 1](#issued_anyOf_i1_anyOf_i1) |
| [item 2](#issued_anyOf_i1_anyOf_i2) |
| [item 3](#issued_anyOf_i1_anyOf_i3) |

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `Document > publisher`

**Title:** publisher

The organization(s) that published the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [publisher items](#publisher_items) | -           |

### <a name="publisher_items"></a>Document > publisher > publisher items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                            |
| ----------------------------------------- |
| [Organization](#publisher_items_anyOf_i0) |
| [item 1](#publisher_items_anyOf_i1)       |

#### <a name="publisher_items_anyOf_i0"></a>Property `Document > publisher > publisher items > anyOf > Organization`

**Title:** Organization

inline description of publisher

| **Type**                  | `object`                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#conformsTo_items_anyOf_i0_identifier_anyOf_i1_anyOf_i1_creator_oneOf_i1) |

#### <a name="publisher_items_anyOf_i1"></a>Property `Document > publisher > publisher items > anyOf > item 1`

reference iri of publisher

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="title"></a>Property `Document > title`

**Title:** title

The title of the Document

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `Document > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="category"></a>Property `Document > category`

**Title:** category

The category, nature, or genre of the Document

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                |
| ----------------------------- |
| [item 0](#category_anyOf_i0)  |
| [Concept](#category_anyOf_i1) |
| [item 2](#category_anyOf_i2)  |

### <a name="category_anyOf_i0"></a>Property `Document > category > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="category_anyOf_i1"></a>Property `Document > category > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | Any type allowed                                        |
| **Same definition as**    | [Concept](#conformsTo_items_anyOf_i0_category_oneOf_i1) |

### <a name="category_anyOf_i2"></a>Property `Document > category > anyOf > item 2`

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

