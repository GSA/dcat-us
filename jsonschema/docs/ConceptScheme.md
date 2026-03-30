

**Title:** ConceptScheme

A system for specifying approved values for a single concept

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                             | Type               | Title/Description                                                                   |
| ------------------------------------ | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                       | string             | -                                                                                   |
| - [@type](#@type )                   | string             | -                                                                                   |
| - [version](#version )               | null or string     | version info                                                                        |
| - [created](#created )               | More than one type | creation date                                                                       |
| - [description](#description )       | null or string     | description                                                                         |
| - [descriptionMap](#descriptionMap ) | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#issued )                 | More than one type | publication date                                                                    |
| - [modified](#modified )             | More than one type | update/modification date                                                            |
| + [title](#title )                   | string             | title                                                                               |
| - [titleMap](#titleMap )             | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `ConceptScheme > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `ConceptScheme > @type`

| **Type**    | `string`          |
| ----------- | ----------------- |
| **Default** | `"ConceptScheme"` |

## <a name="version"></a>Property `ConceptScheme > version`

**Title:** version info

A version number or other version designation of the concept scheme

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="created"></a>Property `ConceptScheme > created`

**Title:** creation date

The date on which the Concept Scheme was first created

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#created_anyOf_i0) |
| [Date string](#created_anyOf_i1)                    |

### <a name="created_anyOf_i0"></a>Property `ConceptScheme > created > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="created_anyOf_i1"></a>Property `ConceptScheme > created > anyOf > Date string`

**Title:** Date string

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_oneOf_i0) |
| [item 1](#created_anyOf_i1_oneOf_i1) |
| [item 2](#created_anyOf_i1_oneOf_i2) |
| [item 3](#created_anyOf_i1_oneOf_i3) |

#### <a name="created_anyOf_i1_oneOf_i0"></a>Property `ConceptScheme > created > anyOf > Date string > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i1"></a>Property `ConceptScheme > created > anyOf > Date string > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i2"></a>Property `ConceptScheme > created > anyOf > Date string > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_oneOf_i3"></a>Property `ConceptScheme > created > anyOf > Date string > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="description"></a>Property `ConceptScheme > description`

**Title:** description

A description of the concept scheme

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="descriptionMap"></a>Property `ConceptScheme > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="issued"></a>Property `ConceptScheme > issued`

**Title:** publication date

The date of formal issuance (e.g., publication) of the concept scheme

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>Property `ConceptScheme > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `ConceptScheme > issued > anyOf > Date string`

**Title:** Date string

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `ConceptScheme > issued > anyOf > Date string > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `ConceptScheme > issued > anyOf > Date string > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `ConceptScheme > issued > anyOf > Date string > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `ConceptScheme > issued > anyOf > Date string > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `ConceptScheme > modified`

**Title:** update/modification date

The most recent date at which the concept scheme was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `ConceptScheme > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `ConceptScheme > modified > anyOf > Date string`

**Title:** Date string

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `ConceptScheme > modified > anyOf > Date string > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `ConceptScheme > modified > anyOf > Date string > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `ConceptScheme > modified > anyOf > Date string > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `ConceptScheme > modified > anyOf > Date string > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="title"></a>Property `ConceptScheme > title`

**Title:** title

The title of the concept scheme

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `ConceptScheme > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

