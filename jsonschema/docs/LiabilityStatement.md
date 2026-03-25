

**Title:** LiabilityStatement

A statement of liability for a dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                 | Type           | Title/Description                                                                       |
| ------------------------ | -------------- | --------------------------------------------------------------------------------------- |
| - [@id](#@id )           | string         | -                                                                                       |
| - [@type](#@type )       | string         | -                                                                                       |
| - [label](#label )       | null or string | liability statement text                                                                |
| - [labelMap](#labelMap ) | null or object | Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                        |
| ----------- | ---------------------- |
| **Type**    | `string`               |
| **Default** | `"LiabilityStatement"` |

## <a name="label"></a>Property `label`

**Title:** liability statement text

Full text of the liability statement

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="labelMap"></a>Property `labelMap`

Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

