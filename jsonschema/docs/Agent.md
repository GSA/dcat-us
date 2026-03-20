# Agent

**Title:** Agent

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity that could be involved with a resource

| Property                 | Type        | Title/Description |
| ------------------------ | ----------- | ----------------- |
| - [@id](#@id )           | string      | -                 |
| - [@type](#@type )       | string      | -                 |
| - [category](#category ) | Combination | category          |
| + [name](#name )         | string      | name              |

## <a name="@id"></a>Property `Agent > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Agent > @type`

|              |           |
| ------------ | --------- |
| **Type**     | `string`  |
| **Required** | No        |
| **Default**  | `"Agent"` |

## <a name="category"></a>Property `Agent > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the agent that makes the item available

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `Agent > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="category_oneOf_i1"></a>Property `Agent > category > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of the agent type

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

#### <a name="category_oneOf_i1_@id"></a>Property `Agent > category > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="category_oneOf_i1_@type"></a>Property `Agent > category > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

#### <a name="category_oneOf_i1_altLabel"></a>Property `Agent > category > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

#### <a name="category_oneOf_i1_altLabelMap"></a>Property `Agent > category > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="category_oneOf_i1_definition"></a>Property `Agent > category > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

#### <a name="category_oneOf_i1_definitionMap"></a>Property `Agent > category > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="category_oneOf_i1_inScheme"></a>Property `Agent > category > oneOf > Concept > inScheme`

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

##### <a name="category_oneOf_i1_inScheme_oneOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_@id"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_@type"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_version"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_description"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_descriptionMap"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

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

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_title"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="category_oneOf_i1_inScheme_oneOf_i0_titleMap"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="category_oneOf_i1_inScheme_oneOf_i1"></a>Property `Agent > category > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

#### <a name="category_oneOf_i1_notation"></a>Property `Agent > category > oneOf > Concept > notation`

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

##### <a name="category_oneOf_i1_notation_anyOf_i0"></a>Property `Agent > category > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="category_oneOf_i1_notation_anyOf_i1"></a>Property `Agent > category > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                            | Description |
| ---------------------------------------------------------- | ----------- |
| [item 1 items](#category_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="category_oneOf_i1_notation_anyOf_i1_items"></a>Agent > category > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="category_oneOf_i1_prefLabel"></a>Property `Agent > category > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

#### <a name="category_oneOf_i1_prefLabelMap"></a>Property `Agent > category > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="category_oneOf_i2"></a>Property `Agent > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the agent type

## <a name="name"></a>Property `Agent > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the agent

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
