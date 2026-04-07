

**Title:** Agent

An entity that could be involved with a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                 | Type          | Title/Description |
| ------------------------ | ------------- | ----------------- |
| - [@id](#@id )           | string        | -                 |
| - [@type](#@type )       | string        | -                 |
| - [category](#category ) | null or array | category          |
| + [name](#name )         | string        | name              |

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

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be   | Description |
| --------------------------------- | ----------- |
| [category items](#category_items) | -           |

### <a name="category_items"></a>Agent > category > category items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Concept](#category_items_anyOf_i0) |
| [Link](#category_items_anyOf_i1)    |

#### <a name="category_items_anyOf_i0"></a>Property `Agent > category > category items > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

#### <a name="category_items_anyOf_i1"></a>Property `Agent > category > category items > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="name"></a>Property `Agent > name`

**Title:** name

The name of the agent

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

