

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                   | Type               | Title/Description |
| ------------------------------------------ | ------------------ | ----------------- |
| - [@id](#@id )                             | string             | -                 |
| - [@type](#@type )                         | string             | -                 |
| - [address](#address )                     | More than one type | address           |
| + [hasEmail](#hasEmail )                   | string             | Email             |
| - [family-name](#family-name )             | null or string     | family name       |
| + [fn](#fn )                               | string             | formatted name    |
| - [given-name](#given-name )               | null or string     | given name        |
| - [organization-name](#organization-name ) | null or string     | organization name |
| - [tel](#tel )                             | null or string     | telephone         |
| - [title](#title )                         | null or string     | position title    |

## <a name="@id"></a>Property `Kind > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Kind > @type`

| **Type**    | `string` |
| ----------- | -------- |
| **Default** | `"Kind"` |

## <a name="address"></a>Property `Kind > address`

**Title:** address

The address of the contact

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)              |
| --------------------------- |
| [item 0](#address_anyOf_i0) |
| [item 1](#address_anyOf_i1) |

### <a name="address_anyOf_i0"></a>Property `Kind > address > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="address_anyOf_i1"></a>Property `Kind > address > anyOf > item 1`

| **Type** | `array` |
| -------- | ------- |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#address_anyOf_i1_items) | -           |

#### <a name="address_anyOf_i1_items"></a>Kind > address > anyOf > item 1 > item 1 items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                              |
| ------------------------------------------- |
| [Address](#address_anyOf_i1_items_oneOf_i0) |
| [item 1](#address_anyOf_i1_items_oneOf_i1)  |

##### <a name="address_anyOf_i1_items_oneOf_i0"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address`

**Title:** Address

inline address information

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Address](./Address.md) |

##### <a name="address_anyOf_i1_items_oneOf_i1"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of Address

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="hasEmail"></a>Property `Kind > hasEmail`

**Title:** Email

Email address for the contact

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

| Restrictions                      |                                                                                                                                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^mailto:[\w\_\~\!\$\&\'\(\)\*\+\,\;\=\:.-]+@[\w.-]+\.[\w.-]+?$``` [Test](https://regex101.com/?regex=%5Emailto%3A%5B%5Cw%5C_%5C~%5C%21%5C%24%5C%26%5C%27%5C%28%5C%29%5C%2A%5C%2B%5C%2C%5C%3B%5C%3D%5C%3A.-%5D%2B%40%5B%5Cw.-%5D%2B%5C.%5B%5Cw.-%5D%2B%3F%24) |

## <a name="family-name"></a>Property `Kind > family-name`

**Title:** family name

The family name of the contact

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="fn"></a>Property `Kind > fn`

**Title:** formatted name

The formatted text of the name of the contact

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="given-name"></a>Property `Kind > given-name`

**Title:** given name

The given name of the contact

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="organization-name"></a>Property `Kind > organization-name`

**Title:** organization name

The name of the organization to contact

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="tel"></a>Property `Kind > tel`

**Title:** telephone

The telephone number for the contact

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="title"></a>Property `Kind > title`

**Title:** position title

The position role of the person to contact

| **Type** | `null or string` |
| -------- | ---------------- |

