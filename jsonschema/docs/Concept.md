

**Title:** Concept

A labeled value from a specified concept scheme

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                           | Type               | Title/Description                                                                    |
| ---------------------------------- | ------------------ | ------------------------------------------------------------------------------------ |
| - [@id](#@id )                     | string             | -                                                                                    |
| - [@type](#@type )                 | string             | -                                                                                    |
| - [altLabel](#altLabel )           | null or string     | alternate label                                                                      |
| - [altLabelMap](#altLabelMap )     | null or object     | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#definition )       | null or string     | definition                                                                           |
| - [definitionMap](#definitionMap ) | null or object     | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#inScheme )           | More than one type | in scheme                                                                            |
| - [notation](#notation )           | More than one type | notation                                                                             |
| + [prefLabel](#prefLabel )         | string             | preferred label                                                                      |
| - [prefLabelMap](#prefLabelMap )   | null or object     | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `Concept > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Concept > @type`

| **Type**    | `string`    |
| ----------- | ----------- |
| **Default** | `"Concept"` |

## <a name="altLabel"></a>Property `Concept > altLabel`

**Title:** alternate label

Alternative label for a concept

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="altLabelMap"></a>Property `Concept > altLabelMap`

Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="definition"></a>Property `Concept > definition`

**Title:** definition

Definition of the controlled vocabulary term

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="definitionMap"></a>Property `Concept > definitionMap`

Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="inScheme"></a>Property `Concept > inScheme`

**Title:** in scheme

Concept scheme defining this concept

| **Type**                  | `combining`      |
| ------------------------- | ---------------- |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                      |
| ----------------------------------- |
| [ConceptScheme](#inScheme_oneOf_i0) |
| [item 1](#inScheme_oneOf_i1)        |

### <a name="inScheme_oneOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

inline description of ConceptScheme

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Conceptscheme](./Conceptscheme.md) |

### <a name="inScheme_oneOf_i1"></a>Property `Concept > inScheme > oneOf > item 1`

reference iri of ConceptScheme

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="notation"></a>Property `Concept > notation`

**Title:** notation

List of abbreviations or codes from code lists for an organization

| **Type**                  | `combining`      |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#notation_anyOf_i0) |
| [item 1](#notation_anyOf_i1) |

### <a name="notation_anyOf_i0"></a>Property `Concept > notation > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="notation_anyOf_i1"></a>Property `Concept > notation > anyOf > item 1`

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#notation_anyOf_i1_items) | -           |

#### <a name="notation_anyOf_i1_items"></a>Concept > notation > anyOf > item 1 > item 1 items

| **Type** | `string` |
| -------- | -------- |

## <a name="prefLabel"></a>Property `Concept > prefLabel`

**Title:** preferred label

Preferred label for the term

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="prefLabelMap"></a>Property `Concept > prefLabelMap`

Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

