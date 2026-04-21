

**Title:** QualityMeasurement

A measurement of a resource against a specific quality metric

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

## <a name="isMeasurementOf"></a>[Optional] Property `QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

**Requirement:** Optional

The metric being observed

| **Type**                  | `object`              |
| ------------------------- | --------------------- |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | [Metric](./Metric.md) |

## <a name="value"></a>[Optional] Property `QualityMeasurement > value`

**Title:** value

**Requirement:** Optional

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

