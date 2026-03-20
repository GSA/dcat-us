# DatasetSeries

**Title:** DatasetSeries

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An ordered series of datasets

| Property                                     | Type           | Title/Description                                                                   |
| -------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                               | string         | -                                                                                   |
| - [@type](#@type )                           | string         | -                                                                                   |
| - [contactPoint](#contactPoint )             | Combination    | contact point                                                                       |
| - [first](#first )                           | Combination    | first                                                                               |
| - [last](#last )                             | Combination    | last                                                                                |
| - [seriesMember](#seriesMember )             | Combination    | series member                                                                       |
| - [accrualPeriodicity](#accrualPeriodicity ) | Combination    | frequency                                                                           |
| + [description](#description )               | string         | description                                                                         |
| - [descriptionMap](#descriptionMap )         | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#issued )                         | Combination    | release date                                                                        |
| - [modified](#modified )                     | Combination    | update/modification date                                                            |
| - [publisher](#publisher )                   | Combination    | publisher                                                                           |
| - [spatial](#spatial )                       | Combination    | spatial/geographic coverage                                                         |
| - [temporal](#temporal )                     | Combination    | temporal coverage                                                                   |
| + [title](#title )                           | string         | title                                                                               |
| - [titleMap](#titleMap )                     | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `DatasetSeries > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `DatasetSeries > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"DatasetSeries"` |

## <a name="contactPoint"></a>Property `DatasetSeries > contactPoint`

**Title:** contact point

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of contacts that can be used for sending comments about the Dataset Series

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#contactPoint_anyOf_i0) |
| [item 1](#contactPoint_anyOf_i1) |

### <a name="contactPoint_anyOf_i0"></a>Property `DatasetSeries > contactPoint > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="contactPoint_anyOf_i1"></a>Property `DatasetSeries > contactPoint > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items) | -           |

#### <a name="contactPoint_anyOf_i1_items"></a>DatasetSeries > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Kind](#contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i1) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | /dcat-us/3.0.0/definitions/kind |

**Description:** inline description of the contact

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

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > @type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"Kind"` |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address`

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

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i0"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items) | -           |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items"></a>DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [Address](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0) |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i1)  |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address`

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

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Address"` |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_country-name"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > country-name`

**Title:** country

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The country of the Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_locality"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > locality`

**Title:** locality

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The city of the Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_postal-code"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > postal-code`

**Title:** postal code

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The postal code of the Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_region"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > region`

**Title:** administrative area

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The administrative area of the Address. Depending on the country, this corresponds to a province, a county, a region, or a state

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i0_street-address"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > Address > street-address`

**Title:** street address

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The street name and civic number of an Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_address_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > address > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Address

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_hasEmail"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > hasEmail`

**Title:** Email

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Email address for the contact

| Restrictions                      |                                                                                                                                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^mailto:[\w\_\~\!\$\&\'\(\)\*\+\,\;\=\:.-]+@[\w.-]+\.[\w.-]+?$``` [Test](https://regex101.com/?regex=%5Emailto%3A%5B%5Cw%5C_%5C~%5C%21%5C%24%5C%26%5C%27%5C%28%5C%29%5C%2A%5C%2B%5C%2C%5C%3B%5C%3D%5C%3A.-%5D%2B%40%5B%5Cw.-%5D%2B%5C.%5B%5Cw.-%5D%2B%3F%24) |

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_family-name"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > family-name`

**Title:** family name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The family name of the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_fn"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > fn`

**Title:** formatted name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The formatted text of the name of the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_given-name"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > given-name`

**Title:** given name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The given name of the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_organization-name"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > organization-name`

**Title:** organization name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The name of the organization to contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_tel"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > tel`

**Title:** telephone

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The telephone number for the contact

###### <a name="contactPoint_anyOf_i1_items_oneOf_i0_title"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind > title`

**Title:** position title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The position role of the person to contact

##### <a name="contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the contact

## <a name="first"></a>Property `DatasetSeries > first`

**Title:** first

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The first dataset in an ordered dataset series

| One of(Option)             |
| -------------------------- |
| [item 0](#first_oneOf_i0)  |
| [Dataset](#first_oneOf_i1) |
| [item 2](#first_oneOf_i2)  |

### <a name="first_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="first_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset`

**Title:** Dataset

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/dataset |

**Description:** inline description of the first dataset

| Property                                                                  | Type           | Title/Description                                                                   |
| ------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_@id )                                             | string         | -                                                                                   |
| - [@type](#first_oneOf_i1_@type )                                         | string         | -                                                                                   |
| - [otherIdentifier](#first_oneOf_i1_otherIdentifier )                     | Combination    | other identifier                                                                    |
| - [sample](#first_oneOf_i1_sample )                                       | Combination    | sample                                                                              |
| - [status](#first_oneOf_i1_status )                                       | Combination    | lifecycle status                                                                    |
| - [supportedSchema](#first_oneOf_i1_supportedSchema )                     | Combination    | supported schema                                                                    |
| - [versionNotes](#first_oneOf_i1_versionNotes )                           | null or string | version notes                                                                       |
| - [contactPoint](#first_oneOf_i1_contactPoint )                           | Combination    | contact point                                                                       |
| - [distribution](#first_oneOf_i1_distribution )                           | Combination    | dataset distribution                                                                |
| - [first](#first_oneOf_i1_first )                                         | Combination    | first                                                                               |
| - [hasCurrentVersion](#first_oneOf_i1_hasCurrentVersion )                 | Combination    | current version                                                                     |
| - [hasVersion](#first_oneOf_i1_hasVersion )                               | Combination    | has version                                                                         |
| - [inSeries](#first_oneOf_i1_inSeries )                                   | Combination    | in series                                                                           |
| - [keyword](#first_oneOf_i1_keyword )                                     | Combination    | keyword/tag                                                                         |
| - [keywordMap](#first_oneOf_i1_keywordMap )                               | null or object | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [landingPage](#first_oneOf_i1_landingPage )                             | Combination    | landing page                                                                        |
| - [previousVersion](#first_oneOf_i1_previousVersion )                     | Combination    | previous version                                                                    |
| - [qualifiedRelation](#first_oneOf_i1_qualifiedRelation )                 | Combination    | qualified relation                                                                  |
| - [spatialResolutionInMeters](#first_oneOf_i1_spatialResolutionInMeters ) | null or string | Spatial resolution (meters)                                                         |
| - [temporalResolution](#first_oneOf_i1_temporalResolution )               | null or string | temporal resolution                                                                 |
| - [theme](#first_oneOf_i1_theme )                                         | Combination    | theme/category                                                                      |
| - [version](#first_oneOf_i1_version )                                     | null or string | version                                                                             |
| - [describedBy](#first_oneOf_i1_describedBy )                             | Combination    | data dictionary                                                                     |
| - [geographicBoundingBox](#first_oneOf_i1_geographicBoundingBox )         | Combination    | geographic bounding box                                                             |
| - [liabilityStatement](#first_oneOf_i1_liabilityStatement )               | Combination    | liability statement                                                                 |
| - [metadataDistribution](#first_oneOf_i1_metadataDistribution )           | Combination    | metadata distribution                                                               |
| - [purpose](#first_oneOf_i1_purpose )                                     | null or string | purpose                                                                             |
| - [purposeMap](#first_oneOf_i1_purposeMap )                               | null or object | Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}        |
| - [accessRights](#first_oneOf_i1_accessRights )                           | Combination    | access rights                                                                       |
| - [accrualPeriodicity](#first_oneOf_i1_accrualPeriodicity )               | Combination    | frequency                                                                           |
| - [conformsTo](#first_oneOf_i1_conformsTo )                               | Combination    | conforms to                                                                         |
| - [contributor](#first_oneOf_i1_contributor )                             | Combination    | contributor                                                                         |
| - [created](#first_oneOf_i1_created )                                     | Combination    | creation date                                                                       |
| - [creator](#first_oneOf_i1_creator )                                     | Combination    | creator                                                                             |
| + [description](#first_oneOf_i1_description )                             | string         | description                                                                         |
| - [descriptionMap](#first_oneOf_i1_descriptionMap )                       | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [hasPart](#first_oneOf_i1_hasPart )                                     | Combination    | has part                                                                            |
| - [identifier](#first_oneOf_i1_identifier )                               | null or string | identifier                                                                          |
| - [isReferencedBy](#first_oneOf_i1_isReferencedBy )                       | Combination    | is referenced by                                                                    |
| - [issued](#first_oneOf_i1_issued )                                       | Combination    | release date                                                                        |
| - [language](#first_oneOf_i1_language )                                   | Combination    | language                                                                            |
| - [modified](#first_oneOf_i1_modified )                                   | Combination    | last modified                                                                       |
| - [provenance](#first_oneOf_i1_provenance )                               | Combination    | provenance                                                                          |
| + [publisher](#first_oneOf_i1_publisher )                                 | Combination    | publisher                                                                           |
| - [relation](#first_oneOf_i1_relation )                                   | Combination    | related resource                                                                    |
| - [replaces](#first_oneOf_i1_replaces )                                   | Combination    | replaces                                                                            |
| - [rights](#first_oneOf_i1_rights )                                       | Combination    | rights                                                                              |
| - [rightsHolder](#first_oneOf_i1_rightsHolder )                           | Combination    | rights holder                                                                       |
| - [source](#first_oneOf_i1_source )                                       | Combination    | data source                                                                         |
| - [spatial](#first_oneOf_i1_spatial )                                     | Combination    | spatial/geographic coverage                                                         |
| - [subject](#first_oneOf_i1_subject )                                     | Combination    | subject                                                                             |
| - [temporal](#first_oneOf_i1_temporal )                                   | Combination    | temporal coverage                                                                   |
| + [title](#first_oneOf_i1_title )                                         | string         | title                                                                               |
| - [titleMap](#first_oneOf_i1_titleMap )                                   | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#first_oneOf_i1_category )                                   | Combination    | category                                                                            |
| - [hasQualityMeasurement](#first_oneOf_i1_hasQualityMeasurement )         | Combination    | quality measurement                                                                 |
| - [page](#first_oneOf_i1_page )                                           | Combination    | documentation                                                                       |
| - [qualifiedAttribution](#first_oneOf_i1_qualifiedAttribution )           | Combination    | qualified attribution                                                               |
| - [wasAttributedTo](#first_oneOf_i1_wasAttributedTo )                     | Combination    | attribution                                                                         |
| - [wasGeneratedBy](#first_oneOf_i1_wasGeneratedBy )                       | Combination    | was generated by                                                                    |
| - [wasUsedBy](#first_oneOf_i1_wasUsedBy )                                 | Combination    | used by                                                                             |
| - [image](#first_oneOf_i1_image )                                         | Combination    | image                                                                               |
| - [scopeNote](#first_oneOf_i1_scopeNote )                                 | null or string | usage note                                                                          |
| - [scopeNoteMap](#first_oneOf_i1_scopeNoteMap )                           | null or object | Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'} |

#### <a name="first_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="first_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Dataset"` |

#### <a name="first_oneOf_i1_otherIdentifier"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier`

**Title:** other identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of structure identifiers

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#first_oneOf_i1_otherIdentifier_anyOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1) |

##### <a name="first_oneOf_i1_otherIdentifier_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_otherIdentifier_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [Identifier](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i1)     |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier`

**Title:** Identifier

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Defined in**            | /dcat-us/3.0.0/definitions/identifier |

**Description:** inline description of other identifier

| Property                                                                                | Type           | Title/Description |
| --------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_@id )                   | string         | -                 |
| - [@type](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_@type )               | string         | -                 |
| - [schemaAgency](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_schemaAgency ) | null or string | schema agency     |
| - [creator](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator )           | Combination    | creator           |
| - [issued](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued )             | Combination    | issued            |
| - [version](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_version )           | null or string | version           |
| - [notation](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_notation )         | null or string | notation          |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > @type`

|              |                |
| ------------ | -------------- |
| **Type**     | `string`       |
| **Required** | No             |
| **Default**  | `"Identifier"` |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_schemaAgency"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > schemaAgency`

**Title:** schema agency

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The name of the agency that issued the identifier

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** the agency that manages the identifier scheme

| One of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i0)       |
| [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |
| [item 2](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i2)       |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization`

**Title:** Organization

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/organization |

**Description:** inline description of the creator

| Property                                                                                                           | Type           | Title/Description                                                                      |
| ------------------------------------------------------------------------------------------------------------------ | -------------- | -------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@id )                             | string         | -                                                                                      |
| - [@type](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@type )                         | string         | -                                                                                      |
| + [name](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_name )                           | string         | name                                                                                   |
| - [subOrganizationOf](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf ) | Combination    | suborganization of                                                                     |
| - [altLabel](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabel )                   | null or string | alternative label                                                                      |
| - [altLabelMap](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabelMap )             | null or object | Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [notation](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation )                   | Combination    | notation                                                                               |
| - [prefLabel](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabel )                 | null or string | preferred label                                                                        |
| - [prefLabelMap](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabelMap )           | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}   |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Organization"` |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_name"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the Organization

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf`

**Title:** suborganization of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| Any of(Option)                                                                                                |
| ------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1) |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabel"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > altLabel`

**Title:** alternative label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** alternative name (trading name, colloquial name) for an organization

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_altLabelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

| Any of(Option)                                                                                       |
| ---------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1) |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                  | Description |
| ---------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_notation_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabel"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > prefLabel`

**Title:** preferred label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred or legal name of the organization

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1_prefLabelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > Organization > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > creator > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the creator

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Identifier

| Any of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                             |
| ------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_version"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > version`

**Title:** version

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** version of the identifier scheme

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_notation"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > Identifier > notation`

**Title:** notation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** abbreviation or code from code lists for an identifier

###### <a name="first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > otherIdentifier > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of other identifier

#### <a name="first_oneOf_i1_sample"></a>Property `DatasetSeries > first > oneOf > Dataset > sample`

**Title:** sample

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of links to samples of a Dataset

| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1) |

##### <a name="first_oneOf_i1_sample_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_sample_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                 |
| -------------------------------------------------------------- |
| [Distribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution`

**Title:** Distribution

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/distribution |

**Description:** inline description of Distribution

| Property                                                                                                 | Type           | Title/Description                                                                   |
| -------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_@id )                                             | string         | -                                                                                   |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_@type )                                         | string         | -                                                                                   |
| - [representationTechnique](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique )     | Combination    | representation technique                                                            |
| - [status](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status )                                       | Combination    | lifecycle status                                                                    |
| - [characterEncoding](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding )                 | Combination    | character encoding                                                                  |
| - [accessService](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService )                         | Combination    | access service                                                                      |
| - [accessURL](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessURL )                                 | Combination    | access URL                                                                          |
| - [byteSize](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_byteSize )                                   | null or string | byte size                                                                           |
| - [compressFormat](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat )                       | Combination    | compression format                                                                  |
| - [downloadURL](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_downloadURL )                             | Combination    | download URL                                                                        |
| - [mediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType )                                 | Combination    | media type                                                                          |
| - [packageFormat](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat )                         | Combination    | packaging format                                                                    |
| - [spatialResolutionInMeters](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters ) | null or string | Spatial resolution (meters)                                                         |
| - [temporalResolution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_temporalResolution )               | null or string | termporal resolution                                                                |
| - [availability](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability )                           | Combination    | availability                                                                        |
| - [accessRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction )                 | Combination    | access restriction                                                                  |
| - [cuiRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction )                       | Combination    | CUI restriction                                                                     |
| - [describedBy](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy )                             | Combination    | data dictionary                                                                     |
| - [useRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction )                       | Combination    | use restriction                                                                     |
| - [accessRights](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights )                           | Combination    | access rights                                                                       |
| - [conformsTo](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo )                               | Combination    | linked schemas                                                                      |
| - [description](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_description )                             | null or string | description                                                                         |
| - [descriptionMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_descriptionMap )                       | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [format](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format )                                       | Combination    | format                                                                              |
| - [identifier](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier )                               | Combination    | identifier                                                                          |
| - [issued](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued )                                       | Combination    | release date                                                                        |
| - [language](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language )                                   | Combination    | language                                                                            |
| - [license](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license )                                     | Combination    | license                                                                             |
| - [modified](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified )                                   | Combination    | last modified                                                                       |
| - [rights](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights )                                       | Combination    | rights                                                                              |
| - [title](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_title )                                         | null or string | title                                                                               |
| - [titleMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_titleMap )                                   | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [hasQualityMeasurement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement )         | Combination    | quality measurement                                                                 |
| - [page](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page )                                           | Combination    | documentation                                                                       |
| - [image](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_image )                                         | Combination    | image                                                                               |
| - [checksum](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum )                                   | Combination    | checksum                                                                            |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Distribution"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique`

**Title:** representation technique

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The format in which an Distribution is released. This is different from the file format as, for example, a ZIP file (file format) could contain an XML schema (representation technique). In DCAT-US profile,  this property SHOULD be used to express the spatial representation type (grid, vector, tin), by using the URIs of the corresponding code list operated by an approved registry

| One of(Option)                                                                             |
| ------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept`

**Title:** Concept

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | /dcat-us/3.0.0/definitions/concept |

**Description:** inline description of Concept

| Property                                                                                                          | Type           | Title/Description                                                                    |
| ----------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@id )                     | string         | -                                                                                    |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@type )                 | string         | -                                                                                    |
| - [altLabel](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabel )           | null or string | alternate label                                                                      |
| - [altLabelMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabelMap )     | null or object | Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [definition](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definition )       | null or string | definition                                                                           |
| - [definitionMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definitionMap ) | null or object | Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}      |
| + [inScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme )           | Combination    | in scheme                                                                            |
| - [notation](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation )           | Combination    | notation                                                                             |
| + [prefLabel](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabel )         | string         | preferred label                                                                      |
| - [prefLabelMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabelMap )   | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > @type`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"Concept"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabel"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > altLabel`

**Title:** alternate label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Alternative label for a concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_altLabelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternate label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definition"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the controlled vocabulary term

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_definitionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > definitionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for definition. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Concept scheme defining this concept

| One of(Option)                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------ |
| [ConceptScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i1)        |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/conceptscheme |

**Description:** inline description of ConceptScheme

| Property                                                                                                                              | Type           | Title/Description                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@id )                       | string         | -                                                                                   |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@type )                   | string         | -                                                                                   |
| - [version](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_version )               | null or string | version info                                                                        |
| - [created](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created )               | Combination    | creation date                                                                       |
| - [description](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_description )       | null or string | description                                                                         |
| - [descriptionMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued )                 | Combination    | publication date                                                                    |
| - [modified](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified )             | Combination    | update/modification date                                                            |
| + [title](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_title )                   | string         | title                                                                               |
| - [titleMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_titleMap )             | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"ConceptScheme"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_version"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > version`

**Title:** version info

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A version number or other version designation of the concept scheme

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Concept Scheme was first created

| Any of(Option)                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_description"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A description of the concept scheme

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the concept scheme

| Any of(Option)                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date at which the concept scheme was changed or modified

| Any of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_title"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the concept scheme

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > ConceptScheme > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > inScheme > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization

| Any of(Option)                                                                                              |
| ----------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                         | Description |
| ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_notation_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabel"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > prefLabel`

**Title:** preferred label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Preferred label for the term

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_prefLabelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > Concept > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > representationTechnique > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status`

**Title:** lifecycle status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The status of the distribution in the context of maturity lifecycle

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_status_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > status > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding`

**Title:** character encoding

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The list of character encodings of the Distribution, by using as value the character set names in the IANA register 

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                 | Description |
| ----------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_characterEncoding_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > characterEncoding > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService`

**Title:** access service

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A data service that gives access to the distribution of the dataset

| Any of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                             | Description |
| ------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                      |
| --------------------------------------------------------------------------------------------------- |
| [DataService](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i1)      |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService`

**Title:** DataService

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | /dcat-us/3.0.0/definitions/dataservice |

**Description:** inline description of DataService

| Property                                                                                                                                       | Type            | Title/Description                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------ |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@id )                                             | string          | -                                                                                    |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@type )                                         | string          | -                                                                                    |
| + [contactPoint](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint )                           | array           | contact point                                                                        |
| - [endpointDescription](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription )             | Combination     | endpoint description                                                                 |
| + [endpointURL](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL )                             | array of string | endpoint URL                                                                         |
| - [keyword](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keyword )                                     | null or string  | keyword/tag                                                                          |
| - [keywordMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keywordMap )                               | null or object  | Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}         |
| - [servesDataset](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset )                         | Combination     | serves dataset                                                                       |
| - [spatialResolutionInMeters](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters ) | Combination     | spatial resolution in meters                                                         |
| - [temporalResolution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution )               | Combination     | temporal resolution                                                                  |
| - [theme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme )                                         | Combination     | theme/category                                                                       |
| - [geographicBoundingBox](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox )         | Combination     | geographic bounding box                                                              |
| - [accessRights](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights )                           | Combination     | access rights                                                                        |
| - [conformsTo](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo )                               | Combination     | conforms to                                                                          |
| - [created](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created )                                     | Combination     | creation date                                                                        |
| - [creator](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator )                                     | Combination     | creator                                                                              |
| - [description](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_description )                             | null or string  | description                                                                          |
| - [descriptionMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_descriptionMap )                       | null or object  | Language map for the description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier )                               | Combination     | identifier                                                                           |
| - [language](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language )                                   | Combination     | language                                                                             |
| - [license](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license )                                     | Combination     | license                                                                              |
| - [modified](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified )                                   | Combination     | update/modification date                                                             |
| + [publisher](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher )                                 | Combination     | publisher                                                                            |
| - [rights](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights )                                       | Combination     | rights                                                                               |
| - [rightsHolder](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder )                           | Combination     | rights holder                                                                        |
| - [spatial](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial )                                     | Combination     | spatial/geographic coverage                                                          |
| - [temporal](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal )                                   | Combination     | temporal coverage                                                                    |
| + [title](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_title )                                         | string          | title                                                                                |
| - [titleMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_titleMap )                                   | null or object  | Language map for the title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category )                                   | Combination     | category                                                                             |
| - [hasQualityMeasurement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement )         | Combination     | quality measurement                                                                  |
| - [qualifiedAttribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution )           | Combination     | qualified attribution                                                                |
| - [wasUsedBy](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy )                                 | Combination     | was used by                                                                          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > @type`

|              |                 |
| ------------ | --------------- |
| **Type**     | `string`        |
| **Required** | No              |
| **Default**  | `"DataService"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint`

**Title:** contact point

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** Contact information that can be used for sending comments about the Data Service

| Each item of this array must be                                                                                               | Description |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [contactPoint items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint > contactPoint items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [Kind](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0)   |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint > contactPoint items > oneOf > Kind`

**Title:** Kind

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Kind](#contactPoint_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Kind

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_contactPoint_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > contactPoint > contactPoint items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Kind

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription`

**Title:** endpoint description

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of descriptions of the services available via the end-points, including their operations, parameters etc

| Any of(Option)                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                         | Description |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1 > item 1 items > anyOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An in-line description of the endpoint description

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointDescription_anyOf_i1_items_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointDescription > anyOf > item 1 > item 1 items > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the endpoint description

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointURL`

**Title:** endpoint URL

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

**Description:** A list of root locations or primary endpoints of the service (a Web-resolvable IRI)

| Each item of this array must be                                                                                             | Description                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [endpointURL items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL_items) | The root location or primary endpoint of the service (a Web-resolvable IRI) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_endpointURL_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > endpointURL > endpointURL items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** The root location or primary endpoint of the service (a Web-resolvable IRI)

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keyword"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > keyword`

**Title:** keyword/tag

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A keyword or tag describing the Data Service

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_keywordMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > keywordMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset`

**Title:** serves dataset

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of datasets that are served by this data service

| Any of(Option)                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                   | Description |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [Dataset](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_servesDataset_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > servesDataset > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters`

**Title:** spatial resolution in meters

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The minimum spatial separation resolvable in a Data Service, measured in meters

| Any of(Option)                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                               | Description |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatialResolutionInMeters > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution`

**Title:** temporal resolution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The minimum time period resolvable by the Data Service

| Any of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                        | Description |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporalResolution_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporalResolution > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme`

**Title:** theme/category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of themes of the Data Service. A Data Service may be associated with multiple themes

| Any of(Option)                                                                                                |
| ------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_theme_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > theme > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox`

**Title:** geographic bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The spatial extent of domain of application of an data service and is standardized in WGS 84 Lat/Long coordinate system

| Any of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                           | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GeographicBoundingBox](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i1)                |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox`

**Title:** GeographicBoundingBox

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Defined in**            | /dcat-us/3.0.0/definitions/geographicboundingbox |

**Description:** inline description of GeographicBoundingBox

| Property                                                                                                                                                                             | Type   | Title/Description       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ----------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@id )                                     | string | -                       |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@type )                                 | string | -                       |
| + [eastBoundingLongitude](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_eastBoundingLongitude ) | string | east bounding longitude |
| + [northBoundingLatitude](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_northBoundingLatitude ) | string | north bounding latitude |
| + [southBoundingLatitude](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_southBoundingLatitude ) | string | south bouding latitude  |
| + [westBoundingLongitude](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_westBoundingLongitude ) | string | west bounding longitude |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > @type`

|              |                           |
| ------------ | ------------------------- |
| **Type**     | `string`                  |
| **Required** | No                        |
| **Default**  | `"GeographicBoundingBox"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_eastBoundingLongitude"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > eastBoundingLongitude`

**Title:** east bounding longitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** East bound longitude in decimal degrees

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_northBoundingLatitude"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > northBoundingLatitude`

**Title:** north bounding latitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** North bound latitude in decimal degrees

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_southBoundingLatitude"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > southBoundingLatitude`

**Title:** south bouding latitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** South bound latitude in decimal degrees

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0_westBoundingLongitude"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox > westBoundingLongitude`

**Title:** west bounding longitude

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** West bound longitude in decimal degrees

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of GeographicBoundingBox

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information regarding access or restrictions based on privacy, security, or other policies

| One of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0)          |
| [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2)          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Defined in**            | /dcat-us/3.0.0/definitions/rightsstatement |

**Description:** inline description of access rights

| Property                                                                                                                                               | Type           | Title/Description                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@id )                               | string         | -                                                                                     |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@type )                           | string         | -                                                                                     |
| - [attributionText](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionText )       | null or string | attribution text                                                                      |
| - [attributionTextMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionTextMap ) | null or object | Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > @type`

|              |                     |
| ------------ | ------------------- |
| **Type**     | `string`            |
| **Required** | No                  |
| **Default**  | `"RightsStatement"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionText"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > attributionText`

**Title:** attribution text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The custom attribution text for the rights statement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1_attributionTextMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > RightsStatement > attributionTextMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for attribution text. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of access rights

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo`

**Title:** conforms to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of general standards or specifications that the Data Service endpoints implement

| Any of(Option)                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                | Description |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| [Standard](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/standard |

**Description:** inline description of Standard

| Property                                                                                                                                                    | Type           | Title/Description                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@id )                       | string         | -                                                                                |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@type )                   | string         | -                                                                                |
| - [created](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created )               | Combination    | creation date                                                                    |
| - [description](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_description )       | null or string | description                                                                      |
| - [descriptionMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_descriptionMap ) | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [identifier](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier )         | Combination    | identifier                                                                       |
| - [issued](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued )                 | Combination    | issued                                                                           |
| - [modified](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified )             | Combination    | last modified                                                                    |
| - [title](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_title )                   | null or string | title                                                                            |
| - [titleMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_titleMap )             | null or object | Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [category](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category )             | Combination    | category                                                                         |
| - [inScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme )             | Combination    | in scheme                                                                        |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Standard"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Standard has been first created

| Any of(Option)                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_description"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The main identifier for the Standard, e.g. the URI or other unique identifier in the context of the Catalogue, or of a reference register

| Any of(Option)                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                                                   | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Standard

| Any of(Option)                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Standard was changed or modified

| Any of(Option)                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_title"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the Standard. A controlled vocabulary for the values has not been established

| One of(Option)                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme`

**Title:** in scheme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The reference register to which the Standard belongs

| One of(Option)                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0)        |
| [ConceptScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2)        |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                           |
| **Required**              | No                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                   |
| **Same definition as**    | [ConceptScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of ConceptScheme

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ConceptScheme

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Data Service has been first created

| Any of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_created_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents primarily responsible for producing the Data Service

| Any of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                             | Description |
| --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------ |
| [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0)  |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | /dcat-us/3.0.0/definitions/agent |

**Description:** inline description of Agent

| Property                                                                                                                                     | Type        | Title/Description |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@id )           | string      | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@type )       | string      | -                 |
| - [category](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category ) | Combination | category          |
| + [name](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_name )         | string      | name              |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > @type`

|              |           |
| ------------ | --------- |
| **Type**     | `string`  |
| **Required** | No        |
| **Default**  | `"Agent"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the agent that makes the item available

| One of(Option)                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the agent type

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the agent type

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0_name"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > Agent > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the agent

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > creator > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_description"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Data Service

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of the main identifiers for the Data Service, e.g. the URI or other unique identifier in the context of the Catalog

| Any of(Option)                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                | Description |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Language or languages supported by the Data Service. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                              | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 2 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license`

**Title:** license

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The license under which the Data Service is made available

| One of(Option)                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i0)          |
| [LicenseDocument](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i2)          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Defined in**            | /dcat-us/3.0.0/definitions/licensedocument |

**Description:** inline description of LicenseDocument

| Property                                                                                                                            | Type           | Title/Description |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@id )                 | string         | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@type )             | string         | -                 |
| - [licenseText](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_licenseText ) | null or string | license text      |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument > @type`

|              |                     |
| ------------ | ------------------- |
| **Type**     | `string`            |
| **Required** | No                  |
| **Default**  | `"LicenseDocument"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1_licenseText"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > LicenseDocument > licenseText`

**Title:** license text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Full text of the license

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > license > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of LicenseDocument

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Data Service was changed or modified

| Any of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** An entity (organization) responsible for making the Data Service available

| One of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0)  |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > publisher > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > publisher > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of statements concerning all rights for the Data Service not addressed with license or accessRights, such as copyright statements

| Any of(Option)                                                                                                 |
| -------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                            | Description |
| -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- |
| [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i1)          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1 > item 1 items > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rights_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rights > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder`

**Title:** rights holder

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of Agents (organizations) holding rights on the Data Service

| Any of(Option)                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                  | Description |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Organization](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > rightsHolder > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region that is covered by the Data Service

| Any of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                             | Description |
| --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- |
| [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/location |

**Description:** inline description of Location

| Property                                                                                                                                             | Type           | Title/Description                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@id )                   | string         | -                                                                                         |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@type )               | string         | -                                                                                         |
| - [bbox](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox )                 | Combination    | bounding box                                                                              |
| - [centroid](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid )         | Combination    | centroid                                                                                  |
| - [identifier](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier )     | Combination    | identifier                                                                                |
| - [geometry](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry )         | Combination    | geometry                                                                                  |
| - [inScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme )         | Combination    | gazetteer                                                                                 |
| - [altLabel](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabel )         | null or string | alternative name                                                                          |
| - [altLabelMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabelMap )   | null or object | Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [prefLabel](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabel )       | null or string | geographic name                                                                           |
| - [prefLabelMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabelMap ) | null or object | Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}      |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Location"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > bbox`

**Title:** bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** bounding box of a location (in any coordinate system)

| Any of(Option)                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > bbox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_bbox_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > bbox > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** Bounding box represented in some string format

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > centroid`

**Title:** centroid

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The geographic center (centroid) of a location

| Any of(Option)                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > centroid > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_centroid_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > centroid > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** Center point in some string format

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of geographic identifiers for the location, e.g., the URI or other unique identifier in the context of the relevant gazetteer

| Any of(Option)                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                                                | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > geometry`

**Title:** geometry

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Associates a location with a corresponding geometry

| Any of(Option)                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > geometry > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_geometry_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > geometry > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** String format of the full geometry of the location

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme`

**Title:** gazetteer

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The gazetteer to which the location belongs

| One of(Option)                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0)        |
| [ConceptScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2)        |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme > oneOf > ConceptScheme`

**Title:** ConceptScheme

|                           |                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                           |
| **Required**              | No                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                   |
| **Same definition as**    | [ConceptScheme](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1_inScheme_oneOf_i0) |

**Description:** inline description of the gazetteer

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_inScheme_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > inScheme > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the gazetteer

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabel"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > altLabel`

**Title:** alternative name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** An alternative name for a location

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_altLabelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the alternative name. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabel"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > prefLabel`

**Title:** geographic name

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred label of the Location

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0_prefLabelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > Location > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for geographic name. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of temporal periods that the DataService covers

| Any of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                              | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| [PeriodOfTime](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/periodoftime |

**Description:** inline description of PeriodOfTime

| Property                                                                                                                                        | Type        | Title/Description |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@id )             | string      | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@type )         | string      | -                 |
| - [endDate](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate )     | Combination | end date          |
| - [startDate](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate ) | Combination | start date        |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"PeriodOfTime"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate`

**Title:** end date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The end date of the period of time

| Any of(Option)                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_endDate_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate`

**Title:** start date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The start date of the period of time

| Any of(Option)                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0_startDate_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_title"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the data service in the indicated language

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Category of the data service

| One of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement`

**Title:** quality measurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Refers to the performed quality measurements

| Any of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                           | Description |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [QualityMeasurement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Defined in**            | /dcat-us/3.0.0/definitions/qualitymeasurement |

**Description:** inline description of QualityMeasurement

| Property                                                                                                                                                                 | Type           | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@id )                         | string         | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@type )                     | string         | -                 |
| + [isMeasurementOf](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf ) | Combination    | is measurement of |
| + [value](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_value )                     | string         | value             |
| - [unitMeasure](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_unitMeasure )         | null or string | unit of measure   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > @type`

|              |                        |
| ------------ | ---------------------- |
| **Type**     | `string`               |
| **Required** | No                     |
| **Default**  | `"QualityMeasurement"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf`

**Title:** is measurement of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The metric being observed

| One of(Option)                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Metric](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric`

**Title:** Metric

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | /dcat-us/3.0.0/definitions/metric |

**Description:** inline description of Metric

| Property                                                                                                                                                                                            | Type           | Title/Description |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@id )                           | string         | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@type )                       | string         | -                 |
| + [expectedDataType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_expectedDataType ) | string         | expected datatype |
| + [inDimension](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_inDimension )           | string         | in dimension      |
| - [definition](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_definition )             | null or string | definition        |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > @type`

|              |            |
| ------------ | ---------- |
| **Type**     | `string`   |
| **Required** | No         |
| **Default**  | `"Metric"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_expectedDataType"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > expectedDataType`

**Title:** expected datatype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...)

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_inDimension"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > inDimension`

**Title:** in dimension

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Represents the dimensions a quality metric, certificate and annotation allow a measurement of.

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i0_definition"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > Metric > definition`

**Title:** definition

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Definition of the metric.

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_isMeasurementOf_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > isMeasurementOf > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Metric

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_value"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > value`

**Title:** value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The value computed by metric

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0_unitMeasure"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement > unitMeasure`

**Title:** unit of measure

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Unit of measure associated with the value

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of QualityMeasurement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution`

**Title:** qualified attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An Agent having some form of responsibility for the DataService

| Any of(Option)                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                                          | Description |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Attribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i1)      |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution`

**Title:** Attribution

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | /dcat-us/3.0.0/definitions/attribution |

**Description:** inline description of Attribution

| Property                                                                                                                                                | Type        | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@id )         | string      | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@type )     | string      | -                 |
| + [hadRole](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_hadRole ) | string      | role              |
| + [agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent )     | Combination | agent             |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > @type`

|              |                 |
| ------------ | --------------- |
| **Type**     | `string`        |
| **Required** | No              |
| **Default**  | `"Attribution"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_hadRole"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > hadRole`

**Title:** role

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The function of an entity or agent with respect to another entity or resource

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > agent`

**Title:** agent

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The agent that plays a role in the resource

| One of(Option)                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i0)  |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > agent > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0_agent_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution > agent > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Attribution

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy`

**Title:** was used by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of activities that used the Data Service

| Any of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                               | Description |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| [Activity](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity`

**Title:** Activity

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/activity |

**Description:** inline description of Activity

| Property                                                                                                                                       | Type           | Title/Description                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------ |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@id )           | string         | -                                                                              |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@type )       | string         | -                                                                              |
| - [category](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category ) | Combination    | category                                                                       |
| - [label](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_label )       | null or string | label                                                                          |
| - [labelMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_labelMap ) | null or object | Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Activity"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The category of the Activity

| Any of(Option)                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category > anyOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the category

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_category_anyOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > category > anyOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the category

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_label"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > label`

**Title:** label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A human-readable label for the activity

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0_labelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > DataService > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Activity

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessService > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of DataService

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessURL"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessURL`

**Title:** access URL

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A URL that gives access to a Distribution of the Dataset

| Any of(Option)                                                              |
| --------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessURL > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessURL_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessURL > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_byteSize"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > byteSize`

**Title:** byte size

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The size of a Distribution in bytes

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat`

**Title:** compression format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i0)    |
| [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i2)    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType`

**Title:** MediaType

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/mediatype |

**Description:** inline description of MediaType

| Property                                                                                       | Type           | Title/Description                                                          |
| ---------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@id )           | string         | -                                                                          |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@type )       | string         | -                                                                          |
| - [label](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_label )       | null or string | label                                                                      |
| - [labelMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_labelMap ) | null or object | Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > @type`

|              |               |
| ------------ | ------------- |
| **Type**     | `string`      |
| **Required** | No            |
| **Default**  | `"MediaType"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_label"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > label`

**Title:** label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The denomination of the Media Type

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1_labelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > MediaType > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for label. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > compressFormat > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_downloadURL"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > downloadURL`

**Title:** download URL

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A URL that is a direct link to a downloadable file of the Distribution in a given format

| Any of(Option)                                                                |
| ----------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > downloadURL > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_downloadURL_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > downloadURL > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType`

**Title:** media type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The media type of the Distribution as defined in the official register of media types managed by IANA

| One of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i0)    |
| [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i2)    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                            |
| **Required**              | No                                                                                  |
| **Additional properties** | Any type allowed                                                                    |
| **Same definition as**    | [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_mediaType_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > mediaType > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat`

**Title:** packaging format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together

| One of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i0)    |
| [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i2)    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                            |
| **Required**              | No                                                                                  |
| **Additional properties** | Any type allowed                                                                    |
| **Same definition as**    | [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_packageFormat_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > packageFormat > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_spatialResolutionInMeters"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The minimum spatial separation resolvable in a dataset distribution, measured in meters

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_temporalResolution"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > temporalResolution`

**Title:** termporal resolution

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The minimum time period resolvable in the dataset distribution

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability`

**Title:** availability

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An indication how long it is planned to keep the Distribution of the Dataset available

| One of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_availability_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > availability > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction`

**Title:** access restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of access restrictions related to the distribution

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                 | Description |
| ----------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                |
| ------------------------------------------------------------------------------------------------------------- |
| [AccessRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i1)            |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction`

**Title:** AccessRestriction

|                           |                                              |
| ------------------------- | -------------------------------------------- |
| **Type**                  | `object`                                     |
| **Required**              | No                                           |
| **Additional properties** | Any type allowed                             |
| **Defined in**            | /dcat-us/3.0.0/definitions/accessrestriction |

**Description:** inline description of AccessRestriction

| Property                                                                                                                               | Type           | Title/Description                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@id )                                 | string         | -                                                                                         |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@type )                             | string         | -                                                                                         |
| - [restrictionNote](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNote )         | null or string | restriction note                                                                          |
| - [restrictionNoteMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap )   | null or object | Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [restrictionStatus](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus )     | Combination    | restriction status                                                                        |
| - [specificRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction ) | Combination    | specific restriction                                                                      |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > @type`

|              |                       |
| ------------ | --------------------- |
| **Type**     | `string`              |
| **Required** | No                    |
| **Default**  | `"AccessRestriction"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNote"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionNote`

**Title:** restriction note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A note related to the access restriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionStatus`

**Title:** restriction status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The indication of whether or not there are access restrictions on the item

| One of(Option)                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------ |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of restriction status

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > restrictionStatus > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of restriction status

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction`

**Title:** specific restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The specific NARA restriction associated with this restriction

| One of(Option)                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the specific restriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > AccessRestriction > specificRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the specific restriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRestriction_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRestriction > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of AccessRestriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction`

**Title:** CUI restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Controlled Unclassified Information restriction related to the distribution

| One of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i0)         |
| [CUIRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i2)         |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction`

**Title:** CUIRestriction

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Defined in**            | /dcat-us/3.0.0/definitions/cuirestriction |

**Description:** inline description of CUIRestriction

| Property                                                                                                                                 | Type        | Title/Description                |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@id )                                                     | string      | -                                |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@type )                                                 | string      | -                                |
| + [cuiBannerMarking](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_cuiBannerMarking )                           | string      | CUI banner marking               |
| + [designationIndicator](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_designationIndicator )                   | string      | CUI designation indicator        |
| - [requiredIndicatorPerAuthority](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority ) | Combination | required indicator per authority |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > @type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `string`           |
| **Required** | No                 |
| **Default**  | `"CUIRestriction"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_cuiBannerMarking"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > cuiBannerMarking`

**Title:** CUI banner marking

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** CUI (Controlled Unclassified Information) banner marking is required for any unclassified information that is deemed sensitive and requires protection

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_designationIndicator"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > designationIndicator`

**Title:** CUI designation indicator

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Designation Indicator shows which agency made the document CUI

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority`

**Title:** required indicator per authority

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of free text of the required indicator

| Any of(Option)                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                                     | Description |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i1_requiredIndicatorPerAuthority_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_cuiRestriction_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > cuiRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of CUIRestriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy`

**Title:** data dictionary

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A distribution containing the Data Dictionary for this distribution

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i0)       |
| [Distribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i2)       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                |
| ------------------------- | -------------------------------------------------------------- |
| **Type**                  | `object`                                                       |
| **Required**              | No                                                             |
| **Additional properties** | Any type allowed                                               |
| **Same definition as**    | [Distribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the data dictionary

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_describedBy_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > describedBy > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the data dictionary

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction`

**Title:** use restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Use restriction related to the distribution

| Any of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                              | Description |
| -------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                          |
| ------------------------------------------------------------------------------------------------------- |
| [UseRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i1)         |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction`

**Title:** UseRestriction

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Defined in**            | /dcat-us/3.0.0/definitions/userestriction |

**Description:** inline description of UseRestriction

| Property                                                                                                                            | Type           | Title/Description                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@id )                                 | string         | -                                                                                         |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@type )                             | string         | -                                                                                         |
| - [restrictionNote](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNote )         | null or string | restriction note                                                                          |
| - [restrictionNoteMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap )   | null or object | Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| + [restrictionStatus](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus )     | Combination    | restriction status                                                                        |
| - [specificRestriction](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction ) | Combination    | specific restriction                                                                      |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > @type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `string`           |
| **Required** | No                 |
| **Default**  | `"UseRestriction"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNote"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionNote`

**Title:** restriction note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Significant information pertaining to the use or reproduction of the data

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionNoteMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the restriction note. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionStatus`

**Title:** restriction status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Indication of whether or not there are use restrictions on the archival materials

| One of(Option)                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------- |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionStatus > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of restriction status

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_restrictionStatus_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > restrictionStatus > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of restriction status

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction`

**Title:** specific restriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The specific NARA restriction associated with the use restriction

| One of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of the specific restriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i0_specificRestriction_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > UseRestriction > specificRestriction > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the specific restriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_useRestriction_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > useRestriction > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of UseRestriction

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information regarding access or restrictions based on privacy, security, or other policies

| One of(Option)                                                                          |
| --------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0)          |
| [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2)          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo`

**Title:** linked schemas

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of established schemas or reference systems to which the described Distribution conforms

| Any of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                          | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                |
| --------------------------------------------------------------------------------------------- |
| [Standard](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                            |
| **Required**              | No                                                                                                                                  |
| **Additional properties** | Any type allowed                                                                                                                    |
| **Same definition as**    | [Standard](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_description"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Distribution

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format`

**Title:** format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The file format of the Distribution

| One of(Option)                                                              |
| --------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i0)    |
| [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i2)    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                            |
| **Required**              | No                                                                                  |
| **Additional properties** | Any type allowed                                                                    |
| **Same definition as**    | [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of the format

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_format_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > format > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the format

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of unique identifiers for the Distribution (e.g. DOI, ISBN)

| Any of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                          | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Distribution

| Any of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A language or languages used in the Distribution. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                        | Description |
| -------------------------------------------------------------------------------------- | ----------- |
| [item 2 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_language_anyOf_i2_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license`

**Title:** license

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A license under which the Distribution is made available

| One of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i0)          |
| [LicenseDocument](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i2)          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license > oneOf > LicenseDocument`

**Title:** LicenseDocument

|                           |                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                 |
| **Required**              | No                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                         |
| **Same definition as**    | [LicenseDocument](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_license_oneOf_i1) |

**Description:** inline description of LicenseDocument

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_license_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > license > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of LicenseDocument

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Distribution was changed or modified

| Any of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A statement that specifies rights associated with the Distribution

| One of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i0)          |
| [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i2)          |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_rights_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > rights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_title"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > title`

**Title:** title

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A name given to the Distribution

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement`

**Title:** quality measurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of quality measurements for the distribution

| Any of(Option)                                                                          |
| --------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                     | Description |
| --------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------ |
| [QualityMeasurement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

|                           |                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                 |
| **Required**              | No                                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                                         |
| **Same definition as**    | [QualityMeasurement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of QualityMeasurement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of QualityMeasurement

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page`

**Title:** documentation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A page or document about this Distribution

| Any of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                    | Description |
| ---------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                          |
| --------------------------------------------------------------------------------------- |
| [Document](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document`

**Title:** Document

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/document |

**Description:** inline description of Document

| Property                                                                                                                      | Type           | Title/Description                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@id )                                     | string         | -                                                                                   |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@type )                                 | string         | -                                                                                   |
| - [creators](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators )                           | Combination    | authors                                                                             |
| - [publishers](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publishers )                       | null or string | publisher                                                                           |
| - [mediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType )                         | Combination    | media type                                                                          |
| - [abstract](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstract )                           | null or string | abstract                                                                            |
| - [abstractMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstractMap )                     | null or object | Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}       |
| - [bibliographicCitation](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_bibliographicCitation ) | null or string | bibliographic citation                                                              |
| - [conformsTo](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo )                       | Combination    | conforms to standard                                                                |
| - [creator](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator )                             | Combination    | corporate author                                                                    |
| - [description](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_description )                     | null or string | description                                                                         |
| - [descriptionMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_descriptionMap )               | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [identifier](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier )                       | Combination    | identifier                                                                          |
| - [issued](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued )                               | Combination    | publication date                                                                    |
| - [publisher](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher )                         | Combination    | publisher                                                                           |
| + [title](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_title )                                 | string         | title                                                                               |
| - [titleMap](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_titleMap )                           | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [category](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category )                           | Combination    | category                                                                            |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Document"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators`

**Title:** authors

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of authors

| Any of(Option)                                                                                          |
| ------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                     | Description |
| ------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creators_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creators > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publishers"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publishers`

**Title:** publisher

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Publisher

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType`

**Title:** media type

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of file formats of the Document

| Any of(Option)                                                                                           |
| -------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                      | Description |
| -------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i1)    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1 > item 1 items > oneOf > MediaType`

**Title:** MediaType

|                           |                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                            |
| **Required**              | No                                                                                  |
| **Additional properties** | Any type allowed                                                                    |
| **Same definition as**    | [MediaType](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_compressFormat_oneOf_i1) |

**Description:** inline description of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_mediaType_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > mediaType > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of MediaType

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstract"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > abstract`

**Title:** abstract

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Text abstract of the document

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_abstractMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > abstractMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for abstract. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_bibliographicCitation"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > bibliographicCitation`

**Title:** bibliographic citation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Bibliographic citation as text

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo`

**Title:** conforms to standard

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A standard to which the document conforms

| Any of(Option)                                                                                            |
| --------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                       | Description |
| --------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [Standard](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                            |
| **Required**              | No                                                                                                                                  |
| **Additional properties** | Any type allowed                                                                                                                    |
| **Same definition as**    | [Standard](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator`

**Title:** corporate author

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The organization responsible for creating the resource

| Any of(Option)                                                                                         |
| ------------------------------------------------------------------------------------------------------ |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------------------ | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------- |
| [Organization](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of corporate author

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > creator > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of corporate author

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_description"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > description`

**Title:** description

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** A free-text account of the Document

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier`

**Title:** identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of unique identifiers for the Document (e.g. DOI, ISBN)

| Any of(Option)                                                                                            |
| --------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                                                                                       | Description |
| --------------------------------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_identifier_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > identifier > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued`

**Title:** publication date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Publication date of the document

| Any of(Option)                                                                                        |
| ----------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                                                 |
| -------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** publisher organization of the document

| One of(Option)                                                                                                 |
| -------------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0)       |
| [Organization](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2)       |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher > oneOf > Organization`

**Title:** Organization

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of publisher organization

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of publisher organization

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_title"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The title of the document in the indicated language

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Category of the document

| One of(Option)                                                                                           |
| -------------------------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i0)  |
| [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i2)  |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0_category_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > Document > category > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > page > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Document

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_image"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > image`

**Title:** image

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A link to a thumbnail picture illustrating the content of the distribution

| Any of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i0) |
| [item 1](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i1) |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > image > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_image_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > image > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** The link to the image

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum`

**Title:** checksum

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A mechanism that can be used to verify that the contents of a distribution have not changed

| One of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i0)   |
| [Checksum](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1) |
| [item 2](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i2)   |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum`

**Title:** Checksum

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | /dcat-us/3.0.0/definitions/checksum |

**Description:** inline description of Checksum

| Property                                                                                           | Type   | Title/Description |
| -------------------------------------------------------------------------------------------------- | ------ | ----------------- |
| - [@id](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@id )                     | string | -                 |
| - [@type](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@type )                 | string | -                 |
| + [algorithm](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_algorithm )         | string | algorithm         |
| + [checksumValue](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_checksumValue ) | string | checksum value    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > @type`

|              |              |
| ------------ | ------------ |
| **Type**     | `string`     |
| **Required** | No           |
| **Default**  | `"Checksum"` |

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_algorithm"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > algorithm`

**Title:** algorithm

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The algorithm used to produce the checksum

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i1_checksumValue"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > Checksum > checksumValue`

**Title:** checksum value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A lower case hexadecimal encoded digest value produced using a specific algorithm

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_checksum_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > Distribution > checksum > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Checksum

###### <a name="first_oneOf_i1_sample_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > sample > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

#### <a name="first_oneOf_i1_status"></a>Property `DatasetSeries > first > oneOf > Dataset > status`

**Title:** lifecycle status

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The status of the dataset  in the context of maturity lifecycle

| One of(Option)                             |
| ------------------------------------------ |
| [item 0](#first_oneOf_i1_status_oneOf_i0)  |
| [Concept](#first_oneOf_i1_status_oneOf_i1) |
| [item 2](#first_oneOf_i1_status_oneOf_i2)  |

##### <a name="first_oneOf_i1_status_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > status > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_status_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > status > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

##### <a name="first_oneOf_i1_status_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > status > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

#### <a name="first_oneOf_i1_supportedSchema"></a>Property `DatasetSeries > first > oneOf > Dataset > supportedSchema`

**Title:** supported schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** supported schema for this dataset

| One of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#first_oneOf_i1_supportedSchema_oneOf_i0)  |
| [Dataset](#first_oneOf_i1_supportedSchema_oneOf_i1) |
| [item 2](#first_oneOf_i1_supportedSchema_oneOf_i2)  |

##### <a name="first_oneOf_i1_supportedSchema_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > supportedSchema > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_supportedSchema_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > supportedSchema > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of the supported schema

##### <a name="first_oneOf_i1_supportedSchema_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > supportedSchema > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the supported schema

#### <a name="first_oneOf_i1_versionNotes"></a>Property `DatasetSeries > first > oneOf > Dataset > versionNotes`

**Title:** version notes

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** version notes for this dataset

#### <a name="first_oneOf_i1_contactPoint"></a>Property `DatasetSeries > first > oneOf > Dataset > contactPoint`

**Title:** contact point

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of contact information that can be used for sending comments about the Dataset

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#first_oneOf_i1_contactPoint_anyOf_i0) |
| [item 1](#first_oneOf_i1_contactPoint_anyOf_i1) |

##### <a name="first_oneOf_i1_contactPoint_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > contactPoint > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_contactPoint_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > contactPoint > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_contactPoint_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_contactPoint_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                 |
| -------------------------------------------------------------- |
| [Kind](#first_oneOf_i1_contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#first_oneOf_i1_contactPoint_anyOf_i1_items_oneOf_i1) |

###### <a name="first_oneOf_i1_contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Kind](#contactPoint_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Kind

###### <a name="first_oneOf_i1_contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Kind

#### <a name="first_oneOf_i1_distribution"></a>Property `DatasetSeries > first > oneOf > Dataset > distribution`

**Title:** dataset distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of available distributions for the Dataset

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#first_oneOf_i1_distribution_anyOf_i0) |
| [item 1](#first_oneOf_i1_distribution_anyOf_i1) |

##### <a name="first_oneOf_i1_distribution_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > distribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_distribution_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > distribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_distribution_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_distribution_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > distribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                       |
| -------------------------------------------------------------------- |
| [Distribution](#first_oneOf_i1_distribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_distribution_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_distribution_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > distribution > anyOf > item 1 > item 1 items > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                |
| ------------------------- | -------------------------------------------------------------- |
| **Type**                  | `object`                                                       |
| **Required**              | No                                                             |
| **Additional properties** | Any type allowed                                               |
| **Same definition as**    | [Distribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Distribution

###### <a name="first_oneOf_i1_distribution_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > distribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

#### <a name="first_oneOf_i1_first"></a>Property `DatasetSeries > first > oneOf > Dataset > first`

**Title:** first

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** the first item of the sequence the dataset belongs to

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#first_oneOf_i1_first_oneOf_i0)  |
| [Dataset](#first_oneOf_i1_first_oneOf_i1) |
| [item 2](#first_oneOf_i1_first_oneOf_i2)  |

##### <a name="first_oneOf_i1_first_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > first > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_first_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > first > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

##### <a name="first_oneOf_i1_first_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > first > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_hasCurrentVersion"></a>Property `DatasetSeries > first > oneOf > Dataset > hasCurrentVersion`

**Title:** current version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** reference to the current (latest) version of a dataset

| One of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#first_oneOf_i1_hasCurrentVersion_oneOf_i0)  |
| [Dataset](#first_oneOf_i1_hasCurrentVersion_oneOf_i1) |
| [item 2](#first_oneOf_i1_hasCurrentVersion_oneOf_i2)  |

##### <a name="first_oneOf_i1_hasCurrentVersion_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasCurrentVersion > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_hasCurrentVersion_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasCurrentVersion > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

##### <a name="first_oneOf_i1_hasCurrentVersion_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > hasCurrentVersion > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_hasVersion"></a>Property `DatasetSeries > first > oneOf > Dataset > hasVersion`

**Title:** has version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related Datasets that are a version, edition, or adaptation of the described Dataset

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#first_oneOf_i1_hasVersion_anyOf_i0) |
| [item 1](#first_oneOf_i1_hasVersion_anyOf_i1) |

##### <a name="first_oneOf_i1_hasVersion_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasVersion > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_hasVersion_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasVersion > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_hasVersion_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_hasVersion_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > hasVersion > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [Dataset](#first_oneOf_i1_hasVersion_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_hasVersion_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_hasVersion_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasVersion > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

###### <a name="first_oneOf_i1_hasVersion_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasVersion > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_inSeries"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries`

**Title:** in series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of Dataset Series this dataset belongs to

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1) |

##### <a name="first_oneOf_i1_inSeries_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_inSeries_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_inSeries_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                    |
| ----------------------------------------------------------------- |
| [DatasetSeries](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i1)        |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries`

**Title:** DatasetSeries

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | /dcat-us/3.0.0/definitions/datasetseries |

**Description:** inline description of DatasetSeries

| Property                                                                                     | Type           | Title/Description                                                                   |
| -------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_@id )                               | string         | -                                                                                   |
| - [@type](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_@type )                           | string         | -                                                                                   |
| - [contactPoint](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint )             | Combination    | contact point                                                                       |
| - [first](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first )                           | Combination    | first                                                                               |
| - [last](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last )                             | Combination    | last                                                                                |
| - [seriesMember](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember )             | Combination    | series member                                                                       |
| - [accrualPeriodicity](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity ) | Combination    | frequency                                                                           |
| + [description](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_description )               | string         | description                                                                         |
| - [descriptionMap](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_descriptionMap )         | null or object | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued )                         | Combination    | release date                                                                        |
| - [modified](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified )                     | Combination    | update/modification date                                                            |
| - [publisher](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher )                   | Combination    | publisher                                                                           |
| - [spatial](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial )                       | Combination    | spatial/geographic coverage                                                         |
| - [temporal](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal )                     | Combination    | temporal coverage                                                                   |
| + [title](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_title )                           | string         | title                                                                               |
| - [titleMap](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_titleMap )                     | null or object | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > @type`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | No                |
| **Default**  | `"DatasetSeries"` |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint`

**Title:** contact point

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of contacts that can be used for sending comments about the Dataset Series

| Any of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                              | Description |
| -------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                  |
| ----------------------------------------------------------------------------------------------- |
| [Kind](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [Kind](#contactPoint_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of the contact

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the contact

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first`

**Title:** first

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The first dataset in an ordered dataset series

| One of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i0)  |
| [Dataset](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i1) |
| [item 2](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i2)  |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of the first dataset

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_first_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > first > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the first dataset

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last`

**Title:** last

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The last dataset in an ordered dataset series

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i0)  |
| [Dataset](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i1) |
| [item 2](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i2)  |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of the last dataset

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_last_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > last > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the last dataset

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember`

**Title:** series member

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of members of the Dataset Series

| Any of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                              | Description |
| -------------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                   |
| ------------------------------------------------------------------------------------------------ |
| [Dataset](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of the member dataset

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_seriesMember_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the member dataset

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity`

**Title:** frequency

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The frequency at which the Dataset Series is updated

| One of(Option)                                                                            |
| ----------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i0)    |
| [frequency](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i1) |
| [item 2](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i2)    |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity > oneOf > frequency`

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/frequency |

**Description:** inline description of Frequency

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_accrualPeriodicity_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > accrualPeriodicity > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Frequency

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_description"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > description`

**Title:** description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A free-text account of the Dataset Series

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g.,publication) of the Dataset Series

| Any of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Dataset Series was changed or modified

| Any of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                                                        |
| ------------------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity (organization) responsible for ensuring the coherency of the Dataset Series

| One of(Option)                                                                |
| ----------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0) |
| [Agent](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1)  |
| [item 2](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of publisher

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_publisher_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of publisher

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region that is covered by the Dataset Series

| Any of(Option)                                                              |
| --------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                         | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                               |
| -------------------------------------------------------------------------------------------- |
| [Location](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Required**              | No                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of temporal periods that the Dataset Series covers

| Any of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1) |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                                          | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                                    |
| ------------------------------------------------------------------------------------------------- |
| [PeriodOfTime](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [PeriodOfTime](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of PeriodOfTime

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_title"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A name given to the Dataset Series

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i0_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > DatasetSeries > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_inSeries_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > inSeries > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of DatasetSeries

#### <a name="first_oneOf_i1_keyword"></a>Property `DatasetSeries > first > oneOf > Dataset > keyword`

**Title:** keyword/tag

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of keywords or tags describing the Dataset

| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#first_oneOf_i1_keyword_anyOf_i0) |
| [item 1](#first_oneOf_i1_keyword_anyOf_i1) |

##### <a name="first_oneOf_i1_keyword_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > keyword > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_keyword_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > keyword > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [item 1 items](#first_oneOf_i1_keyword_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_keyword_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > keyword > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="first_oneOf_i1_keywordMap"></a>Property `DatasetSeries > first > oneOf > Dataset > keywordMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for keyword. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="first_oneOf_i1_landingPage"></a>Property `DatasetSeries > first > oneOf > Dataset > landingPage`

**Title:** landing page

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A web page that provides access to the Dataset, its Distributions and/or additional information

| One of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#first_oneOf_i1_landingPage_oneOf_i0)   |
| [Document](#first_oneOf_i1_landingPage_oneOf_i1) |
| [item 2](#first_oneOf_i1_landingPage_oneOf_i2)   |

##### <a name="first_oneOf_i1_landingPage_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > landingPage > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_landingPage_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > landingPage > oneOf > Document`

**Title:** Document

|                           |                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                |
| **Required**              | No                                                                                      |
| **Additional properties** | Any type allowed                                                                        |
| **Same definition as**    | [Document](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Document

##### <a name="first_oneOf_i1_landingPage_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > landingPage > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Document

#### <a name="first_oneOf_i1_previousVersion"></a>Property `DatasetSeries > first > oneOf > Dataset > previousVersion`

**Title:** previous version

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** reference to the previous dataset version

| One of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#first_oneOf_i1_previousVersion_oneOf_i0)  |
| [Dataset](#first_oneOf_i1_previousVersion_oneOf_i1) |
| [item 2](#first_oneOf_i1_previousVersion_oneOf_i2)  |

##### <a name="first_oneOf_i1_previousVersion_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > previousVersion > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_previousVersion_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > previousVersion > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

##### <a name="first_oneOf_i1_previousVersion_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > previousVersion > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_qualifiedRelation"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation`

**Title:** qualified relation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Qualified relationship with role of the dataset with another resource

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#first_oneOf_i1_qualifiedRelation_anyOf_i0) |
| [item 1](#first_oneOf_i1_qualifiedRelation_anyOf_i1) |

##### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                  | Description |
| ---------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [Relationship](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship`

**Title:** Relationship

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/relationship |

**Description:** inline description of Relationship

| Property                                                                          | Type   | Title/Description |
| --------------------------------------------------------------------------------- | ------ | ----------------- |
| - [@id](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_@id )           | string | -                 |
| - [@type](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_@type )       | string | -                 |
| + [hadRole](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_hadRole )   | string | role              |
| + [relation](#first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_relation ) | string | relation          |

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Relationship"` |

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_hadRole"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > hadRole`

**Title:** role

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The function of an entity or agent with respect to a dataset

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i0_relation"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > Relationship > relation`

**Title:** relation

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `iri`    |

**Description:** Link to the entity related to the dataset

###### <a name="first_oneOf_i1_qualifiedRelation_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedRelation > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Relationship

#### <a name="first_oneOf_i1_spatialResolutionInMeters"></a>Property `DatasetSeries > first > oneOf > Dataset > spatialResolutionInMeters`

**Title:** Spatial resolution (meters)

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Spatial resolution in meters

#### <a name="first_oneOf_i1_temporalResolution"></a>Property `DatasetSeries > first > oneOf > Dataset > temporalResolution`

**Title:** temporal resolution

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Temporal resolution using xsd:duration syntax

#### <a name="first_oneOf_i1_theme"></a>Property `DatasetSeries > first > oneOf > Dataset > theme`

**Title:** theme/category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of themes of the dataset

| Any of(Option)                           |
| ---------------------------------------- |
| [item 0](#first_oneOf_i1_theme_anyOf_i0) |
| [item 1](#first_oneOf_i1_theme_anyOf_i1) |

##### <a name="first_oneOf_i1_theme_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > theme > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_theme_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > theme > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_theme_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_theme_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > theme > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Concept](#first_oneOf_i1_theme_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_theme_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_theme_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > theme > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_theme_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > theme > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

#### <a name="first_oneOf_i1_version"></a>Property `DatasetSeries > first > oneOf > Dataset > version`

**Title:** version

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The version indicator (name or identifier) of a resource

#### <a name="first_oneOf_i1_describedBy"></a>Property `DatasetSeries > first > oneOf > Dataset > describedBy`

**Title:** data dictionary

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A distribution describing the Data Dictionary for this dataset

| One of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#first_oneOf_i1_describedBy_oneOf_i0)       |
| [Distribution](#first_oneOf_i1_describedBy_oneOf_i1) |
| [item 2](#first_oneOf_i1_describedBy_oneOf_i2)       |

##### <a name="first_oneOf_i1_describedBy_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > describedBy > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_describedBy_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > describedBy > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                |
| ------------------------- | -------------------------------------------------------------- |
| **Type**                  | `object`                                                       |
| **Required**              | No                                                             |
| **Additional properties** | Any type allowed                                               |
| **Same definition as**    | [Distribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Distribution

##### <a name="first_oneOf_i1_describedBy_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > describedBy > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

#### <a name="first_oneOf_i1_geographicBoundingBox"></a>Property `DatasetSeries > first > oneOf > Dataset > geographicBoundingBox`

**Title:** geographic bounding box

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of WGS84 Geographic Bounding Boxes for this dataset

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#first_oneOf_i1_geographicBoundingBox_anyOf_i0) |
| [item 1](#first_oneOf_i1_geographicBoundingBox_anyOf_i1) |

##### <a name="first_oneOf_i1_geographicBoundingBox_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > geographicBoundingBox > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_geographicBoundingBox_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > geographicBoundingBox > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                      | Description |
| -------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_geographicBoundingBox_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_geographicBoundingBox_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > geographicBoundingBox > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                         |
| -------------------------------------------------------------------------------------- |
| [GeographicBoundingBox](#first_oneOf_i1_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_geographicBoundingBox_anyOf_i1_items_oneOf_i1)                |

###### <a name="first_oneOf_i1_geographicBoundingBox_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > GeographicBoundingBox`

**Title:** GeographicBoundingBox

|                           |                                                                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                    |
| **Required**              | No                                                                                                                                                          |
| **Additional properties** | Any type allowed                                                                                                                                            |
| **Same definition as**    | [GeographicBoundingBox](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_geographicBoundingBox_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of GeographicBoundingBox

###### <a name="first_oneOf_i1_geographicBoundingBox_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > geographicBoundingBox > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of GeographicBoundingBox

#### <a name="first_oneOf_i1_liabilityStatement"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement`

**Title:** liability statement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A liability statement about the dataset

| One of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#first_oneOf_i1_liabilityStatement_oneOf_i0)             |
| [LiabilityStatement](#first_oneOf_i1_liabilityStatement_oneOf_i1) |
| [item 2](#first_oneOf_i1_liabilityStatement_oneOf_i2)             |

##### <a name="first_oneOf_i1_liabilityStatement_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_liabilityStatement_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement`

**Title:** LiabilityStatement

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Defined in**            | /dcat-us/3.0.0/definitions/liabilitystatement |

**Description:** inline description of LiabilityStatement

| Property                                                            | Type           | Title/Description                                                                       |
| ------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_liabilityStatement_oneOf_i1_@id )           | string         | -                                                                                       |
| - [@type](#first_oneOf_i1_liabilityStatement_oneOf_i1_@type )       | string         | -                                                                                       |
| - [label](#first_oneOf_i1_liabilityStatement_oneOf_i1_label )       | null or string | liability statement text                                                                |
| - [labelMap](#first_oneOf_i1_liabilityStatement_oneOf_i1_labelMap ) | null or object | Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_liabilityStatement_oneOf_i1_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_liabilityStatement_oneOf_i1_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > @type`

|              |                        |
| ------------ | ---------------------- |
| **Type**     | `string`               |
| **Required** | No                     |
| **Default**  | `"LiabilityStatement"` |

###### <a name="first_oneOf_i1_liabilityStatement_oneOf_i1_label"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > label`

**Title:** liability statement text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Full text of the liability statement

###### <a name="first_oneOf_i1_liabilityStatement_oneOf_i1_labelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > LiabilityStatement > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the liability text. E.g. {'es': 'spanish words', 'fr': 'french words'}

##### <a name="first_oneOf_i1_liabilityStatement_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > liabilityStatement > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of LiabilityStatement

#### <a name="first_oneOf_i1_metadataDistribution"></a>Property `DatasetSeries > first > oneOf > Dataset > metadataDistribution`

**Title:** metadata distribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Distribution to "original" metadata document

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#first_oneOf_i1_metadataDistribution_anyOf_i0) |
| [item 1](#first_oneOf_i1_metadataDistribution_anyOf_i1) |

##### <a name="first_oneOf_i1_metadataDistribution_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > metadataDistribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_metadataDistribution_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > metadataDistribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_metadataDistribution_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_metadataDistribution_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > metadataDistribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [Distribution](#first_oneOf_i1_metadataDistribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_metadataDistribution_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_metadataDistribution_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > metadataDistribution > anyOf > item 1 > item 1 items > oneOf > Distribution`

**Title:** Distribution

|                           |                                                                |
| ------------------------- | -------------------------------------------------------------- |
| **Type**                  | `object`                                                       |
| **Required**              | No                                                             |
| **Additional properties** | Any type allowed                                               |
| **Same definition as**    | [Distribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Distribution

###### <a name="first_oneOf_i1_metadataDistribution_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > metadataDistribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Distribution

#### <a name="first_oneOf_i1_purpose"></a>Property `DatasetSeries > first > oneOf > Dataset > purpose`

**Title:** purpose

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The purpose of the dataset

#### <a name="first_oneOf_i1_purposeMap"></a>Property `DatasetSeries > first > oneOf > Dataset > purposeMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for purpose. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="first_oneOf_i1_accessRights"></a>Property `DatasetSeries > first > oneOf > Dataset > accessRights`

**Title:** access rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information that indicates whether the Dataset is open data, has access restrictions or is public

| One of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#first_oneOf_i1_accessRights_oneOf_i0)          |
| [RightsStatement](#first_oneOf_i1_accessRights_oneOf_i1) |
| [item 2](#first_oneOf_i1_accessRights_oneOf_i2)          |

##### <a name="first_oneOf_i1_accessRights_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > accessRights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_accessRights_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > accessRights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

##### <a name="first_oneOf_i1_accessRights_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > accessRights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

#### <a name="first_oneOf_i1_accrualPeriodicity"></a>Property `DatasetSeries > first > oneOf > Dataset > accrualPeriodicity`

**Title:** frequency

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The frequency at which the Dataset is updated

| One of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#first_oneOf_i1_accrualPeriodicity_oneOf_i0)    |
| [frequency](#first_oneOf_i1_accrualPeriodicity_oneOf_i1) |
| [item 2](#first_oneOf_i1_accrualPeriodicity_oneOf_i2)    |

##### <a name="first_oneOf_i1_accrualPeriodicity_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > accrualPeriodicity > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_accrualPeriodicity_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > accrualPeriodicity > oneOf > frequency`

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/frequency |

**Description:** inline description of Frequency

##### <a name="first_oneOf_i1_accrualPeriodicity_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > accrualPeriodicity > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Frequency

#### <a name="first_oneOf_i1_conformsTo"></a>Property `DatasetSeries > first > oneOf > Dataset > conformsTo`

**Title:** conforms to

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of standards to which the described Dataset conforms

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#first_oneOf_i1_conformsTo_anyOf_i0) |
| [item 1](#first_oneOf_i1_conformsTo_anyOf_i1) |

##### <a name="first_oneOf_i1_conformsTo_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > conformsTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_conformsTo_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > conformsTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_conformsTo_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_conformsTo_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > conformsTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                 |
| -------------------------------------------------------------- |
| [Standard](#first_oneOf_i1_conformsTo_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_conformsTo_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_conformsTo_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > conformsTo > anyOf > item 1 > item 1 items > oneOf > Standard`

**Title:** Standard

|                           |                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                            |
| **Required**              | No                                                                                                                                  |
| **Additional properties** | Any type allowed                                                                                                                    |
| **Same definition as**    | [Standard](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_conformsTo_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Standard

###### <a name="first_oneOf_i1_conformsTo_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > conformsTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Standard

#### <a name="first_oneOf_i1_contributor"></a>Property `DatasetSeries > first > oneOf > Dataset > contributor`

**Title:** contributor

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents contributing to the Dataset

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#first_oneOf_i1_contributor_anyOf_i0) |
| [item 1](#first_oneOf_i1_contributor_anyOf_i1) |

##### <a name="first_oneOf_i1_contributor_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > contributor > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_contributor_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > contributor > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                            | Description |
| ---------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_contributor_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_contributor_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > contributor > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [Agent](#first_oneOf_i1_contributor_anyOf_i1_items_oneOf_i0)  |
| [item 1](#first_oneOf_i1_contributor_anyOf_i1_items_oneOf_i1) |

###### <a name="first_oneOf_i1_contributor_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > contributor > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="first_oneOf_i1_contributor_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > contributor > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

#### <a name="first_oneOf_i1_created"></a>Property `DatasetSeries > first > oneOf > Dataset > created`

**Title:** creation date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date on which the Dataset was first created

| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#first_oneOf_i1_created_anyOf_i0) |
| [item 1](#first_oneOf_i1_created_anyOf_i1) |

##### <a name="first_oneOf_i1_created_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > created > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_created_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > created > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#first_oneOf_i1_created_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_created_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_created_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_created_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_created_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_created_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_created_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_created_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > created > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="first_oneOf_i1_creator"></a>Property `DatasetSeries > first > oneOf > Dataset > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity responsible for producing the dataset

| One of(Option)                             |
| ------------------------------------------ |
| [item 0](#first_oneOf_i1_creator_oneOf_i0) |
| [Agent](#first_oneOf_i1_creator_oneOf_i1)  |
| [item 2](#first_oneOf_i1_creator_oneOf_i2) |

##### <a name="first_oneOf_i1_creator_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > creator > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_creator_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > creator > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

##### <a name="first_oneOf_i1_creator_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > creator > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

#### <a name="first_oneOf_i1_description"></a>Property `DatasetSeries > first > oneOf > Dataset > description`

**Title:** description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A free-text account of the Dataset

#### <a name="first_oneOf_i1_descriptionMap"></a>Property `DatasetSeries > first > oneOf > Dataset > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="first_oneOf_i1_hasPart"></a>Property `DatasetSeries > first > oneOf > Dataset > hasPart`

**Title:** has part

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related datasets that are part of the described dataset

| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#first_oneOf_i1_hasPart_anyOf_i0) |
| [item 1](#first_oneOf_i1_hasPart_anyOf_i1) |

##### <a name="first_oneOf_i1_hasPart_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasPart > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_hasPart_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasPart > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [item 1 items](#first_oneOf_i1_hasPart_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_hasPart_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > hasPart > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Dataset](#first_oneOf_i1_hasPart_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_hasPart_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_hasPart_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasPart > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

###### <a name="first_oneOf_i1_hasPart_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasPart > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_identifier"></a>Property `DatasetSeries > first > oneOf > Dataset > identifier`

**Title:** identifier

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The unique identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalog

#### <a name="first_oneOf_i1_isReferencedBy"></a>Property `DatasetSeries > first > oneOf > Dataset > isReferencedBy`

**Title:** is referenced by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of links to related resources, such as publications, that reference, cite, or otherwise point to the Dataset

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#first_oneOf_i1_isReferencedBy_anyOf_i0) |
| [item 1](#first_oneOf_i1_isReferencedBy_anyOf_i1) |

##### <a name="first_oneOf_i1_isReferencedBy_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > isReferencedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_isReferencedBy_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > isReferencedBy > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                               | Description               |
| ------------------------------------------------------------- | ------------------------- |
| [item 1 items](#first_oneOf_i1_isReferencedBy_anyOf_i1_items) | reference iri of Resource |

###### <a name="first_oneOf_i1_isReferencedBy_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > isReferencedBy > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

#### <a name="first_oneOf_i1_issued"></a>Property `DatasetSeries > first > oneOf > Dataset > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Date of formal issuance (e.g., publication) of the dataset

| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#first_oneOf_i1_issued_anyOf_i0) |
| [item 1](#first_oneOf_i1_issued_anyOf_i1) |

##### <a name="first_oneOf_i1_issued_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_issued_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > issued > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#first_oneOf_i1_issued_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_issued_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_issued_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_issued_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="first_oneOf_i1_language"></a>Property `DatasetSeries > first > oneOf > Dataset > language`

**Title:** language

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Language or languages used in the Dataset. This should be provided as an ISO 639-1 language code, which can be seen at https://id.loc.gov/vocabulary/iso639-1.html

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_language_anyOf_i0) |
| [item 1](#first_oneOf_i1_language_anyOf_i1) |
| [item 2](#first_oneOf_i1_language_anyOf_i2) |

##### <a name="first_oneOf_i1_language_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > language > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_language_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > language > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

##### <a name="first_oneOf_i1_language_anyOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > language > anyOf > item 2`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [item 2 items](#first_oneOf_i1_language_anyOf_i2_items) | -           |

###### <a name="first_oneOf_i1_language_anyOf_i2_items"></a>DatasetSeries > first > oneOf > Dataset > language > anyOf > item 2 > item 2 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Max length** | 2 |

#### <a name="first_oneOf_i1_modified"></a>Property `DatasetSeries > first > oneOf > Dataset > modified`

**Title:** last modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Dataset was changed or modified

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_modified_anyOf_i0) |
| [item 1](#first_oneOf_i1_modified_anyOf_i1) |

##### <a name="first_oneOf_i1_modified_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_modified_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > modified > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#first_oneOf_i1_modified_anyOf_i1_oneOf_i0) |
| [item 1](#first_oneOf_i1_modified_anyOf_i1_oneOf_i1) |
| [item 2](#first_oneOf_i1_modified_anyOf_i1_oneOf_i2) |
| [item 3](#first_oneOf_i1_modified_anyOf_i1_oneOf_i3) |

###### <a name="first_oneOf_i1_modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

###### <a name="first_oneOf_i1_modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

###### <a name="first_oneOf_i1_modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

#### <a name="first_oneOf_i1_provenance"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance`

**Title:** provenance

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of statements about the lineage of a Dataset

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#first_oneOf_i1_provenance_anyOf_i0) |
| [item 1](#first_oneOf_i1_provenance_anyOf_i1) |

##### <a name="first_oneOf_i1_provenance_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_provenance_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_provenance_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [ProvenanceStatement](#first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i1)              |

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement`

**Title:** ProvenanceStatement

|                           |                                                |
| ------------------------- | ---------------------------------------------- |
| **Type**                  | `object`                                       |
| **Required**              | No                                             |
| **Additional properties** | Any type allowed                               |
| **Defined in**            | /dcat-us/3.0.0/definitions/provenancestatement |

**Description:** inline description of ProvenanceStatement

| Property                                                                   | Type           | Title/Description                                                                              |
| -------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------- |
| - [@id](#first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_@id )           | string         | -                                                                                              |
| - [@type](#first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_@type )       | string         | -                                                                                              |
| - [label](#first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_label )       | null or string | provenance statement text                                                                      |
| - [labelMap](#first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_labelMap ) | null or object | Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'} |

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_@id"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_@type"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > @type`

|              |                         |
| ------------ | ----------------------- |
| **Type**     | `string`                |
| **Required** | No                      |
| **Default**  | `"ProvenanceStatement"` |

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_label"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > label`

**Title:** provenance statement text

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The text of the Provenance Statement

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i0_labelMap"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > ProvenanceStatement > labelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for provenance statement text. E.g. {'es': 'spanish words', 'fr': 'french words'}

###### <a name="first_oneOf_i1_provenance_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > provenance > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of ProvenanceStatement

#### <a name="first_oneOf_i1_publisher"></a>Property `DatasetSeries > first > oneOf > Dataset > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** An organization responsible for making the Dataset available

| One of(Option)                                     |
| -------------------------------------------------- |
| [Organization](#first_oneOf_i1_publisher_oneOf_i0) |
| [item 1](#first_oneOf_i1_publisher_oneOf_i1)       |

##### <a name="first_oneOf_i1_publisher_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > publisher > oneOf > Organization`

**Title:** Organization

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

##### <a name="first_oneOf_i1_publisher_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > publisher > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

#### <a name="first_oneOf_i1_relation"></a>Property `DatasetSeries > first > oneOf > Dataset > relation`

**Title:** related resource

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of references to a related resource

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_relation_anyOf_i0) |
| [item 1](#first_oneOf_i1_relation_anyOf_i1) |

##### <a name="first_oneOf_i1_relation_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > relation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_relation_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > relation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                         | Description               |
| ------------------------------------------------------- | ------------------------- |
| [item 1 items](#first_oneOf_i1_relation_anyOf_i1_items) | reference iri of Resource |

###### <a name="first_oneOf_i1_relation_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > relation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Resource

#### <a name="first_oneOf_i1_replaces"></a>Property `DatasetSeries > first > oneOf > Dataset > replaces`

**Title:** replaces

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of Datasets replaced by this Dataset

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_replaces_anyOf_i0) |
| [item 1](#first_oneOf_i1_replaces_anyOf_i1) |

##### <a name="first_oneOf_i1_replaces_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > replaces > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_replaces_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > replaces > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_replaces_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_replaces_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > replaces > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [Dataset](#first_oneOf_i1_replaces_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_replaces_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_replaces_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > replaces > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

###### <a name="first_oneOf_i1_replaces_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > replaces > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_rights"></a>Property `DatasetSeries > first > oneOf > Dataset > rights`

**Title:** rights

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of statements concerning all rights for the Dataset not addressed with license or accessRights, such as copyright statements

| One of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#first_oneOf_i1_rights_oneOf_i0)          |
| [RightsStatement](#first_oneOf_i1_rights_oneOf_i1) |
| [item 2](#first_oneOf_i1_rights_oneOf_i2)          |

##### <a name="first_oneOf_i1_rights_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > rights > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_rights_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > rights > oneOf > RightsStatement`

**Title:** RightsStatement

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [RightsStatement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_accessRights_oneOf_i1) |

**Description:** inline description of RightsStatement

##### <a name="first_oneOf_i1_rights_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > rights > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of RightsStatement

#### <a name="first_oneOf_i1_rightsHolder"></a>Property `DatasetSeries > first > oneOf > Dataset > rightsHolder`

**Title:** rights holder

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents (organizations) holding rights on the Dataset

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#first_oneOf_i1_rightsHolder_anyOf_i0) |
| [item 1](#first_oneOf_i1_rightsHolder_anyOf_i1) |

##### <a name="first_oneOf_i1_rightsHolder_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > rightsHolder > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_rightsHolder_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > rightsHolder > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_rightsHolder_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_rightsHolder_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > rightsHolder > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                       |
| -------------------------------------------------------------------- |
| [Organization](#first_oneOf_i1_rightsHolder_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_rightsHolder_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_rightsHolder_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > rightsHolder > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                 |
| **Required**              | No                                                                                       |
| **Additional properties** | Any type allowed                                                                         |
| **Same definition as**    | [Organization](#first_oneOf_i1_otherIdentifier_anyOf_i1_items_oneOf_i0_creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="first_oneOf_i1_rightsHolder_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > rightsHolder > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

#### <a name="first_oneOf_i1_source"></a>Property `DatasetSeries > first > oneOf > Dataset > source`

**Title:** data source

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of related Datasets from which the described Dataset is derived

| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#first_oneOf_i1_source_anyOf_i0) |
| [item 1](#first_oneOf_i1_source_anyOf_i1) |

##### <a name="first_oneOf_i1_source_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > source > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_source_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > source > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_source_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_source_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > source > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                            |
| --------------------------------------------------------- |
| [Dataset](#first_oneOf_i1_source_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_source_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_source_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > source > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of Dataset

###### <a name="first_oneOf_i1_source_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > source > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Dataset

#### <a name="first_oneOf_i1_spatial"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region or regions that are covered by the Dataset

| One of(Option)                               |
| -------------------------------------------- |
| [item 0](#first_oneOf_i1_spatial_oneOf_i0)   |
| [Location](#first_oneOf_i1_spatial_oneOf_i1) |
| [item 2](#first_oneOf_i1_spatial_oneOf_i2)   |
| [item 3](#first_oneOf_i1_spatial_oneOf_i3)   |

##### <a name="first_oneOf_i1_spatial_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_spatial_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Required**              | No                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

##### <a name="first_oneOf_i1_spatial_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

##### <a name="first_oneOf_i1_spatial_oneOf_i3"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial > oneOf > item 3`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [item 3 items](#first_oneOf_i1_spatial_oneOf_i3_items) | -           |

###### <a name="first_oneOf_i1_spatial_oneOf_i3_items"></a>DatasetSeries > first > oneOf > Dataset > spatial > oneOf > item 3 > item 3 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [Location](#first_oneOf_i1_spatial_oneOf_i3_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_spatial_oneOf_i3_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_spatial_oneOf_i3_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial > oneOf > item 3 > item 3 items > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Required**              | No                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

###### <a name="first_oneOf_i1_spatial_oneOf_i3_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > spatial > oneOf > item 3 > item 3 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

#### <a name="first_oneOf_i1_subject"></a>Property `DatasetSeries > first > oneOf > Dataset > subject`

**Title:** subject

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of primary subjects of the dataset

| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#first_oneOf_i1_subject_anyOf_i0) |
| [item 1](#first_oneOf_i1_subject_anyOf_i1) |

##### <a name="first_oneOf_i1_subject_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > subject > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_subject_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > subject > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                        | Description |
| ------------------------------------------------------ | ----------- |
| [item 1 items](#first_oneOf_i1_subject_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_subject_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > subject > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Concept](#first_oneOf_i1_subject_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_subject_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_subject_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > subject > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_subject_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > subject > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

#### <a name="first_oneOf_i1_temporal"></a>Property `DatasetSeries > first > oneOf > Dataset > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of temporal periods that the dataset covers

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_temporal_anyOf_i0) |
| [item 1](#first_oneOf_i1_temporal_anyOf_i1) |

##### <a name="first_oneOf_i1_temporal_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_temporal_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_temporal_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_temporal_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [PeriodOfTime](#first_oneOf_i1_temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_temporal_anyOf_i1_items_oneOf_i1)       |

###### <a name="first_oneOf_i1_temporal_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [PeriodOfTime](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of PeriodOfTime

###### <a name="first_oneOf_i1_temporal_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

#### <a name="first_oneOf_i1_title"></a>Property `DatasetSeries > first > oneOf > Dataset > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A name given to the Dataset

#### <a name="first_oneOf_i1_titleMap"></a>Property `DatasetSeries > first > oneOf > Dataset > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="first_oneOf_i1_category"></a>Property `DatasetSeries > first > oneOf > Dataset > category`

**Title:** category

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of categories of the dataset

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#first_oneOf_i1_category_anyOf_i0) |
| [item 1](#first_oneOf_i1_category_anyOf_i1) |

##### <a name="first_oneOf_i1_category_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > category > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_category_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > category > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_category_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_category_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > category > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                              |
| ----------------------------------------------------------- |
| [Concept](#first_oneOf_i1_category_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_category_anyOf_i1_items_oneOf_i1)  |

###### <a name="first_oneOf_i1_category_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > category > anyOf > item 1 > item 1 items > oneOf > Concept`

**Title:** Concept

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | Any type allowed                                                                           |
| **Same definition as**    | [Concept](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_representationTechnique_oneOf_i1) |

**Description:** inline description of Concept

###### <a name="first_oneOf_i1_category_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > category > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Concept

#### <a name="first_oneOf_i1_hasQualityMeasurement"></a>Property `DatasetSeries > first > oneOf > Dataset > hasQualityMeasurement`

**Title:** quality measurement

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of quality measurements for the dataset

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#first_oneOf_i1_hasQualityMeasurement_anyOf_i0) |
| [item 1](#first_oneOf_i1_hasQualityMeasurement_anyOf_i1) |

##### <a name="first_oneOf_i1_hasQualityMeasurement_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasQualityMeasurement > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_hasQualityMeasurement_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                      | Description |
| -------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_hasQualityMeasurement_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_hasQualityMeasurement_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [QualityMeasurement](#first_oneOf_i1_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_hasQualityMeasurement_anyOf_i1_items_oneOf_i1)             |

###### <a name="first_oneOf_i1_hasQualityMeasurement_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > QualityMeasurement`

**Title:** QualityMeasurement

|                           |                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                 |
| **Required**              | No                                                                                                                                                       |
| **Additional properties** | Any type allowed                                                                                                                                         |
| **Same definition as**    | [QualityMeasurement](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_hasQualityMeasurement_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of QualityMeasurement

###### <a name="first_oneOf_i1_hasQualityMeasurement_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > hasQualityMeasurement > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of QualityMeasurement

#### <a name="first_oneOf_i1_page"></a>Property `DatasetSeries > first > oneOf > Dataset > page`

**Title:** documentation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of pages or documents about this dataset

| Any of(Option)                          |
| --------------------------------------- |
| [item 0](#first_oneOf_i1_page_anyOf_i0) |
| [item 1](#first_oneOf_i1_page_anyOf_i1) |

##### <a name="first_oneOf_i1_page_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > page > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_page_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > page > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_page_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_page_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > page > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Document](#first_oneOf_i1_page_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_page_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_page_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > page > anyOf > item 1 > item 1 items > oneOf > Document`

**Title:** Document

|                           |                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                |
| **Required**              | No                                                                                      |
| **Additional properties** | Any type allowed                                                                        |
| **Same definition as**    | [Document](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_page_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Document

###### <a name="first_oneOf_i1_page_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > page > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Document

#### <a name="first_oneOf_i1_qualifiedAttribution"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedAttribution`

**Title:** qualified attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents having some form of responsibility for the dataset

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#first_oneOf_i1_qualifiedAttribution_anyOf_i0) |
| [item 1](#first_oneOf_i1_qualifiedAttribution_anyOf_i1) |

##### <a name="first_oneOf_i1_qualifiedAttribution_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedAttribution > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_qualifiedAttribution_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedAttribution > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                     | Description |
| ------------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_qualifiedAttribution_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_qualifiedAttribution_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > qualifiedAttribution > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                              |
| --------------------------------------------------------------------------- |
| [Attribution](#first_oneOf_i1_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_qualifiedAttribution_anyOf_i1_items_oneOf_i1)      |

###### <a name="first_oneOf_i1_qualifiedAttribution_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > Attribution`

**Title:** Attribution

|                           |                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                         |
| **Required**              | No                                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                                 |
| **Same definition as**    | [Attribution](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_qualifiedAttribution_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Attribution

###### <a name="first_oneOf_i1_qualifiedAttribution_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > qualifiedAttribution > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Attribution

#### <a name="first_oneOf_i1_wasAttributedTo"></a>Property `DatasetSeries > first > oneOf > Dataset > wasAttributedTo`

**Title:** attribution

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of agents attributed to this dataset

| Any of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#first_oneOf_i1_wasAttributedTo_anyOf_i0) |
| [item 1](#first_oneOf_i1_wasAttributedTo_anyOf_i1) |

##### <a name="first_oneOf_i1_wasAttributedTo_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > wasAttributedTo > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_wasAttributedTo_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > wasAttributedTo > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_wasAttributedTo_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_wasAttributedTo_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > wasAttributedTo > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                    |
| ----------------------------------------------------------------- |
| [Agent](#first_oneOf_i1_wasAttributedTo_anyOf_i1_items_oneOf_i0)  |
| [item 1](#first_oneOf_i1_wasAttributedTo_anyOf_i1_items_oneOf_i1) |

###### <a name="first_oneOf_i1_wasAttributedTo_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > wasAttributedTo > anyOf > item 1 > item 1 items > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Agent

###### <a name="first_oneOf_i1_wasAttributedTo_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > wasAttributedTo > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Agent

#### <a name="first_oneOf_i1_wasGeneratedBy"></a>Property `DatasetSeries > first > oneOf > Dataset > wasGeneratedBy`

**Title:** was generated by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of activities that generated, or provide the business context for the creation of the dataset

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#first_oneOf_i1_wasGeneratedBy_anyOf_i0) |
| [item 1](#first_oneOf_i1_wasGeneratedBy_anyOf_i1) |

##### <a name="first_oneOf_i1_wasGeneratedBy_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > wasGeneratedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_wasGeneratedBy_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > wasGeneratedBy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_wasGeneratedBy_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_wasGeneratedBy_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > wasGeneratedBy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                     |
| ------------------------------------------------------------------ |
| [Activity](#first_oneOf_i1_wasGeneratedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_wasGeneratedBy_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_wasGeneratedBy_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > wasGeneratedBy > anyOf > item 1 > item 1 items > oneOf > Activity`

**Title:** Activity

|                           |                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                           |
| **Required**              | No                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                   |
| **Same definition as**    | [Activity](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Activity

###### <a name="first_oneOf_i1_wasGeneratedBy_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > wasGeneratedBy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Activity

#### <a name="first_oneOf_i1_wasUsedBy"></a>Property `DatasetSeries > first > oneOf > Dataset > wasUsedBy`

**Title:** used by

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of activities that used the Dataset

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#first_oneOf_i1_wasUsedBy_anyOf_i0) |
| [item 1](#first_oneOf_i1_wasUsedBy_anyOf_i1) |

##### <a name="first_oneOf_i1_wasUsedBy_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > wasUsedBy > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_wasUsedBy_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > wasUsedBy > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [item 1 items](#first_oneOf_i1_wasUsedBy_anyOf_i1_items) | -           |

###### <a name="first_oneOf_i1_wasUsedBy_anyOf_i1_items"></a>DatasetSeries > first > oneOf > Dataset > wasUsedBy > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [Activity](#first_oneOf_i1_wasUsedBy_anyOf_i1_items_oneOf_i0) |
| [item 1](#first_oneOf_i1_wasUsedBy_anyOf_i1_items_oneOf_i1)   |

###### <a name="first_oneOf_i1_wasUsedBy_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > Activity`

**Title:** Activity

|                           |                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                           |
| **Required**              | No                                                                                                                                 |
| **Additional properties** | Any type allowed                                                                                                                   |
| **Same definition as**    | [Activity](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_wasUsedBy_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Activity

###### <a name="first_oneOf_i1_wasUsedBy_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > wasUsedBy > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Activity

#### <a name="first_oneOf_i1_image"></a>Property `DatasetSeries > first > oneOf > Dataset > image`

**Title:** image

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Link to a thumbnail picture illustrating the content of the dataset

| Any of(Option)                           |
| ---------------------------------------- |
| [item 0](#first_oneOf_i1_image_anyOf_i0) |
| [item 1](#first_oneOf_i1_image_anyOf_i1) |

##### <a name="first_oneOf_i1_image_anyOf_i0"></a>Property `DatasetSeries > first > oneOf > Dataset > image > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="first_oneOf_i1_image_anyOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset > image > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** The link to the image

#### <a name="first_oneOf_i1_scopeNote"></a>Property `DatasetSeries > first > oneOf > Dataset > scopeNote`

**Title:** usage note

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** usage note for the dataset

#### <a name="first_oneOf_i1_scopeNoteMap"></a>Property `DatasetSeries > first > oneOf > Dataset > scopeNoteMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for the scope note. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="first_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the first dataset

## <a name="last"></a>Property `DatasetSeries > last`

**Title:** last

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The last dataset in an ordered dataset series

| One of(Option)            |
| ------------------------- |
| [item 0](#last_oneOf_i0)  |
| [Dataset](#last_oneOf_i1) |
| [item 2](#last_oneOf_i2)  |

### <a name="last_oneOf_i0"></a>Property `DatasetSeries > last > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="last_oneOf_i1"></a>Property `DatasetSeries > last > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of the last dataset

### <a name="last_oneOf_i2"></a>Property `DatasetSeries > last > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the last dataset

## <a name="seriesMember"></a>Property `DatasetSeries > seriesMember`

**Title:** series member

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of members of the Dataset Series

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#seriesMember_anyOf_i0) |
| [item 1](#seriesMember_anyOf_i1) |

### <a name="seriesMember_anyOf_i0"></a>Property `DatasetSeries > seriesMember > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="seriesMember_anyOf_i1"></a>Property `DatasetSeries > seriesMember > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#seriesMember_anyOf_i1_items) | -           |

#### <a name="seriesMember_anyOf_i1_items"></a>DatasetSeries > seriesMember > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [Dataset](#seriesMember_anyOf_i1_items_oneOf_i0) |
| [item 1](#seriesMember_anyOf_i1_items_oneOf_i1)  |

##### <a name="seriesMember_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

**Description:** inline description of the member dataset

##### <a name="seriesMember_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the member dataset

## <a name="accrualPeriodicity"></a>Property `DatasetSeries > accrualPeriodicity`

**Title:** frequency

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The frequency at which the Dataset Series is updated

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#accrualPeriodicity_oneOf_i0)    |
| [frequency](#accrualPeriodicity_oneOf_i1) |
| [item 2](#accrualPeriodicity_oneOf_i2)    |

### <a name="accrualPeriodicity_oneOf_i0"></a>Property `DatasetSeries > accrualPeriodicity > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="accrualPeriodicity_oneOf_i1"></a>Property `DatasetSeries > accrualPeriodicity > oneOf > frequency`

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Defined in**            | /dcat-us/3.0.0/definitions/frequency |

**Description:** inline description of Frequency

### <a name="accrualPeriodicity_oneOf_i2"></a>Property `DatasetSeries > accrualPeriodicity > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Frequency

## <a name="description"></a>Property `DatasetSeries > description`

**Title:** description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A free-text account of the Dataset Series

## <a name="descriptionMap"></a>Property `DatasetSeries > descriptionMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="issued"></a>Property `DatasetSeries > issued`

**Title:** release date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g.,publication) of the Dataset Series

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `DatasetSeries > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="issued_anyOf_i1"></a>Property `DatasetSeries > issued > anyOf > item 1`

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

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `DatasetSeries > modified`

**Title:** update/modification date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The most recent date on which the Dataset Series was changed or modified

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `DatasetSeries > modified > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="modified_anyOf_i1"></a>Property `DatasetSeries > modified > anyOf > item 1`

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

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `DatasetSeries > publisher`

**Title:** publisher

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity (organization) responsible for ensuring the coherency of the Dataset Series

| One of(Option)                |
| ----------------------------- |
| [item 0](#publisher_oneOf_i0) |
| [Agent](#publisher_oneOf_i1)  |
| [item 2](#publisher_oneOf_i2) |

### <a name="publisher_oneOf_i0"></a>Property `DatasetSeries > publisher > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="publisher_oneOf_i1"></a>Property `DatasetSeries > publisher > oneOf > Agent`

**Title:** Agent

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Required**              | No                                                                                                                            |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of publisher

### <a name="publisher_oneOf_i2"></a>Property `DatasetSeries > publisher > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of publisher

## <a name="spatial"></a>Property `DatasetSeries > spatial`

**Title:** spatial/geographic coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A geographic region that is covered by the Dataset Series

| Any of(Option)              |
| --------------------------- |
| [item 0](#spatial_anyOf_i0) |
| [item 1](#spatial_anyOf_i1) |

### <a name="spatial_anyOf_i0"></a>Property `DatasetSeries > spatial > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="spatial_anyOf_i1"></a>Property `DatasetSeries > spatial > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#spatial_anyOf_i1_items) | -           |

#### <a name="spatial_anyOf_i1_items"></a>DatasetSeries > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#spatial_anyOf_i1_items_oneOf_i1)   |

##### <a name="spatial_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Required**              | No                                                                                                                               |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of Location

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Location

## <a name="temporal"></a>Property `DatasetSeries > temporal`

**Title:** temporal coverage

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A list of temporal periods that the Dataset Series covers

| Any of(Option)               |
| ---------------------------- |
| [item 0](#temporal_anyOf_i0) |
| [item 1](#temporal_anyOf_i1) |

### <a name="temporal_anyOf_i0"></a>Property `DatasetSeries > temporal > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="temporal_anyOf_i1"></a>Property `DatasetSeries > temporal > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>DatasetSeries > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#temporal_anyOf_i1_items_oneOf_i1)       |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Required**              | No                                                                                                                                    |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [PeriodOfTime](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

**Description:** inline description of PeriodOfTime

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of PeriodOfTime

## <a name="title"></a>Property `DatasetSeries > title`

**Title:** title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A name given to the Dataset Series

## <a name="titleMap"></a>Property `DatasetSeries > titleMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
