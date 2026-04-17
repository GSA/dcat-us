

**Title:** Agent

A person, organization, software agent, or other entity involved with a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Agent",
    "name": "National Climate Data Center",
    "category": [
        "https://example.gov/concepts/federal-agency"
    ]
}
```

| Property                 | Type          | Title/Description |
| ------------------------ | ------------- | ----------------- |
| - [@id](#@id )           | string        | -                 |
| - [@type](#@type )       | string        | -                 |
| - [category](#category ) | null or array | category          |
| + [name](#name )         | string        | name              |

## <a name="@id"></a>[Optional] Property `Agent > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/agents/data-steward-001"
```

## <a name="@type"></a>[Optional] Property `Agent > @type`

**Requirement:** Optional

| **Type**    | `string`  |
| ----------- | --------- |
| **Default** | `"Agent"` |

## <a name="category"></a>[Optional] Property `Agent > category`

**Title:** category

**Requirement:** Optional

The type of the agent that makes the item available

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| [Concept](#category_items)      | A controlled term or label, optionally drawn from a concept scheme |

### <a name="category_items"></a>Agent > category > Concept

**Title:** Concept

A controlled term or label, optionally drawn from a concept scheme

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

## <a name="name"></a>[Optional] Property `Agent > name`

**Title:** name

**Requirement:** Optional

The name of the agent

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"National Climate Data Center"
```

```json
"U.S. Department of Commerce Data Stewardship Office"
```

