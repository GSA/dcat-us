

**Title:** QualityMeasurement

A single measurement of one metric

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                               | Type               | Title/Description |
| -------------------------------------- | ------------------ | ----------------- |
| - [@id](#@id )                         | string             | -                 |
| - [@type](#@type )                     | string             | -                 |
| + [isMeasurementOf](#isMeasurementOf ) | More than one type | is measurement of |
| + [value](#value )                     | string             | value             |
| - [unitMeasure](#unitMeasure )         | null or string     | unit of measure   |

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

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| One of(Option)                      |
| ----------------------------------- |
| [Metric](#isMeasurementOf_oneOf_i0) |
| [Link](#isMeasurementOf_oneOf_i1)   |

### <a name="isMeasurementOf_oneOf_i0"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric`

**Title:** Metric

inline description of Metric

| **Type**                  | `object`              |
| ------------------------- | --------------------- |
| **Additional properties** | Any type allowed      |
| **Defined in**            | [Metric](./Metric.md) |

### <a name="isMeasurementOf_oneOf_i1"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Link`

**Title:** Link

reference iri of Metric

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

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

