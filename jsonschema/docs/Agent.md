

**Title:** Agent

An entity that could be involved with a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                 | Type               | Title/Description |
| ------------------------ | ------------------ | ----------------- |
| - [@id](#@id )           | string             | -                 |
| - [@type](#@type )       | string             | -                 |
| - [category](#category ) | More than one type | category          |
| + [name](#name )         | string             | name              |

## <a name="@id"></a>Property `Agent > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Agent > @type`

| **Type**    | `string`  |
| ----------- | --------- |
| **Default** | `"Agent"` |

## <a name="category"></a>Property `Agent > category`

**Title:** category

The type of the agent that makes the item available

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#category_oneOf_i0) |
| [Concept](#category_oneOf_i1)                        |
| [Link](#category_oneOf_i2)                           |

### <a name="category_oneOf_i0"></a>Property `Agent > category > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="category_oneOf_i1"></a>Property `Agent > category > oneOf > Concept`

**Title:** Concept

inline description of the agent type

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="category_oneOf_i2"></a>Property `Agent > category > oneOf > Link`

**Title:** Link

reference iri of the agent type

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="name"></a>Property `Agent > name`

**Title:** name

The name of the agent

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

