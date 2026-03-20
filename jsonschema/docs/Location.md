# Location

**Title:** Location

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about a specific geographic location

| Property                         | Type           | Title/Description                                                                         |
| -------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#@id )                   | string         | -                                                                                         |
| - [@type](#@type )               | string         | -                                                                                         |
| - [bbox](#bbox )                 | Combination    | bounding box                                                                              |
| - [centroid](#centroid )         | Combination    | centroid                                                                                  |
| - [identifier](#identifier )     | Combination    | identifier                                                                                |
| - [geometry](#geometry )         | Combination    | geometry                                                                                  |
| - [inScheme](#inScheme )         | Combination    | gazetteer                                                                                 |
| - [altLabel](#altLabel )         | null or string | alternative name                                                                          |
| - [altLabelMap](#altLabelMap )   | null or object | Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [prefLabel](#prefLabel )       | null or string | geographic name                                                                           |
| - [prefLabelMap](#prefLabelMap ) | null or object | Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}      |

## <a name="@id"></a>Property `Location > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Location > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Location"` |

## <a name="bbox"></a>Property `Location > bbox`

**Title:** bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** bounding box of a location (in any coordinate system)

| Any of(Option)           |
| ------------------------ |
| [item 0](#bbox_anyOf_i0) |
| [item 1](#bbox_anyOf_i1) |

### <a name="bbox_anyOf_i0"></a>Property `Location > bbox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="bbox_anyOf_i1"></a>Property `Location > bbox > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** Bounding box represented in some string format

## <a name="centroid"></a>Property `Location > centroid`

**Title:** centroid

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The geographic center (centroid) of a location

| Any of(Option)               |
| ---------------------------- |
| [item 0](#centroid_anyOf_i0) |
| [item 1](#centroid_anyOf_i1) |

### <a name="centroid_anyOf_i0"></a>Property `Location > centroid > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="centroid_anyOf_i1"></a>Property `Location > centroid > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** Center point in some string format

## <a name="identifier"></a>Property `Location > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of geographic identifiers for the location, e.g., the URI or other unique identifier in the context of the relevant gazetteer

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Location > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="identifier_anyOf_i1"></a>Property `Location > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>Location > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="geometry"></a>Property `Location > geometry`

**Title:** geometry

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Associates a location with a corresponding geometry

| Any of(Option)               |
| ---------------------------- |
| [item 0](#geometry_anyOf_i0) |
| [item 1](#geometry_anyOf_i1) |

### <a name="geometry_anyOf_i0"></a>Property `Location > geometry > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="geometry_anyOf_i1"></a>Property `Location > geometry > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** String format of the full geometry of the location

## <a name="inScheme"></a>Property `Location > inScheme`

**Title:** gazetteer

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The gazetteer to which the location belongs

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#inScheme_oneOf_i0)        |
| [ConceptScheme](#inScheme_oneOf_i1) |
| [item 2](#inScheme_oneOf_i2)        |

### <a name="inScheme_oneOf_i0"></a>Property `Location > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="inScheme_oneOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of the gazetteer

| Property                                               | Type           | Title/Description                                                                   |
| ------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#inScheme_oneOf_i1_@id )                       | string         | -                                                                                   |
| - [@type](#inScheme_oneOf_i1_@type )                   | string         | -                                                                                   |
| - [version](#inScheme_oneOf_i1_version )               | null or string | version info                                                                        |
| - [created](#inScheme_oneOf_i1_created )               | Combination    | creation date                                                                       |
| - [description](#inScheme_oneOf_i1_description )       | null or string | description                                                                         |
| - [descriptionMap](#inScheme_oneOf_i1_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#inScheme_oneOf_i1_issued )                 | Combination    | publication date                                                                    |
| - [modified](#inScheme_oneOf_i1_modified )             | Combination    | update/modification date                                                            |
| + [title](#inScheme_oneOf_i1_title )                   | string         | title                                                                               |
| - [titleMap](#inScheme_oneOf_i1_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

#### <a name="inScheme_oneOf_i1_@id"></a>Property `Location > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="inScheme_oneOf_i1_@type"></a>Property `Location > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

#### <a name="inScheme_oneOf_i1_version"></a>Property `Location > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

#### <a name="inScheme_oneOf_i1_created"></a>Property `Location > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#inScheme_oneOf_i1_created_anyOf_i0) |
| [item 1](#inScheme_oneOf_i1_created_anyOf_i1) |

##### <a name="inScheme_oneOf_i1_created_anyOf_i0"></a>Property `Location > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="inScheme_oneOf_i1_created_anyOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#inScheme_oneOf_i1_created_anyOf_i1_oneOf_i0) |
| [item 1](#inScheme_oneOf_i1_created_anyOf_i1_oneOf_i1) |
| [item 2](#inScheme_oneOf_i1_created_anyOf_i1_oneOf_i2) |
| [item 3](#inScheme_oneOf_i1_created_anyOf_i1_oneOf_i3) |

###### <a name="inScheme_oneOf_i1_created_anyOf_i1_oneOf_i0"></a>Property `Location > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i1_created_anyOf_i1_oneOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i1_created_anyOf_i1_oneOf_i2"></a>Property `Location > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="inScheme_oneOf_i1_created_anyOf_i1_oneOf_i3"></a>Property `Location > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="inScheme_oneOf_i1_description"></a>Property `Location > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

#### <a name="inScheme_oneOf_i1_descriptionMap"></a>Property `Location > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="inScheme_oneOf_i1_issued"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#inScheme_oneOf_i1_issued_anyOf_i0) |
| [item 1](#inScheme_oneOf_i1_issued_anyOf_i1) |

##### <a name="inScheme_oneOf_i1_issued_anyOf_i0"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="inScheme_oneOf_i1_issued_anyOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i0) |
| [item 1](#inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i1) |
| [item 2](#inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i2) |
| [item 3](#inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i3) |

###### <a name="inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i0"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i2"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="inScheme_oneOf_i1_issued_anyOf_i1_oneOf_i3"></a>Property `Location > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="inScheme_oneOf_i1_modified"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#inScheme_oneOf_i1_modified_anyOf_i0) |
| [item 1](#inScheme_oneOf_i1_modified_anyOf_i1) |

##### <a name="inScheme_oneOf_i1_modified_anyOf_i0"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="inScheme_oneOf_i1_modified_anyOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i0) |
| [item 1](#inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i1) |
| [item 2](#inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i2) |
| [item 3](#inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i3) |

###### <a name="inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i0"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i1"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i2"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="inScheme_oneOf_i1_modified_anyOf_i1_oneOf_i3"></a>Property `Location > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="inScheme_oneOf_i1_title"></a>Property `Location > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

#### <a name="inScheme_oneOf_i1_titleMap"></a>Property `Location > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="inScheme_oneOf_i2"></a>Property `Location > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the gazetteer

## <a name="altLabel"></a>Property `Location > altLabel`

**Title:** alternative name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** An alternative name for a location

## <a name="altLabelMap"></a>Property `Location > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="prefLabel"></a>Property `Location > prefLabel`

**Title:** geographic name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred label of the Location

## <a name="prefLabelMap"></a>Property `Location > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
