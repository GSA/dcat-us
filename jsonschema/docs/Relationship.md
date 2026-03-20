# Relationship

**Title:** Relationship

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about an item or entity that has some relationship to a dataset and the nature of the relationship

| Property                 | Type   | Title/Description |
| ------------------------ | ------ | ----------------- |
| - [@id](#@id )           | string | -                 |
| - [@type](#@type )       | string | -                 |
| + [hadRole](#hadRole )   | string | role              |
| + [relation](#relation ) | string | relation          |

## <a name="@id"></a>Property `Relationship > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Relationship > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Relationship"` |

## <a name="hadRole"></a>Property `Relationship > hadRole`

**Title:** role

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The function of an entity or agent with respect to a dataset

## <a name="relation"></a>Property `Relationship > relation`

**Title:** relation

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Link to the entity related to the dataset

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
