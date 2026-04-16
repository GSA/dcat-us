

**Title:** Activity

An activity which a resource could be related to

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Activity",
    "label": "Data Collection",
    "category": [
        "https://example.gov/concepts/data-collection"
    ]
}
```

| Property                 | Type          | Title/Description |
| ------------------------ | ------------- | ----------------- |
| - [@id](#@id )           | string        | -                 |
| - [@type](#@type )       | string        | -                 |
| - [category](#category ) | null or array | category          |
| + [label](#label )       | string        | label             |

## <a name="@id"></a>[Optional] Property `Activity > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/activities/data-processing-001"
```

## <a name="@type"></a>[Optional] Property `Activity > @type`

**Requirement:** Optional

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Activity"` |

**Example:**

```json
"Activity"
```

## <a name="category"></a>[Optional] Property `Activity > category`

**Title:** category

**Requirement:** Optional

List of categories for the Activity

| **Type** | `null or array` |
| -------- | --------------- |

**Examples:**

```json
[
    "https://example.gov/concepts/data-collection"
]
```

```json
[
    {
        "@id": "https://example.gov/concepts/data-processing",
        "@type": "Concept",
        "prefLabel": "Data Processing",
        "definition": "Activities related to processing and transforming raw data into usable formats.",
        "inScheme": {
            "@id": "https://example.gov/concept-schemes/activity-types",
            "@type": "ConceptScheme",
            "title": "Activity Types"
        }
    }
]
```

| Each item of this array must be | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| [Concept](#category_items)      | A labeled value from an optionally specified concept scheme |

### <a name="category_items"></a>Activity > category > Concept

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

## <a name="label"></a>[Mandatory] Property `Activity > label`

**Title:** label

**Requirement:** Mandatory

A human-readable label for the activity

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"Data Collection"
```

```json
"Data Processing and Quality Assurance"
```

