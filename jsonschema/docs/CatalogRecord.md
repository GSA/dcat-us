# CatalogRecord

**Title:** CatalogRecord

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A record in a catalog, describing the registration of a single resource

| Property                         | Type           | Title/Description                                                                   |
| -------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                   | string         | -                                                                                   |
| - [@type](#@type )               | string         | -                                                                                   |
| - [status](#status )             | Combination    | change type                                                                         |
| - [conformsTo](#conformsTo )     | Combination    | application profile                                                                 |
| - [description](#description )   | Combination    | description                                                                         |
| - [issued](#issued )             | Combination    | listing date                                                                        |
| - [language](#language )         | Combination    | language                                                                            |
| + [modified](#modified )         | Combination    | update/modification date                                                            |
| - [source](#source )             | Combination    | source metadata                                                                     |
| - [title](#title )               | null or string | title                                                                               |
| - [titleMap](#titleMap )         | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [primaryTopic](#primaryTopic ) | string         | primary topic                                                                       |

## <a name="@id"></a>Property `CatalogRecord > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `CatalogRecord > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"CatalogRecord"` |

## <a name="status"></a>Property `CatalogRecord > status`

**Title:** change type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The status of the catalog record in the context of editorial flow of the dataset and data service descriptions

| One of(Option)              |
| --------------------------- |
| [item 0](#status_oneOf_i0)  |
| [Concept](#status_oneOf_i1) |
| [item 2](#status_oneOf_i2)  |

### <a name="status_oneOf_i0"></a>Property `CatalogRecord > status > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="status_oneOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of status

| Property                                           | Type           | Title/Description                                                                    |
| -------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#status_oneOf_i1_@id )                     | string         | -                                                                                    |
| - [@type](#status_oneOf_i1_@type )                 | string         | -                                                                                    |
| - [altLabel](#status_oneOf_i1_altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#status_oneOf_i1_altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#status_oneOf_i1_definition )       | null or string | definition                                                                           |
| - [definitionMap](#status_oneOf_i1_definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#status_oneOf_i1_inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#status_oneOf_i1_notation )           | Combination    | notation                                                                             |
| + [prefLabel](#status_oneOf_i1_prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#status_oneOf_i1_prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

#### <a name="status_oneOf_i1_@id"></a>Property `CatalogRecord > status > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="status_oneOf_i1_@type"></a>Property `CatalogRecord > status > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

#### <a name="status_oneOf_i1_altLabel"></a>Property `CatalogRecord > status > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

#### <a name="status_oneOf_i1_altLabelMap"></a>Property `CatalogRecord > status > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="status_oneOf_i1_definition"></a>Property `CatalogRecord > status > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

#### <a name="status_oneOf_i1_definitionMap"></a>Property `CatalogRecord > status > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="status_oneOf_i1_inScheme"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                                      |
| --------------------------------------------------- |
| [ConceptScheme](#status_oneOf_i1_inScheme_oneOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i1)        |

##### <a name="status_oneOf_i1_inScheme_oneOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                                               | Type           | Title/Description                                                                   |
| ---------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#status_oneOf_i1_inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#status_oneOf_i1_inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#status_oneOf_i1_inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#status_oneOf_i1_inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#status_oneOf_i1_inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#status_oneOf_i1_inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#status_oneOf_i1_inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#status_oneOf_i1_inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#status_oneOf_i1_inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#status_oneOf_i1_inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_@id"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_@type"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_version"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [item 0](#status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [item 0](#status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_description"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_descriptionMap"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [item 0](#status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [item 0](#status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [item 0](#status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_title"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="status_oneOf_i1_inScheme_oneOf_i0_titleMap"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="status_oneOf_i1_inScheme_oneOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

#### <a name="status_oneOf_i1_notation"></a>Property `CatalogRecord > status > oneOf > Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#status_oneOf_i1_notation_anyOf_i0) |
| [item 1](#status_oneOf_i1_notation_anyOf_i1) |

##### <a name="status_oneOf_i1_notation_anyOf_i0"></a>Property `CatalogRecord > status > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="status_oneOf_i1_notation_anyOf_i1"></a>Property `CatalogRecord > status > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [item 1 items](#status_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="status_oneOf_i1_notation_anyOf_i1_items"></a>CatalogRecord > status > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="status_oneOf_i1_prefLabel"></a>Property `CatalogRecord > status > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

#### <a name="status_oneOf_i1_prefLabelMap"></a>Property `CatalogRecord > status > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="status_oneOf_i2"></a>Property `CatalogRecord > status > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of status

## <a name="conformsTo"></a>Property `CatalogRecord > conformsTo`

**Title:** application profile

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An Application Profile that the Catalog Record's metadata conforms to

| One of(Option)                   |
| -------------------------------- |
| [item 0](#conformsTo_oneOf_i0)   |
| [Standard](#conformsTo_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i2)   |

### <a name="conformsTo_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="conformsTo_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard`

**Title:** Standard

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/standard |

**Description:** inline description of application profile

| Property                                                 | Type           | Title/Description                                                                |
| -------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------- |
| - [@id](#conformsTo_oneOf_i1_@id )                       | string         | -                                                                                |
| - [@type](#conformsTo_oneOf_i1_@type )                   | string         | -                                                                                |
| - [created](#conformsTo_oneOf_i1_created )               | Combination    | creation date                                                                    |
| - [description](#conformsTo_oneOf_i1_description )       | null or string | description                                                                      |
| - [descriptionMap](#conformsTo_oneOf_i1_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#conformsTo_oneOf_i1_identifier )         | Combination    | identifier                                                                       |
| - [issued](#conformsTo_oneOf_i1_issued )                 | Combination    | issued                                                                           |
| - [modified](#conformsTo_oneOf_i1_modified )             | Combination    | last modified                                                                    |
| - [title](#conformsTo_oneOf_i1_title )                   | null or string | title                                                                            |
| - [titleMap](#conformsTo_oneOf_i1_titleMap )             | null or object | Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#conformsTo_oneOf_i1_category )             | Combination    | category                                                                         |
| - [inScheme](#conformsTo_oneOf_i1_inScheme )             | Combination    | in scheme                                                                        |

#### <a name="conformsTo_oneOf_i1_@id"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="conformsTo_oneOf_i1_@type"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Standard"` |

#### <a name="conformsTo_oneOf_i1_created"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Standard has been first created

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_created_anyOf_i0) |
| [item 1](#conformsTo_oneOf_i1_created_anyOf_i1) |

##### <a name="conformsTo_oneOf_i1_created_anyOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="conformsTo_oneOf_i1_created_anyOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_oneOf_i1_created_anyOf_i1_oneOf_i3"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="conformsTo_oneOf_i1_description"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Standard

#### <a name="conformsTo_oneOf_i1_descriptionMap"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="conformsTo_oneOf_i1_identifier"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The main identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalogue, or of a reference register

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_identifier_anyOf_i0) |
| [item 1](#conformsTo_oneOf_i1_identifier_anyOf_i1) |

##### <a name="conformsTo_oneOf_i1_identifier_anyOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="conformsTo_oneOf_i1_identifier_anyOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 1 items](#conformsTo_oneOf_i1_identifier_anyOf_i1_items) | -           |

###### <a name="conformsTo_oneOf_i1_identifier_anyOf_i1_items"></a>CatalogRecord > conformsTo > oneOf > Standard > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="conformsTo_oneOf_i1_issued"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Standard

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_issued_anyOf_i0) |
| [item 1](#conformsTo_oneOf_i1_issued_anyOf_i1) |

##### <a name="conformsTo_oneOf_i1_issued_anyOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="conformsTo_oneOf_i1_issued_anyOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_oneOf_i1_issued_anyOf_i1_oneOf_i3"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="conformsTo_oneOf_i1_modified"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Standard was changed or modified

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#conformsTo_oneOf_i1_modified_anyOf_i0) |
| [item 1](#conformsTo_oneOf_i1_modified_anyOf_i1) |

##### <a name="conformsTo_oneOf_i1_modified_anyOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="conformsTo_oneOf_i1_modified_anyOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                            |
| --------------------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_oneOf_i1_modified_anyOf_i1_oneOf_i3"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="conformsTo_oneOf_i1_title"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Standard

#### <a name="conformsTo_oneOf_i1_titleMap"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="conformsTo_oneOf_i1_category"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the Standard. A controlled vocabulary for the values has not been established

| One of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_category_oneOf_i0)  |
| [Concept](#conformsTo_oneOf_i1_category_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i1_category_oneOf_i2)  |

##### <a name="conformsTo_oneOf_i1_category_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="conformsTo_oneOf_i1_category_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > category > oneOf > Concept`

**Title:** Concept

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Same definition as**    | [Concept](#status_oneOf_i1) |

**Description:** inline description of Concept

##### <a name="conformsTo_oneOf_i1_category_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

#### <a name="conformsTo_oneOf_i1_inScheme"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The reference register to which the Standard belongs

| One of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#conformsTo_oneOf_i1_inScheme_oneOf_i0)        |
| [ConceptScheme](#conformsTo_oneOf_i1_inScheme_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i1_inScheme_oneOf_i2)        |

##### <a name="conformsTo_oneOf_i1_inScheme_oneOf_i0"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="conformsTo_oneOf_i1_inScheme_oneOf_i1"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Any type allowed                                    |
| **Same definition as**    | [ConceptScheme](#status_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of ConceptScheme

##### <a name="conformsTo_oneOf_i1_inScheme_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > Standard > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

### <a name="conformsTo_oneOf_i2"></a>Property `CatalogRecord > conformsTo > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of application profile

## <a name="description"></a>Property `CatalogRecord > description`

**Title:** description

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of free-text accounts of the catalog record

| Any of(Option)                  |
| ------------------------------- |
| [item 0](#description_anyOf_i0) |
| [item 1](#description_anyOf_i1) |

### <a name="description_anyOf_i0"></a>Property `CatalogRecord > description > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="description_anyOf_i1"></a>Property `CatalogRecord > description > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [item 1 items](#description_anyOf_i1_items) | -           |

#### <a name="description_anyOf_i1_items"></a>CatalogRecord > description > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="issued"></a>Property `CatalogRecord > issued`

**Title:** listing date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of dates on which the catalog record was included in the catalog

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `CatalogRecord > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="issued_anyOf_i1"></a>Property `CatalogRecord > issued > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#issued_anyOf_i1_items) | -           |

#### <a name="issued_anyOf_i1_items"></a>CatalogRecord > issued > anyOf > item 1 > item 1 items

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#issued_anyOf_i1_items_oneOf_i0) |
| [item 1](#issued_anyOf_i1_items_oneOf_i1) |
| [item 2](#issued_anyOf_i1_items_oneOf_i2) |
| [item 3](#issued_anyOf_i1_items_oneOf_i3) |

##### <a name="issued_anyOf_i1_items_oneOf_i0"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

##### <a name="issued_anyOf_i1_items_oneOf_i1"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

##### <a name="issued_anyOf_i1_items_oneOf_i2"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

##### <a name="issued_anyOf_i1_items_oneOf_i3"></a>Property `CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `CatalogRecord > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A language or languages used in the textual metadata describing titles, descriptions, etc. of the catalog record. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)               |
| ---------------------------- |
| [item 0](#language_anyOf_i0) |
| [item 1](#language_anyOf_i1) |
| [item 2](#language_anyOf_i2) |

### <a name="language_anyOf_i0"></a>Property `CatalogRecord > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="language_anyOf_i1"></a>Property `CatalogRecord > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `CatalogRecord > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 2 items](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>CatalogRecord > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="modified"></a>Property `CatalogRecord > modified`

**Title:** update/modification date

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | Yes         |

**Description:** The most recent date on which the catalog record was changed or modified

| One of(Option)               |
| ---------------------------- |
| [item 0](#modified_oneOf_i0) |
| [item 1](#modified_oneOf_i1) |
| [item 2](#modified_oneOf_i2) |
| [item 3](#modified_oneOf_i3) |

### <a name="modified_oneOf_i0"></a>Property `CatalogRecord > modified > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

### <a name="modified_oneOf_i1"></a>Property `CatalogRecord > modified > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

### <a name="modified_oneOf_i2"></a>Property `CatalogRecord > modified > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

### <a name="modified_oneOf_i3"></a>Property `CatalogRecord > modified > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="source"></a>Property `CatalogRecord > source`

**Title:** source metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The original metadata that was used in creating metadata for the items in the catalog record

| One of(Option)               |
| ---------------------------- |
| [item 0](#source_oneOf_i0)   |
| [resource](#source_oneOf_i1) |
| [item 2](#source_oneOf_i2)   |

### <a name="source_oneOf_i0"></a>Property `CatalogRecord > source > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="source_oneOf_i1"></a>Property `CatalogRecord > source > oneOf > resource`

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/resource |

**Description:** inline description of the source

### <a name="source_oneOf_i2"></a>Property `CatalogRecord > source > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the source

## <a name="title"></a>Property `CatalogRecord > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Catalog Record

## <a name="titleMap"></a>Property `CatalogRecord > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="primaryTopic"></a>Property `CatalogRecord > primaryTopic`

**Title:** primary topic

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A link to the Dataset, Data service or Catalog described in the Catalog Record

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
