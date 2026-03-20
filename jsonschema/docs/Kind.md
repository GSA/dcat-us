# Kind

**Title:** Kind

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Contact information for an individual or entity

| Property                                   | Type           | Title/Description |
| ------------------------------------------ | -------------- | ----------------- |
| - [@id](#@id )                             | string         | -                 |
| - [@type](#@type )                         | string         | -                 |
| - [address](#address )                     | Combination    | address           |
| + [hasEmail](#hasEmail )                   | string         | Email             |
| - [family-name](#family-name )             | null or string | family name       |
| + [fn](#fn )                               | string         | formatted name    |
| - [given-name](#given-name )               | null or string | given name        |
| - [organization-name](#organization-name ) | null or string | organization name |
| - [tel](#tel )                             | null or string | telephone         |
| - [title](#title )                         | null or string | position title    |

## <a name="@id"></a>Property `Kind > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Kind > @type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"Kind"` |

## <a name="address"></a>Property `Kind > address`

**Title:** address

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The address of the contact

| Any of(Option)              |
| --------------------------- |
| [item 0](#address_anyOf_i0) |
| [item 1](#address_anyOf_i1) |

### <a name="address_anyOf_i0"></a>Property `Kind > address > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="address_anyOf_i1"></a>Property `Kind > address > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#address_anyOf_i1_items) | -           |

#### <a name="address_anyOf_i1_items"></a>Kind > address > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                              |
| ------------------------------------------- |
| [Address](#address_anyOf_i1_items_oneOf_i0) |
| [item 1](#address_anyOf_i1_items_oneOf_i1)  |

##### <a name="address_anyOf_i1_items_oneOf_i0"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address`

**Title:** Address

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/address |

**Description:** inline address information

| Property                                                             | Type           | Title/Description   |
| -------------------------------------------------------------------- | -------------- | ------------------- |
| - [@id](#address_anyOf_i1_items_oneOf_i0_@id )                       | string         | -                   |
| - [@type](#address_anyOf_i1_items_oneOf_i0_@type )                   | string         | -                   |
| - [country-name](#address_anyOf_i1_items_oneOf_i0_country-name )     | null or string | country             |
| - [locality](#address_anyOf_i1_items_oneOf_i0_locality )             | null or string | locality            |
| - [postal-code](#address_anyOf_i1_items_oneOf_i0_postal-code )       | null or string | postal code         |
| - [region](#address_anyOf_i1_items_oneOf_i0_region )                 | null or string | administrative area |
| - [street-address](#address_anyOf_i1_items_oneOf_i0_street-address ) | null or string | street address      |

###### <a name="address_anyOf_i1_items_oneOf_i0_@id"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="address_anyOf_i1_items_oneOf_i0_@type"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Address"` |

###### <a name="address_anyOf_i1_items_oneOf_i0_country-name"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > country-name`

**Title:** country

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The country of the Address

###### <a name="address_anyOf_i1_items_oneOf_i0_locality"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > locality`

**Title:** locality

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The city of the Address

###### <a name="address_anyOf_i1_items_oneOf_i0_postal-code"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > postal-code`

**Title:** postal code

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The postal code of the Address

###### <a name="address_anyOf_i1_items_oneOf_i0_region"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > region`

**Title:** administrative area

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The administrative area of the Address. Depending on the country, this corresponds to a province, a county, a region, or a state

###### <a name="address_anyOf_i1_items_oneOf_i0_street-address"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > street-address`

**Title:** street address

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The street name and civic number of an Address

##### <a name="address_anyOf_i1_items_oneOf_i1"></a>Property `Kind > address > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Address

## <a name="hasEmail"></a>Property `Kind > hasEmail`

**Title:** Email

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Email address for the contact

| Restrictions                      |                                                                                                                                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^mailto:[\w\_\~\!\$\&\'\(\)\*\+\,\;\=\:.-]+@[\w.-]+\.[\w.-]+?$``` [Test](https://regex101.com/?regex=%5Emailto%3A%5B%5Cw%5C_%5C~%5C%21%5C%24%5C%26%5C%27%5C%28%5C%29%5C%2A%5C%2B%5C%2C%5C%3B%5C%3D%5C%3A.-%5D%2B%40%5B%5Cw.-%5D%2B%5C.%5B%5Cw.-%5D%2B%3F%24) |

## <a name="family-name"></a>Property `Kind > family-name`

**Title:** family name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The family name of the contact

## <a name="fn"></a>Property `Kind > fn`

**Title:** formatted name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The formatted text of the name of the contact

## <a name="given-name"></a>Property `Kind > given-name`

**Title:** given name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The given name of the contact

## <a name="organization-name"></a>Property `Kind > organization-name`

**Title:** organization name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The name of the organization to contact

## <a name="tel"></a>Property `Kind > tel`

**Title:** telephone

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The telephone number for the contact

## <a name="title"></a>Property `Kind > title`

**Title:** position title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The position role of the person to contact

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
