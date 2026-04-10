

**Title:** Location

Information about a specific geographic location

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                               | Type               | Title/Description |
| -------------------------------------- | ------------------ | ----------------- |
| - [@id](#@id )                         | string             | -                 |
| - [@type](#@type )                     | string             | -                 |
| - [bbox](#bbox )                       | More than one type | bounding box      |
| - [centroid](#centroid )               | More than one type | centroid          |
| - [identifier](#identifier )           | More than one type | identifier        |
| - [otherIdentifier](#otherIdentifier ) | null or array      | other identifier  |
| - [geometry](#geometry )               | More than one type | geometry          |
| - [inScheme](#inScheme )               | More than one type | gazetteer         |
| - [altLabel](#altLabel )               | null or string     | alternative name  |
| - [prefLabel](#prefLabel )             | null or string     | geographic name   |

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

bounding box of a location described in WKT, GeoJSON, or GML format

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)           |
| ------------------------ |
| [item 0](#bbox_anyOf_i0) |
| [item 1](#bbox_anyOf_i1) |
| [item 2](#bbox_anyOf_i2) |

### <a name="bbox_anyOf_i0"></a>Property `Location > bbox > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="bbox_anyOf_i1"></a>Property `Location > bbox > anyOf > item 1`

Bounding box represented in WKT, GeoJSON (stringified), or GML format

| **Type** | `string` |
| -------- | -------- |

### <a name="bbox_anyOf_i2"></a>Property `Location > bbox > anyOf > item 2`

Bounding box represented in GeoJSON format, either as a Polygon or in bbox array format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                     | Type  | Title/Description |
| -------------------------------------------- | ----- | ----------------- |
| + [coordinates](#bbox_anyOf_i2_coordinates ) | array | -                 |
| + [type](#bbox_anyOf_i2_type )               | const | -                 |

#### <a name="bbox_anyOf_i2_coordinates"></a>Property `Location > bbox > anyOf > item 2 > coordinates`

| **Type**     | `array` |
| ------------ | ------- |
| **Required** | Yes     |

#### <a name="bbox_anyOf_i2_type"></a>Property `Location > bbox > anyOf > item 2 > type`

| **Type**     | `const` |
| ------------ | ------- |
| **Required** | Yes     |

Specific value: `"Polygon"`

## <a name="centroid"></a>Property `Location > centroid`

**Title:** centroid

The geographic center (centroid) of a location described in WKT, GeoJSON, or GML format

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#centroid_anyOf_i0) |
| [item 1](#centroid_anyOf_i1) |
| [item 2](#centroid_anyOf_i2) |

### <a name="centroid_anyOf_i0"></a>Property `Location > centroid > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="centroid_anyOf_i1"></a>Property `Location > centroid > anyOf > item 1`

Center point represented in WKT, GeoJSON (stringified), or GML format

| **Type** | `string` |
| -------- | -------- |

### <a name="centroid_anyOf_i2"></a>Property `Location > centroid > anyOf > item 2`

Centroid represented in GeoJSON format; force point usage with coordinates of longitude and latitude

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                         | Type            | Title/Description |
| ------------------------------------------------ | --------------- | ----------------- |
| + [coordinates](#centroid_anyOf_i2_coordinates ) | array of number | -                 |
| + [type](#centroid_anyOf_i2_type )               | const           | -                 |

#### <a name="centroid_anyOf_i2_coordinates"></a>Property `Location > centroid > anyOf > item 2 > coordinates`

| **Type**     | `array of number` |
| ------------ | ----------------- |
| **Required** | Yes               |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [coordinates items](#centroid_anyOf_i2_coordinates_items) | -           |

##### <a name="centroid_anyOf_i2_coordinates_items"></a>Location > centroid > anyOf > item 2 > coordinates > coordinates items

| **Type** | `number` |
| -------- | -------- |

#### <a name="centroid_anyOf_i2_type"></a>Property `Location > centroid > anyOf > item 2 > type`

| **Type**     | `const` |
| ------------ | ------- |
| **Required** | Yes     |

Specific value: `"Point"`

## <a name="identifier"></a>Property `Location > identifier`

**Title:** identifier

The unique geographic identifier for the Location, e.g., the URI or other unique identifier in the context of the relevant gazetteer

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                     |
| ---------------------------------- |
| [item 0](#identifier_anyOf_i0)     |
| [Identifier](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Location > identifier > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="identifier_anyOf_i1"></a>Property `Location > identifier > anyOf > Identifier`

**Title:** Identifier

inline description of Identifier

| **Type**                  | More than one type            |
| ------------------------- | ----------------------------- |
| **Additional properties** | Any type allowed              |
| **Defined in**            | [Identifier](./Identifier.md) |

## <a name="otherIdentifier"></a>Property `Location > otherIdentifier`

**Title:** other identifier

A list of geographic identifiers for the Location besides the main identifier, e.g. the URI or other unique identifiers in the context of the relevant gazetteer

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be      | Description                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| [Identifier](#otherIdentifier_items) | A unique identifier and optionally it's scheme and other relevant information |

### <a name="otherIdentifier_items"></a>Location > otherIdentifier > Identifier

**Title:** Identifier

A unique identifier and optionally it's scheme and other relevant information

| **Type**                  | More than one type                 |
| ------------------------- | ---------------------------------- |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Identifier](#identifier_anyOf_i1) |

## <a name="geometry"></a>Property `Location > geometry`

**Title:** geometry

Associates a location with a corresponding geometry described in WKT, GeoJSON, or GML format

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#geometry_anyOf_i0) |
| [item 1](#geometry_anyOf_i1) |
| [item 2](#geometry_anyOf_i2) |

### <a name="geometry_anyOf_i0"></a>Property `Location > geometry > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="geometry_anyOf_i1"></a>Property `Location > geometry > anyOf > item 1`

String format of the full geometry of the location in WKT, GeoJSON, or GML format

| **Type** | `string` |
| -------- | -------- |

### <a name="geometry_anyOf_i2"></a>Property `Location > geometry > anyOf > item 2`

Geometry represented in GeoJSON format

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

#### <a name="autogenerated_heading_1"></a>The following properties are required
* type
* coordinates

## <a name="inScheme"></a>Property `Location > inScheme`

**Title:** gazetteer

The gazetteer to which the location belongs

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#inScheme_anyOf_i0)        |
| [ConceptScheme](#inScheme_anyOf_i1) |

### <a name="inScheme_anyOf_i0"></a>Property `Location > inScheme > anyOf > item 0`

| **Type** | `null` |
| -------- | ------ |

### <a name="inScheme_anyOf_i1"></a>Property `Location > inScheme > anyOf > ConceptScheme`

**Title:** ConceptScheme

inline description of the gazetteer

| **Type**                  | `object`                            |
| ------------------------- | ----------------------------------- |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | [Conceptscheme](./Conceptscheme.md) |

## <a name="altLabel"></a>Property `Location > altLabel`

**Title:** alternative name

An alternative label or name for a location

| **Type** | `null or string` |
| -------- | ---------------- |

## <a name="prefLabel"></a>Property `Location > prefLabel`

**Title:** geographic name

Preferred label or name of the Location

| **Type** | `null or string` |
| -------- | ---------------- |

