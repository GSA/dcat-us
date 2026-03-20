# AccessRestriction

**Title:** AccessRestriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A restriction on the permitted access to a resource

| Property                                       | Type           | Title/Description                                                                         |
| ---------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#@id )                                 | string         | -                                                                                         |
| - [@type](#@type )                             | string         | -                                                                                         |
| - [restrictionNote](#restrictionNote )         | null or string | restriction note                                                                          |
| - [restrictionNoteMap](#restrictionNoteMap )   | null or object | Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [restrictionStatus](#restrictionStatus )     | Combination    | restriction status                                                                        |
| - [specificRestriction](#specificRestriction ) | Combination    | specific restriction                                                                      |

## <a name="@id"></a>Property `AccessRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `AccessRestriction > @type`

|              |                       |
| ------------ | --------------------- |
| **Type**     | `string`              |
| **Required** | No                    |
| **Default**  | `"AccessRestriction"` |

## <a name="restrictionNote"></a>Property `AccessRestriction > restrictionNote`

**Title:** restriction note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A note related to the access restriction

## <a name="restrictionNoteMap"></a>Property `AccessRestriction > restrictionNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="restrictionStatus"></a>Property `AccessRestriction > restrictionStatus`

**Title:** restriction status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The indication of whether or not there are access restrictions on the item

| One of(Option)                         |
| -------------------------------------- |
| [Concept](#restrictionStatus_oneOf_i0) |
| [item 1](#restrictionStatus_oneOf_i1)  |

### <a name="restrictionStatus_oneOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of restriction status

| Property                                                      | Type           | Title/Description                                                                    |
| ------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#restrictionStatus_oneOf_i0_@id )                     | string         | -                                                                                    |
| - [@type](#restrictionStatus_oneOf_i0_@type )                 | string         | -                                                                                    |
| - [altLabel](#restrictionStatus_oneOf_i0_altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#restrictionStatus_oneOf_i0_altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#restrictionStatus_oneOf_i0_definition )       | null or string | definition                                                                           |
| - [definitionMap](#restrictionStatus_oneOf_i0_definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#restrictionStatus_oneOf_i0_inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#restrictionStatus_oneOf_i0_notation )           | Combination    | notation                                                                             |
| + [prefLabel](#restrictionStatus_oneOf_i0_prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#restrictionStatus_oneOf_i0_prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

#### <a name="restrictionStatus_oneOf_i0_@id"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="restrictionStatus_oneOf_i0_@type"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

#### <a name="restrictionStatus_oneOf_i0_altLabel"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

#### <a name="restrictionStatus_oneOf_i0_altLabelMap"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="restrictionStatus_oneOf_i0_definition"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

#### <a name="restrictionStatus_oneOf_i0_definitionMap"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="restrictionStatus_oneOf_i0_inScheme"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                                                 |
| -------------------------------------------------------------- |
| [ConceptScheme](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i1)        |

##### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                                                          | Type           | Title/Description                                                                   |
| --------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_@id"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_@type"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_version"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [item 0](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_description"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_descriptionMap"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [item 0](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [item 0](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_title"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i0_titleMap"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="restrictionStatus_oneOf_i0_inScheme_oneOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

#### <a name="restrictionStatus_oneOf_i0_notation"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#restrictionStatus_oneOf_i0_notation_anyOf_i0) |
| [item 1](#restrictionStatus_oneOf_i0_notation_anyOf_i1) |

##### <a name="restrictionStatus_oneOf_i0_notation_anyOf_i0"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="restrictionStatus_oneOf_i0_notation_anyOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [item 1 items](#restrictionStatus_oneOf_i0_notation_anyOf_i1_items) | -           |

###### <a name="restrictionStatus_oneOf_i0_notation_anyOf_i1_items"></a>AccessRestriction > restrictionStatus > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="restrictionStatus_oneOf_i0_prefLabel"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

#### <a name="restrictionStatus_oneOf_i0_prefLabelMap"></a>Property `AccessRestriction > restrictionStatus > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="restrictionStatus_oneOf_i1"></a>Property `AccessRestriction > restrictionStatus > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of restriction status

## <a name="specificRestriction"></a>Property `AccessRestriction > specificRestriction`

**Title:** specific restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The specific NARA restriction associated with this restriction

| One of(Option)                           |
| ---------------------------------------- |
| [item 0](#specificRestriction_oneOf_i0)  |
| [Concept](#specificRestriction_oneOf_i1) |
| [item 2](#specificRestriction_oneOf_i2)  |

### <a name="specificRestriction_oneOf_i0"></a>Property `AccessRestriction > specificRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="specificRestriction_oneOf_i1"></a>Property `AccessRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Same definition as**    | [Concept](#restrictionStatus_oneOf_i0) |

**Description:** inline description of the specific restriction

### <a name="specificRestriction_oneOf_i2"></a>Property `AccessRestriction > specificRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the specific restriction

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
