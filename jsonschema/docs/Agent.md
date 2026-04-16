

**Title:** Agent

An entity that could be involved with a resource

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

**Example:**

```json
"Agent"
```

## <a name="category"></a>[Optional] Property `Agent > category`

**Title:** category

**Requirement:** Optional

The type of the agent that makes the item available

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#category_items)      | A labeled value from an optionally specified concept scheme |

### <a name="category_items"></a>Agent > category > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

## <a name="name"></a>[Mandatory] Property `Agent > name`

**Title:** name

**Requirement:** Mandatory

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

