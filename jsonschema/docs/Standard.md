

**Title:** Standard

A standard or specification that another resource conforms to

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Standard",
    "title": "DCAT-US 3.0",
    "description": "Data Catalog Vocabulary - United States Profile version 3.0",
    "issued": "2024-01-15",
    "identifier": {
        "@type": "Identifier",
        "notation": "DCAT-US-3.0",
        "schemaAgency": "U.S. General Services Administration"
    },
    "inScheme": {
        "@type": "ConceptScheme",
        "title": "Federal Data Standards",
        "description": "A collection of data standards used by federal agencies"
    }
}
```

| Property                               | Type               | Title/Description |
| -------------------------------------- | ------------------ | ----------------- |
| - [@id](#@id )                         | string             | -                 |
| - [@type](#@type )                     | string             | -                 |
| - [created](#created )                 | More than one type | creation date     |
| - [description](#description )         | null or string     | description       |
| - [identifier](#identifier )           | More than one type | identifier        |
| - [otherIdentifier](#otherIdentifier ) | null or array      | other identifier  |
| - [issued](#issued )                   | More than one type | issued            |
| - [modified](#modified )               | More than one type | last modified     |
| - [title](#title )                     | null or string     | title             |
| - [category](#category )               | null or array      | category          |
| - [inScheme](#inScheme )               | More than one type | in scheme         |

## <a name="@id"></a>[Optional] Property `Standard > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/standards/dcat-us-3"
```

## <a name="@type"></a>[Optional] Property `Standard > @type`

**Requirement:** Optional

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Standard"` |

## <a name="created"></a>[Optional] Property `Standard > created`

**Title:** creation date

**Requirement:** Optional

The date on which the Standard has been first created

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2023-01-01"
```

```json
"2024-01-15T10:30:00Z"
```

```json
"2024"
```

```json
"2024-01"
```

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#created_anyOf_i0) |
| [Date string](#created_anyOf_i1)                    |

### <a name="created_anyOf_i0"></a>Property `Standard > created > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>Property `Standard > created > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_anyOf_i0) |
| [item 1](#created_anyOf_i1_anyOf_i1) |
| [item 2](#created_anyOf_i1_anyOf_i2) |
| [item 3](#created_anyOf_i1_anyOf_i3) |

#### <a name="created_anyOf_i1_anyOf_i0"></a>Property `Standard > created > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="created_anyOf_i1_anyOf_i1"></a>Property `Standard > created > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="created_anyOf_i1_anyOf_i2"></a>Property `Standard > created > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_anyOf_i3"></a>Property `Standard > created > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="description"></a>[Optional] Property `Standard > description`

**Title:** description

**Requirement:** Optional

Plain-language summary of the standard

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"Data Catalog Vocabulary - United States Profile version 3.0"
```

```json
"The DCAT-US 3.0 schema defines a standard metadata format for data catalogs in the United States government, based on W3C DCAT."
```

## <a name="identifier"></a>[Optional] Property `Standard > identifier`

**Title:** identifier

**Requirement:** Optional

The unique identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalog

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [Null allowed when not required](#identifier_anyOf_i0) |
| [Identifier](#identifier_anyOf_i1)                     |

### <a name="identifier_anyOf_i0"></a>Property `Standard > identifier > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Standard > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type            |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Defined in**            | [Identifier](./Identifier.md) |

## <a name="otherIdentifier"></a>[Optional] Property `Standard > otherIdentifier`

**Title:** other identifier

**Requirement:** Optional

A list of identifiers for the Standard besides the main identifier, e.g. the URI or other unique identifiers in the context of the Catalog

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>Standard > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type                 |
| ------------------------- | ---------------------------------- |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Identifier](#identifier_anyOf_i1) |

## <a name="issued"></a>[Optional] Property `Standard > issued`

**Title:** issued

**Requirement:** Optional

The date of formal issuance (e.g., publication) of the Standard

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-01-15"
```

```json
"2024-01-15T10:30:00Z"
```

```json
"2024"
```

```json
"2024-01"
```

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>Property `Standard > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Standard > issued > anyOf > Date string`

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

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `Standard > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `Standard > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `Standard > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `Standard > issued > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>[Optional] Property `Standard > modified`

**Title:** last modified

**Requirement:** Optional

The most recent date on which the Standard was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"2024-06-01"
```

```json
"2024-01-15T10:30:00Z"
```

```json
"2024"
```

```json
"2024-01"
```

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `Standard > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `Standard > modified > anyOf > Date string`

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

#### <a name="modified_anyOf_i1_anyOf_i0"></a>Property `Standard > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>Property `Standard > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>Property `Standard > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>Property `Standard > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="title"></a>[Optional] Property `Standard > title`

**Title:** title

**Requirement:** Optional

Human-readable title of the standard

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"DCAT-US 3.0"
```

```json
"DCAT-US 3.0 - Data Catalog Vocabulary United States Profile"
```

## <a name="category"></a>[Optional] Property `Standard > category`

**Title:** category

**Requirement:** Optional

List of categories for the Standard

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| [Concept](#category_items)      | A controlled term or label, optionally drawn from a concept scheme |

### <a name="category_items"></a>Standard > category > Concept

**Title:** Concept

A controlled term or label, optionally drawn from a concept scheme

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

## <a name="inScheme"></a>[Optional] Property `Standard > inScheme`

**Title:** in scheme

**Requirement:** Optional

The reference register to which the Standard belongs

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#inScheme_anyOf_i0) |
| [ConceptScheme](#inScheme_anyOf_i1)                  |

### <a name="inScheme_anyOf_i0"></a>Property `Standard > inScheme > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="inScheme_anyOf_i1"></a>Property `Standard > inScheme > anyOf > ConceptScheme`

**Title:** ConceptScheme

inline description of ConceptScheme

| **Type**                  | `object`                                      |
| ------------------------- | --------------------------------------------- |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [inScheme](#category_items_anyOf_i1_inScheme) |

