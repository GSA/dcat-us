

**Title:** Metric

A standard used to measure one aspect of data quality

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Metric",
    "expectedDataType": "xsd:decimal",
    "inDimension": "https://example.gov/dimensions/completeness",
    "definition": "Percentage of non-null values in the dataset."
}
```

| Property                                 | Type           | Title/Description |
| ---------------------------------------- | -------------- | ----------------- |
| - [@id](#@id )                           | string         | -                 |
| - [@type](#@type )                       | string         | -                 |
| + [expectedDataType](#expectedDataType ) | string         | expected datatype |
| + [inDimension](#inDimension )           | string         | in dimension      |
| - [definition](#definition )             | null or string | definition        |

## <a name="@id"></a>[Optional] Property `Metric > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/metrics/record-completeness"
```

## <a name="@type"></a>[Optional] Property `Metric > @type`

**Requirement:** Optional

| **Type**    | `string`   |
| ----------- | ---------- |
| **Default** | `"Metric"` |

## <a name="expectedDataType"></a>[Optional] Property `Metric > expectedDataType`

**Title:** expected datatype

**Requirement:** Optional

Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"xsd:decimal"
```

```json
"xsd:double"
```

## <a name="inDimension"></a>[Optional] Property `Metric > inDimension`

**Title:** in dimension

**Requirement:** Optional

Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"https://example.gov/dimensions/completeness"
```

```json
"https://www.w3.org/TR/vocab-dqv/#dqv:completeness"
```

## <a name="definition"></a>[Optional] Property `Metric > definition`

**Title:** definition

**Requirement:** Optional

Definition of the metric.

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"Percentage of non-null values in the dataset."
```

```json
"The percentage of non-null values for required fields in a dataset. A value of 1.0 indicates 100% completeness."
```

