# Address

**Title:** Address

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A single physical address

| Property                             | Type           | Title/Description   |
| ------------------------------------ | -------------- | ------------------- |
| - [@id](#@id )                       | string         | -                   |
| - [@type](#@type )                   | string         | -                   |
| - [country-name](#country-name )     | null or string | country             |
| - [locality](#locality )             | null or string | locality            |
| - [postal-code](#postal-code )       | null or string | postal code         |
| - [region](#region )                 | null or string | administrative area |
| - [street-address](#street-address ) | null or string | street address      |

## <a name="@id"></a>Property `Address > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Address > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Address"` |

## <a name="country-name"></a>Property `Address > country-name`

**Title:** country

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The country of the Address

## <a name="locality"></a>Property `Address > locality`

**Title:** locality

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The city of the Address

## <a name="postal-code"></a>Property `Address > postal-code`

**Title:** postal code

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The postal code of the Address

## <a name="region"></a>Property `Address > region`

**Title:** administrative area

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The administrative area of the Address. Depending on the country, this corresponds to a province, a county, a region, or a state

## <a name="street-address"></a>Property `Address > street-address`

**Title:** street address

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The street name and civic number of an Address

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
