

**Title:** Relationship

Information about an item or entity that has some relationship to a dataset and the nature of the relationship

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                 | Type   | Title/Description |
| ------------------------ | ------ | ----------------- |
| - [@id](#@id )           | string | -                 |
| - [@type](#@type )       | string | -                 |
| + [hadRole](#hadRole )   | string | role              |
| + [relation](#relation ) | string | relation          |

## <a name="@id"></a>Property `Relationship > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Relationship > @type`

| **Type**    | `string`         |
| ----------- | ---------------- |
| **Default** | `"Relationship"` |

## <a name="hadRole"></a>Property `Relationship > hadRole`

**Title:** role

The function of an entity or agent with respect to a dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="relation"></a>Property `Relationship > relation`

**Title:** relation

The entity related to the dataset. This string should unambiguously identify the related resource using an appropriate identifier.

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

