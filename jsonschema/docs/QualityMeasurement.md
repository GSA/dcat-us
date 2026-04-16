

**Title:** QualityMeasurement

A single measurement of one metric

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "QualityMeasurement",
    "isMeasurementOf": {
        "expectedDataType": "xsd:decimal",
        "inDimension": "https://example.gov/dimensions/completeness"
    },
    "value": "98.5",
    "unitMeasure": "percent"
}
```

| Property                               | Type           | Title/Description |
| -------------------------------------- | -------------- | ----------------- |
| - [@id](#@id )                         | string         | -                 |
| - [@type](#@type )                     | string         | -                 |
| + [isMeasurementOf](#isMeasurementOf ) | object         | is measurement of |
| + [value](#value )                     | string         | value             |
| - [unitMeasure](#unitMeasure )         | null or string | unit of measure   |

## <a name="@id"></a>[Optional] Property `QualityMeasurement > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/quality-measurements/completeness-001"
```

## <a name="@type"></a>[Optional] Property `QualityMeasurement > @type`

**Requirement:** Optional

| **Type**    | `string`               |
| ----------- | ---------------------- |
| **Default** | `"QualityMeasurement"` |

**Example:**

```json
"QualityMeasurement"
```

## <a name="isMeasurementOf"></a>[Mandatory] Property `QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

**Requirement:** Mandatory

The metric being observed

| **Type**                  | `object`              |
| ------------------------- | --------------------- |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | [Metric](./Metric.md) |

**Examples:**

```json
{
    "expectedDataType": "xsd:decimal",
    "inDimension": "https://example.gov/dimensions/completeness"
}
```

```json
{
    "@id": "https://example.gov/metrics/data-completeness-001",
    "@type": "Metric",
    "definition": "The percentage of expected data values that are present in the dataset.",
    "expectedDataType": "xsd:decimal",
    "inDimension": "https://example.gov/concepts/completeness-dimension"
}
```

## <a name="value"></a>[Mandatory] Property `QualityMeasurement > value`

**Title:** value

**Requirement:** Mandatory

The value computed by metric

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Example:**

```json
"98.5"
```

## <a name="unitMeasure"></a>[Optional] Property `QualityMeasurement > unitMeasure`

**Title:** unit of measure

**Requirement:** Optional

Unit of measure associated with the value

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"percent"
```

