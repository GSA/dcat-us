# Concept

**Title:** Concept

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A labeled value from a specified concept scheme

| Property                           | Type           | Title/Description                                                                    |
| ---------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#@id )                     | string         | -                                                                                    |
| - [@type](#@type )                 | string         | -                                                                                    |
| - [altLabel](#altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#definition )       | null or string | definition                                                                           |
| - [definitionMap](#definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#notation )           | Combination    | notation                                                                             |
| + [prefLabel](#prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

## <a name="altLabel"></a>Property `Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

## <a name="altLabelMap"></a>Property `Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="definition"></a>Property `Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

## <a name="definitionMap"></a>Property `Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="inScheme"></a>Property `Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                      |
| ----------------------------------- |
| [ConceptScheme](#inScheme_oneOf_i0) |
| [item 1](#inScheme_oneOf_i1)        |

### <a name="inScheme_oneOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                               | Type           | Title/Description                                                                   |
| ------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

#### <a name="inScheme_oneOf_i0_@id"></a>Property `Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="inScheme_oneOf_i0_@type"></a>Property `Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

#### <a name="inScheme_oneOf_i0_version"></a>Property `Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

#### <a name="inScheme_oneOf_i0_created"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#inScheme_oneOf_i0_created_anyOf_i1) |

##### <a name="inScheme_oneOf_i0_created_anyOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="inScheme_oneOf_i0_created_anyOf_i1"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="inScheme_oneOf_i0_description"></a>Property `Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

#### <a name="inScheme_oneOf_i0_descriptionMap"></a>Property `Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="inScheme_oneOf_i0_issued"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#inScheme_oneOf_i0_issued_anyOf_i1) |

##### <a name="inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="inScheme_oneOf_i0_modified"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#inScheme_oneOf_i0_modified_anyOf_i1) |

##### <a name="inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="inScheme_oneOf_i0_title"></a>Property `Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

#### <a name="inScheme_oneOf_i0_titleMap"></a>Property `Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="inScheme_oneOf_i1"></a>Property `Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

## <a name="notation"></a>Property `Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)               |
| ---------------------------- |
| [item 0](#notation_anyOf_i0) |
| [item 1](#notation_anyOf_i1) |

### <a name="notation_anyOf_i0"></a>Property `Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="notation_anyOf_i1"></a>Property `Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#notation_anyOf_i1_items) | -           |

#### <a name="notation_anyOf_i1_items"></a>Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="prefLabel"></a>Property `Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

## <a name="prefLabelMap"></a>Property `Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
