

**Title:** Attribution

An attribution that an agent plays some role

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property               | Type   | Title/Description |
| ---------------------- | ------ | ----------------- |
| - [@id](#@id )         | string | -                 |
| - [@type](#@type )     | string | -                 |
| + [hadRole](#hadRole ) | string | role              |
| + [agent](#agent )     | object | agent             |

## <a name="@id"></a>Property `Attribution > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Attribution > @type`

| **Type**    | `string`        |
| ----------- | --------------- |
| **Default** | `"Attribution"` |

## <a name="hadRole"></a>Property `Attribution > hadRole`

**Title:** role

The function of an entity or agent with respect to another entity or resource

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="agent"></a>Property `Attribution > agent`

**Title:** agent

The agent that plays a role in the resource

| **Type**                  | `object`            |
| ------------------------- | ------------------- |
| **Required**              | Yes                 |
| **Additional properties** | Any type allowed    |
| **Defined in**            | [Agent](./Agent.md) |

