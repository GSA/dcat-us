

**Title:** CatalogRecord

A record in a catalog, describing the registration of a single resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                         | Type               | Title/Description                                                                   |
| -------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                   | string             | -                                                                                   |
| - [@type](#@type )               | string             | -                                                                                   |
| - [status](#status )             | More than one type | change type                                                                         |
| - [conformsTo](#conformsTo )     | More than one type | application profile                                                                 |
| - [description](#description )   | More than one type | description                                                                         |
| - [issued](#issued )             | More than one type | listing date                                                                        |
| - [language](#language )         | More than one type | language                                                                            |
| + [modified](#modified )         | More than one type | update/modification date                                                            |
| - [source](#source )             | More than one type | source metadata                                                                     |
| - [title](#title )               | null or string     | title                                                                               |
| - [titleMap](#titleMap )         | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [primaryTopic](#primaryTopic ) | string             | primary topic                                                                       |

## <a name="@id"></a>Property `CatalogRecord > @id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `CatalogRecord > @type`

|             |                   |
| ----------- | ----------------- |
| **Type**    | `string`          |
| **Default** | `"CatalogRecord"` |

## <a name="status"></a>Property `CatalogRecord > status`

**Title:** change type

The status of the catalog record in the context of editorial flow of the dataset and data service descriptions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)              |
| --------------------------- |
| [item 0](#status_oneOf_i0)  |
| [Concept](#status_oneOf_i1) |
| [item 2](#status_oneOf_i2)  |

### <a name="status_oneOf_i0"></a>Property `CatalogRecord > status > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="status_oneOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept`

**Title:** Concept

inline description of status

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="status_oneOf_i2"></a>Property `CatalogRecord > status > oneOf > item 2`

reference iri of status

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="conformsTo"></a>Property `CatalogRecord > conformsTo`

**Title:** application profile

An Application Profile that the Catalog Record's metadata conforms to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                   |
| -------------------------------- |
| [item 0](#conformsTo_oneOf_i0)   |
| [Standard](#conformsTo_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i2)   |

### <a name="conformsTo_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="conformsTo_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard`

**Title:** Standard

inline description of application profile

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

### <a name="conformsTo_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > item 2`

reference iri of application profile

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `CatalogRecord > description`

**Title:** description

A list of free-text accounts of the catalog record

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                  |
| ------------------------------- |
| [item 0](#description_anyOf_i0) |
| [item 1](#description_anyOf_i1) |

### <a name="description_anyOf_i0"></a>Property `CatalogRecord > description > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="description_anyOf_i1"></a>Property `CatalogRecord > description > anyOf > item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [item 1 items](#description_anyOf_i1_items) | -           |

#### <a name="description_anyOf_i1_items"></a>CatalogRecord > description > anyOf > item 1 > item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="issued"></a>Property `CatalogRecord > issued`

**Title:** listing date

List of dates on which the catalog record was included in the catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `CatalogRecord > issued > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="issued_anyOf_i1"></a>Property `CatalogRecord > issued > anyOf > item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#issued_anyOf_i1_items) | -           |

#### <a name="issued_anyOf_i1_items"></a>CatalogRecord > issued > anyOf > item 1 > item 1 items

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#issued_anyOf_i1_items_oneOf_i0) |
| [item 1](#issued_anyOf_i1_items_oneOf_i1) |
| [item 2](#issued_anyOf_i1_items_oneOf_i2) |
| [item 3](#issued_anyOf_i1_items_oneOf_i3) |

##### <a name="issued_anyOf_i1_items_oneOf_i0"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

##### <a name="issued_anyOf_i1_items_oneOf_i1"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

##### <a name="issued_anyOf_i1_items_oneOf_i2"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

##### <a name="issued_anyOf_i1_items_oneOf_i3"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `CatalogRecord > language`

**Title:** language

A language or languages used in the textual metadata describing titles, descriptions, etc. of the catalog record. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#language_anyOf_i0) |
| [item 1](#language_anyOf_i1) |
| [item 2](#language_anyOf_i2) |

### <a name="language_anyOf_i0"></a>Property `CatalogRecord > language > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="language_anyOf_i1"></a>Property `CatalogRecord > language > anyOf > item 1`

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `CatalogRecord > language > anyOf > item 2`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 2 items](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>CatalogRecord > language > anyOf > item 2 > item 2 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="modified"></a>Property `CatalogRecord > modified`

**Title:** update/modification date

The most recent date on which the catalog record was changed or modified

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | Yes         |

| One of(Option)               |
| ---------------------------- |
| [item 0](#modified_oneOf_i0) |
| [item 1](#modified_oneOf_i1) |
| [item 2](#modified_oneOf_i2) |
| [item 3](#modified_oneOf_i3) |

### <a name="modified_oneOf_i0"></a>Property `CatalogRecord > modified > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

### <a name="modified_oneOf_i1"></a>Property `CatalogRecord > modified > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

### <a name="modified_oneOf_i2"></a>Property `CatalogRecord > modified > oneOf > item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

### <a name="modified_oneOf_i3"></a>Property `CatalogRecord > modified > oneOf > item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="source"></a>Property `CatalogRecord > source`

**Title:** source metadata

The original metadata that was used in creating metadata for the items in the catalog record

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)               |
| ---------------------------- |
| [item 0](#source_oneOf_i0)   |
| [resource](#source_oneOf_i1) |
| [item 2](#source_oneOf_i2)   |

### <a name="source_oneOf_i0"></a>Property `CatalogRecord > source > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="source_oneOf_i1"></a>Property `CatalogRecord > source > oneOf > resource`

inline description of the source

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Resource](./Resource.md) |

### <a name="source_oneOf_i2"></a>Property `CatalogRecord > source > oneOf > item 2`

reference iri of the source

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `CatalogRecord > title`

**Title:** title

A name given to the Catalog Record

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="titleMap"></a>Property `CatalogRecord > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="primaryTopic"></a>Property `CatalogRecord > primaryTopic`

**Title:** primary topic

A link to the Dataset, Data service or Catalog described in the Catalog Record

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

