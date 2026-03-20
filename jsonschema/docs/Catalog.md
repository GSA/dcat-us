# DCAT-US 3 Catalog

**Title:** DCAT-US 3 Catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The main item defined by DCAT-US 3 is the Catalog class

| Property                                         | Type                    | Title/Description                                                                   |
| ------------------------------------------------ | ----------------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                                   | string                  | -                                                                                   |
| - [@type](#@type )                               | string                  | -                                                                                   |
| - [catalog](#catalog )                           | Combination             | catalog                                                                             |
| - [contactPoint](#contactPoint )                 | Combination             | contact point                                                                       |
| + [dataset](#dataset )                           | array                   | dataset                                                                             |
| - [keyword](#keyword )                           | null or array of string | keyword/tag                                                                         |
| - [keywordMap](#keywordMap )                     | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [record](#record )                             | Combination             | catalog record                                                                      |
| - [service](#service )                           | Combination             | service                                                                             |
| - [theme](#theme )                               | Combination             | theme/category                                                                      |
| - [themeTaxonomy](#themeTaxonomy )               | Combination             | themes                                                                              |
| - [accessRights](#accessRights )                 | Combination             | access rights                                                                       |
| - [conformsTo](#conformsTo )                     | Combination             | schema version                                                                      |
| - [creator](#creator )                           | Combination             | creator                                                                             |
| - [description](#description )                   | null or string          | description                                                                         |
| - [descriptionMap](#descriptionMap )             | null or object          | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#hasPart )                           | Combination             | has part                                                                            |
| - [identifier](#identifier )                     | Combination             | identifier                                                                          |
| - [issued](#issued )                             | Combination             | release date                                                                        |
| - [language](#language )                         | Combination             | language                                                                            |
| - [license](#license )                           | Combination             | license                                                                             |
| - [modified](#modified )                         | Combination             | update/modification date                                                            |
| - [publisher](#publisher )                       | Combination             | publisher                                                                           |
| - [rights](#rights )                             | Combination             | rights                                                                              |
| - [rightsHolder](#rightsHolder )                 | Combination             | rights holder                                                                       |
| - [spatial](#spatial )                           | Combination             | spatial/geographic coverage                                                         |
| - [subject](#subject )                           | Combination             | subject                                                                             |
| - [temporal](#temporal )                         | Combination             | temporal coverage                                                                   |
| - [title](#title )                               | null or string          | title                                                                               |
| - [titleMap](#titleMap )                         | null or object          | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#category )                         | Combination             | category                                                                            |
| - [homepage](#homepage )                         | Combination             | homepage                                                                            |
| - [qualifiedAttribution](#qualifiedAttribution ) | Combination             | qualified attribution                                                               |

## <a name="@id"></a>Property `DCAT-US 3 Catalog > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `DCAT-US 3 Catalog > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Catalog"` |

## <a name="catalog"></a>Property `DCAT-US 3 Catalog > catalog`

**Title:** catalog

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related catalogs whose contents are of interest in the context of this catalog

| Any of(Option)              |
| --------------------------- |
| [item 0](#catalog_anyOf_i0) |
| [item 1](#catalog_anyOf_i1) |

### <a name="catalog_anyOf_i0"></a>Property `DCAT-US 3 Catalog > catalog > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="catalog_anyOf_i1"></a>Property `DCAT-US 3 Catalog > catalog > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#catalog_anyOf_i1_items) | -           |

#### <a name="catalog_anyOf_i1_items"></a>DCAT-US 3 Catalog > catalog > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                              |
| ------------------------------------------- |
| [catalog](#catalog_anyOf_i1_items_oneOf_i0) |
| [item 1](#catalog_anyOf_i1_items_oneOf_i1)  |

##### <a name="catalog_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > catalog > anyOf > item 1 > item 1 items > oneOf > catalog`

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/catalog |

**Description:** inline description of Catalog

##### <a name="catalog_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > catalog > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Catalog

## <a name="contactPoint"></a>Property `DCAT-US 3 Catalog > contactPoint`

**Title:** contact point

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Contact information that can be used for sending comments about the Catalog

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#contactPoint_anyOf_i0) |
| [item 1](#contactPoint_anyOf_i1) |

### <a name="contactPoint_anyOf_i0"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="contactPoint_anyOf_i1"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items) | -           |

#### <a name="contactPoint_anyOf_i1_items"></a>DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Kind](#contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i1) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | /dcat-us/3.0.0/definitions/kind |

**Description:** inline value for contact point

| Property                                                                        | Type           | Title/Description |
| ------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#contactPoint_anyOf_i1_items_oneOf_i0_@id )                             | string         | -                 |
| - [@type](#contactPoint_anyOf_i1_items_oneOf_i0_@type )                         | string         | -                 |
| - [address](#contactPoint_anyOf_i1_items_oneOf_i0_address )                     | Combination    | address           |
| + [hasEmail](#contactPoint_anyOf_i1_items_oneOf_i0_hasEmail )                   | string         | Email             |
| - [family-name](#contactPoint_anyOf_i1_items_oneOf_i0_family-name )             | null or string | family name       |
| + [fn](#contactPoint_anyOf_i1_items_oneOf_i0_fn )                               | string         | formatted name    |
| - [given-name](#contactPoint_anyOf_i1_items_oneOf_i0_given-name )               | null or string | given name        |
| - [organization-name](#contactPoint_anyOf_i1_items_oneOf_i0_organization-name ) | null or string | organization name |
| - [tel](#contactPoint_anyOf_i1_items_oneOf_i0_tel )                             | null or string | telephone         |
| - [title](#contactPoint_anyOf_i1_items_oneOf_i0_title )                         | null or string | position title    |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > @type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"Kind"` |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address`

**Title:** address

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The address of the contact

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i0) |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1) |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i0"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items) | -           |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items"></a>DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [Address](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0) |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i1)  |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address`

**Title:** Address

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/address |

**Description:** inline address information

| Property                                                                                                  | Type           | Title/Description   |
| --------------------------------------------------------------------------------------------------------- | -------------- | ------------------- |
| - [@id](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_@id )                       | string         | -                   |
| - [@type](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_@type )                   | string         | -                   |
| - [country-name](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_country-name )     | null or string | country             |
| - [locality](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_locality )             | null or string | locality            |
| - [postal-code](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_postal-code )       | null or string | postal code         |
| - [region](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_region )                 | null or string | administrative area |
| - [street-address](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_street-address ) | null or string | street address      |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Address"` |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_country-name"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > country-name`

**Title:** country

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The country of the Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_locality"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > locality`

**Title:** locality

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The city of the Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_postal-code"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > postal-code`

**Title:** postal code

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The postal code of the Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_region"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > region`

**Title:** administrative area

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The administrative area of the Address. Depending on the country, this corresponds to a province, a county, a region, or a state

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_street-address"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > street-address`

**Title:** street address

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The street name and civic number of an Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_hasEmail"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > hasEmail`

**Title:** Email

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Email address for the contact

| Restrictions                      |                                                                                                                                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^mailto:[\w\_\~\!\$\&\'\(\)\*\+\,\;\=\:.-]+@[\w.-]+\.[\w.-]+?$``` [Test](https://regex101.com/?regex=%5Emailto%3A%5B%5Cw%5C_%5C~%5C%21%5C%24%5C%26%5C%27%5C%28%5C%29%5C%2A%5C%2B%5C%2C%5C%3B%5C%3D%5C%3A.-%5D%2B%40%5B%5Cw.-%5D%2B%5C.%5B%5Cw.-%5D%2B%3F%24) |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_family-name"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > family-name`

**Title:** family name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The family name of the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_fn"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > fn`

**Title:** formatted name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The formatted text of the name of the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_given-name"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > given-name`

**Title:** given name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The given name of the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_organization-name"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > organization-name`

**Title:** organization name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The name of the organization to contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_tel"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > tel`

**Title:** telephone

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The telephone number for the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > title`

**Title:** position title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The position role of the person to contact

##### <a name="contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of contact point

## <a name="dataset"></a>Property `DCAT-US 3 Catalog > dataset`

**Title:** dataset

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** List of Datasets that are part of the Catalog

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [dataset items](#dataset_items) | -           |

### <a name="dataset_items"></a>DCAT-US 3 Catalog > dataset > dataset items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                     |
| ---------------------------------- |
| [Dataset](#dataset_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i1)  |

#### <a name="dataset_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/dataset |

**Description:** inline description of Dataset

| Property                                                                          | Type           | Title/Description                                                                   |
| --------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_@id )                                             | string         | -                                                                                   |
| - [@type](#dataset_items_oneOf_i0_@type )                                         | string         | -                                                                                   |
| - [otherIdentifier](#dataset_items_oneOf_i0_otherIdentifier )                     | Combination    | other identifier                                                                    |
| - [sample](#dataset_items_oneOf_i0_sample )                                       | Combination    | sample                                                                              |
| - [status](#dataset_items_oneOf_i0_status )                                       | Combination    | lifecycle status                                                                    |
| - [supportedSchema](#dataset_items_oneOf_i0_supportedSchema )                     | Combination    | supported schema                                                                    |
| - [versionNotes](#dataset_items_oneOf_i0_versionNotes )                           | null or string | version notes                                                                       |
| - [contactPoint](#dataset_items_oneOf_i0_contactPoint )                           | Combination    | contact point                                                                       |
| - [distribution](#dataset_items_oneOf_i0_distribution )                           | Combination    | dataset distribution                                                                |
| - [first](#dataset_items_oneOf_i0_first )                                         | Combination    | first                                                                               |
| - [hasCurrentVersion](#dataset_items_oneOf_i0_hasCurrentVersion )                 | Combination    | current version                                                                     |
| - [hasVersion](#dataset_items_oneOf_i0_hasVersion )                               | Combination    | has version                                                                         |
| - [inSeries](#dataset_items_oneOf_i0_inSeries )                                   | Combination    | in series                                                                           |
| - [keyword](#dataset_items_oneOf_i0_keyword )                                     | Combination    | keyword/tag                                                                         |
| - [keywordMap](#dataset_items_oneOf_i0_keywordMap )                               | null or object | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [landingPage](#dataset_items_oneOf_i0_landingPage )                             | Combination    | landing page                                                                        |
| - [previousVersion](#dataset_items_oneOf_i0_previousVersion )                     | Combination    | previous version                                                                    |
| - [qualifiedRelation](#dataset_items_oneOf_i0_qualifiedRelation )                 | Combination    | qualified relation                                                                  |
| - [spatialResolutionInMeters](#dataset_items_oneOf_i0_spatialResolutionInMeters ) | null or string | Spatial resolution (meters)                                                         |
| - [temporalResolution](#dataset_items_oneOf_i0_temporalResolution )               | null or string | temporal resolution                                                                 |
| - [theme](#dataset_items_oneOf_i0_theme )                                         | Combination    | theme/category                                                                      |
| - [version](#dataset_items_oneOf_i0_version )                                     | null or string | version                                                                             |
| - [describedBy](#dataset_items_oneOf_i0_describedBy )                             | Combination    | data dictionary                                                                     |
| - [geographicBoundingBox](#dataset_items_oneOf_i0_geographicBoundingBox )         | Combination    | geographic bounding box                                                             |
| - [liabilityStatement](#dataset_items_oneOf_i0_liabilityStatement )               | Combination    | liability statement                                                                 |
| - [metadataDistribution](#dataset_items_oneOf_i0_metadataDistribution )           | Combination    | metadata distribution                                                               |
| - [purpose](#dataset_items_oneOf_i0_purpose )                                     | null or string | purpose                                                                             |
| - [purposeMap](#dataset_items_oneOf_i0_purposeMap )                               | null or object | Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [accessRights](#dataset_items_oneOf_i0_accessRights )                           | Combination    | access rights                                                                       |
| - [accrualPeriodicity](#dataset_items_oneOf_i0_accrualPeriodicity )               | Combination    | frequency                                                                           |
| - [conformsTo](#dataset_items_oneOf_i0_conformsTo )                               | Combination    | conforms to                                                                         |
| - [contributor](#dataset_items_oneOf_i0_contributor )                             | Combination    | contributor                                                                         |
| - [created](#dataset_items_oneOf_i0_created )                                     | Combination    | creation date                                                                       |
| - [creator](#dataset_items_oneOf_i0_creator )                                     | Combination    | creator                                                                             |
| + [description](#dataset_items_oneOf_i0_description )                             | string         | description                                                                         |
| - [descriptionMap](#dataset_items_oneOf_i0_descriptionMap )                       | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#dataset_items_oneOf_i0_hasPart )                                     | Combination    | has part                                                                            |
| - [identifier](#dataset_items_oneOf_i0_identifier )                               | null or string | identifier                                                                          |
| - [isReferencedBy](#dataset_items_oneOf_i0_isReferencedBy )                       | Combination    | is referenced by                                                                    |
| - [issued](#dataset_items_oneOf_i0_issued )                                       | Combination    | release date                                                                        |
| - [language](#dataset_items_oneOf_i0_language )                                   | Combination    | language                                                                            |
| - [modified](#dataset_items_oneOf_i0_modified )                                   | Combination    | last modified                                                                       |
| - [provenance](#dataset_items_oneOf_i0_provenance )                               | Combination    | provenance                                                                          |
| + [publisher](#dataset_items_oneOf_i0_publisher )                                 | Combination    | publisher                                                                           |
| - [relation](#dataset_items_oneOf_i0_relation )                                   | Combination    | related resource                                                                    |
| - [replaces](#dataset_items_oneOf_i0_replaces )                                   | Combination    | replaces                                                                            |
| - [rights](#dataset_items_oneOf_i0_rights )                                       | Combination    | rights                                                                              |
| - [rightsHolder](#dataset_items_oneOf_i0_rightsHolder )                           | Combination    | rights holder                                                                       |
| - [source](#dataset_items_oneOf_i0_source )                                       | Combination    | data source                                                                         |
| - [spatial](#dataset_items_oneOf_i0_spatial )                                     | Combination    | spatial/geographic coverage                                                         |
| - [subject](#dataset_items_oneOf_i0_subject )                                     | Combination    | subject                                                                             |
| - [temporal](#dataset_items_oneOf_i0_temporal )                                   | Combination    | temporal coverage                                                                   |
| + [title](#dataset_items_oneOf_i0_title )                                         | string         | title                                                                               |
| - [titleMap](#dataset_items_oneOf_i0_titleMap )                                   | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#dataset_items_oneOf_i0_category )                                   | Combination    | category                                                                            |
| - [hasQualityMeasurement](#dataset_items_oneOf_i0_hasQualityMeasurement )         | Combination    | quality measurement                                                                 |
| - [page](#dataset_items_oneOf_i0_page )                                           | Combination    | documentation                                                                       |
| - [qualifiedAttribution](#dataset_items_oneOf_i0_qualifiedAttribution )           | Combination    | qualified attribution                                                               |
| - [wasAttributedTo](#dataset_items_oneOf_i0_wasAttributedTo )                     | Combination    | attribution                                                                         |
| - [wasGeneratedBy](#dataset_items_oneOf_i0_wasGeneratedBy )                       | Combination    | was generated by                                                                    |
| - [wasUsedBy](#dataset_items_oneOf_i0_wasUsedBy )                                 | Combination    | used by                                                                             |
| - [image](#dataset_items_oneOf_i0_image )                                         | Combination    | image                                                                               |
| - [scopeNote](#dataset_items_oneOf_i0_scopeNote )                                 | null or string | usage note                                                                          |
| - [scopeNoteMap](#dataset_items_oneOf_i0_scopeNoteMap )                           | null or object | Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'} |

##### <a name="dataset_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

##### <a name="dataset_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Dataset"` |

##### <a name="dataset_items_oneOf_i0_otherIdentifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier`

**Title:** other identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of structure identifiers

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                        | Description |
| ---------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                |
| ----------------------------------------------------------------------------- |
| [Identifier](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i1)     |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier`

**Title:** Identifier

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Defined in**            | /dcat-us/3.0.0/definitions/identifier |

**Description:** inline description of other identifier

| Property                                                                                        | Type           | Title/Description |
| ----------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_@id )                   | string         | -                 |
| - [@type](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_@type )               | string         | -                 |
| - [schemaAgency](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_schemaAgency ) | null or string | schema agency     |
| - [creator](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator )           | Combination    | creator           |
| - [issued](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued )             | Combination    | issued            |
| - [version](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_version )           | null or string | version           |
| - [notation](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_notation )         | null or string | notation          |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > @type`

|              |                |
| ------------ | -------------- |
| **Type**     | `string`       |
| **Required** | No             |
| **Default**  | `"Identifier"` |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_schemaAgency"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > schemaAgency`

**Title:** schema agency

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The name of the agency that issued the identifier

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** the agency that manages the identifier scheme

| One of(Option)                                                                                   |
| ------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i0)       |
| [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i2)       |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization`

**Title:** Organization

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/organization |

**Description:** inline description of the creator

| Property                                                                                                                   | Type           | Title/Description                                                                      |
| -------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@id )                             | string         | -                                                                                      |
| - [@type](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@type )                         | string         | -                                                                                      |
| + [name](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_name )                           | string         | name                                                                                   |
| - [subOrganizationOf](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf ) | Combination    | suborganization of                                                                     |
| - [altLabel](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabel )                   | null or string | alternative label                                                                      |
| - [altLabelMap](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabelMap )             | null or object | Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [notation](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation )                   | Combination    | notation                                                                               |
| - [prefLabel](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabel )                 | null or string | preferred label                                                                        |
| - [prefLabelMap](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabelMap )           | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}   |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Organization"` |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_name"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the Organization

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf`

**Title:** suborganization of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| Any of(Option)                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                   | Description |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabel"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > altLabel`

**Title:** alternative label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** alternative name (trading name, colloquial name) for an organization

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

| Any of(Option)                                                                                               |
| ------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                          | Description |
| ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabel"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > prefLabel`

**Title:** preferred label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred or legal name of the organization

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the creator

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Identifier

| Any of(Option)                                                                            |
| ----------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                     |
| -------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_version"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > version`

**Title:** version

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** version of the identifier scheme

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_notation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > notation`

**Title:** notation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** abbreviation or code from code lists for an identifier

###### <a name="dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of other identifier

##### <a name="dataset_items_oneOf_i0_sample"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample`

**Title:** sample

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of links to samples of a Dataset

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Distribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution`

**Title:** Distribution

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/distribution |

**Description:** inline description of Distribution

| Property                                                                                                         | Type           | Title/Description                                                                   |
| ---------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_@id )                                             | string         | -                                                                                   |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_@type )                                         | string         | -                                                                                   |
| - [representationTechnique](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique )     | Combination    | representation technique                                                            |
| - [status](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status )                                       | Combination    | lifecycle status                                                                    |
| - [characterEncoding](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding )                 | Combination    | character encoding                                                                  |
| - [accessService](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService )                         | Combination    | access service                                                                      |
| - [accessURL](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessURL )                                 | Combination    | access URL                                                                          |
| - [byteSize](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_byteSize )                                   | null or string | byte size                                                                           |
| - [compressFormat](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat )                       | Combination    | compression format                                                                  |
| - [downloadURL](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_downloadURL )                             | Combination    | download URL                                                                        |
| - [mediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType )                                 | Combination    | media type                                                                          |
| - [packageFormat](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat )                         | Combination    | packaging format                                                                    |
| - [spatialResolutionInMeters](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters ) | null or string | Spatial resolution (meters)                                                         |
| - [temporalResolution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_temporalResolution )               | null or string | termporal resolution                                                                |
| - [availability](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability )                           | Combination    | availability                                                                        |
| - [accessRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction )                 | Combination    | access restriction                                                                  |
| - [cuiRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction )                       | Combination    | CUI restriction                                                                     |
| - [describedBy](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy )                             | Combination    | data dictionary                                                                     |
| - [useRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction )                       | Combination    | use restriction                                                                     |
| - [accessRights](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights )                           | Combination    | access rights                                                                       |
| - [conformsTo](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo )                               | Combination    | linked schemas                                                                      |
| - [description](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_description )                             | null or string | description                                                                         |
| - [descriptionMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_descriptionMap )                       | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [format](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format )                                       | Combination    | format                                                                              |
| - [identifier](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier )                               | Combination    | identifier                                                                          |
| - [issued](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued )                                       | Combination    | release date                                                                        |
| - [language](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language )                                   | Combination    | language                                                                            |
| - [license](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license )                                     | Combination    | license                                                                             |
| - [modified](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified )                                   | Combination    | last modified                                                                       |
| - [rights](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights )                                       | Combination    | rights                                                                              |
| - [title](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_title )                                         | null or string | title                                                                               |
| - [titleMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_titleMap )                                   | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [hasQualityMeasurement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement )         | Combination    | quality measurement                                                                 |
| - [page](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page )                                           | Combination    | documentation                                                                       |
| - [image](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_image )                                         | Combination    | image                                                                               |
| - [checksum](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum )                                   | Combination    | checksum                                                                            |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Distribution"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique`

**Title:** representation technique

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The format in which an Distribution is released. This is different from the file format as, for example, a ZIP file (file format) could contain an XML schema (representation technique). In DCAT-US profile,  this property SHOULD be used to express the spatial representation type (grid, vector, tin), by using the URIs of the corresponding code list operated by an approved registry

| One of(Option)                                                                                     |
| -------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of Concept

| Property                                                                                                                  | Type           | Title/Description                                                                    |
| ------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@id )                     | string         | -                                                                                    |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@type )                 | string         | -                                                                                    |
| - [altLabel](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definition )       | null or string | definition                                                                           |
| - [definitionMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation )           | Combination    | notation                                                                             |
| + [prefLabel](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabel"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definition"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definitionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i1)        |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                                                                                                                      | Type           | Title/Description                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_version"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                 | Description |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabel"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status`

**Title:** lifecycle status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The status of the distribution in the context of maturity lifecycle

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding`

**Title:** character encoding

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The list of character encodings of the Distribution, by using as value the character set names in the IANA register 

| Any of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                         | Description |
| ------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService`

**Title:** access service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A data service that gives access to the distribution of the dataset

| Any of(Option)                                                                          |
| --------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                     | Description |
| --------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                              |
| ----------------------------------------------------------------------------------------------------------- |
| [DataService](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i1)      |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService`

**Title:** DataService

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | /dcat-us/3.0.0/definitions/dataservice |

**Description:** inline description of DataService

| Property                                                                                                                                               | Type            | Title/Description                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ------------------------------------------------------------------------------------ |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@id )                                             | string          | -                                                                                    |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@type )                                         | string          | -                                                                                    |
| + [contactPoint](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint )                           | array           | contact point                                                                        |
| - [endpointDescription](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription )             | Combination     | endpoint description                                                                 |
| + [endpointURL](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL )                             | array of string | endpoint URL                                                                         |
| - [keyword](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keyword )                                     | null or string  | keyword/tag                                                                          |
| - [keywordMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keywordMap )                               | null or object  | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}         |
| - [servesDataset](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset )                         | Combination     | serves dataset                                                                       |
| - [spatialResolutionInMeters](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters ) | Combination     | spatial resolution in meters                                                         |
| - [temporalResolution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution )               | Combination     | temporal resolution                                                                  |
| - [theme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme )                                         | Combination     | theme/category                                                                       |
| - [geographicBoundingBox](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox )         | Combination     | geographic bounding box                                                              |
| - [accessRights](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights )                           | Combination     | access rights                                                                        |
| - [conformsTo](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo )                               | Combination     | conforms to                                                                          |
| - [created](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created )                                     | Combination     | creation date                                                                        |
| - [creator](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator )                                     | Combination     | creator                                                                              |
| - [description](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_description )                             | null or string  | description                                                                          |
| - [descriptionMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_descriptionMap )                       | null or object  | Language map for the description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier )                               | Combination     | identifier                                                                           |
| - [language](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language )                                   | Combination     | language                                                                             |
| - [license](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license )                                     | Combination     | license                                                                              |
| - [modified](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified )                                   | Combination     | update/modification date                                                             |
| + [publisher](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher )                                 | Combination     | publisher                                                                            |
| - [rights](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights )                                       | Combination     | rights                                                                               |
| - [rightsHolder](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder )                           | Combination     | rights holder                                                                        |
| - [spatial](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial )                                     | Combination     | spatial/geographic coverage                                                          |
| - [temporal](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal )                                   | Combination     | temporal coverage                                                                    |
| + [title](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_title )                                         | string          | title                                                                                |
| - [titleMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_titleMap )                                   | null or object  | Language map for the title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category )                                   | Combination     | category                                                                             |
| - [hasQualityMeasurement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement )         | Combination     | quality measurement                                                                  |
| - [qualifiedAttribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution )           | Combination     | qualified attribution                                                                |
| - [wasUsedBy](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy )                                 | Combination     | was used by                                                                          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > @type`

|              |                 |
| ------------ | --------------- |
| **Type**     | `string`        |
| **Required** | No              |
| **Default**  | `"DataService"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint`

**Title:** contact point

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** Contact information that can be used for sending comments about the Data Service

| Each item of this array must be                                                                                                       | Description |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [contactPoint items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint > contactPoint items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [Kind](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0)   |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint > contactPoint items > oneOf > Kind`

**Title:** Kind

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Kind](#contactPoint_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Kind

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint > contactPoint items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Kind

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription`

**Title:** endpoint description

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of descriptions of the services available via the end-points, including their operations, parameters etc

| Any of(Option)                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                                 | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1 > item 1 items > anyOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An in-line description of the endpoint description

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1 > item 1 items > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the endpoint description

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointURL`

**Title:** endpoint URL

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

**Description:** A list of root locations or primary endpoints of the service (a Web-resolvable IRI)

| Each item of this array must be                                                                                                     | Description                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [endpointURL items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL_items) | The root location or primary endpoint of the service (a Web-resolvable IRI) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointURL > endpointURL items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** The root location or primary endpoint of the service (a Web-resolvable IRI)

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keyword"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > keyword`

**Title:** keyword/tag

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A keyword or tag describing the Data Service

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keywordMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > keywordMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset`

**Title:** serves dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of datasets that are served by this data service

| Any of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                           | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
| [Dataset](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters`

**Title:** spatial resolution in meters

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The minimum spatial separation resolvable in a Data Service, measured in meters

| Any of(Option)                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                                       | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution`

**Title:** temporal resolution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The minimum time period resolvable by the Data Service

| Any of(Option)                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                                | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme`

**Title:** theme/category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of themes of the Data Service. A Data Service may be associated with multiple themes

| Any of(Option)                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                   | Description |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox`

**Title:** geographic bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The spatial extent of domain of application of an data service and is standardized in WGS 84 Lat/Long coordinate system

| Any of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                                   | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GeographicBoundingBox](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i1)                |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox`

**Title:** GeographicBoundingBox

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Defined in**            | /dcat-us/3.0.0/definitions/geographicboundingbox |

**Description:** inline description of GeographicBoundingBox

| Property                                                                                                                                                                                     | Type   | Title/Description       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@id )                                     | string | -                       |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@type )                                 | string | -                       |
| + [eastBoundingLongitude](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_eastBoundingLongitude ) | string | east bounding longitude |
| + [northBoundingLatitude](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_northBoundingLatitude ) | string | north bounding latitude |
| + [southBoundingLatitude](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_southBoundingLatitude ) | string | south bouding latitude  |
| + [westBoundingLongitude](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_westBoundingLongitude ) | string | west bounding longitude |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > @type`

|              |                           |
| ------------ | ------------------------- |
| **Type**     | `string`                  |
| **Required** | No                        |
| **Default**  | `"GeographicBoundingBox"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_eastBoundingLongitude"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > eastBoundingLongitude`

**Title:** east bounding longitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** East bound longitude in decimal degrees

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_northBoundingLatitude"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > northBoundingLatitude`

**Title:** north bounding latitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** North bound latitude in decimal degrees

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_southBoundingLatitude"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > southBoundingLatitude`

**Title:** south bouding latitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** South bound latitude in decimal degrees

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_westBoundingLongitude"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > westBoundingLongitude`

**Title:** west bounding longitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** West bound longitude in decimal degrees

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of GeographicBoundingBox

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information regarding access or restrictions based on privacy, security, or other policies

| One of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0)          |
| [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Defined in**            | /dcat-us/3.0.0/definitions/rightsstatement |

**Description:** inline description of access rights

| Property                                                                                                                                                       | Type           | Title/Description                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@id )                               | string         | -                                                                                     |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@type )                           | string         | -                                                                                     |
| - [attributionText](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionText )       | null or string | attribution text                                                                      |
| - [attributionTextMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionTextMap ) | null or object | Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > @type`

|              |                     |
| ------------ | ------------------- |
| **Type**     | `string`            |
| **Required** | No                  |
| **Default**  | `"RightsStatement"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionText"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > attributionText`

**Title:** attribution text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The custom attribution text for the rights statement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionTextMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > attributionTextMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of access rights

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo`

**Title:** conforms to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of general standards or specifications that the Data Service endpoints implement

| Any of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                        | Description |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/standard |

**Description:** inline description of Standard

| Property                                                                                                                                                            | Type           | Title/Description                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@id )                       | string         | -                                                                                |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@type )                   | string         | -                                                                                |
| - [created](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created )               | Combination    | creation date                                                                    |
| - [description](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_description )       | null or string | description                                                                      |
| - [descriptionMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier )         | Combination    | identifier                                                                       |
| - [issued](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued )                 | Combination    | issued                                                                           |
| - [modified](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified )             | Combination    | last modified                                                                    |
| - [title](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_title )                   | null or string | title                                                                            |
| - [titleMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_titleMap )             | null or object | Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category )             | Combination    | category                                                                         |
| - [inScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme )             | Combination    | in scheme                                                                        |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Standard"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Standard has been first created

| Any of(Option)                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The main identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalogue, or of a reference register

| Any of(Option)                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Standard

| Any of(Option)                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Standard was changed or modified

| Any of(Option)                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the Standard. A controlled vocabulary for the values has not been established

| One of(Option)                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The reference register to which the Standard belongs

| One of(Option)                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0)        |
| [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2)        |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                   |
| **Required**              | No                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of ConceptScheme

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Data Service has been first created

| Any of(Option)                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents primarily responsible for producing the Data Service

| Any of(Option)                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                     | Description |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- |
| [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0)  |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | /dcat-us/3.0.0/definitions/agent |

**Description:** inline description of Agent

| Property                                                                                                                                             | Type        | Title/Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@id )           | string      | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@type )       | string      | -                 |
| - [category](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category ) | Combination | category          |
| + [name](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_name )         | string      | name              |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > @type`

|              |           |
| ------------ | --------- |
| **Type**     | `string`  |
| **Required** | No        |
| **Default**  | `"Agent"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the agent that makes the item available

| One of(Option)                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the agent type

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the agent type

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_name"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the agent

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Data Service

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of the main identifiers for the Data Service, e.g. the URI or other unique identifier in the context of the Catalog

| Any of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                        | Description |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Language or languages supported by the Data Service. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                      | Description |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 2 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license`

**Title:** license

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The license under which the Data Service is made available

| One of(Option)                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i0)          |
| [LicenseDocument](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Defined in**            | /dcat-us/3.0.0/definitions/licensedocument |

**Description:** inline description of LicenseDocument

| Property                                                                                                                                    | Type           | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@id )                 | string         | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@type )             | string         | -                 |
| - [licenseText](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_licenseText ) | null or string | license text      |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument > @type`

|              |                     |
| ------------ | ------------------- |
| **Type**     | `string`            |
| **Required** | No                  |
| **Default**  | `"LicenseDocument"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_licenseText"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument > licenseText`

**Title:** license text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Full text of the license

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of LicenseDocument

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Data Service was changed or modified

| Any of(Option)                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** An entity (organization) responsible for making the Data Service available

| One of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0)  |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > publisher > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > publisher > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of statements concerning all rights for the Data Service not addressed with license or accessRights, such as copyright statements

| Any of(Option)                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                    | Description |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i1)          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1 > item 1 items > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder`

**Title:** rights holder

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of Agents (organizations) holding rights on the Data Service

| Any of(Option)                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                          | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Organization](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region that is covered by the Data Service

| Any of(Option)                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                     | Description |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/location |

**Description:** inline description of Location

| Property                                                                                                                                                     | Type           | Title/Description                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@id )                   | string         | -                                                                                         |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@type )               | string         | -                                                                                         |
| - [bbox](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox )                 | Combination    | bounding box                                                                              |
| - [centroid](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid )         | Combination    | centroid                                                                                  |
| - [identifier](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier )     | Combination    | identifier                                                                                |
| - [geometry](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry )         | Combination    | geometry                                                                                  |
| - [inScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme )         | Combination    | gazetteer                                                                                 |
| - [altLabel](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabel )         | null or string | alternative name                                                                          |
| - [altLabelMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabelMap )   | null or object | Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [prefLabel](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabel )       | null or string | geographic name                                                                           |
| - [prefLabelMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabelMap ) | null or object | Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}      |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Location"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > bbox`

**Title:** bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** bounding box of a location (in any coordinate system)

| Any of(Option)                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > bbox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > bbox > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** Bounding box represented in some string format

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > centroid`

**Title:** centroid

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The geographic center (centroid) of a location

| Any of(Option)                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > centroid > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > centroid > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** Center point in some string format

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of geographic identifiers for the location, e.g., the URI or other unique identifier in the context of the relevant gazetteer

| Any of(Option)                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                                                        | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > geometry`

**Title:** geometry

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Associates a location with a corresponding geometry

| Any of(Option)                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > geometry > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > geometry > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** String format of the full geometry of the location

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme`

**Title:** gazetteer

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The gazetteer to which the location belongs

| One of(Option)                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0)        |
| [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2)        |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                   |
| **Required**              | No                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of the gazetteer

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the gazetteer

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabel"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > altLabel`

**Title:** alternative name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** An alternative name for a location

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabel"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > prefLabel`

**Title:** geographic name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred label of the Location

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of temporal periods that the DataService covers

| Any of(Option)                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                      | Description |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
| [PeriodOfTime](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/periodoftime |

**Description:** inline description of PeriodOfTime

| Property                                                                                                                                                | Type        | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@id )             | string      | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@type )         | string      | -                 |
| - [endDate](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate )     | Combination | end date          |
| - [startDate](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate ) | Combination | start date        |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"PeriodOfTime"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate`

**Title:** end date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The end date of the period of time

| Any of(Option)                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate`

**Title:** start date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The start date of the period of time

| Any of(Option)                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the data service in the indicated language

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Category of the data service

| One of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement`

**Title:** quality measurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Refers to the performed quality measurements

| Any of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                                   | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [QualityMeasurement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Defined in**            | /dcat-us/3.0.0/definitions/qualitymeasurement |

**Description:** inline description of QualityMeasurement

| Property                                                                                                                                                                         | Type           | Title/Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@id )                         | string         | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@type )                     | string         | -                 |
| + [isMeasurementOf](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf ) | Combination    | is measurement of |
| + [value](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_value )                     | string         | value             |
| - [unitMeasure](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_unitMeasure )         | null or string | unit of measure   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > @type`

|              |                        |
| ------------ | ---------------------- |
| **Type**     | `string`               |
| **Required** | No                     |
| **Default**  | `"QualityMeasurement"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The metric being observed

| One of(Option)                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Metric](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric`

**Title:** Metric

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | /dcat-us/3.0.0/definitions/metric |

**Description:** inline description of Metric

| Property                                                                                                                                                                                                    | Type           | Title/Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@id )                           | string         | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@type )                       | string         | -                 |
| + [expectedDataType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_expectedDataType ) | string         | expected datatype |
| + [inDimension](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_inDimension )           | string         | in dimension      |
| - [definition](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_definition )             | null or string | definition        |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > @type`

|              |            |
| ------------ | ---------- |
| **Type**     | `string`   |
| **Required** | No         |
| **Default**  | `"Metric"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_expectedDataType"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > expectedDataType`

**Title:** expected datatype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_inDimension"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > inDimension`

**Title:** in dimension

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_definition"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the metric.

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Metric

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_value"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > value`

**Title:** value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The value computed by metric

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_unitMeasure"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > unitMeasure`

**Title:** unit of measure

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Unit of measure associated with the value

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of QualityMeasurement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution`

**Title:** qualified attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An Agent having some form of responsibility for the DataService

| Any of(Option)                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                                  | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Attribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i1)      |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution`

**Title:** Attribution

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | /dcat-us/3.0.0/definitions/attribution |

**Description:** inline description of Attribution

| Property                                                                                                                                                        | Type        | Title/Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@id )         | string      | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@type )     | string      | -                 |
| + [hadRole](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_hadRole ) | string      | role              |
| + [agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent )     | Combination | agent             |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > @type`

|              |                 |
| ------------ | --------------- |
| **Type**     | `string`        |
| **Required** | No              |
| **Default**  | `"Attribution"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_hadRole"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > hadRole`

**Title:** role

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The function of an entity or agent with respect to another entity or resource

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > agent`

**Title:** agent

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The agent that plays a role in the resource

| One of(Option)                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i0)  |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > agent > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > agent > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Attribution

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy`

**Title:** was used by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of activities that used the Data Service

| Any of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                       | Description |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Activity](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity`

**Title:** Activity

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/activity |

**Description:** inline description of Activity

| Property                                                                                                                                               | Type           | Title/Description                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------ |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@id )           | string         | -                                                                              |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@type )       | string         | -                                                                              |
| - [category](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category ) | Combination    | category                                                                       |
| - [label](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_label )       | null or string | label                                                                          |
| - [labelMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_labelMap ) | null or object | Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Activity"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The category of the Activity

| Any of(Option)                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category > anyOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the category

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category > anyOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the category

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_label"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > label`

**Title:** label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A human-readable label for the activity

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_labelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Activity

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of DataService

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessURL"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessURL`

**Title:** access URL

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A URL that gives access to a Distribution of the Dataset

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessURL > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessURL > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_byteSize"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > byteSize`

**Title:** byte size

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The size of a Distribution in bytes

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat`

**Title:** compression format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file

| One of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i0)    |
| [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i2)    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType`

**Title:** MediaType

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/mediatype |

**Description:** inline description of MediaType

| Property                                                                                               | Type           | Title/Description                                                          |
| ------------------------------------------------------------------------------------------------------ | -------------- | -------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@id )           | string         | -                                                                          |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@type )       | string         | -                                                                          |
| - [label](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_label )       | null or string | label                                                                      |
| - [labelMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_labelMap ) | null or object | Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > @type`

|              |               |
| ------------ | ------------- |
| **Type**     | `string`      |
| **Required** | No            |
| **Default**  | `"MediaType"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_label"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > label`

**Title:** label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The denomination of the Media Type

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_labelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_downloadURL"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > downloadURL`

**Title:** download URL

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A URL that is a direct link to a downloadable file of the Distribution in a given format

| Any of(Option)                                                                        |
| ------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > downloadURL > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > downloadURL > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType`

**Title:** media type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The media type of the Distribution as defined in the official register of media types managed by IANA

| One of(Option)                                                                         |
| -------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i0)    |
| [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i2)    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                    |
| **Required**              | No                                                                                          |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat`

**Title:** packaging format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together

| One of(Option)                                                                             |
| ------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i0)    |
| [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i2)    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                    |
| **Required**              | No                                                                                          |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The minimum spatial separation resolvable in a dataset distribution, measured in meters

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_temporalResolution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > temporalResolution`

**Title:** termporal resolution

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The minimum time period resolvable in the dataset distribution

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability`

**Title:** availability

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An indication how long it is planned to keep the Distribution of the Dataset available

| One of(Option)                                                                          |
| --------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction`

**Title:** access restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of access restrictions related to the distribution

| Any of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                         | Description |
| ------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- |
| [AccessRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i1)            |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction`

**Title:** AccessRestriction

|                           |                                              |
| ------------------------- | -------------------------------------------- |
| **Type**                  | `object`                                     |
| **Required**              | No                                           |
| **Additional properties** | Any type allowed                             |
| **Defined in**            | /dcat-us/3.0.0/definitions/accessrestriction |

**Description:** inline description of AccessRestriction

| Property                                                                                                                                       | Type           | Title/Description                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@id )                                 | string         | -                                                                                         |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@type )                             | string         | -                                                                                         |
| - [restrictionNote](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNote )         | null or string | restriction note                                                                          |
| - [restrictionNoteMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap )   | null or object | Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [restrictionStatus](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus )     | Combination    | restriction status                                                                        |
| - [specificRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction ) | Combination    | specific restriction                                                                      |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > @type`

|              |                       |
| ------------ | --------------------- |
| **Type**     | `string`              |
| **Required** | No                    |
| **Default**  | `"AccessRestriction"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNote"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionNote`

**Title:** restriction note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A note related to the access restriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionStatus`

**Title:** restriction status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The indication of whether or not there are access restrictions on the item

| One of(Option)                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of restriction status

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionStatus > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of restriction status

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction`

**Title:** specific restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The specific NARA restriction associated with this restriction

| One of(Option)                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the specific restriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the specific restriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of AccessRestriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction`

**Title:** CUI restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Controlled Unclassified Information restriction related to the distribution

| One of(Option)                                                                                   |
| ------------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i0)         |
| [CUIRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i2)         |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction`

**Title:** CUIRestriction

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Defined in**            | /dcat-us/3.0.0/definitions/cuirestriction |

**Description:** inline description of CUIRestriction

| Property                                                                                                                                         | Type        | Title/Description                |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@id )                                                     | string      | -                                |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@type )                                                 | string      | -                                |
| + [cuiBannerMarking](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_cuiBannerMarking )                           | string      | CUI banner marking               |
| + [designationIndicator](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_designationIndicator )                   | string      | CUI designation indicator        |
| - [requiredIndicatorPerAuthority](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority ) | Combination | required indicator per authority |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > @type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `string`           |
| **Required** | No                 |
| **Default**  | `"CUIRestriction"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_cuiBannerMarking"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > cuiBannerMarking`

**Title:** CUI banner marking

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** CUI (Controlled Unclassified Information) banner marking is required for any unclassified information that is deemed sensitive and requires protection

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_designationIndicator"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > designationIndicator`

**Title:** CUI designation indicator

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Designation Indicator shows which agency made the document CUI

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority`

**Title:** required indicator per authority

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of free text of the required indicator

| Any of(Option)                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                             | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of CUIRestriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy`

**Title:** data dictionary

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A distribution containing the Data Dictionary for this distribution

| One of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i0)       |
| [Distribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i2)       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **Type**                  | `object`                                                               |
| **Required**              | No                                                                     |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [Distribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the data dictionary

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the data dictionary

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction`

**Title:** use restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Use restriction related to the distribution

| Any of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                      | Description |
| ---------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [UseRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i1)         |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction`

**Title:** UseRestriction

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Defined in**            | /dcat-us/3.0.0/definitions/userestriction |

**Description:** inline description of UseRestriction

| Property                                                                                                                                    | Type           | Title/Description                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@id )                                 | string         | -                                                                                         |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@type )                             | string         | -                                                                                         |
| - [restrictionNote](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNote )         | null or string | restriction note                                                                          |
| - [restrictionNoteMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap )   | null or object | Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [restrictionStatus](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus )     | Combination    | restriction status                                                                        |
| - [specificRestriction](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction ) | Combination    | specific restriction                                                                      |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > @type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `string`           |
| **Required** | No                 |
| **Default**  | `"UseRestriction"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNote"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionNote`

**Title:** restriction note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Significant information pertaining to the use or reproduction of the data

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionStatus`

**Title:** restriction status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Indication of whether or not there are use restrictions on the archival materials

| One of(Option)                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of restriction status

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionStatus > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of restriction status

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction`

**Title:** specific restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The specific NARA restriction associated with the use restriction

| One of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the specific restriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the specific restriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of UseRestriction

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information regarding access or restrictions based on privacy, security, or other policies

| One of(Option)                                                                                  |
| ----------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0)          |
| [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo`

**Title:** linked schemas

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of established schemas or reference systems to which the described Distribution conforms

| Any of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                  | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                        |
| ----------------------------------------------------------------------------------------------------- |
| [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                    |
| **Required**              | No                                                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Distribution

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format`

**Title:** format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The file format of the Distribution

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i0)    |
| [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i2)    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                    |
| **Required**              | No                                                                                          |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of the format

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the format

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of unique identifiers for the Distribution (e.g. DOI, ISBN)

| Any of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                  | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Distribution

| Any of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                            |
| ----------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A language or languages used in the Distribution. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                | Description |
| ---------------------------------------------------------------------------------------------- | ----------- |
| [item 2 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license`

**Title:** license

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A license under which the Distribution is made available

| One of(Option)                                                                             |
| ------------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i0)          |
| [LicenseDocument](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Required**              | No                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [LicenseDocument](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

**Description:** inline description of LicenseDocument

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of LicenseDocument

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Distribution was changed or modified

| Any of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A statement that specifies rights associated with the Distribution

| One of(Option)                                                                            |
| ----------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i0)          |
| [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Distribution

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement`

**Title:** quality measurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of quality measurements for the distribution

| Any of(Option)                                                                                  |
| ----------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                             | Description |
| ----------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [QualityMeasurement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

|                           |                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                         |
| **Required**              | No                                                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                                                 |
| **Same definition as**    | [QualityMeasurement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of QualityMeasurement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of QualityMeasurement

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page`

**Title:** documentation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A page or document about this Distribution

| Any of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                            | Description |
| ------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                  |
| ----------------------------------------------------------------------------------------------- |
| [Document](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document`

**Title:** Document

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/document |

**Description:** inline description of Document

| Property                                                                                                                              | Type           | Title/Description                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@id )                                     | string         | -                                                                                   |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@type )                                 | string         | -                                                                                   |
| - [creators](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators )                           | Combination    | authors                                                                             |
| - [publishers](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publishers )                       | null or string | publisher                                                                           |
| - [mediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType )                         | Combination    | media type                                                                          |
| - [abstract](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstract )                           | null or string | abstract                                                                            |
| - [abstractMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstractMap )                     | null or object | Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [bibliographicCitation](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_bibliographicCitation ) | null or string | bibliographic citation                                                              |
| - [conformsTo](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo )                       | Combination    | conforms to standard                                                                |
| - [creator](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator )                             | Combination    | corporate author                                                                    |
| - [description](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_description )                     | null or string | description                                                                         |
| - [descriptionMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_descriptionMap )               | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [identifier](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier )                       | Combination    | identifier                                                                          |
| - [issued](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued )                               | Combination    | publication date                                                                    |
| - [publisher](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher )                         | Combination    | publisher                                                                           |
| + [title](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_title )                                 | string         | title                                                                               |
| - [titleMap](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_titleMap )                           | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category )                           | Combination    | category                                                                            |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Document"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators`

**Title:** authors

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of authors

| Any of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                             | Description |
| --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publishers"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publishers`

**Title:** publisher

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Publisher

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType`

**Title:** media type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of file formats of the Document

| Any of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                              | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i1)    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                    |
| **Required**              | No                                                                                          |
| **Additional properties** | Any type allowed                                                                            |
| **Same definition as**    | [MediaType](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstract"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > abstract`

**Title:** abstract

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Text abstract of the document

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstractMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > abstractMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_bibliographicCitation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > bibliographicCitation`

**Title:** bibliographic citation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Bibliographic citation as text

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo`

**Title:** conforms to standard

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A standard to which the document conforms

| Any of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                               | Description |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                    |
| **Required**              | No                                                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator`

**Title:** corporate author

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The organization responsible for creating the resource

| Any of(Option)                                                                                                 |
| -------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                            | Description |
| -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| [Organization](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of corporate author

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of corporate author

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Document

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of unique identifiers for the Document (e.g. DOI, ISBN)

| Any of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                               | Description |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Publication date of the document

| Any of(Option)                                                                                                |
| ------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** publisher organization of the document

| One of(Option)                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0)       |
| [Organization](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2)       |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of publisher organization

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of publisher organization

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the document in the indicated language

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Category of the document

| One of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Document

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_image"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > image`

**Title:** image

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A link to a thumbnail picture illustrating the content of the distribution

| Any of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > image > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > image > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** The link to the image

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum`

**Title:** checksum

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A mechanism that can be used to verify that the contents of a distribution have not changed

| One of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i0)   |
| [Checksum](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i2)   |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum`

**Title:** Checksum

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/checksum |

**Description:** inline description of Checksum

| Property                                                                                                   | Type   | Title/Description |
| ---------------------------------------------------------------------------------------------------------- | ------ | ----------------- |
| - [@id](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@id )                     | string | -                 |
| - [@type](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@type )                 | string | -                 |
| + [algorithm](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_algorithm )         | string | algorithm         |
| + [checksumValue](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_checksumValue ) | string | checksum value    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Checksum"` |

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_algorithm"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > algorithm`

**Title:** algorithm

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The algorithm used to produce the checksum

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_checksumValue"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > checksumValue`

**Title:** checksum value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A lower case hexadecimal encoded digest value produced using a specific algorithm

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Checksum

###### <a name="dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

##### <a name="dataset_items_oneOf_i0_status"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > status`

**Title:** lifecycle status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The status of the dataset  in the context of maturity lifecycle

| One of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_status_oneOf_i0)  |
| [Concept](#dataset_items_oneOf_i0_status_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_status_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_status_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > status > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_status_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > status > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_status_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > status > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

##### <a name="dataset_items_oneOf_i0_supportedSchema"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > supportedSchema`

**Title:** supported schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** supported schema for this dataset

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_supportedSchema_oneOf_i0)  |
| [Dataset](#dataset_items_oneOf_i0_supportedSchema_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_supportedSchema_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_supportedSchema_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > supportedSchema > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_supportedSchema_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > supportedSchema > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of the supported schema

###### <a name="dataset_items_oneOf_i0_supportedSchema_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > supportedSchema > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the supported schema

##### <a name="dataset_items_oneOf_i0_versionNotes"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > versionNotes`

**Title:** version notes

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** version notes for this dataset

##### <a name="dataset_items_oneOf_i0_contactPoint"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contactPoint`

**Title:** contact point

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of contact information that can be used for sending comments about the Dataset

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_contactPoint_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_contactPoint_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_contactPoint_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contactPoint > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_contactPoint_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contactPoint > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_contactPoint_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_contactPoint_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Kind](#dataset_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#dataset_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Kind](#contactPoint_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Kind

###### <a name="dataset_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Kind

##### <a name="dataset_items_oneOf_i0_distribution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > distribution`

**Title:** dataset distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of available distributions for the Dataset

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_distribution_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_distribution_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_distribution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > distribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_distribution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > distribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_distribution_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_distribution_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > distribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [Distribution](#dataset_items_oneOf_i0_distribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_distribution_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_distribution_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > distribution > anyOf > item 1 > item 1 items > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **Type**                  | `object`                                                               |
| **Required**              | No                                                                     |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [Distribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Distribution

###### <a name="dataset_items_oneOf_i0_distribution_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > distribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

##### <a name="dataset_items_oneOf_i0_first"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > first`

**Title:** first

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** the first item of the sequence the dataset belongs to

| One of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_first_oneOf_i0)  |
| [Dataset](#dataset_items_oneOf_i0_first_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_first_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_first_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > first > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_first_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > first > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_first_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > first > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_hasCurrentVersion"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasCurrentVersion`

**Title:** current version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** reference to the current (latest) version of a dataset

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_hasCurrentVersion_oneOf_i0)  |
| [Dataset](#dataset_items_oneOf_i0_hasCurrentVersion_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_hasCurrentVersion_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_hasCurrentVersion_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasCurrentVersion > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_hasCurrentVersion_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasCurrentVersion > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_hasCurrentVersion_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasCurrentVersion > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_hasVersion"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasVersion`

**Title:** has version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related Datasets that are a version, edition, or adaptation of the described Dataset

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_hasVersion_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_hasVersion_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_hasVersion_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasVersion > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_hasVersion_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasVersion > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_hasVersion_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_hasVersion_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasVersion > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [Dataset](#dataset_items_oneOf_i0_hasVersion_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_hasVersion_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_hasVersion_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasVersion > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_hasVersion_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasVersion > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_inSeries"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries`

**Title:** in series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of Dataset Series this dataset belongs to

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [DatasetSeries](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i1)        |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries`

**Title:** DatasetSeries

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/datasetseries |

**Description:** inline description of DatasetSeries

| Property                                                                                             | Type           | Title/Description                                                                   |
| ---------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_@id )                               | string         | -                                                                                   |
| - [@type](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_@type )                           | string         | -                                                                                   |
| - [contactPoint](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint )             | Combination    | contact point                                                                       |
| - [first](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first )                           | Combination    | first                                                                               |
| - [last](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last )                             | Combination    | last                                                                                |
| - [seriesMember](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember )             | Combination    | series member                                                                       |
| - [accrualPeriodicity](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity ) | Combination    | frequency                                                                           |
| + [description](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_description )               | string         | description                                                                         |
| - [descriptionMap](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_descriptionMap )         | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued )                         | Combination    | release date                                                                        |
| - [modified](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified )                     | Combination    | update/modification date                                                            |
| - [publisher](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher )                   | Combination    | publisher                                                                           |
| - [spatial](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial )                       | Combination    | spatial/geographic coverage                                                         |
| - [temporal](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal )                     | Combination    | temporal coverage                                                                   |
| + [title](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_title )                           | string         | title                                                                               |
| - [titleMap](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_titleMap )                     | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"DatasetSeries"` |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint`

**Title:** contact point

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of contacts that can be used for sending comments about the Dataset Series

| Any of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                      | Description |
| ---------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                          |
| ------------------------------------------------------------------------------------------------------- |
| [Kind](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Kind](#contactPoint_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the contact

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the contact

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first`

**Title:** first

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The first dataset in an ordered dataset series

| One of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i0)  |
| [Dataset](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of the first dataset

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the first dataset

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last`

**Title:** last

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The last dataset in an ordered dataset series

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i0)  |
| [Dataset](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of the last dataset

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the last dataset

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember`

**Title:** series member

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of members of the Dataset Series

| Any of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                      | Description |
| ---------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                           |
| -------------------------------------------------------------------------------------------------------- |
| [Dataset](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of the member dataset

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the member dataset

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity`

**Title:** frequency

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The frequency at which the Dataset Series is updated

| One of(Option)                                                                                    |
| ------------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i0)    |
| [frequency](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i2)    |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity > oneOf > frequency`

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/frequency |

**Description:** inline description of Frequency

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Frequency

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > description`

**Title:** description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A free-text account of the Dataset Series

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g.,publication) of the Dataset Series

| Any of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Dataset Series was changed or modified

| Any of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                |
| --------------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity (organization) responsible for ensuring the coherency of the Dataset Series

| One of(Option)                                                                        |
| ------------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0) |
| [Agent](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1)  |
| [item 2](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of publisher

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of publisher

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region that is covered by the Dataset Series

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                 | Description |
| ----------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                       |
| ---------------------------------------------------------------------------------------------------- |
| [Location](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                 |
| **Required**              | No                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                         |
| **Same definition as**    | [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of temporal periods that the Dataset Series covers

| Any of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                  | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                            |
| --------------------------------------------------------------------------------------------------------- |
| [PeriodOfTime](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                      |
| **Required**              | No                                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of PeriodOfTime

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A name given to the Dataset Series

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_inSeries_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of DatasetSeries

##### <a name="dataset_items_oneOf_i0_keyword"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > keyword`

**Title:** keyword/tag

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of keywords or tags describing the Dataset

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_keyword_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_keyword_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_keyword_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > keyword > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_keyword_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > keyword > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_keyword_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_keyword_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > keyword > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="dataset_items_oneOf_i0_keywordMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > keywordMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="dataset_items_oneOf_i0_landingPage"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > landingPage`

**Title:** landing page

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A web page that provides access to the Dataset, its Distributions and/or additional information

| One of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_landingPage_oneOf_i0)   |
| [Document](#dataset_items_oneOf_i0_landingPage_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_landingPage_oneOf_i2)   |

###### <a name="dataset_items_oneOf_i0_landingPage_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > landingPage > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_landingPage_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > landingPage > oneOf > Document`

**Title:** Document

|                           |                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                        |
| **Required**              | No                                                                                              |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Document](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Document

###### <a name="dataset_items_oneOf_i0_landingPage_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > landingPage > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Document

##### <a name="dataset_items_oneOf_i0_previousVersion"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > previousVersion`

**Title:** previous version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** reference to the previous dataset version

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_previousVersion_oneOf_i0)  |
| [Dataset](#dataset_items_oneOf_i0_previousVersion_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_previousVersion_oneOf_i2)  |

###### <a name="dataset_items_oneOf_i0_previousVersion_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > previousVersion > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_previousVersion_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > previousVersion > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_previousVersion_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > previousVersion > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_qualifiedRelation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation`

**Title:** qualified relation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Qualified relationship with role of the dataset with another resource

| Any of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                          | Description |
| ------------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [Relationship](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship`

**Title:** Relationship

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/relationship |

**Description:** inline description of Relationship

| Property                                                                                  | Type   | Title/Description |
| ----------------------------------------------------------------------------------------- | ------ | ----------------- |
| - [@id](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_@id )           | string | -                 |
| - [@type](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_@type )       | string | -                 |
| + [hadRole](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_hadRole )   | string | role              |
| + [relation](#dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_relation ) | string | relation          |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Relationship"` |

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_hadRole"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > hadRole`

**Title:** role

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The function of an entity or agent with respect to a dataset

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i0_relation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > relation`

**Title:** relation

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Link to the entity related to the dataset

###### <a name="dataset_items_oneOf_i0_qualifiedRelation_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Relationship

##### <a name="dataset_items_oneOf_i0_spatialResolutionInMeters"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Spatial resolution in meters

##### <a name="dataset_items_oneOf_i0_temporalResolution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporalResolution`

**Title:** temporal resolution

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Temporal resolution using xsd:duration syntax

##### <a name="dataset_items_oneOf_i0_theme"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > theme`

**Title:** theme/category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of themes of the dataset

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_theme_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_theme_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_theme_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > theme > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_theme_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > theme > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                              | Description |
| ------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_theme_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_theme_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > theme > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Concept](#dataset_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > theme > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > theme > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

##### <a name="dataset_items_oneOf_i0_version"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > version`

**Title:** version

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The version indicator (name or identifier) of a resource

##### <a name="dataset_items_oneOf_i0_describedBy"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > describedBy`

**Title:** data dictionary

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A distribution describing the Data Dictionary for this dataset

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_describedBy_oneOf_i0)       |
| [Distribution](#dataset_items_oneOf_i0_describedBy_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_describedBy_oneOf_i2)       |

###### <a name="dataset_items_oneOf_i0_describedBy_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > describedBy > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_describedBy_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > describedBy > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **Type**                  | `object`                                                               |
| **Required**              | No                                                                     |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [Distribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Distribution

###### <a name="dataset_items_oneOf_i0_describedBy_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > describedBy > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

##### <a name="dataset_items_oneOf_i0_geographicBoundingBox"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > geographicBoundingBox`

**Title:** geographic bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of WGS84 Geographic Bounding Boxes for this dataset

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > geographicBoundingBox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > geographicBoundingBox > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > geographicBoundingBox > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                 |
| ---------------------------------------------------------------------------------------------- |
| [GeographicBoundingBox](#dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i1)                |

###### <a name="dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox`

**Title:** GeographicBoundingBox

|                           |                                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                            |
| **Required**              | No                                                                                                                                                                  |
| **Additional properties** | Any type allowed                                                                                                                                                    |
| **Same definition as**    | [GeographicBoundingBox](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of GeographicBoundingBox

###### <a name="dataset_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of GeographicBoundingBox

##### <a name="dataset_items_oneOf_i0_liabilityStatement"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement`

**Title:** liability statement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A liability statement about the dataset

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i0)             |
| [LiabilityStatement](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i2)             |

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement`

**Title:** LiabilityStatement

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Defined in**            | /dcat-us/3.0.0/definitions/liabilitystatement |

**Description:** inline description of LiabilityStatement

| Property                                                                    | Type           | Title/Description                                                                       |
| --------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_@id )           | string         | -                                                                                       |
| - [@type](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_@type )       | string         | -                                                                                       |
| - [label](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_label )       | null or string | liability statement text                                                                |
| - [labelMap](#dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_labelMap ) | null or object | Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > @type`

|              |                        |
| ------------ | ---------------------- |
| **Type**     | `string`               |
| **Required** | No                     |
| **Default**  | `"LiabilityStatement"` |

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_label"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > label`

**Title:** liability statement text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Full text of the liability statement

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i1_labelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_liabilityStatement_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > liabilityStatement > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of LiabilityStatement

##### <a name="dataset_items_oneOf_i0_metadataDistribution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > metadataDistribution`

**Title:** metadata distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Distribution to "original" metadata document

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_metadataDistribution_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_metadataDistribution_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_metadataDistribution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > metadataDistribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_metadataDistribution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > metadataDistribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_metadataDistribution_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_metadataDistribution_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > metadataDistribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [Distribution](#dataset_items_oneOf_i0_metadataDistribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_metadataDistribution_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_metadataDistribution_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > metadataDistribution > anyOf > item 1 > item 1 items > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **Type**                  | `object`                                                               |
| **Required**              | No                                                                     |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [Distribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Distribution

###### <a name="dataset_items_oneOf_i0_metadataDistribution_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > metadataDistribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

##### <a name="dataset_items_oneOf_i0_purpose"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > purpose`

**Title:** purpose

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The purpose of the dataset

##### <a name="dataset_items_oneOf_i0_purposeMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > purposeMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="dataset_items_oneOf_i0_accessRights"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information that indicates whether the Dataset is open data, has access restrictions or is public

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_accessRights_oneOf_i0)          |
| [RightsStatement](#dataset_items_oneOf_i0_accessRights_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_accessRights_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_accessRights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_accessRights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="dataset_items_oneOf_i0_accessRights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

##### <a name="dataset_items_oneOf_i0_accrualPeriodicity"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accrualPeriodicity`

**Title:** frequency

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The frequency at which the Dataset is updated

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_accrualPeriodicity_oneOf_i0)    |
| [frequency](#dataset_items_oneOf_i0_accrualPeriodicity_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_accrualPeriodicity_oneOf_i2)    |

###### <a name="dataset_items_oneOf_i0_accrualPeriodicity_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accrualPeriodicity > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_accrualPeriodicity_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accrualPeriodicity > oneOf > frequency`

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/frequency |

**Description:** inline description of Frequency

###### <a name="dataset_items_oneOf_i0_accrualPeriodicity_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > accrualPeriodicity > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Frequency

##### <a name="dataset_items_oneOf_i0_conformsTo"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > conformsTo`

**Title:** conforms to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of standards to which the described Dataset conforms

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Standard](#dataset_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                    |
| **Required**              | No                                                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

###### <a name="dataset_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

##### <a name="dataset_items_oneOf_i0_contributor"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contributor`

**Title:** contributor

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents contributing to the Dataset

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_contributor_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_contributor_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_contributor_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contributor > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_contributor_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contributor > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_contributor_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_contributor_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contributor > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [Agent](#dataset_items_oneOf_i0_contributor_anyOf_i1_items_oneOf_i0)  |
| [item 1](#dataset_items_oneOf_i0_contributor_anyOf_i1_items_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_contributor_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contributor > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="dataset_items_oneOf_i0_contributor_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > contributor > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

##### <a name="dataset_items_oneOf_i0_created"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Dataset was first created

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_created_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_created_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_created_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_created_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

##### <a name="dataset_items_oneOf_i0_creator"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity responsible for producing the dataset

| One of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_creator_oneOf_i0) |
| [Agent](#dataset_items_oneOf_i0_creator_oneOf_i1)  |
| [item 2](#dataset_items_oneOf_i0_creator_oneOf_i2) |

###### <a name="dataset_items_oneOf_i0_creator_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > creator > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_creator_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > creator > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="dataset_items_oneOf_i0_creator_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > creator > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

##### <a name="dataset_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > description`

**Title:** description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A free-text account of the Dataset

##### <a name="dataset_items_oneOf_i0_descriptionMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="dataset_items_oneOf_i0_hasPart"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasPart`

**Title:** has part

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related datasets that are part of the described dataset

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_hasPart_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_hasPart_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_hasPart_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasPart > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_hasPart_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasPart > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_hasPart_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_hasPart_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasPart > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                     |
| ------------------------------------------------------------------ |
| [Dataset](#dataset_items_oneOf_i0_hasPart_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_hasPart_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_hasPart_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasPart > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_hasPart_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasPart > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_identifier"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > identifier`

**Title:** identifier

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The unique identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalog

##### <a name="dataset_items_oneOf_i0_isReferencedBy"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > isReferencedBy`

**Title:** is referenced by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of links to related resources, such as publications, that reference, cite, or otherwise point to the Dataset

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_isReferencedBy_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_isReferencedBy_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_isReferencedBy_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > isReferencedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_isReferencedBy_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > isReferencedBy > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                       | Description               |
| --------------------------------------------------------------------- | ------------------------- |
| [item 1 items](#dataset_items_oneOf_i0_isReferencedBy_anyOf_i1_items) | reference iri of Resource |

###### <a name="dataset_items_oneOf_i0_isReferencedBy_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > isReferencedBy > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

##### <a name="dataset_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Date of formal issuance (e.g., publication) of the dataset

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

##### <a name="dataset_items_oneOf_i0_language"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Language or languages used in the Dataset. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_language_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_language_anyOf_i1) |
| [item 2](#dataset_items_oneOf_i0_language_anyOf_i2) |

###### <a name="dataset_items_oneOf_i0_language_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_language_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="dataset_items_oneOf_i0_language_anyOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [item 2 items](#dataset_items_oneOf_i0_language_anyOf_i2_items) | -           |

###### <a name="dataset_items_oneOf_i0_language_anyOf_i2_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

##### <a name="dataset_items_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Dataset was changed or modified

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="dataset_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

##### <a name="dataset_items_oneOf_i0_provenance"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance`

**Title:** provenance

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of statements about the lineage of a Dataset

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_provenance_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_provenance_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_provenance_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [ProvenanceStatement](#dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i1)              |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement`

**Title:** ProvenanceStatement

|                           |                                                |
| ------------------------- | ---------------------------------------------- |
| **Type**                  | `object`                                       |
| **Required**              | No                                             |
| **Additional properties** | Any type allowed                               |
| **Defined in**            | /dcat-us/3.0.0/definitions/provenancestatement |

**Description:** inline description of ProvenanceStatement

| Property                                                                           | Type           | Title/Description                                                                              |
| ---------------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------- |
| - [@id](#dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_@id )           | string         | -                                                                                              |
| - [@type](#dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_@type )       | string         | -                                                                                              |
| - [label](#dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_label )       | null or string | provenance statement text                                                                      |
| - [labelMap](#dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_labelMap ) | null or object | Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > @type`

|              |                         |
| ------------ | ----------------------- |
| **Type**     | `string`                |
| **Required** | No                      |
| **Default**  | `"ProvenanceStatement"` |

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_label"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > label`

**Title:** provenance statement text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The text of the Provenance Statement

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i0_labelMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="dataset_items_oneOf_i0_provenance_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ProvenanceStatement

##### <a name="dataset_items_oneOf_i0_publisher"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** An organization responsible for making the Dataset available

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Organization](#dataset_items_oneOf_i0_publisher_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_publisher_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > publisher > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="dataset_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > publisher > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

##### <a name="dataset_items_oneOf_i0_relation"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > relation`

**Title:** related resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of references to a related resource

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_relation_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_relation_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_relation_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > relation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_relation_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > relation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                 | Description               |
| --------------------------------------------------------------- | ------------------------- |
| [item 1 items](#dataset_items_oneOf_i0_relation_anyOf_i1_items) | reference iri of Resource |

###### <a name="dataset_items_oneOf_i0_relation_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > relation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

##### <a name="dataset_items_oneOf_i0_replaces"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > replaces`

**Title:** replaces

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of Datasets replaced by this Dataset

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_replaces_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_replaces_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_replaces_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > replaces > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_replaces_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > replaces > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_replaces_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_replaces_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > replaces > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                      |
| ------------------------------------------------------------------- |
| [Dataset](#dataset_items_oneOf_i0_replaces_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_replaces_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_replaces_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > replaces > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_replaces_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > replaces > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_rights"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of statements concerning all rights for the Dataset not addressed with license or accessRights, such as copyright statements

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_rights_oneOf_i0)          |
| [RightsStatement](#dataset_items_oneOf_i0_rights_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_rights_oneOf_i2)          |

###### <a name="dataset_items_oneOf_i0_rights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_rights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="dataset_items_oneOf_i0_rights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

##### <a name="dataset_items_oneOf_i0_rightsHolder"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rightsHolder`

**Title:** rights holder

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents (organizations) holding rights on the Dataset

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_rightsHolder_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_rightsHolder_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_rightsHolder_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rightsHolder > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_rightsHolder_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rightsHolder > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_rightsHolder_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_rightsHolder_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rightsHolder > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [Organization](#dataset_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rightsHolder > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="dataset_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > rightsHolder > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

##### <a name="dataset_items_oneOf_i0_source"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > source`

**Title:** data source

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related Datasets from which the described Dataset is derived

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_source_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_source_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_source_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > source > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_source_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > source > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_source_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_source_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > source > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                    |
| ----------------------------------------------------------------- |
| [Dataset](#dataset_items_oneOf_i0_source_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_source_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_source_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > source > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [Dataset](#dataset_items_oneOf_i0) |

**Description:** inline description of Dataset

###### <a name="dataset_items_oneOf_i0_source_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > source > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

##### <a name="dataset_items_oneOf_i0_spatial"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region or regions that are covered by the Dataset

| One of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_spatial_oneOf_i0)   |
| [Location](#dataset_items_oneOf_i0_spatial_oneOf_i1) |
| [item 2](#dataset_items_oneOf_i0_spatial_oneOf_i2)   |
| [item 3](#dataset_items_oneOf_i0_spatial_oneOf_i3)   |

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                 |
| **Required**              | No                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                         |
| **Same definition as**    | [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i2"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i3"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > item 3`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 3 items](#dataset_items_oneOf_i0_spatial_oneOf_i3_items) | -           |

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i3_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > item 3 > item 3 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                      |
| ------------------------------------------------------------------- |
| [Location](#dataset_items_oneOf_i0_spatial_oneOf_i3_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_spatial_oneOf_i3_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i3_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > item 3 > item 3 items > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                 |
| **Required**              | No                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                         |
| **Same definition as**    | [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

###### <a name="dataset_items_oneOf_i0_spatial_oneOf_i3_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > spatial > oneOf > item 3 > item 3 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

##### <a name="dataset_items_oneOf_i0_subject"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > subject`

**Title:** subject

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of primary subjects of the dataset

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_subject_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_subject_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_subject_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > subject > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_subject_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > subject > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_subject_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_subject_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > subject > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                     |
| ------------------------------------------------------------------ |
| [Concept](#dataset_items_oneOf_i0_subject_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_subject_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_subject_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > subject > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_subject_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > subject > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

##### <a name="dataset_items_oneOf_i0_temporal"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of temporal periods that the dataset covers

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_temporal_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_temporal_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_temporal_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_temporal_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_temporal_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_temporal_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [PeriodOfTime](#dataset_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1)       |

###### <a name="dataset_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                      |
| **Required**              | No                                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of PeriodOfTime

###### <a name="dataset_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

##### <a name="dataset_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A name given to the Dataset

##### <a name="dataset_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="dataset_items_oneOf_i0_category"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of categories of the dataset

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_category_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_category_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_category_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > category > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_category_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > category > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_category_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_category_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > category > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                      |
| ------------------------------------------------------------------- |
| [Concept](#dataset_items_oneOf_i0_category_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_category_anyOf_i1_items_oneOf_i1)  |

###### <a name="dataset_items_oneOf_i0_category_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > category > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="dataset_items_oneOf_i0_category_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > category > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

##### <a name="dataset_items_oneOf_i0_hasQualityMeasurement"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasQualityMeasurement`

**Title:** quality measurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of quality measurements for the dataset

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasQualityMeasurement > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [QualityMeasurement](#dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

###### <a name="dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

|                           |                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                         |
| **Required**              | No                                                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                                                 |
| **Same definition as**    | [QualityMeasurement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of QualityMeasurement

###### <a name="dataset_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of QualityMeasurement

##### <a name="dataset_items_oneOf_i0_page"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > page`

**Title:** documentation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of pages or documents about this dataset

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_page_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_page_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_page_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > page > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_page_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > page > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_page_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_page_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > page > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Document](#dataset_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_page_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > page > anyOf > item 1 > item 1 items > oneOf > Document`

**Title:** Document

|                           |                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                        |
| **Required**              | No                                                                                              |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Document](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Document

###### <a name="dataset_items_oneOf_i0_page_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > page > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Document

##### <a name="dataset_items_oneOf_i0_qualifiedAttribution"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedAttribution`

**Title:** qualified attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents having some form of responsibility for the dataset

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedAttribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedAttribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedAttribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [Attribution](#dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i1)      |

###### <a name="dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution`

**Title:** Attribution

|                           |                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                 |
| **Required**              | No                                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                                         |
| **Same definition as**    | [Attribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Attribution

###### <a name="dataset_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Attribution

##### <a name="dataset_items_oneOf_i0_wasAttributedTo"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasAttributedTo`

**Title:** attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents attributed to this dataset

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_wasAttributedTo_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_wasAttributedTo_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasAttributedTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasAttributedTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                        | Description |
| ---------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasAttributedTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [Agent](#dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1_items_oneOf_i0)  |
| [item 1](#dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1_items_oneOf_i1) |

###### <a name="dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasAttributedTo > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="dataset_items_oneOf_i0_wasAttributedTo_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasAttributedTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

##### <a name="dataset_items_oneOf_i0_wasGeneratedBy"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasGeneratedBy`

**Title:** was generated by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of activities that generated, or provide the business context for the creation of the dataset

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasGeneratedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasGeneratedBy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasGeneratedBy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [Activity](#dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasGeneratedBy > anyOf > item 1 > item 1 items > oneOf > Activity`

**Title:** Activity

|                           |                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                   |
| **Required**              | No                                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                           |
| **Same definition as**    | [Activity](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Activity

###### <a name="dataset_items_oneOf_i0_wasGeneratedBy_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasGeneratedBy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Activity

##### <a name="dataset_items_oneOf_i0_wasUsedBy"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasUsedBy`

**Title:** used by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of activities that used the Dataset

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#dataset_items_oneOf_i0_wasUsedBy_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_wasUsedBy_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_wasUsedBy_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasUsedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_wasUsedBy_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasUsedBy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                  | Description |
| ---------------------------------------------------------------- | ----------- |
| [item 1 items](#dataset_items_oneOf_i0_wasUsedBy_anyOf_i1_items) | -           |

###### <a name="dataset_items_oneOf_i0_wasUsedBy_anyOf_i1_items"></a>DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasUsedBy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [Activity](#dataset_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#dataset_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i1)   |

###### <a name="dataset_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity`

**Title:** Activity

|                           |                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                   |
| **Required**              | No                                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                           |
| **Same definition as**    | [Activity](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Activity

###### <a name="dataset_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Activity

##### <a name="dataset_items_oneOf_i0_image"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > image`

**Title:** image

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Link to a thumbnail picture illustrating the content of the dataset

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#dataset_items_oneOf_i0_image_anyOf_i0) |
| [item 1](#dataset_items_oneOf_i0_image_anyOf_i1) |

###### <a name="dataset_items_oneOf_i0_image_anyOf_i0"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > image > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="dataset_items_oneOf_i0_image_anyOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > image > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** The link to the image

##### <a name="dataset_items_oneOf_i0_scopeNote"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > scopeNote`

**Title:** usage note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** usage note for the dataset

##### <a name="dataset_items_oneOf_i0_scopeNoteMap"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > Dataset > scopeNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="dataset_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > dataset > dataset items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

## <a name="keyword"></a>Property `DCAT-US 3 Catalog > keyword`

**Title:** keyword/tag

|              |                           |
| ------------ | ------------------------- |
| **Type**     | `null or array of string` |
| **Required** | No                        |

**Description:** A list of keywords or tags describing the resource

## <a name="keywordMap"></a>Property `DCAT-US 3 Catalog > keywordMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="record"></a>Property `DCAT-US 3 Catalog > record`

**Title:** catalog record

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A record describing a single resource (e.g., a dataset, a data service) that is part of the catalog

| Any of(Option)             |
| -------------------------- |
| [item 0](#record_anyOf_i0) |
| [item 1](#record_anyOf_i1) |

### <a name="record_anyOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="record_anyOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#record_anyOf_i1_items) | -           |

#### <a name="record_anyOf_i1_items"></a>DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [CatalogRecord](#record_anyOf_i1_items_oneOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i1)        |

##### <a name="record_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord`

**Title:** CatalogRecord

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/catalogrecord |

**Description:** inline description of the record

| Property                                                        | Type           | Title/Description                                                                   |
| --------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#record_anyOf_i1_items_oneOf_i0_@id )                   | string         | -                                                                                   |
| - [@type](#record_anyOf_i1_items_oneOf_i0_@type )               | string         | -                                                                                   |
| - [status](#record_anyOf_i1_items_oneOf_i0_status )             | Combination    | change type                                                                         |
| - [conformsTo](#record_anyOf_i1_items_oneOf_i0_conformsTo )     | Combination    | application profile                                                                 |
| - [description](#record_anyOf_i1_items_oneOf_i0_description )   | Combination    | description                                                                         |
| - [issued](#record_anyOf_i1_items_oneOf_i0_issued )             | Combination    | listing date                                                                        |
| - [language](#record_anyOf_i1_items_oneOf_i0_language )         | Combination    | language                                                                            |
| + [modified](#record_anyOf_i1_items_oneOf_i0_modified )         | Combination    | update/modification date                                                            |
| - [source](#record_anyOf_i1_items_oneOf_i0_source )             | Combination    | source metadata                                                                     |
| - [title](#record_anyOf_i1_items_oneOf_i0_title )               | null or string | title                                                                               |
| - [titleMap](#record_anyOf_i1_items_oneOf_i0_titleMap )         | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [primaryTopic](#record_anyOf_i1_items_oneOf_i0_primaryTopic ) | string         | primary topic                                                                       |

###### <a name="record_anyOf_i1_items_oneOf_i0_@id"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="record_anyOf_i1_items_oneOf_i0_@type"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"CatalogRecord"` |

###### <a name="record_anyOf_i1_items_oneOf_i0_status"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > status`

**Title:** change type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The status of the catalog record in the context of editorial flow of the dataset and data service descriptions

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_status_oneOf_i0)  |
| [Concept](#record_anyOf_i1_items_oneOf_i0_status_oneOf_i1) |
| [item 2](#record_anyOf_i1_items_oneOf_i0_status_oneOf_i2)  |

###### <a name="record_anyOf_i1_items_oneOf_i0_status_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > status > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="record_anyOf_i1_items_oneOf_i0_status_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > status > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of status

###### <a name="record_anyOf_i1_items_oneOf_i0_status_oneOf_i2"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > status > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of status

###### <a name="record_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > conformsTo`

**Title:** application profile

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An Application Profile that the Catalog Record's metadata conforms to

| One of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_conformsTo_oneOf_i0)   |
| [Standard](#record_anyOf_i1_items_oneOf_i0_conformsTo_oneOf_i1) |
| [item 2](#record_anyOf_i1_items_oneOf_i0_conformsTo_oneOf_i2)   |

###### <a name="record_anyOf_i1_items_oneOf_i0_conformsTo_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > conformsTo > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="record_anyOf_i1_items_oneOf_i0_conformsTo_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > conformsTo > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                    |
| **Required**              | No                                                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of application profile

###### <a name="record_anyOf_i1_items_oneOf_i0_conformsTo_oneOf_i2"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > conformsTo > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of application profile

###### <a name="record_anyOf_i1_items_oneOf_i0_description"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > description`

**Title:** description

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of free-text accounts of the catalog record

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_description_anyOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i0_description_anyOf_i1) |

###### <a name="record_anyOf_i1_items_oneOf_i0_description_anyOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > description > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="record_anyOf_i1_items_oneOf_i0_description_anyOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > description > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                            | Description |
| -------------------------------------------------------------------------- | ----------- |
| [item 1 items](#record_anyOf_i1_items_oneOf_i0_description_anyOf_i1_items) | -           |

###### <a name="record_anyOf_i1_items_oneOf_i0_description_anyOf_i1_items"></a>DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > description > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued`

**Title:** listing date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of dates on which the catalog record was included in the catalog

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [item 1 items](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items) | -           |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items"></a>DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 1 > item 1 items

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [item 0](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i1) |
| [item 2](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i2) |
| [item 3](#record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i3) |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i2"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="record_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_items_oneOf_i3"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > issued > anyOf > item 1 > item 1 items > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="record_anyOf_i1_items_oneOf_i0_language"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A language or languages used in the textual metadata describing titles, descriptions, etc. of the catalog record. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_language_anyOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i0_language_anyOf_i1) |
| [item 2](#record_anyOf_i1_items_oneOf_i0_language_anyOf_i2) |

###### <a name="record_anyOf_i1_items_oneOf_i0_language_anyOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="record_anyOf_i1_items_oneOf_i0_language_anyOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="record_anyOf_i1_items_oneOf_i0_language_anyOf_i2"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                         | Description |
| ----------------------------------------------------------------------- | ----------- |
| [item 2 items](#record_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items) | -           |

###### <a name="record_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items"></a>DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="record_anyOf_i1_items_oneOf_i0_modified"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > modified`

**Title:** update/modification date

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | Yes         |

**Description:** The most recent date on which the catalog record was changed or modified

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_modified_oneOf_i0) |
| [item 1](#record_anyOf_i1_items_oneOf_i0_modified_oneOf_i1) |
| [item 2](#record_anyOf_i1_items_oneOf_i0_modified_oneOf_i2) |
| [item 3](#record_anyOf_i1_items_oneOf_i0_modified_oneOf_i3) |

###### <a name="record_anyOf_i1_items_oneOf_i0_modified_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > modified > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="record_anyOf_i1_items_oneOf_i0_modified_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > modified > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="record_anyOf_i1_items_oneOf_i0_modified_oneOf_i2"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > modified > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="record_anyOf_i1_items_oneOf_i0_modified_oneOf_i3"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > modified > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="record_anyOf_i1_items_oneOf_i0_source"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > source`

**Title:** source metadata

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The original metadata that was used in creating metadata for the items in the catalog record

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#record_anyOf_i1_items_oneOf_i0_source_oneOf_i0)   |
| [resource](#record_anyOf_i1_items_oneOf_i0_source_oneOf_i1) |
| [item 2](#record_anyOf_i1_items_oneOf_i0_source_oneOf_i2)   |

###### <a name="record_anyOf_i1_items_oneOf_i0_source_oneOf_i0"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > source > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="record_anyOf_i1_items_oneOf_i0_source_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > source > oneOf > resource`

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/resource |

**Description:** inline description of the source

###### <a name="record_anyOf_i1_items_oneOf_i0_source_oneOf_i2"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > source > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the source

###### <a name="record_anyOf_i1_items_oneOf_i0_title"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Catalog Record

###### <a name="record_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="record_anyOf_i1_items_oneOf_i0_primaryTopic"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > CatalogRecord > primaryTopic`

**Title:** primary topic

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A link to the Dataset, Data service or Catalog described in the Catalog Record

##### <a name="record_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > record > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the record

## <a name="service"></a>Property `DCAT-US 3 Catalog > service`

**Title:** service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of data services that are listed in the Catalog

| Any of(Option)              |
| --------------------------- |
| [item 0](#service_anyOf_i0) |
| [item 1](#service_anyOf_i1) |

### <a name="service_anyOf_i0"></a>Property `DCAT-US 3 Catalog > service > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="service_anyOf_i1"></a>Property `DCAT-US 3 Catalog > service > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#service_anyOf_i1_items) | -           |

#### <a name="service_anyOf_i1_items"></a>DCAT-US 3 Catalog > service > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [DataService](#service_anyOf_i1_items_oneOf_i0) |
| [item 1](#service_anyOf_i1_items_oneOf_i1)      |

##### <a name="service_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > service > anyOf > item 1 > item 1 items > oneOf > DataService`

**Title:** DataService

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [DataService](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the service

##### <a name="service_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > service > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the service

## <a name="theme"></a>Property `DCAT-US 3 Catalog > theme`

**Title:** theme/category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of categories for the Catalog. A Catalog may be associated with multiple themes

| Any of(Option)            |
| ------------------------- |
| [item 0](#theme_anyOf_i0) |
| [item 1](#theme_anyOf_i1) |

### <a name="theme_anyOf_i0"></a>Property `DCAT-US 3 Catalog > theme > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="theme_anyOf_i1"></a>Property `DCAT-US 3 Catalog > theme > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [item 1 items](#theme_anyOf_i1_items) | -           |

#### <a name="theme_anyOf_i1_items"></a>DCAT-US 3 Catalog > theme > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [Concept](#theme_anyOf_i1_items_oneOf_i0) |
| [item 1](#theme_anyOf_i1_items_oneOf_i1)  |

##### <a name="theme_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > theme > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the theme

##### <a name="theme_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > theme > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the theme

## <a name="themeTaxonomy"></a>Property `DCAT-US 3 Catalog > themeTaxonomy`

**Title:** themes

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A knowledge organization system (KOS) used to classify the resources documented in the catalog (e.g., datasets and services)

| Any of(Option)                    |
| --------------------------------- |
| [item 0](#themeTaxonomy_anyOf_i0) |
| [item 1](#themeTaxonomy_anyOf_i1) |

### <a name="themeTaxonomy_anyOf_i0"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="themeTaxonomy_anyOf_i1"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [item 1 items](#themeTaxonomy_anyOf_i1_items) | -           |

#### <a name="themeTaxonomy_anyOf_i1_items"></a>DCAT-US 3 Catalog > themeTaxonomy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [ConceptScheme](#themeTaxonomy_anyOf_i1_items_oneOf_i0) |
| [item 1](#themeTaxonomy_anyOf_i1_items_oneOf_i1)        |

##### <a name="themeTaxonomy_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > item 1 > item 1 items > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                   |
| **Required**              | No                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                           |
| **Same definition as**    | [ConceptScheme](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of ConceptScheme

##### <a name="themeTaxonomy_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > themeTaxonomy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

## <a name="accessRights"></a>Property `DCAT-US 3 Catalog > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information that indicates whether the Catalog is open data, has access restrictions or is not public

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#accessRights_oneOf_i0)          |
| [RightsStatement](#accessRights_oneOf_i1) |
| [item 2](#accessRights_oneOf_i2)          |

### <a name="accessRights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="accessRights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of access rights

### <a name="accessRights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the access rights

## <a name="conformsTo"></a>Property `DCAT-US 3 Catalog > conformsTo`

**Title:** schema version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An established standard to which the described catalog conforms

| One of(Option)                   |
| -------------------------------- |
| [item 0](#conformsTo_oneOf_i0)   |
| [Standard](#conformsTo_oneOf_i1) |
| [item 2](#conformsTo_oneOf_i2)   |

### <a name="conformsTo_oneOf_i0"></a>Property `DCAT-US 3 Catalog > conformsTo > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="conformsTo_oneOf_i1"></a>Property `DCAT-US 3 Catalog > conformsTo > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                    |
| **Required**              | No                                                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                                            |
| **Same definition as**    | [Standard](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

### <a name="conformsTo_oneOf_i2"></a>Property `DCAT-US 3 Catalog > conformsTo > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

## <a name="creator"></a>Property `DCAT-US 3 Catalog > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The entity responsible for creating the resource

| Any of(Option)              |
| --------------------------- |
| [item 0](#creator_anyOf_i0) |
| [item 1](#creator_anyOf_i1) |

### <a name="creator_anyOf_i0"></a>Property `DCAT-US 3 Catalog > creator > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="creator_anyOf_i1"></a>Property `DCAT-US 3 Catalog > creator > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#creator_anyOf_i1_items) | -           |

#### <a name="creator_anyOf_i1_items"></a>DCAT-US 3 Catalog > creator > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                             |
| ------------------------------------------ |
| [Agent](#creator_anyOf_i1_items_oneOf_i0)  |
| [item 1](#creator_anyOf_i1_items_oneOf_i1) |

##### <a name="creator_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > creator > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of creator

##### <a name="creator_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > creator > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of creator

## <a name="description"></a>Property `DCAT-US 3 Catalog > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Free-text description of the catalog (in the language indicated in the language property)

## <a name="descriptionMap"></a>Property `DCAT-US 3 Catalog > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="hasPart"></a>Property `DCAT-US 3 Catalog > hasPart`

**Title:** has part

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of related catalogs that are part of the described catalog

| Any of(Option)              |
| --------------------------- |
| [item 0](#hasPart_anyOf_i0) |
| [item 1](#hasPart_anyOf_i1) |

### <a name="hasPart_anyOf_i0"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="hasPart_anyOf_i1"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#hasPart_anyOf_i1_items) | -           |

#### <a name="hasPart_anyOf_i1_items"></a>DCAT-US 3 Catalog > hasPart > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [DCAT-US 3 Catalog](#hasPart_anyOf_i1_items_oneOf_i0) |
| [item 1](#hasPart_anyOf_i1_items_oneOf_i1)            |

##### <a name="hasPart_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > item 1 > item 1 items > oneOf > DCAT-US 3 Catalog`

**Title:** DCAT-US 3 Catalog

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [DCAT-US 3 Catalog](#root) |

**Description:** inline description of the related catalog

##### <a name="hasPart_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > hasPart > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the related catalog

## <a name="identifier"></a>Property `DCAT-US 3 Catalog > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of identifiers for the Catalog, e.g. the URI or other unique identifier

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_anyOf_i0) |
| [item 1](#identifier_anyOf_i1) |

### <a name="identifier_anyOf_i0"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="identifier_anyOf_i1"></a>Property `DCAT-US 3 Catalog > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#identifier_anyOf_i1_items) | -           |

#### <a name="identifier_anyOf_i1_items"></a>DCAT-US 3 Catalog > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="issued"></a>Property `DCAT-US 3 Catalog > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Date of formal issuance (e.g., publication) of the catalog

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `DCAT-US 3 Catalog > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="issued_anyOf_i1"></a>Property `DCAT-US 3 Catalog > issued > anyOf > item 1`

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

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="language"></a>Property `DCAT-US 3 Catalog > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Language or languages used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalog. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)               |
| ---------------------------- |
| [item 0](#language_anyOf_i0) |
| [item 1](#language_anyOf_i1) |
| [item 2](#language_anyOf_i2) |

### <a name="language_anyOf_i0"></a>Property `DCAT-US 3 Catalog > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="language_anyOf_i1"></a>Property `DCAT-US 3 Catalog > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

### <a name="language_anyOf_i2"></a>Property `DCAT-US 3 Catalog > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 2 items](#language_anyOf_i2_items) | -           |

#### <a name="language_anyOf_i2_items"></a>DCAT-US 3 Catalog > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

## <a name="license"></a>Property `DCAT-US 3 Catalog > license`

**Title:** license

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The license under which the Catalog can be used or reused

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#license_oneOf_i0)          |
| [LicenseDocument](#license_oneOf_i1) |
| [item 2](#license_oneOf_i2)          |

### <a name="license_oneOf_i0"></a>Property `DCAT-US 3 Catalog > license > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="license_oneOf_i1"></a>Property `DCAT-US 3 Catalog > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Required**              | No                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [LicenseDocument](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

**Description:** inline description of the license

### <a name="license_oneOf_i2"></a>Property `DCAT-US 3 Catalog > license > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the license

## <a name="modified"></a>Property `DCAT-US 3 Catalog > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Most recent date on which the catalog was changed, updated or modified

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `DCAT-US 3 Catalog > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="modified_anyOf_i1"></a>Property `DCAT-US 3 Catalog > modified > anyOf > item 1`

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

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `DCAT-US 3 Catalog > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `DCAT-US 3 Catalog > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `DCAT-US 3 Catalog > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `DCAT-US 3 Catalog > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `DCAT-US 3 Catalog > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Agent responsible for making the catalog available

| One of(Option)                |
| ----------------------------- |
| [item 0](#publisher_oneOf_i0) |
| [Agent](#publisher_oneOf_i1)  |
| [item 2](#publisher_oneOf_i2) |

### <a name="publisher_oneOf_i0"></a>Property `DCAT-US 3 Catalog > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="publisher_oneOf_i1"></a>Property `DCAT-US 3 Catalog > publisher > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [Agent](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the publisher

### <a name="publisher_oneOf_i2"></a>Property `DCAT-US 3 Catalog > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the publisher

## <a name="rights"></a>Property `DCAT-US 3 Catalog > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A statement that specifies rights associated with the catalog

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#rights_oneOf_i0)          |
| [RightsStatement](#rights_oneOf_i1) |
| [item 2](#rights_oneOf_i2)          |

### <a name="rights_oneOf_i0"></a>Property `DCAT-US 3 Catalog > rights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="rights_oneOf_i1"></a>Property `DCAT-US 3 Catalog > rights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [RightsStatement](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of rights

### <a name="rights_oneOf_i2"></a>Property `DCAT-US 3 Catalog > rights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of rights

## <a name="rightsHolder"></a>Property `DCAT-US 3 Catalog > rightsHolder`

**Title:** rights holder

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of organizations holding rights on the catalog

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#rightsHolder_anyOf_i0) |
| [item 1](#rightsHolder_anyOf_i1) |

### <a name="rightsHolder_anyOf_i0"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="rightsHolder_anyOf_i1"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#rightsHolder_anyOf_i1_items) | -           |

#### <a name="rightsHolder_anyOf_i1_items"></a>DCAT-US 3 Catalog > rightsHolder > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Organization](#rightsHolder_anyOf_i1_items_oneOf_i0) |
| [item 1](#rightsHolder_anyOf_i1_items_oneOf_i1)       |

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                         |
| **Required**              | No                                                                                               |
| **Additional properties** | Any type allowed                                                                                 |
| **Same definition as**    | [Organization](#dataset_items_oneOf_i0_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of rights holder

##### <a name="rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > rightsHolder > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of rights holder

## <a name="spatial"></a>Property `DCAT-US 3 Catalog > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The geographical area covered by the catalog

| Any of(Option)              |
| --------------------------- |
| [item 0](#spatial_anyOf_i0) |
| [item 1](#spatial_anyOf_i1) |

### <a name="spatial_anyOf_i0"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="spatial_anyOf_i1"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#spatial_anyOf_i1_items) | -           |

#### <a name="spatial_anyOf_i1_items"></a>DCAT-US 3 Catalog > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#spatial_anyOf_i1_items_oneOf_i1)   |

##### <a name="spatial_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                 |
| **Required**              | No                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                         |
| **Same definition as**    | [Location](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of geographical coverage

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of geographical coverage

## <a name="subject"></a>Property `DCAT-US 3 Catalog > subject`

**Title:** subject

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of subjects of the catalog

| Any of(Option)              |
| --------------------------- |
| [item 0](#subject_anyOf_i0) |
| [item 1](#subject_anyOf_i1) |

### <a name="subject_anyOf_i0"></a>Property `DCAT-US 3 Catalog > subject > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="subject_anyOf_i1"></a>Property `DCAT-US 3 Catalog > subject > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#subject_anyOf_i1_items) | -           |

#### <a name="subject_anyOf_i1_items"></a>DCAT-US 3 Catalog > subject > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                              |
| ------------------------------------------- |
| [Concept](#subject_anyOf_i1_items_oneOf_i0) |
| [item 1](#subject_anyOf_i1_items_oneOf_i1)  |

##### <a name="subject_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > subject > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the subject

##### <a name="subject_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > subject > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the subject

## <a name="temporal"></a>Property `DCAT-US 3 Catalog > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of temporal periods that the Catalog covers

| Any of(Option)               |
| ---------------------------- |
| [item 0](#temporal_anyOf_i0) |
| [item 1](#temporal_anyOf_i1) |

### <a name="temporal_anyOf_i0"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="temporal_anyOf_i1"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>DCAT-US 3 Catalog > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#temporal_anyOf_i1_items_oneOf_i1)       |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                      |
| **Required**              | No                                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                                              |
| **Same definition as**    | [PeriodOfTime](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the temporal coverage

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the temporal coverage

## <a name="title"></a>Property `DCAT-US 3 Catalog > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The title of the catalog in the indicated language

## <a name="titleMap"></a>Property `DCAT-US 3 Catalog > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="category"></a>Property `DCAT-US 3 Catalog > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The category of the Catalog

| One of(Option)                |
| ----------------------------- |
| [item 0](#category_oneOf_i0)  |
| [Concept](#category_oneOf_i1) |
| [item 2](#category_oneOf_i2)  |

### <a name="category_oneOf_i0"></a>Property `DCAT-US 3 Catalog > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="category_oneOf_i1"></a>Property `DCAT-US 3 Catalog > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                           |
| **Required**              | No                                                                                                 |
| **Additional properties** | Any type allowed                                                                                   |
| **Same definition as**    | [Concept](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the category

### <a name="category_oneOf_i2"></a>Property `DCAT-US 3 Catalog > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the category

## <a name="homepage"></a>Property `DCAT-US 3 Catalog > homepage`

**Title:** homepage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The home page of the catalog (a public Web document usually available in HTML)

| One of(Option)                 |
| ------------------------------ |
| [item 0](#homepage_oneOf_i0)   |
| [Document](#homepage_oneOf_i1) |
| [item 2](#homepage_oneOf_i2)   |

### <a name="homepage_oneOf_i0"></a>Property `DCAT-US 3 Catalog > homepage > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="homepage_oneOf_i1"></a>Property `DCAT-US 3 Catalog > homepage > oneOf > Document`

**Title:** Document

|                           |                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                        |
| **Required**              | No                                                                                              |
| **Additional properties** | Any type allowed                                                                                |
| **Same definition as**    | [Document](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the home page

### <a name="homepage_oneOf_i2"></a>Property `DCAT-US 3 Catalog > homepage > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the home page

## <a name="qualifiedAttribution"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution`

**Title:** qualified attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of agents having some form of responsibility for the catalog

| Any of(Option)                           |
| ---------------------------------------- |
| [item 0](#qualifiedAttribution_anyOf_i0) |
| [item 1](#qualifiedAttribution_anyOf_i1) |

### <a name="qualifiedAttribution_anyOf_i0"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="qualifiedAttribution_anyOf_i1"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 1 items](#qualifiedAttribution_anyOf_i1_items) | -           |

#### <a name="qualifiedAttribution_anyOf_i1_items"></a>DCAT-US 3 Catalog > qualifiedAttribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [Attribution](#qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#qualifiedAttribution_anyOf_i1_items_oneOf_i1)      |

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution`

**Title:** Attribution

|                           |                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                 |
| **Required**              | No                                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                                         |
| **Same definition as**    | [Attribution](#dataset_items_oneOf_i0_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Attribution

##### <a name="qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `DCAT-US 3 Catalog > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Attribution

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
