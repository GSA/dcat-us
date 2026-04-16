

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

## <a name="@id"></a>[Optional] Property `Relationship > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>[Optional] Property `Relationship > @type`

**Requirement:** Optional

| **Type**    | `string`         |
| ----------- | ---------------- |
| **Default** | `"Relationship"` |

## <a name="hadRole"></a>[Mandatory] Property `Relationship > hadRole`

**Title:** role

**Requirement:** Mandatory

The function of an entity or agent with respect to a dataset

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="relation"></a>[Mandatory] Property `Relationship > relation`

**Title:** relation

**Requirement:** Mandatory

The entity related to the dataset. This string should unambiguously identify the related resource using an appropriate identifier.

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

