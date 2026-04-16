

**Title:** Checksum

A mechanism that can be used to verify that the contents of a distribution have not changed

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                           | Type   | Title/Description |
| ---------------------------------- | ------ | ----------------- |
| - [@id](#@id )                     | string | -                 |
| - [@type](#@type )                 | string | -                 |
| + [algorithm](#algorithm )         | string | algorithm         |
| + [checksumValue](#checksumValue ) | string | checksum value    |

## <a name="@id"></a>[Optional] Property `Checksum > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>[Optional] Property `Checksum > @type`

**Requirement:** Optional

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Checksum"` |

## <a name="algorithm"></a>[Mandatory] Property `Checksum > algorithm`

**Title:** algorithm

**Requirement:** Mandatory

The algorithm used to produce the checksum

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="checksumValue"></a>[Mandatory] Property `Checksum > checksumValue`

**Title:** checksum value

**Requirement:** Mandatory

A lower case hexadecimal encoded digest value produced using a specific algorithm

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

