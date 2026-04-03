

**Title:** Attribution

An attribution that an agent plays some role

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property               | Type               | Title/Description |
| ---------------------- | ------------------ | ----------------- |
| - [@id](#@id )         | string             | -                 |
| - [@type](#@type )     | string             | -                 |
| + [hadRole](#hadRole ) | string             | role              |
| + [agent](#agent )     | More than one type | agent             |

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

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| Any of(Option)           |
| ------------------------ |
| [Agent](#agent_anyOf_i0) |
| [Link](#agent_anyOf_i1)  |

### <a name="agent_anyOf_i0"></a>Property `Attribution > agent > anyOf > Agent`

**Title:** Agent

inline description of Agent

| **Type**                  | `object`            |
| ------------------------- | ------------------- |
| **Additional properties** | Any type allowed    |
| **Defined in**            | [Agent](./Agent.md) |

### <a name="agent_anyOf_i1"></a>Property `Attribution > agent > anyOf > Link`

**Title:** Link

reference iri of Agent

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

