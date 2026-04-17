

**Title:** Relationship

Additional information about how one resource is related to another

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Relationship",
    "hadRole": "isInputTo",
    "relation": "https://example.gov/models/climate-prediction"
}
```

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

**Example:**

```json
"https://example.gov/relationships/dataset-001-data-provider"
```

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

**Examples:**

```json
"isInputTo"
```

```json
"dataProvider"
```

## <a name="relation"></a>[Mandatory] Property `Relationship > relation`

**Title:** relation

**Requirement:** Mandatory

The entity related to the dataset. This string should unambiguously identify the related resource using an appropriate identifier.

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"https://example.gov/models/climate-prediction"
```

```json
"https://example.gov/organizations/national-weather-service"
```

