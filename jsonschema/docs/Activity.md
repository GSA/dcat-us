

**Title:** Activity

An activity which a resource could be related to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                 | Type               | Title/Description                                                              |
| ------------------------ | ------------------ | ------------------------------------------------------------------------------ |
| - [@id](#@id )           | string             | -                                                                              |
| - [@type](#@type )       | string             | -                                                                              |
| - [category](#category ) | More than one type | category                                                                       |
| - [label](#label )       | null or string     | label                                                                          |
| - [labelMap](#labelMap ) | null or object     | Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |              |
| ----------- | ------------ |
| **Type**    | `string`     |
| **Default** | `"Activity"` |

## <a name="category"></a>Property `category`

**Title:** category

The category of the Activity

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                |
| ----------------------------- |
| [item 0](#category_anyOf_i0)  |
| [Concept](#category_anyOf_i1) |
| [item 2](#category_anyOf_i2)  |

### <a name="category_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="category_anyOf_i1"></a>Property `Concept`

**Title:** Concept

inline description of the category

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="category_anyOf_i2"></a>Property `item 2`

reference iri of the category

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="label"></a>Property `label`

**Title:** label

A human-readable label for the activity

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="labelMap"></a>Property `labelMap`

Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

