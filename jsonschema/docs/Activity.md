

**Title:** Activity

An activity which a resource could be related to

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                 | Type           | Title/Description                                                              |
| ------------------------ | -------------- | ------------------------------------------------------------------------------ |
| - [@id](#@id )           | string         | -                                                                              |
| - [@type](#@type )       | string         | -                                                                              |
| - [category](#category ) | null or array  | category                                                                       |
| + [label](#label )       | string         | label                                                                          |
| - [labelMap](#labelMap ) | null or object | Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `Activity > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Activity > @type`

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Activity"` |

## <a name="category"></a>Property `Activity > category`

**Title:** category

List of categories for the Activity

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be   | Description |
| --------------------------------- | ----------- |
| [category items](#category_items) | -           |

### <a name="category_items"></a>Activity > category > category items

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [Concept](#category_items_anyOf_i0) |
| [Link](#category_items_anyOf_i1)    |

#### <a name="category_items_anyOf_i0"></a>Property `Activity > category > category items > anyOf > Concept`

**Title:** Concept

inline description of Concept

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

#### <a name="category_items_anyOf_i1"></a>Property `Activity > category > category items > anyOf > Link`

**Title:** Link

reference iri of Concept

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="label"></a>Property `Activity > label`

**Title:** label

A human-readable label for the activity

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="labelMap"></a>Property `Activity > labelMap`

Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

