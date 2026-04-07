

**Title:** UseRestriction

A restriction on usage of another item

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

## <a name="@id"></a>Property `UseRestriction > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `UseRestriction > @type`

| **Type**    | `string`           |
| ----------- | ------------------ |
| **Default** | `"UseRestriction"` |

## <a name="restrictionNote"></a>Property `UseRestriction > restrictionNote`

**Title:** restriction note

Significant information pertaining to the use or reproduction of the data

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="restrictionNoteMap"></a>Property `UseRestriction > restrictionNoteMap`

Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="restrictionStatus"></a>Property `UseRestriction > restrictionStatus`

**Title:** restriction status

Indication of whether or not there are use restrictions on the archival materials

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Required**              | Yes                |
| **Additional properties** | Any type allowed   |

| Any of(Option)                         |
| -------------------------------------- |
| [Concept](#restrictionStatus_anyOf_i0) |
| [Link](#restrictionStatus_anyOf_i1)    |

### <a name="restrictionStatus_anyOf_i0"></a>Property `UseRestriction > restrictionStatus > anyOf > Concept`

**Title:** Concept

inline description of restriction status

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="restrictionStatus_anyOf_i1"></a>Property `UseRestriction > restrictionStatus > anyOf > Link`

**Title:** Link

reference iri of restriction status

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="specificRestriction"></a>Property `UseRestriction > specificRestriction`

**Title:** specific restriction

The specific NARA restriction associated with the use restriction

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [Null allowed when not required](#specificRestriction_anyOf_i0) |
| [Concept](#specificRestriction_anyOf_i1)                        |
| [Link](#specificRestriction_anyOf_i2)                           |

### <a name="specificRestriction_anyOf_i0"></a>Property `UseRestriction > specificRestriction > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="specificRestriction_anyOf_i1"></a>Property `UseRestriction > specificRestriction > anyOf > Concept`

**Title:** Concept

inline description of the specific restriction

| **Type**                  | More than one type                     |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Concept](#restrictionStatus_anyOf_i0) |

### <a name="specificRestriction_anyOf_i2"></a>Property `UseRestriction > specificRestriction > anyOf > Link`

**Title:** Link

reference iri of the specific restriction

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

