

**Title:** Standard

Information about a particular standard that another item conforms to

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                             | Type               | Title/Description                                                                |
| ------------------------------------ | ------------------ | -------------------------------------------------------------------------------- |
| - [@id](#@id )                       | string             | -                                                                                |
| - [@type](#@type )                   | string             | -                                                                                |
| - [created](#created )               | More than one type | creation date                                                                    |
| - [description](#description )       | null or string     | description                                                                      |
| - [descriptionMap](#descriptionMap ) | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#identifier )         | More than one type | identifier                                                                       |
| - [issued](#issued )                 | More than one type | issued                                                                           |
| - [modified](#modified )             | More than one type | last modified                                                                    |
| - [title](#title )                   | null or string     | title                                                                            |
| - [titleMap](#titleMap )             | null or object     | Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#category )             | More than one type | category                                                                         |
| - [inScheme](#inScheme )             | More than one type | in scheme                                                                        |

## <a name="@id"></a>Property `Standard > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Standard > @type`

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Standard"` |

## <a name="created"></a>Property `Standard > created`

**Title:** creation date

The date on which the Standard has been first created

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)              |
| --------------------------- |
| [item 0](#created_anyOf_i0) |
| [item 1](#created_anyOf_i1) |

### <a name="created_anyOf_i0"></a>Property `Standard > created > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>Property `Standard > created > anyOf > item 1`

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_oneOf_i0) |
| [item 1](#created_anyOf_i1_oneOf_i1) |
| [item 2](#created_anyOf_i1_oneOf_i2) |
| [item 3](#created_anyOf_i1_oneOf_i3) |

#### <a name="created_anyOf_i1_oneOf_i0"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i1"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i2"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_oneOf_i3"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="description"></a>Property `Standard > description`

**Title:** description

A free-text account of the Standard

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="descriptionMap"></a>Property `Standard > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="identifier"></a>Property `Standard > identifier`

**Title:** identifier

The main identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalogue, or of a reference register

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Standard > identifier > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Standard > identifier > anyOf > item 1`

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>Standard > identifier > anyOf > item 1 > item 1 items

| **Type** | `string` |
| -------- | -------- |

## <a name="issued"></a>Property `Standard > issued`

**Title:** issued

The date of formal issuance (e.g., publication) of the Standard

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Standard > issued > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Standard > issued > anyOf > item 1`

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `Standard > modified`

**Title:** last modified

The most recent date on which the Standard was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `Standard > modified > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `Standard > modified > anyOf > item 1`

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="title"></a>Property `Standard > title`

**Title:** title

A name given to the Standard

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="titleMap"></a>Property `Standard > titleMap`

Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="category"></a>Property `Standard > category`

**Title:** category

The type of the Standard. A controlled vocabulary for the values has not been established

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `Standard > category > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="category_oneOf_i1"></a>Property `Standard > category > oneOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="category_oneOf_i2"></a>Property `Standard > category > oneOf > item 2`

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="inScheme"></a>Property `Standard > inScheme`

**Title:** in scheme

The reference register to which the Standard belongs

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#inScheme_oneOf_i0)        |
| [ConceptScheme](#inScheme_oneOf_i1) |
| [item 2](#inScheme_oneOf_i2)        |

### <a name="inScheme_oneOf_i0"></a>Property `Standard > inScheme > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="inScheme_oneOf_i1"></a>Property `Standard > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

inline description of ConceptScheme

| **Type**                  | `object`                                              |
| ------------------------- | ----------------------------------------------------- |
| **Additional properties** | Any type allowed                                      |
| **Same definition as**    | [ConceptScheme](#category_oneOf_i1_inScheme_oneOf_i0) |

### <a name="inScheme_oneOf_i2"></a>Property `Standard > inScheme > oneOf > item 2`

reference iri of ConceptScheme

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

