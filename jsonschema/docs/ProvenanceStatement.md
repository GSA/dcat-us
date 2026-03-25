

**Title:** ProvenanceStatement

A single statement about the provenance of a dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                 | Type           | Title/Description                                                                              |
| ------------------------ | -------------- | ---------------------------------------------------------------------------------------------- |
| - [@id](#@id )           | string         | -                                                                                              |
| - [@type](#@type )       | string         | -                                                                                              |
| - [label](#label )       | null or string | provenance statement text                                                                      |
| - [labelMap](#labelMap ) | null or object | Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                         |
| ----------- | ----------------------- |
| **Type**    | `string`                |
| **Default** | `"ProvenanceStatement"` |

## <a name="label"></a>Property `label`

**Title:** provenance statement text

The text of the Provenance Statement

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="labelMap"></a>Property `labelMap`

Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

