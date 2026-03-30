

**Title:** Identifier

Information about an identifier scheme

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                         | Type               | Title/Description |
| -------------------------------- | ------------------ | ----------------- |
| - [@id](#@id )                   | string             | -                 |
| - [@type](#@type )               | string             | -                 |
| - [schemaAgency](#schemaAgency ) | null or string     | schema agency     |
| - [creator](#creator )           | More than one type | creator           |
| - [issued](#issued )             | More than one type | issued            |
| - [version](#version )           | null or string     | version           |
| - [notation](#notation )         | null or string     | notation          |

## <a name="@id"></a>Property `Identifier > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Identifier > @type`

| **Type**    | `string`       |
| ----------- | -------------- |
| **Default** | `"Identifier"` |

## <a name="schemaAgency"></a>Property `Identifier > schemaAgency`

**Title:** schema agency

The name of the agency that issued the identifier

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="creator"></a>Property `Identifier > creator`

**Title:** creator

the agency that manages the identifier scheme

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                    |
| --------------------------------- |
| [item 0](#creator_oneOf_i0)       |
| [Organization](#creator_oneOf_i1) |
| [item 2](#creator_oneOf_i2)       |

### <a name="creator_oneOf_i0"></a>Property `Identifier > creator > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="creator_oneOf_i1"></a>Property `Identifier > creator > oneOf > Organization`

**Title:** Organization

inline description of the creator

| **Type**                  | `object`                          |
| ------------------------- | --------------------------------- |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | [Organization](./Organization.md) |

### <a name="creator_oneOf_i2"></a>Property `Identifier > creator > oneOf > item 2`

reference iri of the creator

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="issued"></a>Property `Identifier > issued`

**Title:** issued

The date of formal issuance (e.g., publication) of the Identifier

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Identifier > issued > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `Identifier > issued > anyOf > item 1`

| **Type** | More than one type |
| -------- | ------------------ |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 0`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="version"></a>Property `Identifier > version`

**Title:** version

version of the identifier scheme

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="notation"></a>Property `Identifier > notation`

**Title:** notation

abbreviation or code from code lists for an identifier

| **Type** | `null or string` |
| -------- | ---------------- |

