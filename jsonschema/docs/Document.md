

**Title:** Document

A publication or other document related to a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Document",
    "title": "Climate Data User Guide",
    "description": "A guide for accessing and using the National Climate Data Center's data products.",
    "accessURL": "https://example.gov/docs/climate-user-guide",
    "mediaType": "application/pdf",
    "identifier": "NCDC-UG-2024-001",
    "issued": "2024-03-15",
    "publisher": [
        {
            "@type": "Organization",
            "name": "National Climate Data Center"
        }
    ],
    "bibliographicCitation": "National Climate Data Center. (2024). Climate Data User Guide. Retrieved from https://example.gov/docs/climate-user-guide"
}
```

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

## <a name="@id"></a>[Optional] Property `Document > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/documents/climate-user-guide-001"
```

## <a name="@type"></a>[Optional] Property `Document > @type`

**Requirement:** Optional

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Document"` |

## <a name="accessURL"></a>[Optional] Property `Document > accessURL`

**Title:** access URL

**Requirement:** Optional

A URL that gives access to the Document

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"https://example.gov/docs/climate-user-guide"
```

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

## <a name="downloadURL"></a>[Optional] Property `Document > downloadURL`

**Title:** download URL

**Requirement:** Optional

A URL that is a direct link to a downloadable file of the Document in a given format

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"https://example.gov/docs/climate-user-guide.pdf"
```

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

## <a name="creator"></a>[Optional] Property `Document > creator`

**Title:** author

**Requirement:** Optional

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

## <a name="mediaType"></a>[Optional] Property `Document > mediaType`

**Title:** media type

**Requirement:** Optional

The file format of the Document as defined in the official register of media types managed by IANA: https://www.iana.org/assignments/media-types/media-types.xhtml

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"application/pdf"
```

## <a name="abstract"></a>[Optional] Property `Document > abstract`

**Title:** abstract

**Requirement:** Optional

Text abstract of the Document

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"This document provides detailed instructions for using climate data products, including API access, file formats, and data interpretation guidelines."
```

## <a name="bibliographicCitation"></a>[Recommended] Property `Document > bibliographicCitation`

**Title:** bibliographic citation

**Requirement:** Recommended

Bibliographic citation as text

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"National Climate Data Center. (2024). Climate Data User Guide. Retrieved from https://example.gov/docs/climate-user-guide"
```

```json
"National Climate Data Center. (2024). Climate Data User Guide. U.S. Department of Commerce."
```

## <a name="conformsTo"></a>[Optional] Property `Document > conformsTo`

**Title:** conforms to

**Requirement:** Optional

List of standards or specifications the document follows

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| [Standard](#conformsTo_items)   | A standard or specification that another resource conforms to |

### <a name="conformsTo_items"></a>Document > conformsTo > Standard

**Title:** Standard

A standard or specification that another resource conforms to

| **Type**                  | `object`                  |
| ------------------------- | ------------------------- |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

## <a name="corporateCreator"></a>[Optional] Property `Document > corporateCreator`

**Title:** corporate author

**Requirement:** Optional

The corporate organization(s) responsible for creating the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be         | Description                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------- |
| [Organization](#corporateCreator_items) | An organization involved with a resource, including parent or child organizations |

### <a name="corporateCreator_items"></a>Document > corporateCreator > Organization

**Title:** Organization

An organization involved with a resource, including parent or child organizations

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [Organization](#conformsTo_items_identifier_anyOf_i1_anyOf_i1_creator_anyOf_i1) |

## <a name="description"></a>[Recommended] Property `Document > description`

**Title:** description

**Requirement:** Recommended

Plain-language summary of the document

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"A guide for accessing and using the National Climate Data Center's data products."
```

```json
"A comprehensive guide for accessing and using the National Climate Data Center's data products and services."
```

## <a name="identifier"></a>[Recommended] Property `Document > identifier`

**Title:** identifier

**Requirement:** Recommended

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

## <a name="otherIdentifier"></a>[Optional] Property `Document > otherIdentifier`

**Title:** other identifier

**Requirement:** Optional

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

## <a name="issued"></a>[Recommended] Property `Document > issued`

**Title:** publication date

**Requirement:** Recommended

Publication date of the Document

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-03-15"
```

```json
"2024-01-15"
```

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

## <a name="publisher"></a>[Recommended] Property `Document > publisher`

**Title:** publisher

**Requirement:** Recommended

The organization(s) that published the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be  | Description                                                                       |
| -------------------------------- | --------------------------------------------------------------------------------- |
| [Organization](#publisher_items) | An organization involved with a resource, including parent or child organizations |

### <a name="publisher_items"></a>Document > publisher > Organization

**Title:** Organization

An organization involved with a resource, including parent or child organizations

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [Organization](#conformsTo_items_identifier_anyOf_i1_anyOf_i1_creator_anyOf_i1) |

## <a name="title"></a>[Mandatory] Property `Document > title`

**Title:** title

**Requirement:** Mandatory

The title of the Document

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Example:**

```json
"Climate Data User Guide"
```

## <a name="category"></a>[Optional] Property `Document > category`

**Title:** category

**Requirement:** Optional

List of categories/genres for the Document

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| [Concept](#category_items)      | A controlled term or label, optionally drawn from a concept scheme |

### <a name="category_items"></a>Document > category > Concept

**Title:** Concept

A controlled term or label, optionally drawn from a concept scheme

| **Type**                  | More than one type                          |
| ------------------------- | ------------------------------------------- |
| **Additional properties** | Any type allowed                            |
| **Same definition as**    | [Concept](#conformsTo_items_category_items) |

