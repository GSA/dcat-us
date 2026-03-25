

**Title:** Address

A single physical address

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

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

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Address > @type`

|             |             |
| ----------- | ----------- |
| **Type**    | `string`    |
| **Default** | `"Address"` |

## <a name="country-name"></a>Property `Address > country-name`

**Title:** country

The country of the Address

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="locality"></a>Property `Address > locality`

**Title:** locality

The city of the Address

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="postal-code"></a>Property `Address > postal-code`

**Title:** postal code

The postal code of the Address

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="region"></a>Property `Address > region`

**Title:** administrative area

The administrative area of the Address. Depending on the country, this corresponds to a province, a county, a region, or a state

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="street-address"></a>Property `Address > street-address`

**Title:** street address

The street name and civic number of an Address

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

