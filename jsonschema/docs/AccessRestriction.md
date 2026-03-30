

**Title:** AccessRestriction

A restriction on the permitted access to a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                       | Type               | Title/Description                                                                         |
| ---------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------- |
| - [@id](#@id )                                 | string             | -                                                                                         |
| - [@type](#@type )                             | string             | -                                                                                         |
| - [restrictionNote](#restrictionNote )         | null or string     | restriction note                                                                          |
| - [restrictionNoteMap](#restrictionNoteMap )   | null or object     | Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [restrictionStatus](#restrictionStatus )     | More than one type | restriction status                                                                        |
| - [specificRestriction](#specificRestriction ) | More than one type | specific restriction                                                                      |

## <a name="@id"></a>Property `AccessRestriction > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `AccessRestriction > @type`

| **Type**    | `string`              |
| ----------- | --------------------- |
| **Default** | `"AccessRestriction"` |

## <a name="restrictionNote"></a>Property `AccessRestriction > restrictionNote`

**Title:** restriction note

A note related to the access restriction

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="restrictionNoteMap"></a>Property `AccessRestriction > restrictionNoteMap`

Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="restrictionStatus"></a>Property `AccessRestriction > restrictionStatus`

**Title:** restriction status

The indication of whether or not there are access restrictions on the item

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| One of(Option)                         |
| -------------------------------------- |
| [Concept](#restrictionStatus_oneOf_i0) |
| [Link](#restrictionStatus_oneOf_i1)    |

### <a name="restrictionStatus_oneOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

inline description of restriction status

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="restrictionStatus_oneOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Link`

**Title:** Link

reference iri of restriction status

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="specificRestriction"></a>Property `AccessRestriction > specificRestriction`

**Title:** specific restriction

The specific NARA restriction associated with this restriction

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                                                  |
| --------------------------------------------------------------- |
| [Null allowed when not required](#specificRestriction_oneOf_i0) |
| [Concept](#specificRestriction_oneOf_i1)                        |
| [Link](#specificRestriction_oneOf_i2)                           |

### <a name="specificRestriction_oneOf_i0"></a>Property `AccessRestriction > specificRestriction > oneOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="specificRestriction_oneOf_i1"></a>Property `AccessRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

inline description of the specific restriction

| **Type**                  | `object`                               |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Concept](#restrictionStatus_oneOf_i0) |

### <a name="specificRestriction_oneOf_i2"></a>Property `AccessRestriction > specificRestriction > oneOf > Link`

**Title:** Link

reference iri of the specific restriction

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

