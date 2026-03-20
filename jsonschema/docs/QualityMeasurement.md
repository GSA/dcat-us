# QualityMeasurement

**Title:** QualityMeasurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A single measurement of one metric

| Property                               | Type           | Title/Description |
| -------------------------------------- | -------------- | ----------------- |
| - [@id](#@id )                         | string         | -                 |
| - [@type](#@type )                     | string         | -                 |
| + [isMeasurementOf](#isMeasurementOf ) | Combination    | is measurement of |
| + [value](#value )                     | string         | value             |
| - [unitMeasure](#unitMeasure )         | null or string | unit of measure   |

## <a name="@id"></a>Property `QualityMeasurement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `QualityMeasurement > @type`

|              |                        |
| ------------ | ---------------------- |
| **Type**     | `string`               |
| **Required** | No                     |
| **Default**  | `"QualityMeasurement"` |

## <a name="isMeasurementOf"></a>Property `QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The metric being observed

| One of(Option)                      |
| ----------------------------------- |
| [Metric](#isMeasurementOf_oneOf_i0) |
| [item 1](#isMeasurementOf_oneOf_i1) |

### <a name="isMeasurementOf_oneOf_i0"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric`

**Title:** Metric

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | /dcat-us/3.0.0/definitions/metric |

**Description:** inline description of Metric

| Property                                                          | Type           | Title/Description |
| ----------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#isMeasurementOf_oneOf_i0_@id )                           | string         | -                 |
| - [@type](#isMeasurementOf_oneOf_i0_@type )                       | string         | -                 |
| + [expectedDataType](#isMeasurementOf_oneOf_i0_expectedDataType ) | string         | expected datatype |
| + [inDimension](#isMeasurementOf_oneOf_i0_inDimension )           | string         | in dimension      |
| - [definition](#isMeasurementOf_oneOf_i0_definition )             | null or string | definition        |

#### <a name="isMeasurementOf_oneOf_i0_@id"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="isMeasurementOf_oneOf_i0_@type"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric > @type`

|              |            |
| ------------ | ---------- |
| **Type**     | `string`   |
| **Required** | No         |
| **Default**  | `"Metric"` |

#### <a name="isMeasurementOf_oneOf_i0_expectedDataType"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric > expectedDataType`

**Title:** expected datatype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

#### <a name="isMeasurementOf_oneOf_i0_inDimension"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric > inDimension`

**Title:** in dimension

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

#### <a name="isMeasurementOf_oneOf_i0_definition"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > Metric > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the metric.

### <a name="isMeasurementOf_oneOf_i1"></a>Property `QualityMeasurement > isMeasurementOf > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Metric

## <a name="value"></a>Property `QualityMeasurement > value`

**Title:** value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The value computed by metric

## <a name="unitMeasure"></a>Property `QualityMeasurement > unitMeasure`

**Title:** unit of measure

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Unit of measure associated with the value

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
