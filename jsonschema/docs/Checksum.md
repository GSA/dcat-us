

**Title:** Checksum

A mechanism that can be used to verify that the contents of a distribution have not changed

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Checksum",
    "algorithm": "SHA-256",
    "checksumValue": "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"
}
```

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

**Example:**

```json
"https://example.gov/checksums/dataset-001-sha256"
```

## <a name="@type"></a>[Optional] Property `Checksum > @type`

**Requirement:** Optional

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Checksum"` |

**Example:**

```json
"Checksum"
```

## <a name="algorithm"></a>[Mandatory] Property `Checksum > algorithm`

**Title:** algorithm

**Requirement:** Mandatory

The algorithm used to produce the checksum

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Example:**

```json
"SHA-256"
```

## <a name="checksumValue"></a>[Mandatory] Property `Checksum > checksumValue`

**Title:** checksum value

**Requirement:** Mandatory

A lower case hexadecimal encoded digest value produced using a specific algorithm

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"
```

```json
"a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
```

