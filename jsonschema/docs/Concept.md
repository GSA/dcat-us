

**Title:** Concept

A labeled value from an optionally specified concept scheme

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)       |
| -------------------- |
| [Concept](#anyOf_i0) |
| [item 1](#anyOf_i1)  |

## <a name="anyOf_i0"></a>Property `Concept > anyOf > Concept`

**Title:** Concept

The value of the concept, expressed as a string. This is only used when the concept is not further described by the properties of the Concept object and is not linked to a concept scheme.

| **Type** | `string` |
| -------- | -------- |

## <a name="anyOf_i1"></a>Property `Concept > anyOf > item 1`

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                              | Type               | Title/Description |
| ------------------------------------- | ------------------ | ----------------- |
| - [@id](#anyOf_i1_@id )               | string             | -                 |
| - [@type](#anyOf_i1_@type )           | string             | -                 |
| - [altLabel](#anyOf_i1_altLabel )     | null or string     | alternate label   |
| - [definition](#anyOf_i1_definition ) | null or string     | definition        |
| - [inScheme](#anyOf_i1_inScheme )     | object             | in scheme         |
| - [notation](#anyOf_i1_notation )     | More than one type | notation          |
| + [prefLabel](#anyOf_i1_prefLabel )   | string             | preferred label   |

### <a name="anyOf_i1_@id"></a>Property `Concept > anyOf > item 1 > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

### <a name="anyOf_i1_@type"></a>Property `Concept > anyOf > item 1 > @type`

| **Type**    | `string`    |
| ----------- | ----------- |
| **Default** | `"Concept"` |

### <a name="anyOf_i1_altLabel"></a>Property `Concept > anyOf > item 1 > altLabel`

**Title:** alternate label

Alternative label for a concept

| **Type** | `null or string` |
| -------- | ---------------- |

### <a name="anyOf_i1_definition"></a>Property `Concept > anyOf > item 1 > definition`

**Title:** definition

Definition of the controlled vocabulary term

| **Type** | `null or string` |
| -------- | ---------------- |

### <a name="anyOf_i1_inScheme"></a>Property `Concept > anyOf > item 1 > inScheme`

**Title:** in scheme

Concept scheme defining this concept

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Conceptscheme](./Conceptscheme.md) |

### <a name="anyOf_i1_notation"></a>Property `Concept > anyOf > item 1 > notation`

**Title:** notation

List of abbreviations or codes from code lists for the Concept

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#anyOf_i1_notation_anyOf_i0) |
| [item 1](#anyOf_i1_notation_anyOf_i1) |

#### <a name="anyOf_i1_notation_anyOf_i0"></a>Property `Concept > anyOf > item 1 > notation > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

#### <a name="anyOf_i1_notation_anyOf_i1"></a>Property `Concept > anyOf > item 1 > notation > anyOf > item 1`

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 1 items](#anyOf_i1_notation_anyOf_i1_items) | -           |

##### <a name="anyOf_i1_notation_anyOf_i1_items"></a>Concept > anyOf > item 1 > notation > anyOf > item 1 > item 1 items

| **Type** | `string` |
| -------- | -------- |

### <a name="anyOf_i1_prefLabel"></a>Property `Concept > anyOf > item 1 > prefLabel`

**Title:** preferred label

Preferred label for the term

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

