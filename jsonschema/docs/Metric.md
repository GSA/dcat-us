# Metric

**Title:** Metric

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                 | Type           | Title/Description |
| ---------------------------------------- | -------------- | ----------------- |
| - [@id](#@id )                           | string         | -                 |
| - [@type](#@type )                       | string         | -                 |
| + [expectedDataType](#expectedDataType ) | string         | expected datatype |
| + [inDimension](#inDimension )           | string         | in dimension      |
| - [definition](#definition )             | null or string | definition        |

## <a name="@id"></a>Property `Metric > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Metric > @type`

|              |            |
| ------------ | ---------- |
| **Type**     | `string`   |
| **Required** | No         |
| **Default**  | `"Metric"` |

## <a name="expectedDataType"></a>Property `Metric > expectedDataType`

**Title:** expected datatype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

## <a name="inDimension"></a>Property `Metric > inDimension`

**Title:** in dimension

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

## <a name="definition"></a>Property `Metric > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the metric.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
