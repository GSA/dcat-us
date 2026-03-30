

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)      |
| ------------------- |
| [item 0](#anyOf_i0) |
| [item 1](#anyOf_i1) |

## <a name="anyOf_i0"></a>Property `Identifier > anyOf > item 0`

| **Type** | `string` |
| -------- | -------- |

## <a name="anyOf_i1"></a>Property `Identifier > anyOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                  | Type               | Title/Description |
| ----------------------------------------- | ------------------ | ----------------- |
| - [@id](#anyOf_i1_@id )                   | string             | -                 |
| - [@type](#anyOf_i1_@type )               | string             | -                 |
| - [schemaAgency](#anyOf_i1_schemaAgency ) | null or string     | schema agency     |
| - [creator](#anyOf_i1_creator )           | More than one type | creator           |
| - [issued](#anyOf_i1_issued )             | More than one type | issued            |
| - [version](#anyOf_i1_version )           | null or string     | version           |
| - [notation](#anyOf_i1_notation )         | null or string     | notation          |

### <a name="anyOf_i1_@id"></a>Property `Identifier > anyOf > item 1 > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="anyOf_i1_@type"></a>Property `Identifier > anyOf > item 1 > @type`

| **Type**    | `string`       |
| ----------- | -------------- |
| **Default** | `"Identifier"` |

### <a name="anyOf_i1_schemaAgency"></a>Property `Identifier > anyOf > item 1 > schemaAgency`

**Title:** schema agency

The name of the agency that issued the identifier

| **Type** | `null or string` |
| -------- | ---------------- |

### <a name="anyOf_i1_creator"></a>Property `Identifier > anyOf > item 1 > creator`

**Title:** creator

the agency that manages the identifier scheme

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                             |
| ------------------------------------------ |
| [item 0](#anyOf_i1_creator_oneOf_i0)       |
| [Organization](#anyOf_i1_creator_oneOf_i1) |
| [item 2](#anyOf_i1_creator_oneOf_i2)       |

#### <a name="anyOf_i1_creator_oneOf_i0"></a>Property `Identifier > anyOf > item 1 > creator > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

#### <a name="anyOf_i1_creator_oneOf_i1"></a>Property `Identifier > anyOf > item 1 > creator > oneOf > Organization`

**Title:** Organization

inline description of the creator

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Organization](./Organization.md) |

#### <a name="anyOf_i1_creator_oneOf_i2"></a>Property `Identifier > anyOf > item 1 > creator > oneOf > item 2`

reference iri of the creator

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="anyOf_i1_issued"></a>Property `Identifier > anyOf > item 1 > issued`

**Title:** issued

The date of formal issuance (e.g., publication) of the Identifier

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#anyOf_i1_issued_anyOf_i0) |
| [item 1](#anyOf_i1_issued_anyOf_i1) |

#### <a name="anyOf_i1_issued_anyOf_i0"></a>Property `Identifier > anyOf > item 1 > issued > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

#### <a name="anyOf_i1_issued_anyOf_i1"></a>Property `Identifier > anyOf > item 1 > issued > anyOf > item 1`

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                               |
| -------------------------------------------- |
| [item 0](#anyOf_i1_issued_anyOf_i1_oneOf_i0) |
| [item 1](#anyOf_i1_issued_anyOf_i1_oneOf_i1) |
| [item 2](#anyOf_i1_issued_anyOf_i1_oneOf_i2) |
| [item 3](#anyOf_i1_issued_anyOf_i1_oneOf_i3) |

##### <a name="anyOf_i1_issued_anyOf_i1_oneOf_i0"></a>Property `Identifier > anyOf > item 1 > issued > anyOf > item 1 > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

##### <a name="anyOf_i1_issued_anyOf_i1_oneOf_i1"></a>Property `Identifier > anyOf > item 1 > issued > anyOf > item 1 > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

##### <a name="anyOf_i1_issued_anyOf_i1_oneOf_i2"></a>Property `Identifier > anyOf > item 1 > issued > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

##### <a name="anyOf_i1_issued_anyOf_i1_oneOf_i3"></a>Property `Identifier > anyOf > item 1 > issued > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

### <a name="anyOf_i1_version"></a>Property `Identifier > anyOf > item 1 > version`

**Title:** version

version of the identifier scheme

| **Type** | `null or string` |
| -------- | ---------------- |

### <a name="anyOf_i1_notation"></a>Property `Identifier > anyOf > item 1 > notation`

**Title:** notation

abbreviation or code from code lists for an identifier

| **Type** | `null or string` |
| -------- | ---------------- |

