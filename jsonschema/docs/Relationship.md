

**Title:** Relationship

Information about an item or entity that has some relationship to a dataset and the nature of the relationship

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                 | Type   | Title/Description |
| ------------------------ | ------ | ----------------- |
| - [@id](#@id )           | string | -                 |
| - [@type](#@type )       | string | -                 |
| + [hadRole](#hadRole )   | string | role              |
| + [relation](#relation ) | string | relation          |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                  |
| ----------- | ---------------- |
| **Type**    | `string`         |
| **Default** | `"Relationship"` |

## <a name="hadRole"></a>Property `hadRole`

**Title:** role

The function of an entity or agent with respect to a dataset

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="relation"></a>Property `relation`

**Title:** relation

Link to the entity related to the dataset

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

