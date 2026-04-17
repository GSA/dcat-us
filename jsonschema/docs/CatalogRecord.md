

**Title:** CatalogRecord

A record in a catalog, describing the registration of a single resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "CatalogRecord",
    "modified": "2024-06-15",
    "primaryTopic": "https://example.gov/datasets/climate-data-2024",
    "title": "Climate Data 2024 Catalog Entry",
    "issued": [
        "2024-01-15"
    ],
    "status": "published",
    "conformsTo": {
        "@type": "Standard",
        "title": "DCAT-US 3.0"
    }
}
```

| Property                         | Type                    | Title/Description        |
| -------------------------------- | ----------------------- | ------------------------ |
| - [@id](#@id )                   | string                  | -                        |
| - [@type](#@type )               | string                  | -                        |
| - [status](#status )             | More than one type      | change type              |
| - [conformsTo](#conformsTo )     | More than one type      | application profile      |
| - [description](#description )   | null or array of string | Descriptions             |
| - [issued](#issued )             | null or array           | listing date             |
| - [language](#language )         | More than one type      | language                 |
| + [modified](#modified )         | More than one type      | update/modification date |
| - [source](#source )             | null or string          | source metadata          |
| - [title](#title )               | null or string          | title                    |
| + [primaryTopic](#primaryTopic ) | string                  | primary topic            |

## <a name="@id"></a>[Optional] Property `CatalogRecord > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/catalog-records/climate-dataset-record-001"
```

## <a name="@type"></a>[Optional] Property `CatalogRecord > @type`

**Requirement:** Optional

| **Type**    | `string`          |
| ----------- | ----------------- |
| **Default** | `"CatalogRecord"` |

## <a name="status"></a>[Recommended] Property `CatalogRecord > status`

**Title:** change type

**Requirement:** Recommended

The status of the catalog record in the context of editorial flow of the dataset and data service descriptions

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#status_anyOf_i0) |
| [Concept](#status_anyOf_i1)                        |

### <a name="status_anyOf_i0"></a>Property `CatalogRecord > status > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="status_anyOf_i1"></a>Property `CatalogRecord > status > anyOf > Concept`

**Title:** Concept

inline description of status

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

## <a name="conformsTo"></a>[Recommended] Property `CatalogRecord > conformsTo`

**Title:** application profile

**Requirement:** Recommended

An Application Profile that the Catalog Record's metadata conforms to

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#conformsTo_anyOf_i0) |
| [Standard](#conformsTo_anyOf_i1)                       |

### <a name="conformsTo_anyOf_i0"></a>Property `CatalogRecord > conformsTo > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="conformsTo_anyOf_i1"></a>Property `CatalogRecord > conformsTo > anyOf > Standard`

**Title:** Standard

inline description of application profile

| **Type**                  | `object`                  |
| ------------------------- | ------------------------- |
| **Additional properties** | Any type allowed          |
| **Defined in**            | [Standard](./Standard.md) |

## <a name="description"></a>[Optional] Property `CatalogRecord > description`

**Title:** Descriptions

**Requirement:** Optional

A list of free-text accounts of the catalog record

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "This catalog record describes the registration of the Climate Data 2023 dataset.",
    "Contains metadata about when the dataset was added and last updated."
]
```

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [Description string](#description_items) | -           |

### <a name="description_items"></a>CatalogRecord > description > Description string

**Title:** Description string

| **Type** | `string` |
| -------- | -------- |

## <a name="issued"></a>[Optional] Property `CatalogRecord > issued`

**Title:** listing date

**Requirement:** Optional

List of dates on which the catalog record was included in the catalog

| **Type** | `null or array` |
| -------- | --------------- |

**Examples:**

```json
[
    "2024-01-15"
]
```

```json
[
    "2023-06-01"
]
```

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [Date string](#issued_items)    | -           |

### <a name="issued_items"></a>CatalogRecord > issued > Date string

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#issued_items_anyOf_i0) |
| [item 1](#issued_items_anyOf_i1) |
| [item 2](#issued_items_anyOf_i2) |
| [item 3](#issued_items_anyOf_i3) |

#### <a name="issued_items_anyOf_i0"></a>Property `CatalogRecord > issued > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_items_anyOf_i1"></a>Property `CatalogRecord > issued > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_items_anyOf_i2"></a>Property `CatalogRecord > issued > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_items_anyOf_i3"></a>Property `CatalogRecord > issued > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>[Optional] Property `CatalogRecord > language`

**Title:** language

**Requirement:** Optional

Language code used in catalog record metadata text, using ISO 639-1 values such as en or es

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
[
    "en",
    "es"
]
```

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#language_anyOf_i0) |
| [Language code](#language_anyOf_i1)                  |
| [Array of language codes](#language_anyOf_i2)        |

### <a name="language_anyOf_i0"></a>Property `CatalogRecord > language > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="language_anyOf_i1"></a>Property `CatalogRecord > language > anyOf > Language code`

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `CatalogRecord > language > anyOf > Array of language codes`

**Title:** Array of language codes

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Language code](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>CatalogRecord > language > anyOf > Array of language codes > Language code

**Title:** Language code

| **Type** | `string` |
| -------- | -------- |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="modified"></a>[Mandatory] Property `CatalogRecord > modified`

**Title:** update/modification date

**Requirement:** Mandatory

The most recent date on which the catalog record was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-06-15"
```

```json
"2024-01-15T10:30:00Z"
```

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |
| [item 2](#modified_anyOf_i2) |
| [item 3](#modified_anyOf_i3) |

### <a name="modified_anyOf_i0"></a>Property `CatalogRecord > modified > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

### <a name="modified_anyOf_i1"></a>Property `CatalogRecord > modified > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

### <a name="modified_anyOf_i2"></a>Property `CatalogRecord > modified > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

### <a name="modified_anyOf_i3"></a>Property `CatalogRecord > modified > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="source"></a>[Optional] Property `CatalogRecord > source`

**Title:** source metadata

**Requirement:** Optional

The original metadata that was used in creating metadata for the items in the catalog record, either a URL referencing the source metadata or a string of the source metadata itself

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Original metadata harvested from NOAA data portal"
```

## <a name="title"></a>[Optional] Property `CatalogRecord > title`

**Title:** title

**Requirement:** Optional

A name given to the Catalog Record

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"Climate Data 2024 Catalog Entry"
```

```json
"Climate Data 2023 Catalog Record"
```

## <a name="primaryTopic"></a>[Mandatory] Property `CatalogRecord > primaryTopic`

**Title:** primary topic

**Requirement:** Mandatory

A link to the Dataset, Data service or Catalog described in the Catalog Record

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"https://example.gov/datasets/climate-data-2024"
```

```json
"https://example.gov/datasets/climate-data-2023"
```

