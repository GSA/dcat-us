

**Title:** Metric

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                 | Type           | Title/Description |
| ---------------------------------------- | -------------- | ----------------- |
| - [@id](#@id )                           | string         | -                 |
| - [@type](#@type )                       | string         | -                 |
| + [expectedDataType](#expectedDataType ) | string         | expected datatype |
| + [inDimension](#inDimension )           | string         | in dimension      |
| - [definition](#definition )             | null or string | definition        |

## <a name="@id"></a>Property `Metric > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Metric > @type`

| **Type**    | `string`   |
| ----------- | ---------- |
| **Default** | `"Metric"` |

## <a name="expectedDataType"></a>Property `Metric > expectedDataType`

**Title:** expected datatype

Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="inDimension"></a>Property `Metric > inDimension`

**Title:** in dimension

Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="definition"></a>Property `Metric > definition`

**Title:** definition

Definition of the metric.

| **Type** | `null or string` |
| -------- | ---------------- |

