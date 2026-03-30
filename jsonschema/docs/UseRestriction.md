

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

| One of(Option)                         |
| -------------------------------------- |
| [Concept](#restrictionStatus_oneOf_i0) |
| [item 1](#restrictionStatus_oneOf_i1)  |

### <a name="restrictionStatus_oneOf_i0"></a>Property `UseRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

inline description of restriction status

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

### <a name="restrictionStatus_oneOf_i1"></a>Property `UseRestriction > restrictionStatus > oneOf > item 1`

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

| One of(Option)                           |
| ---------------------------------------- |
| [item 0](#specificRestriction_oneOf_i0)  |
| [Concept](#specificRestriction_oneOf_i1) |
| [item 2](#specificRestriction_oneOf_i2)  |

### <a name="specificRestriction_oneOf_i0"></a>Property `UseRestriction > specificRestriction > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="specificRestriction_oneOf_i1"></a>Property `UseRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

inline description of the specific restriction

| **Type**                  | `object`                               |
| ------------------------- | -------------------------------------- |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Concept](#restrictionStatus_oneOf_i0) |

### <a name="specificRestriction_oneOf_i2"></a>Property `UseRestriction > specificRestriction > oneOf > item 2`

reference iri of the specific restriction

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

