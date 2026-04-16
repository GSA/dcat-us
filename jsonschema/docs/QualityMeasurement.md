

**Title:** QualityMeasurement

A single measurement of one metric

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

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

## <a name="@type"></a>[Optional] Property `QualityMeasurement > @type`

**Requirement:** Optional

| **Type**    | `string`               |
| ----------- | ---------------------- |
| **Default** | `"QualityMeasurement"` |

## <a name="isMeasurementOf"></a>[Mandatory] Property `QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

**Requirement:** Mandatory

The metric being observed

| **Type**                  | `object`              |
| ------------------------- | --------------------- |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | [Metric](./Metric.md) |

## <a name="value"></a>[Mandatory] Property `QualityMeasurement > value`

**Title:** value

**Requirement:** Mandatory

The value computed by metric

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="unitMeasure"></a>[Optional] Property `QualityMeasurement > unitMeasure`

**Title:** unit of measure

**Requirement:** Optional

Unit of measure associated with the value

| **Type** | `null or string` |
| -------- | ---------------- |

