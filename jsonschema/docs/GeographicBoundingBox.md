

**Title:** GeographicBoundingBox

A bounding box in latitude and longitude

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                           | Type   | Title/Description       |
| -------------------------------------------------- | ------ | ----------------------- |
| - [@id](#@id )                                     | string | -                       |
| - [@type](#@type )                                 | string | -                       |
| + [eastBoundingLongitude](#eastBoundingLongitude ) | string | east bounding longitude |
| + [northBoundingLatitude](#northBoundingLatitude ) | string | north bounding latitude |
| + [southBoundingLatitude](#southBoundingLatitude ) | string | south bouding latitude  |
| + [westBoundingLongitude](#westBoundingLongitude ) | string | west bounding longitude |

## <a name="@id"></a>Property `GeographicBoundingBox > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `GeographicBoundingBox > @type`

| **Type**    | `string`                  |
| ----------- | ------------------------- |
| **Default** | `"GeographicBoundingBox"` |

## <a name="eastBoundingLongitude"></a>Property `GeographicBoundingBox > eastBoundingLongitude`

**Title:** east bounding longitude

East bound longitude in decimal degrees

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="northBoundingLatitude"></a>Property `GeographicBoundingBox > northBoundingLatitude`

**Title:** north bounding latitude

North bound latitude in decimal degrees

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="southBoundingLatitude"></a>Property `GeographicBoundingBox > southBoundingLatitude`

**Title:** south bouding latitude

South bound latitude in decimal degrees

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="westBoundingLongitude"></a>Property `GeographicBoundingBox > westBoundingLongitude`

**Title:** west bounding longitude

West bound longitude in decimal degrees

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

