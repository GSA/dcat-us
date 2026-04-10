

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

## <a name="@id"></a>Property `QualityMeasurement > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `QualityMeasurement > @type`

| **Type**    | `string`               |
| ----------- | ---------------------- |
| **Default** | `"QualityMeasurement"` |

## <a name="isMeasurementOf"></a>Property `QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

The metric being observed

| **Type**                  | `object`              |
| ------------------------- | --------------------- |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | [Metric](./Metric.md) |

## <a name="value"></a>Property `QualityMeasurement > value`

**Title:** value

The value computed by metric

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="unitMeasure"></a>Property `QualityMeasurement > unitMeasure`

**Title:** unit of measure

Unit of measure associated with the value

| **Type** | `null or string` |
| -------- | ---------------- |

