# LiabilityStatement

**Title:** LiabilityStatement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A statement of liability for a dataset

| Property                 | Type           | Title/Description                                                                       |
| ------------------------ | -------------- | --------------------------------------------------------------------------------------- |
| - [@id](#@id )           | string         | -                                                                                       |
| - [@type](#@type )       | string         | -                                                                                       |
| - [label](#label )       | null or string | liability statement text                                                                |
| - [labelMap](#labelMap ) | null or object | Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `LiabilityStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `LiabilityStatement > @type`

|              |                        |
| ------------ | ---------------------- |
| **Type**     | `string`               |
| **Required** | No                     |
| **Default**  | `"LiabilityStatement"` |

## <a name="label"></a>Property `LiabilityStatement > label`

**Title:** liability statement text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Full text of the liability statement

## <a name="labelMap"></a>Property `LiabilityStatement > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
