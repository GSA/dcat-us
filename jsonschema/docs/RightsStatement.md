

**Title:** RightsStatement

A statement about rights held with respect to another item

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                     | Type           | Title/Description                                                                     |
| -------------------------------------------- | -------------- | ------------------------------------------------------------------------------------- |
| - [@id](#@id )                               | string         | -                                                                                     |
| - [@type](#@type )                           | string         | -                                                                                     |
| - [attributionText](#attributionText )       | null or string | attribution text                                                                      |
| - [attributionTextMap](#attributionTextMap ) | null or object | Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                     |
| ----------- | ------------------- |
| **Type**    | `string`            |
| **Default** | `"RightsStatement"` |

## <a name="attributionText"></a>Property `attributionText`

**Title:** attribution text

The custom attribution text for the rights statement

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="attributionTextMap"></a>Property `attributionTextMap`

Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

