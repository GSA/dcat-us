

**Title:** Location

Information about a specific geographic location

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                         | Type               | Title/Description                                                                         |
| -------------------------------- | ------------------ | ----------------------------------------------------------------------------------------- |
| - [@id](#@id )                   | string             | -                                                                                         |
| - [@type](#@type )               | string             | -                                                                                         |
| - [bbox](#bbox )                 | More than one type | bounding box                                                                              |
| - [centroid](#centroid )         | More than one type | centroid                                                                                  |
| - [identifier](#identifier )     | More than one type | identifier                                                                                |
| - [geometry](#geometry )         | More than one type | geometry                                                                                  |
| - [inScheme](#inScheme )         | More than one type | gazetteer                                                                                 |
| - [altLabel](#altLabel )         | null or string     | alternative name                                                                          |
| - [altLabelMap](#altLabelMap )   | null or object     | Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [prefLabel](#prefLabel )       | null or string     | geographic name                                                                           |
| - [prefLabelMap](#prefLabelMap ) | null or object     | Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}      |

## <a name="@id"></a>Property `Location > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `Location > @type`

| **Type**    | `string`     |
| ----------- | ------------ |
| **Default** | `"Location"` |

## <a name="bbox"></a>Property `Location > bbox`

**Title:** bounding box

bounding box of a location (in any coordinate system)

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)           |
| ------------------------ |
| [item 0](#bbox_anyOf_i0) |
| [item 1](#bbox_anyOf_i1) |

### <a name="bbox_anyOf_i0"></a>Property `Location > bbox > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="bbox_anyOf_i1"></a>Property `Location > bbox > anyOf > item 1`

Bounding box represented in some string format

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="centroid"></a>Property `Location > centroid`

**Title:** centroid

The geographic center (centroid) of a location

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#centroid_anyOf_i0) |
| [item 1](#centroid_anyOf_i1) |

### <a name="centroid_anyOf_i0"></a>Property `Location > centroid > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="centroid_anyOf_i1"></a>Property `Location > centroid > anyOf > item 1`

Center point in some string format

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="identifier"></a>Property `Location > identifier`

**Title:** identifier

A list of geographic identifiers for the location, e.g., the URI or other unique identifier in the context of the relevant gazetteer

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Location > identifier > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Location > identifier > anyOf > item 1`

| **Type** | `array of string` |
| -------- | ----------------- |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>Location > identifier > anyOf > item 1 > item 1 items

| **Type** | `string` |
| -------- | -------- |

## <a name="geometry"></a>Property `Location > geometry`

**Title:** geometry

Associates a location with a corresponding geometry

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#geometry_anyOf_i0) |
| [item 1](#geometry_anyOf_i1) |

### <a name="geometry_anyOf_i0"></a>Property `Location > geometry > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="geometry_anyOf_i1"></a>Property `Location > geometry > anyOf > item 1`

String format of the full geometry of the location

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="inScheme"></a>Property `Location > inScheme`

**Title:** gazetteer

The gazetteer to which the location belongs

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#inScheme_oneOf_i0)        |
| [ConceptScheme](#inScheme_oneOf_i1) |
| [item 2](#inScheme_oneOf_i2)        |

### <a name="inScheme_oneOf_i0"></a>Property `Location > inScheme > oneOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="inScheme_oneOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

inline description of the gazetteer

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Conceptscheme](./Conceptscheme.md) |

### <a name="inScheme_oneOf_i2"></a>Property `Location > inScheme > oneOf > item 2`

reference iri of the gazetteer

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="altLabel"></a>Property `Location > altLabel`

**Title:** alternative name

An alternative name for a location

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="altLabelMap"></a>Property `Location > altLabelMap`

Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

## <a name="prefLabel"></a>Property `Location > prefLabel`

**Title:** geographic name

Preferred label of the Location

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="prefLabelMap"></a>Property `Location > prefLabelMap`

Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}

| **Type** | `null or object` |
| -------- | ---------------- |

