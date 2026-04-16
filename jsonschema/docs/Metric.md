

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

## <a name="@id"></a>[Optional] Property `Metric > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>[Optional] Property `Metric > @type`

**Requirement:** Optional

| **Type**    | `string`   |
| ----------- | ---------- |
| **Default** | `"Metric"` |

## <a name="expectedDataType"></a>[Mandatory] Property `Metric > expectedDataType`

**Title:** expected datatype

**Requirement:** Mandatory

Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="inDimension"></a>[Mandatory] Property `Metric > inDimension`

**Title:** in dimension

**Requirement:** Mandatory

Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="definition"></a>[Recommended] Property `Metric > definition`

**Title:** definition

**Requirement:** Recommended

Definition of the metric.

| **Type** | `null or string` |
| -------- | ---------------- |

