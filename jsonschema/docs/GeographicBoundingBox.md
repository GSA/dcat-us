# GeographicBoundingBox

**Title:** GeographicBoundingBox

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A bounding box in latitude and longitude

| Property                                           | Type   | Title/Description       |
| -------------------------------------------------- | ------ | ----------------------- |
| - [@id](#@id )                                     | string | -                       |
| - [@type](#@type )                                 | string | -                       |
| + [eastBoundingLongitude](#eastBoundingLongitude ) | string | east bounding longitude |
| + [northBoundingLatitude](#northBoundingLatitude ) | string | north bounding latitude |
| + [southBoundingLatitude](#southBoundingLatitude ) | string | south bouding latitude  |
| + [westBoundingLongitude](#westBoundingLongitude ) | string | west bounding longitude |

## <a name="@id"></a>Property `GeographicBoundingBox > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `GeographicBoundingBox > @type`

|              |                           |
| ------------ | ------------------------- |
| **Type**     | `string`                  |
| **Required** | No                        |
| **Default**  | `"GeographicBoundingBox"` |

## <a name="eastBoundingLongitude"></a>Property `GeographicBoundingBox > eastBoundingLongitude`

**Title:** east bounding longitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** East bound longitude in decimal degrees

## <a name="northBoundingLatitude"></a>Property `GeographicBoundingBox > northBoundingLatitude`

**Title:** north bounding latitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** North bound latitude in decimal degrees

## <a name="southBoundingLatitude"></a>Property `GeographicBoundingBox > southBoundingLatitude`

**Title:** south bouding latitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** South bound latitude in decimal degrees

## <a name="westBoundingLongitude"></a>Property `GeographicBoundingBox > westBoundingLongitude`

**Title:** west bounding longitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** West bound longitude in decimal degrees

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
