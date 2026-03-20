# Document

**Title:** Document

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about a text document

| Property                                           | Type           | Title/Description                                                                   |
| -------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                     | string         | -                                                                                   |
| - [@type](#@type )                                 | string         | -                                                                                   |
| - [creators](#creators )                           | Combination    | authors                                                                             |
| - [publishers](#publishers )                       | null or string | publisher                                                                           |
| - [mediaType](#mediaType )                         | Combination    | media type                                                                          |
| - [abstract](#abstract )                           | null or string | abstract                                                                            |
| - [abstractMap](#abstractMap )                     | null or object | Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [bibliographicCitation](#bibliographicCitation ) | null or string | bibliographic citation                                                              |
| - [conformsTo](#conformsTo )                       | Combination    | conforms to standard                                                                |
| - [creator](#creator )                             | Combination    | corporate author                                                                    |
| - [description](#description )                     | null or string | description                                                                         |
| - [descriptionMap](#descriptionMap )               | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [identifier](#identifier )                       | Combination    | identifier                                                                          |
| - [issued](#issued )                               | Combination    | publication date                                                                    |
| - [publisher](#publisher )                         | Combination    | publisher                                                                           |
| + [title](#title )                                 | string         | title                                                                               |
| - [titleMap](#titleMap )                           | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                           | Combination    | category                                                                            |

## <a name="@id"></a>Property `Document > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Document > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Document"` |

## <a name="creators"></a>Property `Document > creators`

**Title:** authors

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of authors

| Any of(Option)               |
| ---------------------------- |
| [item 0](#creators_anyOf_i0) |
| [item 1](#creators_anyOf_i1) |

### <a name="creators_anyOf_i0"></a>Property `Document > creators > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="creators_anyOf_i1"></a>Property `Document > creators > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#creators_anyOf_i1_items) | -           |

#### <a name="creators_anyOf_i1_items"></a>Document > creators > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="publishers"></a>Property `Document > publishers`

**Title:** publisher

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Publisher

## <a name="mediaType"></a>Property `Document > mediaType`

**Title:** media type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of file formats of the Document

| Any of(Option)                |
| ----------------------------- |
| [item 0](#mediaType_anyOf_i0) |
| [item 1](#mediaType_anyOf_i1) |

### <a name="mediaType_anyOf_i0"></a>Property `Document > mediaType > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="mediaType_anyOf_i1"></a>Property `Document > mediaType > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [item 1 items](#mediaType_anyOf_i1_items) | -           |

#### <a name="mediaType_anyOf_i1_items"></a>Document > mediaType > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [MediaType](#mediaType_anyOf_i1_items_oneOf_i0) |
| [item 1](#mediaType_anyOf_i1_items_oneOf_i1)    |

##### <a name="mediaType_anyOf_i1_items_oneOf_i0"></a>Property `Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType`

**Title:** MediaType

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/mediatype |

**Description:** inline description of MediaType

| Property                                                   | Type           | Title/Description                                                          |
| ---------------------------------------------------------- | -------------- | -------------------------------------------------------------------------- |
| - [@id](#mediaType_anyOf_i1_items_oneOf_i0_@id )           | string         | -                                                                          |
| - [@type](#mediaType_anyOf_i1_items_oneOf_i0_@type )       | string         | -                                                                          |
| - [label](#mediaType_anyOf_i1_items_oneOf_i0_label )       | null or string | label                                                                      |
| - [labelMap](#mediaType_anyOf_i1_items_oneOf_i0_labelMap ) | null or object | Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="mediaType_anyOf_i1_items_oneOf_i0_@id"></a>Property `Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="mediaType_anyOf_i1_items_oneOf_i0_@type"></a>Property `Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType > @type`

|              |               |
| ------------ | ------------- |
| **Type**     | `string`      |
| **Required** | No            |
| **Default**  | `"MediaType"` |

###### <a name="mediaType_anyOf_i1_items_oneOf_i0_label"></a>Property `Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType > label`

**Title:** label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The denomination of the Media Type

###### <a name="mediaType_anyOf_i1_items_oneOf_i0_labelMap"></a>Property `Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="mediaType_anyOf_i1_items_oneOf_i1"></a>Property `Document > mediaType > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

## <a name="abstract"></a>Property `Document > abstract`

**Title:** abstract

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Text abstract of the document

## <a name="abstractMap"></a>Property `Document > abstractMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="bibliographicCitation"></a>Property `Document > bibliographicCitation`

**Title:** bibliographic citation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Bibliographic citation as text

## <a name="conformsTo"></a>Property `Document > conformsTo`

**Title:** conforms to standard

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A standard to which the document conforms

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#conformsTo_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1) |

### <a name="conformsTo_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="conformsTo_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#conformsTo_anyOf_i1_items) | -           |

#### <a name="conformsTo_anyOf_i1_items"></a>Document > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Standard](#conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i1)   |

##### <a name="conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/standard |

**Description:** inline description of Standard

| Property                                                                | Type           | Title/Description                                                                |
| ----------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------- |
| - [@id](#conformsTo_anyOf_i1_items_oneOf_i0_@id )                       | string         | -                                                                                |
| - [@type](#conformsTo_anyOf_i1_items_oneOf_i0_@type )                   | string         | -                                                                                |
| - [created](#conformsTo_anyOf_i1_items_oneOf_i0_created )               | Combination    | creation date                                                                    |
| - [description](#conformsTo_anyOf_i1_items_oneOf_i0_description )       | null or string | description                                                                      |
| - [descriptionMap](#conformsTo_anyOf_i1_items_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#conformsTo_anyOf_i1_items_oneOf_i0_identifier )         | Combination    | identifier                                                                       |
| - [issued](#conformsTo_anyOf_i1_items_oneOf_i0_issued )                 | Combination    | issued                                                                           |
| - [modified](#conformsTo_anyOf_i1_items_oneOf_i0_modified )             | Combination    | last modified                                                                    |
| - [title](#conformsTo_anyOf_i1_items_oneOf_i0_title )                   | null or string | title                                                                            |
| - [titleMap](#conformsTo_anyOf_i1_items_oneOf_i0_titleMap )             | null or object | Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#conformsTo_anyOf_i1_items_oneOf_i0_category )             | Combination    | category                                                                         |
| - [inScheme](#conformsTo_anyOf_i1_items_oneOf_i0_inScheme )             | Combination    | in scheme                                                                        |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_@id"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_@type"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Standard"` |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Standard has been first created

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_description"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Standard

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_identifier"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The main identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalogue, or of a reference register

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                               | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [item 1 items](#conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Standard

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Standard was changed or modified

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_title"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Standard

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the Standard. A controlled vocabulary for the values has not been established

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of Concept

| Property                                                                                | Type           | Title/Description                                                                    |
| --------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_@id )                     | string         | -                                                                                    |
| - [@type](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_@type )                 | string         | -                                                                                    |
| - [altLabel](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_definition )       | null or string | definition                                                                           |
| - [definitionMap](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation )           | Combination    | notation                                                                             |
| + [prefLabel](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_@id"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_@type"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_altLabel"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_altLabelMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_definition"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_definitionMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [ConceptScheme](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i1)        |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                                                                                    | Type           | Title/Description                                                                   |
| ----------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_@id"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_@type"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_version"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                                                                     |
| -------------------------------------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                              |
| ----------------------------------------------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_description"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_descriptionMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                                                                                    |
| ------------------------------------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                             |
| ---------------------------------------------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                                                                      |
| --------------------------------------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                               |
| ------------------------------------------------------------------------------------------------------------ |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_title"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0_titleMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation_anyOf_i0) |
| [item 1](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation_anyOf_i1) |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation_anyOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation_anyOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                               | Description |
| --------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_notation_anyOf_i1_items"></a>Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_prefLabel"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_prefLabelMap"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_inScheme"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The reference register to which the Standard belongs

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [item 0](#conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0)        |
| [ConceptScheme](#conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1) |
| [item 2](#conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2)        |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [ConceptScheme](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of ConceptScheme

###### <a name="conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

##### <a name="conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

## <a name="creator"></a>Property `Document > creator`

**Title:** corporate author

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The organization responsible for creating the resource

| Any of(Option)              |
| --------------------------- |
| [item 0](#creator_anyOf_i0) |
| [item 1](#creator_anyOf_i1) |

### <a name="creator_anyOf_i0"></a>Property `Document > creator > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="creator_anyOf_i1"></a>Property `Document > creator > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#creator_anyOf_i1_items) | -           |

#### <a name="creator_anyOf_i1_items"></a>Document > creator > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [Organization](#creator_anyOf_i1_items_oneOf_i0) |
| [item 1](#creator_anyOf_i1_items_oneOf_i1)       |

##### <a name="creator_anyOf_i1_items_oneOf_i0"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/organization |

**Description:** inline description of corporate author

| Property                                                                   | Type           | Title/Description                                                                      |
| -------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------- |
| - [@id](#creator_anyOf_i1_items_oneOf_i0_@id )                             | string         | -                                                                                      |
| - [@type](#creator_anyOf_i1_items_oneOf_i0_@type )                         | string         | -                                                                                      |
| + [name](#creator_anyOf_i1_items_oneOf_i0_name )                           | string         | name                                                                                   |
| - [subOrganizationOf](#creator_anyOf_i1_items_oneOf_i0_subOrganizationOf ) | Combination    | suborganization of                                                                     |
| - [altLabel](#creator_anyOf_i1_items_oneOf_i0_altLabel )                   | null or string | alternative label                                                                      |
| - [altLabelMap](#creator_anyOf_i1_items_oneOf_i0_altLabelMap )             | null or object | Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [notation](#creator_anyOf_i1_items_oneOf_i0_notation )                   | Combination    | notation                                                                               |
| - [prefLabel](#creator_anyOf_i1_items_oneOf_i0_prefLabel )                 | null or string | preferred label                                                                        |
| - [prefLabelMap](#creator_anyOf_i1_items_oneOf_i0_prefLabelMap )           | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}   |

###### <a name="creator_anyOf_i1_items_oneOf_i0_@id"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="creator_anyOf_i1_items_oneOf_i0_@type"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Organization"` |

###### <a name="creator_anyOf_i1_items_oneOf_i0_name"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the Organization

###### <a name="creator_anyOf_i1_items_oneOf_i0_subOrganizationOf"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > subOrganizationOf`

**Title:** suborganization of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| Any of(Option)                                                        |
| --------------------------------------------------------------------- |
| [item 0](#creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i0) |
| [item 1](#creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1) |

###### <a name="creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i0"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > subOrganizationOf > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > subOrganizationOf > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                   | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1_items) | -           |

###### <a name="creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1_items"></a>Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                             |
| ------------------------------------------------------------------------------------------ |
| [Organization](#creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1_items_oneOf_i0) |
| [item 1](#creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1_items_oneOf_i1)       |

###### <a name="creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1_items_oneOf_i0"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [Organization](#creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Organization

###### <a name="creator_anyOf_i1_items_oneOf_i0_subOrganizationOf_anyOf_i1_items_oneOf_i1"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

###### <a name="creator_anyOf_i1_items_oneOf_i0_altLabel"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > altLabel`

**Title:** alternative label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** alternative name (trading name, colloquial name) for an organization

###### <a name="creator_anyOf_i1_items_oneOf_i0_altLabelMap"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="creator_anyOf_i1_items_oneOf_i0_notation"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

| Any of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#creator_anyOf_i1_items_oneOf_i0_notation_anyOf_i0) |
| [item 1](#creator_anyOf_i1_items_oneOf_i0_notation_anyOf_i1) |

###### <a name="creator_anyOf_i1_items_oneOf_i0_notation_anyOf_i0"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="creator_anyOf_i1_items_oneOf_i0_notation_anyOf_i1"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                          | Description |
| ------------------------------------------------------------------------ | ----------- |
| [item 1 items](#creator_anyOf_i1_items_oneOf_i0_notation_anyOf_i1_items) | -           |

###### <a name="creator_anyOf_i1_items_oneOf_i0_notation_anyOf_i1_items"></a>Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="creator_anyOf_i1_items_oneOf_i0_prefLabel"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > prefLabel`

**Title:** preferred label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred or legal name of the organization

###### <a name="creator_anyOf_i1_items_oneOf_i0_prefLabelMap"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="creator_anyOf_i1_items_oneOf_i1"></a>Property `Document > creator > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of corporate author

## <a name="description"></a>Property `Document > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Document

## <a name="descriptionMap"></a>Property `Document > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="identifier"></a>Property `Document > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of unique identifiers for the Document (e.g. DOI, ISBN)

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `Document > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="identifier_anyOf_i1"></a>Property `Document > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>Document > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="issued"></a>Property `Document > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Publication date of the document

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Document > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="issued_anyOf_i1"></a>Property `Document > issued > anyOf > item 1`

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

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Document > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Document > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Document > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Document > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `Document > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** publisher organization of the document

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#publisher_oneOf_i0)       |
| [Organization](#publisher_oneOf_i1) |
| [item 2](#publisher_oneOf_i2)       |

### <a name="publisher_oneOf_i0"></a>Property `Document > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="publisher_oneOf_i1"></a>Property `Document > publisher > oneOf > Organization`

**Title:** Organization

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [Organization](#creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of publisher organization

### <a name="publisher_oneOf_i2"></a>Property `Document > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of publisher organization

## <a name="title"></a>Property `Document > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the document in the indicated language

## <a name="titleMap"></a>Property `Document > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="category"></a>Property `Document > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Category of the document

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `Document > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="category_oneOf_i1"></a>Property `Document > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                  |
| ------------------------- | ---------------------------------------------------------------- |
| **Type**                  | `object`                                                         |
| **Required**              | No                                                               |
| **Additional properties** | Any type allowed                                                 |
| **Same definition as**    | [Concept](#conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |

**Description:** inline description of Concept

### <a name="category_oneOf_i2"></a>Property `Document > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
