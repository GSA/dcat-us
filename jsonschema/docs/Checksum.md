

**Title:** Checksum

A mechanism that can be used to verify that the contents of a distribution have not changed

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                           | Type   | Title/Description |
| ---------------------------------- | ------ | ----------------- |
| - [@id](#@id )                     | string | -                 |
| - [@type](#@type )                 | string | -                 |
| + [algorithm](#algorithm )         | string | algorithm         |
| + [checksumValue](#checksumValue ) | string | checksum value    |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |              |
| ----------- | ------------ |
| **Type**    | `string`     |
| **Default** | `"Checksum"` |

## <a name="algorithm"></a>Property `algorithm`

**Title:** algorithm

The algorithm used to produce the checksum

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="checksumValue"></a>Property `checksumValue`

**Title:** checksum value

A lower case hexadecimal encoded digest value produced using a specific algorithm

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

