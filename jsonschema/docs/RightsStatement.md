# RightsStatement

**Title:** RightsStatement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A statement about rights held with respect to another item

| Property                                     | Type           | Title/Description                                                                     |
| -------------------------------------------- | -------------- | ------------------------------------------------------------------------------------- |
| - [@id](#@id )                               | string         | -                                                                                     |
| - [@type](#@type )                           | string         | -                                                                                     |
| - [attributionText](#attributionText )       | null or string | attribution text                                                                      |
| - [attributionTextMap](#attributionTextMap ) | null or object | Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `RightsStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `RightsStatement > @type`

|              |                     |
| ------------ | ------------------- |
| **Type**     | `string`            |
| **Required** | No                  |
| **Default**  | `"RightsStatement"` |

## <a name="attributionText"></a>Property `RightsStatement > attributionText`

**Title:** attribution text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The custom attribution text for the rights statement

## <a name="attributionTextMap"></a>Property `RightsStatement > attributionTextMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
