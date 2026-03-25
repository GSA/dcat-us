

**Title:** Organization

Information about an organization, including other organizations that it is part of

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                   | Type               | Title/Description                                                                      |
| ------------------------------------------ | ------------------ | -------------------------------------------------------------------------------------- |
| - [@id](#@id )                             | string             | -                                                                                      |
| - [@type](#@type )                         | string             | -                                                                                      |
| + [name](#name )                           | string             | name                                                                                   |
| - [subOrganizationOf](#subOrganizationOf ) | More than one type | suborganization of                                                                     |
| - [altLabel](#altLabel )                   | null or string     | alternative label                                                                      |
| - [altLabelMap](#altLabelMap )             | null or object     | Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'} |
| - [notation](#notation )                   | More than one type | notation                                                                               |
| - [prefLabel](#prefLabel )                 | null or string     | preferred label                                                                        |
| - [prefLabelMap](#prefLabelMap )           | null or object     | Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}   |

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                  |
| ----------- | ---------------- |
| **Type**    | `string`         |
| **Default** | `"Organization"` |

## <a name="name"></a>Property `name`

**Title:** name

The full name of the Organization

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="subOrganizationOf"></a>Property `subOrganizationOf`

**Title:** suborganization of

Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#subOrganizationOf_anyOf_i0) |
| [item 1](#subOrganizationOf_anyOf_i1) |

### <a name="subOrganizationOf_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="subOrganizationOf_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [item 1 items](#subOrganizationOf_anyOf_i1_items) | -           |

#### <a name="subOrganizationOf_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                             |
| ---------------------------------------------------------- |
| [Organization](#subOrganizationOf_anyOf_i1_items_oneOf_i0) |
| [item 1](#subOrganizationOf_anyOf_i1_items_oneOf_i1)       |

##### <a name="subOrganizationOf_anyOf_i1_items_oneOf_i0"></a>Property `Organization`

**Title:** Organization

inline description of Organization

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Additional properties** | Any type allowed      |
| **Same definition as**    | [Organization](#root) |

##### <a name="subOrganizationOf_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Organization

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="altLabel"></a>Property `altLabel`

**Title:** alternative label

alternative name (trading name, colloquial name) for an organization

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="altLabelMap"></a>Property `altLabelMap`

Language map for alternative label. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="notation"></a>Property `notation`

**Title:** notation

List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#notation_anyOf_i0) |
| [item 1](#notation_anyOf_i1) |

### <a name="notation_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="notation_anyOf_i1"></a>Property `item 1`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#notation_anyOf_i1_items) | -           |

#### <a name="notation_anyOf_i1_items"></a>item 1 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="prefLabel"></a>Property `prefLabel`

**Title:** preferred label

Preferred or legal name of the organization

|          |                  |
| -------- | ---------------- |
| **Type** | `null or string` |

## <a name="prefLabelMap"></a>Property `prefLabelMap`

Language map for preferred label. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

