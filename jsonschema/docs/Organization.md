# Organization

**Title:** Organization

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about an organization, including other organizations that it is part of

| Property                                   | Type           | Title/Description                                                                      |
| ------------------------------------------ | -------------- | -------------------------------------------------------------------------------------- |
| - [@id](#@id )                             | string         | -                                                                                      |
| - [@type](#@type )                         | string         | -                                                                                      |
| + [name](#name )                           | string         | name                                                                                   |
| - [subOrganizationOf](#subOrganizationOf ) | Combination    | suborganization of                                                                     |
| - [altLabel](#altLabel )                   | null or string | alternative label                                                                      |
| - [altLabelMap](#altLabelMap )             | null or object | Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [notation](#notation )                   | Combination    | notation                                                                               |
| - [prefLabel](#prefLabel )                 | null or string | preferred label                                                                        |
| - [prefLabelMap](#prefLabelMap )           | null or object | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}   |

## <a name="@id"></a>Property `Organization > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `Organization > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"Organization"` |

## <a name="name"></a>Property `Organization > name`

**Title:** name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the Organization

## <a name="subOrganizationOf"></a>Property `Organization > subOrganizationOf`

**Title:** suborganization of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#subOrganizationOf_anyOf_i0) |
| [item 1](#subOrganizationOf_anyOf_i1) |

### <a name="subOrganizationOf_anyOf_i0"></a>Property `Organization > subOrganizationOf > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="subOrganizationOf_anyOf_i1"></a>Property `Organization > subOrganizationOf > anyOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 1 items](#subOrganizationOf_anyOf_i1_items) | -           |

#### <a name="subOrganizationOf_anyOf_i1_items"></a>Organization > subOrganizationOf > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Organization](#subOrganizationOf_anyOf_i1_items_oneOf_i0) |
| [item 1](#subOrganizationOf_anyOf_i1_items_oneOf_i1)       |

##### <a name="subOrganizationOf_anyOf_i1_items_oneOf_i0"></a>Property `Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > Organization`

**Title:** Organization

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | No                    |
| **Additional properties** | Any type allowed      |
| **Same definition as**    | [Organization](#root) |

**Description:** inline description of Organization

##### <a name="subOrganizationOf_anyOf_i1_items_oneOf_i1"></a>Property `Organization > subOrganizationOf > anyOf > item 1 > item 1 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

**Description:** reference iri of Organization

## <a name="altLabel"></a>Property `Organization > altLabel`

**Title:** alternative label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** alternative name (trading name, colloquial name) for an organization

## <a name="altLabelMap"></a>Property `Organization > altLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'}

## <a name="notation"></a>Property `Organization > notation`

**Title:** notation

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

| Any of(Option)               |
| ---------------------------- |
| [item 0](#notation_anyOf_i0) |
| [item 1](#notation_anyOf_i1) |

### <a name="notation_anyOf_i0"></a>Property `Organization > notation > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="notation_anyOf_i1"></a>Property `Organization > notation > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#notation_anyOf_i1_items) | -           |

#### <a name="notation_anyOf_i1_items"></a>Organization > notation > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="prefLabel"></a>Property `Organization > prefLabel`

**Title:** preferred label

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or string` |
| **Required** | No               |

**Description:** Preferred or legal name of the organization

## <a name="prefLabelMap"></a>Property `Organization > prefLabelMap`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `null or object` |
| **Required** | No               |

**Description:** Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
