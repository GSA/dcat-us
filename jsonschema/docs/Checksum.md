# Checksum

**Title:** Checksum

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A mechanism that can be used to verify that the contents of a distribution have not changed

| Property                           | Type   | Title/Description |
| ---------------------------------- | ------ | ----------------- |
| - [@id](#@id )                     | string | -                 |
| - [@type](#@type )                 | string | -                 |
| + [algorithm](#algorithm )         | string | algorithm         |
| + [checksumValue](#checksumValue ) | string | checksum value    |

## <a name="@id"></a>Property `Checksum > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Checksum > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Checksum"` |

## <a name="algorithm"></a>Property `Checksum > algorithm`

**Title:** algorithm

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The algorithm used to produce the checksum

## <a name="checksumValue"></a>Property `Checksum > checksumValue`

**Title:** checksum value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A lower case hexadecimal encoded digest value produced using a specific algorithm

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
