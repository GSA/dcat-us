# ProvenanceStatement

**Title:** ProvenanceStatement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A single statement about the provenance of a dataset

| Property                 | Type           | Title/Description                                                                              |
| ------------------------ | -------------- | ---------------------------------------------------------------------------------------------- |
| - [@id](#@id )           | string         | -                                                                                              |
| - [@type](#@type )       | string         | -                                                                                              |
| - [label](#label )       | null or string | provenance statement text                                                                      |
| - [labelMap](#labelMap ) | null or object | Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `ProvenanceStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `ProvenanceStatement > @type`

|              |                         |
| ------------ | ----------------------- |
| **Type**     | `string`                |
| **Required** | No                      |
| **Default**  | `"ProvenanceStatement"` |

## <a name="label"></a>Property `ProvenanceStatement > label`

**Title:** provenance statement text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The text of the Provenance Statement

## <a name="labelMap"></a>Property `ProvenanceStatement > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
