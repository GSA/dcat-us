

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

| Each item of this array must be | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| [Kind](#creator_items)          | Contact information for an individual or entity |

### <a name="creator_items"></a>Document > creator > Kind

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

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

| Each item of this array must be | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| [Standard](#conformsTo_items)   | Information about a particular standard that another item conforms to |

### <a name="conformsTo_items"></a>Document > conformsTo > Standard

**Title:** Standard

Information about a particular standard that another item conforms to

| **Type**                  | `object`                  |
| ------------------------- | ------------------------- |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

## <a name="corporateCreator"></a>Property `Document > corporateCreator`

**Title:** corporate author

The corporate organization(s) responsible for creating the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be         | Description                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| [Organization](#corporateCreator_items) | Information about an organization, including other organizations that it is part of |

### <a name="corporateCreator_items"></a>Document > corporateCreator > Organization

**Title:** Organization

Information about an organization, including other organizations that it is part of

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [Organization](#conformsTo_items_identifier_anyOf_i1_anyOf_i1_creator_anyOf_i1) |

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

### <a name="identifier_anyOf_i0"></a>Property `Document > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Document > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type                                  |
| ------------------------- | --------------------------------------------------- |
| **Additional properties** | Any type allowed                                    |
| **Same definition as**    | [Identifier](#conformsTo_items_identifier_anyOf_i1) |

## <a name="otherIdentifier"></a>Property `Document > otherIdentifier`

**Title:** other identifier

A list of identifiers for the Document besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>Document > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type                                  |
| ------------------------- | --------------------------------------------------- |
| **Additional properties** | Any type allowed                                    |
| **Same definition as**    | [Identifier](#conformsTo_items_identifier_anyOf_i1) |

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

| Each item of this array must be  | Description                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| [Organization](#publisher_items) | Information about an organization, including other organizations that it is part of |

### <a name="publisher_items"></a>Document > publisher > Organization

**Title:** Organization

Information about an organization, including other organizations that it is part of

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [Organization](#conformsTo_items_identifier_anyOf_i1_anyOf_i1_creator_anyOf_i1) |

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

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#category_items)      | A labeled value from an optionally specified concept scheme |

### <a name="category_items"></a>Document > category > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type                          |
| ------------------------- | ------------------------------------------- |
| **Additional properties** | Any type allowed                            |
| **Same definition as**    | [Concept](#conformsTo_items_category_items) |

