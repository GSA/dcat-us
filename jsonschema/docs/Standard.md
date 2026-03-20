# Standard

**Title:** Standard

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about a particular standard that another item conforms to

| Property                             | Type           | Title/Description                                                                |
| ------------------------------------ | -------------- | -------------------------------------------------------------------------------- |
| - [@id](#@id )                       | string         | -                                                                                |
| - [@type](#@type )                   | string         | -                                                                                |
| - [created](#created )               | Combination    | creation date                                                                    |
| - [description](#description )       | null or string | description                                                                      |
| - [descriptionMap](#descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#identifier )         | Combination    | identifier                                                                       |
| - [issued](#issued )                 | Combination    | issued                                                                           |
| - [modified](#modified )             | Combination    | last modified                                                                    |
| - [title](#title )                   | null or string | title                                                                            |
| - [titleMap](#titleMap )             | null or object | Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#category )             | Combination    | category                                                                         |
| - [inScheme](#inScheme )             | Combination    | in scheme                                                                        |

## <a name="@id"></a>Property `Standard > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Standard > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Standard"` |

## <a name="created"></a>Property `Standard > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Standard has been first created

| Any of(Option)              |
| --------------------------- |
| [item 0](#created_anyOf_i0) |
| [item 1](#created_anyOf_i1) |

### <a name="created_anyOf_i0"></a>Property `Standard > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="created_anyOf_i1"></a>Property `Standard > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#created_anyOf_i1_oneOf_i0) |
| [item 1](#created_anyOf_i1_oneOf_i1) |
| [item 2](#created_anyOf_i1_oneOf_i2) |
| [item 3](#created_anyOf_i1_oneOf_i3) |

#### <a name="created_anyOf_i1_oneOf_i0"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i1"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="created_anyOf_i1_oneOf_i2"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="created_anyOf_i1_oneOf_i3"></a>Property `Standard > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="description"></a>Property `Standard > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Standard

## <a name="descriptionMap"></a>Property `Standard > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="identifier"></a>Property `Standard > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The main identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalogue, or of a reference register

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Standard > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="identifier_anyOf_i1"></a>Property `Standard > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>Standard > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="issued"></a>Property `Standard > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Standard

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Standard > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="issued_anyOf_i1"></a>Property `Standard > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Standard > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `Standard > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Standard was changed or modified

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `Standard > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="modified_anyOf_i1"></a>Property `Standard > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `Standard > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="title"></a>Property `Standard > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Standard

## <a name="titleMap"></a>Property `Standard > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="category"></a>Property `Standard > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the Standard. A controlled vocabulary for the values has not been established

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `Standard > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="category_oneOf_i1"></a>Property `Standard > category > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of Concept

| Property                                             | Type           | Title/Description                                                                    |
| ---------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#category_oneOf_i1_@id )                     | string         | -                                                                                    |
| - [@type](#category_oneOf_i1_@type )                 | string         | -                                                                                    |
| - [altLabel](#category_oneOf_i1_altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#category_oneOf_i1_altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#category_oneOf_i1_definition )       | null or string | definition                                                                           |
| - [definitionMap](#category_oneOf_i1_definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#category_oneOf_i1_inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#category_oneOf_i1_notation )           | Combination    | notation                                                                             |
| + [prefLabel](#category_oneOf_i1_prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#category_oneOf_i1_prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

#### <a name="category_oneOf_i1_@id"></a>Property `Standard > category > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="category_oneOf_i1_@type"></a>Property `Standard > category > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

#### <a name="category_oneOf_i1_altLabel"></a>Property `Standard > category > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

#### <a name="category_oneOf_i1_altLabelMap"></a>Property `Standard > category > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="category_oneOf_i1_definition"></a>Property `Standard > category > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

#### <a name="category_oneOf_i1_definitionMap"></a>Property `Standard > category > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="category_oneOf_i1_inScheme"></a>Property `Standard > category > oneOf > Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                                        |
| ----------------------------------------------------- |
| [ConceptScheme](#category_oneOf_i1_inScheme_oneOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i1)        |

##### <a name="category_oneOf_i1_inScheme_oneOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                                                 | Type           | Title/Description                                                                   |
| ------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#category_oneOf_i1_inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#category_oneOf_i1_inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#category_oneOf_i1_inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#category_oneOf_i1_inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#category_oneOf_i1_inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#category_oneOf_i1_inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#category_oneOf_i1_inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#category_oneOf_i1_inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#category_oneOf_i1_inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#category_oneOf_i1_inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_@id"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_@type"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_version"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [item 0](#category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_description"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_descriptionMap"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [item 0](#category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [item 0](#category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [item 0](#category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_title"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_titleMap"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="category_oneOf_i1_inScheme_oneOf_i1"></a>Property `Standard > category > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

#### <a name="category_oneOf_i1_notation"></a>Property `Standard > category > oneOf > Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#category_oneOf_i1_notation_anyOf_i0) |
| [item 1](#category_oneOf_i1_notation_anyOf_i1) |

##### <a name="category_oneOf_i1_notation_anyOf_i0"></a>Property `Standard > category > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="category_oneOf_i1_notation_anyOf_i1"></a>Property `Standard > category > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                            | Description |
| ---------------------------------------------------------- | ----------- |
| [item 1 items](#category_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="category_oneOf_i1_notation_anyOf_i1_items"></a>Standard > category > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="category_oneOf_i1_prefLabel"></a>Property `Standard > category > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

#### <a name="category_oneOf_i1_prefLabelMap"></a>Property `Standard > category > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="category_oneOf_i2"></a>Property `Standard > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

## <a name="inScheme"></a>Property `Standard > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The reference register to which the Standard belongs

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#inScheme_oneOf_i0)        |
| [ConceptScheme](#inScheme_oneOf_i1) |
| [item 2](#inScheme_oneOf_i2)        |

### <a name="inScheme_oneOf_i0"></a>Property `Standard > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="inScheme_oneOf_i1"></a>Property `Standard > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                       |
| ------------------------- | ----------------------------------------------------- |
| **Type**                  | `object`                                              |
| **Required**              | No                                                    |
| **Additional properties** | Any type allowed                                      |
| **Same definition as**    | [ConceptScheme](#category_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of ConceptScheme

### <a name="inScheme_oneOf_i2"></a>Property `Standard > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
