

**Title:** Attribution

An attribution that an agent plays some role

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property               | Type               | Title/Description |
| ---------------------- | ------------------ | ----------------- |
| - [@id](#@id )         | string             | -                 |
| - [@type](#@type )     | string             | -                 |
| + [hadRole](#hadRole ) | string             | role              |
| + [agent](#agent )     | More than one type | agent             |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                 |
| ----------- | --------------- |
| **Type**    | `string`        |
| **Default** | `"Attribution"` |

## <a name="hadRole"></a>Property `hadRole`

**Title:** role

The function of an entity or agent with respect to another entity or resource

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="agent"></a>Property `agent`

**Title:** agent

The agent that plays a role in the resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)            |
| ------------------------- |
| [Agent](#agent_oneOf_i0)  |
| [item 1](#agent_oneOf_i1) |

### <a name="agent_oneOf_i0"></a>Property `Agent`

**Title:** Agent

inline description of Agent

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Additional properties** | Any type allowed    |
| **Defined in**            | [Agent](./Agent.md) |

### <a name="agent_oneOf_i1"></a>Property `item 1`

reference iri of Agent

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

