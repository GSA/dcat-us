# Identifier

**Title:** Identifier

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about an identifier scheme

| Property                         | Type           | Title/Description |
| -------------------------------- | -------------- | ----------------- |
| - [@id](#@id )                   | string         | -                 |
| - [@type](#@type )               | string         | -                 |
| - [schemaAgency](#schemaAgency ) | null or string | schema agency     |
| - [creator](#creator )           | Combination    | creator           |
| - [issued](#issued )             | Combination    | issued            |
| - [version](#version )           | null or string | version           |
| - [notation](#notation )         | null or string | notation          |

## <a name="@id"></a>Property `Identifier > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Identifier > @type`

|              |                |
| ------------ | -------------- |
| **Type**     | `string`       |
| **Required** | No             |
| **Default**  | `"Identifier"` |

## <a name="schemaAgency"></a>Property `Identifier > schemaAgency`

**Title:** schema agency

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** The name of the agency that issued the identifier

## <a name="creator"></a>Property `Identifier > creator`

**Title:** creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** the agency that manages the identifier scheme

| One of(Option)                    |
| --------------------------------- |
| [item 0](#creator_oneOf_i0)       |
| [Organization](#creator_oneOf_i1) |
| [item 2](#creator_oneOf_i2)       |

### <a name="creator_oneOf_i0"></a>Property `Identifier > creator > oneOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="creator_oneOf_i1"></a>Property `Identifier > creator > oneOf > Organization`

**Title:** Organization

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | /dcat-us/3.0.0/definitions/organization |

**Description:** inline description of the creator

| Property                                                    | Type           | Title/Description                                                                      |
| ----------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------- |
| - [@id](#creator_oneOf_i1_@id )                             | string         | -                                                                                      |
| - [@type](#creator_oneOf_i1_@type )                         | string         | -                                                                                      |
| + [name](#creator_oneOf_i1_name )                           | string         | name                                                                                   |
| - [subOrganizationOf](#creator_oneOf_i1_subOrganizationOf ) | Combination    | suborganization of                                                                     |
| - [altLabel](#creator_oneOf_i1_altLabel )                   | null or string | alternative label                                                                      |
| - [altLabelMap](#creator_oneOf_i1_altLabelMap )             | null or object | Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [notation](#creator_oneOf_i1_notation )                   | Combination    | notation                                                                               |
| - [prefLabel](#creator_oneOf_i1_prefLabel )                 | null or string | preferred label                                                                        |
| - [prefLabelMap](#creator_oneOf_i1_prefLabelMap )           | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}   |

#### <a name="creator_oneOf_i1_@id"></a>Property `Identifier > creator > oneOf > Organization > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

#### <a name="creator_oneOf_i1_@type"></a>Property `Identifier > creator > oneOf > Organization > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Organization"` |

#### <a name="creator_oneOf_i1_name"></a>Property `Identifier > creator > oneOf > Organization > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the Organization

#### <a name="creator_oneOf_i1_subOrganizationOf"></a>Property `Identifier > creator > oneOf > Organization > subOrganizationOf`

**Title:** suborganization of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#creator_oneOf_i1_subOrganizationOf_anyOf_i0) |
| [item 1](#creator_oneOf_i1_subOrganizationOf_anyOf_i1) |

##### <a name="creator_oneOf_i1_subOrganizationOf_anyOf_i0"></a>Property `Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="creator_oneOf_i1_subOrganizationOf_anyOf_i1"></a>Property `Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [item 1 items](#creator_oneOf_i1_subOrganizationOf_anyOf_i1_items) | -           |

###### <a name="creator_oneOf_i1_subOrganizationOf_anyOf_i1_items"></a>Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                              |
| --------------------------------------------------------------------------- |
| [Organization](#creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i0) |
| [item 1](#creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i1)       |

###### <a name="creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i0"></a>Property `Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Same definition as**    | [Organization](#creator_oneOf_i1) |

**Description:** inline description of Organization

###### <a name="creator_oneOf_i1_subOrganizationOf_anyOf_i1_items_oneOf_i1"></a>Property `Identifier > creator > oneOf > Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

#### <a name="creator_oneOf_i1_altLabel"></a>Property `Identifier > creator > oneOf > Organization > altLabel`

**Title:** alternative label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** alternative name (trading name, colloquial name) for an organization

#### <a name="creator_oneOf_i1_altLabelMap"></a>Property `Identifier > creator > oneOf > Organization > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'}

#### <a name="creator_oneOf_i1_notation"></a>Property `Identifier > creator > oneOf > Organization > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#creator_oneOf_i1_notation_anyOf_i0) |
| [item 1](#creator_oneOf_i1_notation_anyOf_i1) |

##### <a name="creator_oneOf_i1_notation_anyOf_i0"></a>Property `Identifier > creator > oneOf > Organization > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="creator_oneOf_i1_notation_anyOf_i1"></a>Property `Identifier > creator > oneOf > Organization > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [item 1 items](#creator_oneOf_i1_notation_anyOf_i1_items) | -           |

###### <a name="creator_oneOf_i1_notation_anyOf_i1_items"></a>Identifier > creator > oneOf > Organization > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="creator_oneOf_i1_prefLabel"></a>Property `Identifier > creator > oneOf > Organization > prefLabel`

**Title:** preferred label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred or legal name of the organization

#### <a name="creator_oneOf_i1_prefLabelMap"></a>Property `Identifier > creator > oneOf > Organization > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

### <a name="creator_oneOf_i2"></a>Property `Identifier > creator > oneOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of the creator

## <a name="issued"></a>Property `Identifier > issued`

**Title:** issued

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The date of formal issuance (e.g., publication) of the Identifier

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `Identifier > issued > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="issued_anyOf_i1"></a>Property `Identifier > issued > anyOf > item 1`

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

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `Identifier > issued > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="version"></a>Property `Identifier > version`

**Title:** version

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** version of the identifier scheme

## <a name="notation"></a>Property `Identifier > notation`

**Title:** notation

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** abbreviation or code from code lists for an identifier

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
