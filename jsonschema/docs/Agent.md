

**Title:** Agent

An entity that could be involved with a resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                 | Type               | Title/Description |
| ------------------------ | ------------------ | ----------------- |
| - [@id](#@id )           | string             | -                 |
| - [@type](#@type )       | string             | -                 |
| - [category](#category ) | More than one type | category          |
| + [name](#name )         | string             | name              |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |           |
| ----------- | --------- |
| **Type**    | `string`  |
| **Default** | `"Agent"` |

## <a name="category"></a>Property `category`

**Title:** category

The type of the agent that makes the item available

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="category_oneOf_i1"></a>Property `Concept`

**Title:** Concept

inline description of the agent type

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="category_oneOf_i2"></a>Property `item 2`

reference iri of the agent type

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="name"></a>Property `name`

**Title:** name

The name of the agent

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

