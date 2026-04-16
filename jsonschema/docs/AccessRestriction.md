

**Title:** AccessRestriction

A restriction on the permitted access to a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "AccessRestriction",
    "restrictionStatus": "https://example.gov/concepts/restricted",
    "specificRestriction": "https://www.archives.gov/cui/registry/category-list",
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

**Example:**

```json
"AccessRestriction"
```

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

## <a name="restrictionStatus"></a>[Mandatory] Property `AccessRestriction > restrictionStatus`

**Title:** restriction status

**Requirement:** Mandatory

The indication of whether or not there are access restrictions on the item

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

**Example:**

```json
"https://example.gov/concepts/restricted"
```

## <a name="specificRestriction"></a>[Recommended] Property `AccessRestriction > specificRestriction`

**Title:** specific restriction

**Requirement:** Recommended

The specific NARA restriction associated with this restriction

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Example:**

```json
"https://www.archives.gov/cui/registry/category-list"
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

