

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                              |
| ------------------------------------------- |
| [Simple string identifier](#anyOf_i0)       |
| [Identifier as a complex object](#anyOf_i1) |

## <a name="anyOf_i0"></a>Property `Identifier > anyOf > Simple string identifier`

**Title:** Simple string identifier

| **Type** | `string` |
| -------- | -------- |

## <a name="anyOf_i1"></a>Property `Identifier > anyOf > Identifier as a complex object`

**Title:** Identifier as a complex object

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

### <a name="anyOf_i1_@id"></a>Property `Identifier > anyOf > Identifier as a complex object > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="anyOf_i1_@type"></a>Property `Identifier > anyOf > Identifier as a complex object > @type`

| **Type**    | `string`       |
| ----------- | -------------- |
| **Default** | `"Identifier"` |

### <a name="anyOf_i1_schemaAgency"></a>Property `Identifier > anyOf > Identifier as a complex object > schemaAgency`

**Title:** schema agency

The name of the agency that issued the identifier

| **Type** | `null or string` |
| -------- | ---------------- |

### <a name="anyOf_i1_creator"></a>Property `Identifier > anyOf > Identifier as a complex object > creator`

**Title:** creator

the agency that manages the identifier scheme

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                               |
| ------------------------------------------------------------ |
| [Null allowed when not required](#anyOf_i1_creator_anyOf_i0) |
| [Organization](#anyOf_i1_creator_anyOf_i1)                   |

#### <a name="anyOf_i1_creator_anyOf_i0"></a>Property `Identifier > anyOf > Identifier as a complex object > creator > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

#### <a name="anyOf_i1_creator_anyOf_i1"></a>Property `Identifier > anyOf > Identifier as a complex object > creator > anyOf > Organization`

**Title:** Organization

inline description of the creator

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Organization](./Organization.md) |

### <a name="anyOf_i1_issued"></a>Property `Identifier > anyOf > Identifier as a complex object > issued`

**Title:** issued

The date of formal issuance (e.g., publication) of the Identifier

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [Null allowed when not required](#anyOf_i1_issued_anyOf_i0) |
| [Date string](#anyOf_i1_issued_anyOf_i1)                    |

#### <a name="anyOf_i1_issued_anyOf_i0"></a>Property `Identifier > anyOf > Identifier as a complex object > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

#### <a name="anyOf_i1_issued_anyOf_i1"></a>Property `Identifier > anyOf > Identifier as a complex object > issued > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#anyOf_i1_issued_anyOf_i1_anyOf_i0) |
| [item 1](#anyOf_i1_issued_anyOf_i1_anyOf_i1) |
| [item 2](#anyOf_i1_issued_anyOf_i1_anyOf_i2) |
| [item 3](#anyOf_i1_issued_anyOf_i1_anyOf_i3) |

##### <a name="anyOf_i1_issued_anyOf_i1_anyOf_i0"></a>Property `Identifier > anyOf > Identifier as a complex object > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

##### <a name="anyOf_i1_issued_anyOf_i1_anyOf_i1"></a>Property `Identifier > anyOf > Identifier as a complex object > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

##### <a name="anyOf_i1_issued_anyOf_i1_anyOf_i2"></a>Property `Identifier > anyOf > Identifier as a complex object > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

##### <a name="anyOf_i1_issued_anyOf_i1_anyOf_i3"></a>Property `Identifier > anyOf > Identifier as a complex object > issued > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

### <a name="anyOf_i1_version"></a>Property `Identifier > anyOf > Identifier as a complex object > version`

**Title:** version

version of the identifier scheme

| **Type** | `null or string` |
| -------- | ---------------- |

### <a name="anyOf_i1_notation"></a>Property `Identifier > anyOf > Identifier as a complex object > notation`

**Title:** notation

abbreviation or code from code lists for an identifier

| **Type** | `null or string` |
| -------- | ---------------- |

