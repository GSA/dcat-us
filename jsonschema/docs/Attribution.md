

**Title:** Attribution

A responsibility that an agent has for a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Attribution",
    "hadRole": "Data Steward",
    "agent": {
        "name": "Environmental Data Management Office"
    }
}
```

| Property               | Type   | Title/Description |
| ---------------------- | ------ | ----------------- |
| - [@id](#@id )         | string | -                 |
| - [@type](#@type )     | string | -                 |
| + [hadRole](#hadRole ) | string | role              |
| + [agent](#agent )     | object | agent             |

## <a name="@id"></a>[Optional] Property `Attribution > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/attributions/dataset-steward-001"
```

## <a name="@type"></a>[Optional] Property `Attribution > @type`

**Requirement:** Optional

| **Type**    | `string`        |
| ----------- | --------------- |
| **Default** | `"Attribution"` |

## <a name="hadRole"></a>[Optional] Property `Attribution > hadRole`

**Title:** role

**Requirement:** Optional

The function of an entity or agent with respect to another entity or resource

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Example:**

```json
"Data Steward"
```

## <a name="agent"></a>[Optional] Property `Attribution > agent`

**Title:** agent

**Requirement:** Optional

The agent that plays a role in the resource

| **Type**                  | `object`            |
| ------------------------- | ------------------- |
| **Required**              | Yes                 |
| **Additional properties** | Any type allowed    |
| **Defined in**            | [Agent](./Agent.md) |

