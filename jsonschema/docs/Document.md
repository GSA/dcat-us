

**Title:** Document

Information about a text document

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                           | Type               | Title/Description      |
| -------------------------------------------------- | ------------------ | ---------------------- |
| - [@id](#@id )                                     | string             | -                      |
| - [@type](#@type )                                 | string             | -                      |
| - [accessURL](#accessURL )                         | More than one type | access URL             |
| - [downloadURL](#downloadURL )                     | More than one type | download URL           |
| - [creator](#creator )                             | null or array      | author                 |
| - [mediaType](#mediaType )                         | null or string     | media type             |
| - [abstract](#abstract )                           | null or string     | abstract               |
| - [bibliographicCitation](#bibliographicCitation ) | null or string     | bibliographic citation |
| - [conformsTo](#conformsTo )                       | null or array      | conforms to            |
| - [corporateCreator](#corporateCreator )           | null or array      | corporate author       |
| - [description](#description )                     | null or string     | description            |
| - [identifier](#identifier )                       | More than one type | identifier             |
| - [otherIdentifier](#otherIdentifier )             | null or array      | other identifier       |
| - [issued](#issued )                               | More than one type | publication date       |
| - [publisher](#publisher )                         | null or array      | publisher              |
| + [title](#title )                                 | string             | title                  |
| - [category](#category )                           | null or array      | category               |

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

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#accessURL_anyOf_i0) |
| [URL](#accessURL_anyOf_i1)                            |

### <a name="accessURL_anyOf_i0"></a>Property `Document > accessURL > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accessURL_anyOf_i1"></a>Property `Document > accessURL > anyOf > URL`

**Title:** URL

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

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [Null allowed when not required](#downloadURL_anyOf_i0) |
| [URL](#downloadURL_anyOf_i1)                            |

### <a name="downloadURL_anyOf_i0"></a>Property `Document > downloadURL > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="downloadURL_anyOf_i1"></a>Property `Document > downloadURL > anyOf > URL`

**Title:** URL

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
| [Kind or link](#creator_items)  | -           |

### <a name="creator_items"></a>Document > creator > Kind or link

**Title:** Kind or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                  |
| ------------------------------- |
| [Kind](#creator_items_anyOf_i0) |
| [Link](#creator_items_anyOf_i1) |

#### <a name="creator_items_anyOf_i0"></a>Property `Document > creator > Kind or link > anyOf > Kind`

**Title:** Kind

inline description of author

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

#### <a name="creator_items_anyOf_i1"></a>Property `Document > creator > Kind or link > anyOf > Link`

**Title:** Link

reference iri of author

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="mediaType"></a>Property `Document > mediaType`

**Title:** media type

The file format of the Document as defined in the official register of media types managed by IANA: https://www.iana.org/assignments/media-types/media-types.xhtml

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="abstract"></a>Property `Document > abstract`

**Title:** abstract

Text abstract of the Document

| **Type** | `null or string` |
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

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [Standard object or link](#conformsTo_items) | -           |

### <a name="conformsTo_items"></a>Document > conformsTo > Standard object or link

**Title:** Standard object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [Standard](#conformsTo_items_anyOf_i0) |
| [Link](#conformsTo_items_anyOf_i1)     |

#### <a name="conformsTo_items_anyOf_i0"></a>Property `Document > conformsTo > Standard object or link > anyOf > Standard`

**Title:** Standard

inline description of Standard

| **Type**                  | `object`                  |
| ------------------------- | ------------------------- |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

#### <a name="conformsTo_items_anyOf_i1"></a>Property `Document > conformsTo > Standard object or link > anyOf > Link`

**Title:** Link

reference iri of Standard

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="corporateCreator"></a>Property `Document > corporateCreator`

**Title:** corporate author

The corporate organization(s) responsible for creating the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [Organization or link](#corporateCreator_items) | -           |

### <a name="corporateCreator_items"></a>Document > corporateCreator > Organization or link

**Title:** Organization or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                   |
| ------------------------------------------------ |
| [Organization](#corporateCreator_items_anyOf_i0) |
| [Link](#corporateCreator_items_anyOf_i1)         |

#### <a name="corporateCreator_items_anyOf_i0"></a>Property `Document > corporateCreator > Organization or link > anyOf > Organization`

**Title:** Organization

inline description of corporate author

| **Type**                  | `object`                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#conformsTo_items_anyOf_i0_identifier_anyOf_i1_anyOf_i1_creator_anyOf_i1) |

#### <a name="corporateCreator_items_anyOf_i1"></a>Property `Document > corporateCreator > Organization or link > anyOf > Link`

**Title:** Link

reference iri of corporate author

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="description"></a>Property `Document > description`

**Title:** description

A free-text account of the Document

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="identifier"></a>Property `Document > identifier`

**Title:** identifier

The unique identifier for the Document (e.g. DOI, ISBN)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#identifier_anyOf_i0) |
| [Identifier](#identifier_anyOf_i1)                     |
| [Link](#identifier_anyOf_i2)                           |

### <a name="identifier_anyOf_i0"></a>Property `Document > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Document > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                           |
| ------------------------- | ------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                             |
| **Same definition as**    | [Identifier](#conformsTo_items_anyOf_i0_identifier_anyOf_i1) |

### <a name="identifier_anyOf_i2"></a>Property `Document > identifier > anyOf > Link`

**Title:** Link

reference iri of Identifier

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="otherIdentifier"></a>Property `Document > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Document besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [Identifier object or link](#otherIdentifier_items) | -           |

### <a name="otherIdentifier_items"></a>Document > otherIdentifier > Identifier object or link

**Title:** Identifier object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                |
| --------------------------------------------- |
| [Identifier](#otherIdentifier_items_anyOf_i0) |
| [Link](#otherIdentifier_items_anyOf_i1)       |

#### <a name="otherIdentifier_items_anyOf_i0"></a>Property `Document > otherIdentifier > Identifier object or link > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                           |
| ------------------------- | ------------------------------------------------------------ |
| **Additional properties** | Any type allowed                                             |
| **Same definition as**    | [Identifier](#conformsTo_items_anyOf_i0_identifier_anyOf_i1) |

#### <a name="otherIdentifier_items_anyOf_i1"></a>Property `Document > otherIdentifier > Identifier object or link > anyOf > Link`

**Title:** Link

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

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1)                         |

### <a name="issued_anyOf_i0"></a>Property `Document > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Document > issued > anyOf > item 1`

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_anyOf_i0) |
| [item 1](#issued_anyOf_i1_anyOf_i1) |
| [item 2](#issued_anyOf_i1_anyOf_i2) |
| [item 3](#issued_anyOf_i1_anyOf_i3) |

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `Document > issued > anyOf > item 1 > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `Document > publisher`

**Title:** publisher

The organization(s) that published the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [Organization object or link](#publisher_items) | -           |

### <a name="publisher_items"></a>Document > publisher > Organization object or link

**Title:** Organization object or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                            |
| ----------------------------------------- |
| [Organization](#publisher_items_anyOf_i0) |
| [Link](#publisher_items_anyOf_i1)         |

#### <a name="publisher_items_anyOf_i0"></a>Property `Document > publisher > Organization object or link > anyOf > Organization`

**Title:** Organization

inline description of publisher

| **Type**                  | `object`                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#conformsTo_items_anyOf_i0_identifier_anyOf_i1_anyOf_i1_creator_anyOf_i1) |

#### <a name="publisher_items_anyOf_i1"></a>Property `Document > publisher > Organization object or link > anyOf > Link`

**Title:** Link

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

## <a name="category"></a>Property `Document > category`

**Title:** category

List of categories/genres for the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [Category or link](#category_items) | -           |

### <a name="category_items"></a>Document > category > Category or link

**Title:** Category or link

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Concept](#category_items_anyOf_i0) |
| [Link](#category_items_anyOf_i1)    |

#### <a name="category_items_anyOf_i0"></a>Property `Document > category > Category or link > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type                                            |
| ------------------------- | ------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Concept](#conformsTo_items_anyOf_i0_category_items_anyOf_i0) |

#### <a name="category_items_anyOf_i1"></a>Property `Document > category > Category or link > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

