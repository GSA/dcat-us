

**Title:** UseRestriction

A restriction on usage of another item

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

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

## <a name="restrictionStatus"></a>[Mandatory] Property `UseRestriction > restrictionStatus`

**Title:** restriction status

**Requirement:** Mandatory

Indication of whether or not there are use restrictions on the archival materials

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

## <a name="specificRestriction"></a>[Recommended] Property `UseRestriction > specificRestriction`

**Title:** specific restriction

**Requirement:** Recommended

The specific NARA restriction associated with the use restriction

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

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

