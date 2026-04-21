

**Title:** AccessRestriction

Rules or indicators that describe who can access a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "AccessRestriction",
    "restrictionStatus": "Restricted - Fully",
    "specificRestriction": "PRMPA - National Security Classified (B)",
    "restrictionNote": "Access restricted to authorized personnel only."
}
```

| Property                                       | Type               | Title/Description    |
| ---------------------------------------------- | ------------------ | -------------------- |
| - [@id](#@id )                                 | string             | -                    |
| - [@type](#@type )                             | string             | -                    |
| - [restrictionNote](#restrictionNote )         | null or string     | restriction note     |
| + [restrictionStatus](#restrictionStatus )     | object             | restriction status   |
| - [specificRestriction](#specificRestriction ) | More than one type | specific restriction |

## <a name="@id"></a>[Optional] Property `AccessRestriction > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>[Optional] Property `AccessRestriction > @type`

**Requirement:** Optional

| **Type**    | `string`              |
| ----------- | --------------------- |
| **Default** | `"AccessRestriction"` |

## <a name="restrictionNote"></a>[Optional] Property `AccessRestriction > restrictionNote`

**Title:** restriction note

**Requirement:** Optional

A note related to the access restriction

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Access restricted to authorized personnel only."
```

## <a name="restrictionStatus"></a>[Optional] Property `AccessRestriction > restrictionStatus`

**Title:** restriction status

**Requirement:** Optional

The indication of whether or not there are access restrictions on the item, consider using a controlled vocabulary such as https://www.archives.gov/research/catalog/lcdrg/authority-lists/access-restriction-status

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

## <a name="specificRestriction"></a>[Optional] Property `AccessRestriction > specificRestriction`

**Title:** specific restriction

**Requirement:** Optional

Authority, code list entry, or policy reference that defines the specific access restriction; consider using a controlled vocabulary such as the NARA https://www.archives.gov/research/catalog/lcdrg/authority-lists/specific-access-restriction

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

### <a name="specificRestriction_anyOf_i0"></a>Property `AccessRestriction > specificRestriction > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="specificRestriction_anyOf_i1"></a>Property `AccessRestriction > specificRestriction > anyOf > Concept`

**Title:** Concept

inline description of the specific restriction

| **Type**                  | More than one type                      |
| ------------------------- | --------------------------------------- |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [restrictionStatus](#restrictionStatus) |

