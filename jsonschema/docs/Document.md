

**Title:** Document

Information about a text document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                           | Type               | Title/Description                                                                   |
| -------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                     | string             | -                                                                                   |
| - [@type](#@type )                                 | string             | -                                                                                   |
| - [creators](#creators )                           | More than one type | authors                                                                             |
| - [publishers](#publishers )                       | null or string     | publisher                                                                           |
| - [mediaType](#mediaType )                         | More than one type | media type                                                                          |
| - [abstract](#abstract )                           | null or string     | abstract                                                                            |
| - [abstractMap](#abstractMap )                     | null or object     | Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [bibliographicCitation](#bibliographicCitation ) | null or string     | bibliographic citation                                                              |
| - [conformsTo](#conformsTo )                       | More than one type | conforms to standard                                                                |
| - [creator](#creator )                             | More than one type | corporate author                                                                    |
| - [description](#description )                     | null or string     | description                                                                         |
| - [descriptionMap](#descriptionMap )               | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [identifier](#identifier )                       | More than one type | identifier                                                                          |
| - [issued](#issued )                               | More than one type | publication date                                                                    |
| - [publisher](#publisher )                         | More than one type | publisher                                                                           |
| + [title](#title )                                 | string             | title                                                                               |
| - [titleMap](#titleMap )                           | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                           | More than one type | category                                                                            |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |              |
| ----------- | ------------ |
| **Type**    | `string`     |
| **Default** | `"Document"` |

## <a name="creators"></a>Property `creators`

**Title:** authors

List of authors

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#creators_anyOf_i0) |
| [item 1](#creators_anyOf_i1) |

### <a name="creators_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="creators_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#creators_anyOf_i1_items) | -           |

#### <a name="creators_anyOf_i1_items"></a>item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="publishers"></a>Property `publishers`

**Title:** publisher

Publisher

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="mediaType"></a>Property `mediaType`

**Title:** media type

List of file formats of the Document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                |
| ----------------------------- |
| [item 0](#mediaType_anyOf_i0) |
| [item 1](#mediaType_anyOf_i1) |

### <a name="mediaType_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="mediaType_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [item 1 items](#mediaType_anyOf_i1_items) | -           |

#### <a name="mediaType_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [MediaType](#mediaType_anyOf_i1_items_oneOf_i0) |
| [item 1](#mediaType_anyOf_i1_items_oneOf_i1)    |

##### <a name="mediaType_anyOf_i1_items_oneOf_i0"></a>Property `MediaType`

**Title:** MediaType

inline description of MediaType

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Additional properties** | Any type allowed            |
| **Defined in**            | [Mediatype](./Mediatype.md) |

##### <a name="mediaType_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of MediaType

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="abstract"></a>Property `abstract`

**Title:** abstract

Text abstract of the document

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="abstractMap"></a>Property `abstractMap`

Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="bibliographicCitation"></a>Property `bibliographicCitation`

**Title:** bibliographic citation

Bibliographic citation as text

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="conformsTo"></a>Property `conformsTo`

**Title:** conforms to standard

A standard to which the document conforms

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

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Standard

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="creator"></a>Property `creator`

**Title:** corporate author

The organization responsible for creating the resource

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

| One of(Option)                                   |
| ------------------------------------------------ |
| [Organization](#creator_anyOf_i1_items_oneOf_i0) |
| [item 1](#creator_anyOf_i1_items_oneOf_i1)       |

##### <a name="creator_anyOf_i1_items_oneOf_i0"></a>Property `Organization`

**Title:** Organization

inline description of corporate author

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Organization](./Organization.md) |

##### <a name="creator_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of corporate author

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `description`

**Title:** description

A free-text account of the Document

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="descriptionMap"></a>Property `descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="identifier"></a>Property `identifier`

**Title:** identifier

List of unique identifiers for the Document (e.g. DOI, ISBN)

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

**Title:** publication date

Publication date of the document

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

## <a name="publisher"></a>Property `publisher`

**Title:** publisher

publisher organization of the document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#publisher_oneOf_i0)       |
| [Organization](#publisher_oneOf_i1) |
| [item 2](#publisher_oneOf_i2)       |

### <a name="publisher_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="publisher_oneOf_i1"></a>Property `Organization`

**Title:** Organization

inline description of publisher organization

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [Organization](#creator_anyOf_i1_items_oneOf_i0) |

### <a name="publisher_oneOf_i2"></a>Property `item 2`

reference iri of publisher organization

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `title`

**Title:** title

The title of the document in the indicated language

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

Category of the document

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

inline description of Concept

|                           |                                                                  |
| ------------------------- | ---------------------------------------------------------------- |
| **Type**                  | `object`                                                         |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Concept](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |

### <a name="category_oneOf_i2"></a>Property `item 2`

reference iri of Concept

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

