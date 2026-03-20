# MediaType

**Title:** MediaType

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about a specific file format

| Property                 | Type           | Title/Description                                                          |
| ------------------------ | -------------- | -------------------------------------------------------------------------- |
| - [@id](#@id )           | string         | -                                                                          |
| - [@type](#@type )       | string         | -                                                                          |
| - [label](#label )       | null or string | label                                                                      |
| - [labelMap](#labelMap ) | null or object | Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `MediaType > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `MediaType > @type`

|              |               |
| ------------ | ------------- |
| **Type**     | `string`      |
| **Required** | No            |
| **Default**  | `"MediaType"` |

## <a name="label"></a>Property `MediaType > label`

**Title:** label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The denomination of the Media Type

## <a name="labelMap"></a>Property `MediaType > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
