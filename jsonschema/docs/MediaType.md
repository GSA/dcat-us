

**Title:** MediaType

Information about a specific file format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                 | Type           | Title/Description                                                          |
| ------------------------ | -------------- | -------------------------------------------------------------------------- |
| - [@id](#@id )           | string         | -                                                                          |
| - [@type](#@type )       | string         | -                                                                          |
| - [label](#label )       | null or string | label                                                                      |
| - [labelMap](#labelMap ) | null or object | Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |               |
| ----------- | ------------- |
| **Type**    | `string`      |
| **Default** | `"MediaType"` |

## <a name="label"></a>Property `label`

**Title:** label

The denomination of the Media Type

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="labelMap"></a>Property `labelMap`

Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

