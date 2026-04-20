

**Title:** UseRestriction

Rules or legal limits on how a resource may be used

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "UseRestriction",
    "restrictionStatus": "Restricted - Fully",
    "specificRestriction": "PRMPA - National Security Classified (B)",
    "restrictionNote": "This data may be used for any purpose without restriction."
}
```

| Property                                       | Type               | Title/Description    |
| ---------------------------------------------- | ------------------ | -------------------- |
| - [@id](#@id )                                 | string             | -                    |
| - [@type](#@type )                             | string             | -                    |
| - [restrictionNote](#restrictionNote )         | null or string     | restriction note     |
| + [restrictionStatus](#restrictionStatus )     | object             | restriction status   |
| - [specificRestriction](#specificRestriction ) | More than one type | specific restriction |

## <a name="@id"></a>[Optional] Property `UseRestriction > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/restrictions/use-restriction-001"
```

## <a name="@type"></a>[Optional] Property `UseRestriction > @type`

**Requirement:** Optional

| **Type**    | `string`           |
| ----------- | ------------------ |
| **Default** | `"UseRestriction"` |

## <a name="restrictionNote"></a>[Optional] Property `UseRestriction > restrictionNote`

**Title:** restriction note

**Requirement:** Optional

Significant information pertaining to the use or reproduction of the data

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"This data may be used for any purpose without restriction."
```

```json
"This data may be used for research purposes. Commercial use requires written permission from the data steward."
```

## <a name="restrictionStatus"></a>[Optional] Property `UseRestriction > restrictionStatus`

**Title:** restriction status

**Requirement:** Optional

Indication of whether or not there are use restrictions on the archival materials, consider using a controlled vocabulary such as https://www.archives.gov/research/catalog/lcdrg/authority-lists/access-restriction-status

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

**Examples:**

```json
"Restricted - Fully"
```

```json
"Unrestricted"
```

## <a name="specificRestriction"></a>[Optional] Property `UseRestriction > specificRestriction`

**Title:** specific restriction

**Requirement:** Optional

Authority, code list entry, or policy reference that defines the specific use restriction; consider using a controlled vocabulary such as the NARA https://www.archives.gov/research/catalog/lcdrg/authority-lists/specific-access-restriction

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"CRCCRCA 4(1)(A)"
```

```json
"PRMPA - National Security Classified (B)"
```

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [Null allowed when not required](#specificRestriction_anyOf_i0) |
| [Concept](#specificRestriction_anyOf_i1)                        |

### <a name="specificRestriction_anyOf_i0"></a>Property `UseRestriction > specificRestriction > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="specificRestriction_anyOf_i1"></a>Property `UseRestriction > specificRestriction > anyOf > Concept`

**Title:** Concept

inline description of the specific restriction

| **Type**                  | More than one type                      |
| ------------------------- | --------------------------------------- |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [restrictionStatus](#restrictionStatus) |

