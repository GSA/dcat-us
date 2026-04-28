# Agents

Data information classes including Agent, Organization, and Kind, which describe organizations, people, and contact information.

<a name="agent"></a>

## Class Agent

**Title:** Agent

A person, organization, software agent, or other entity involved with a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Agent",
    "name": "National Climate Data Center",
    "category": [
        "https://example.gov/concepts/federal-agency"
    ]
}
```

| Property               | Type          | Requirement Level | Title/Description |
| ---------------------- | ------------- | ----------------- | ----------------- |
| [@id](#agent--@id)           | string        | Optional          | -                 |
| [@type](#agent--@type)       | string        | Optional          | -                 |
| [category](#agent--category) | null or array | Optional          | category          |
| [name](#agent--name)         | string        | Mandatory         | name              |

## <a name="agent--@id"></a>`Agent > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/agents/data-steward-001"
```

## <a name="agent--@type"></a>`Agent > @type`

**Requirement:** Optional

| **Type**    | `string`  |
| ----------- | --------- |
| **Default** | `"Agent"` |

## <a name="agent--category"></a>`Agent > category`

**Title:** category

**Requirement:** Optional

The type of the agent that makes the item available

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                       | Description                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------ |
| [Concept](./identifiers-and-relationships.md#concept) | A controlled term or label, optionally drawn from a concept scheme |

## <a name="agent--name"></a>`Agent > name`

**Title:** name

**Requirement:** Mandatory

The name of the agent

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"National Climate Data Center"
```

```json
"U.S. Department of Commerce Data Stewardship Office"
```

---

<a name="organization"></a>

## Class Organization

**Title:** Organization

An organization involved with a resource, including parent or child organizations

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Examples:**

```json
{
    "@type": "Organization",
    "name": "National Climate Data Center",
    "altLabel": "NCDC"
}
```

```json
{
    "@id": "https://example.gov/organizations/census-bureau",
    "@type": "Organization",
    "name": "U.S. Census Bureau",
    "prefLabel": "United States Census Bureau",
    "altLabel": "Census Bureau",
    "notation": [
        "USCB",
        "CB"
    ],
    "subOrganizationOf": [
        {
            "@id": "https://example.gov/organizations/doc",
            "@type": "Organization",
            "name": "U.S. Department of Commerce"
        }
    ]
}
```

| Property                                 | Type                    | Requirement Level | Title/Description  |
| ---------------------------------------- | ----------------------- | ----------------- | ------------------ |
| [@id](#organization--@id)                             | string                  | Optional          | -                  |
| [@type](#organization--@type)                         | string                  | Optional          | -                  |
| [name](#organization--name)                           | string                  | Mandatory         | name               |
| [subOrganizationOf](#organization--subOrganizationOf) | null or array           | Optional          | suborganization of |
| [altLabel](#organization--altLabel)                   | null or string          | Optional          | alternative label  |
| [notation](#organization--notation)                   | null or array of string | Optional          | notation           |
| [prefLabel](#organization--prefLabel)                 | null or string          | Optional          | preferred label    |

## <a name="organization--@id"></a>`Organization > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/organizations/census-bureau"
```

## <a name="organization--@type"></a>`Organization > @type`

**Requirement:** Optional

| **Type**    | `string`         |
| ----------- | ---------------- |
| **Default** | `"Organization"` |

## <a name="organization--name"></a>`Organization > name`

**Title:** name

**Requirement:** Mandatory

The full name of the Organization

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"National Climate Data Center"
```

```json
"U.S. Census Bureau"
```

## <a name="organization--subOrganizationOf"></a>`Organization > subOrganizationOf`

**Title:** suborganization of

**Requirement:** Optional

Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be          | Description                                                                       |
| ---------------------------------------- | --------------------------------------------------------------------------------- |
| [Organization](./agents.md#organization) | An organization involved with a resource, including parent or child organizations |

## <a name="organization--altLabel"></a>`Organization > altLabel`

**Title:** alternative label

**Requirement:** Optional

alternative name (trading name, colloquial name) for an organization

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"NCDC"
```

```json
"Census Bureau"
```

## <a name="organization--notation"></a>`Organization > notation`

**Title:** notation

**Requirement:** Optional

List of abbreviations or codes from code lists for an organization (e.g. DOI, DOD)

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "USCB",
    "CB"
]
```

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [Abbreviation](#organization--notation_items) | -           |

### <a name="organization--notation_items"></a>Abbreviation

**Title:** Abbreviation

| **Type** | `string` |
| -------- | -------- |

## <a name="organization--prefLabel"></a>`Organization > prefLabel`

**Title:** preferred label

**Requirement:** Optional

Preferred or legal name of the organization

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"United States Census Bureau"
```

---

<a name="kind"></a>

## Class Kind

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Examples:**

```json
{
    "@type": "Kind",
    "fn": "Climate Data Support Team",
    "hasEmail": "mailto:climate-support@example.gov",
    "organization-name": "National Climate Data Center",
    "tel": "+1-555-123-4567"
}
```

```json
{
    "@type": "Kind",
    "fn": "Dr. Jane Smith",
    "hasEmail": "mailto:jane.smith@example.gov"
}
```

| Property                                 | Type           | Requirement Level | Title/Description |
| ---------------------------------------- | -------------- | ----------------- | ----------------- |
| [@id](#kind--@id)                             | string         | Optional          | -                 |
| [@type](#kind--@type)                         | string         | Optional          | -                 |
| [address](#kind--address)                     | null or array  | Optional          | address           |
| [hasEmail](#kind--hasEmail)                   | string         | Mandatory         | Email             |
| [family-name](#kind--family-name)             | null or string | Optional          | family name       |
| [fn](#kind--fn)                               | string         | Mandatory         | formatted name    |
| [given-name](#kind--given-name)               | null or string | Optional          | given name        |
| [organization-name](#kind--organization-name) | null or string | Optional          | organization name |
| [tel](#kind--tel)                             | null or string | Optional          | telephone         |
| [title](#kind--title)                         | null or string | Optional          | position title    |

## <a name="kind--@id"></a>`Kind > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/contacts/climate-support-001"
```

## <a name="kind--@type"></a>`Kind > @type`

**Requirement:** Optional

| **Type**    | `string` |
| ----------- | -------- |
| **Default** | `"Kind"` |

## <a name="kind--address"></a>`Kind > address`

**Title:** address

**Requirement:** Optional

The address of the contact

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be                  | Description               |
| ------------------------------------------------ | ------------------------- |
| [Address](./temporal-spatial-metrics.md#address) | A single physical address |

## <a name="kind--hasEmail"></a>`Kind > hasEmail`

**Title:** Email

**Requirement:** Mandatory

Email address for the contact in mailto: format (for example, mailto:support@example.gov)

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"mailto:climate-support@example.gov"
```

```json
"mailto:jane.smith@example.gov"
```

| Restrictions                      |                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^mailto:[\w\_\~\!\$\&\'\(\)\*\+\,\;\=\:.-]+@[\w.-]+\.[\w.-]+?$``` [Test](https://regex101.com/?regex=%5Emailto%3A%5B%5Cw%5C_%5C~%5C%21%5C%24%5C%26%5C%27%5C%28%5C%29%5C%2A%5C%2B%5C%2C%5C%3B%5C%3D%5C%3A.-%5D%2B%40%5B%5Cw.-%5D%2B%5C.%5B%5Cw.-%5D%2B%3F%24&testString=%22mailto%3Aclimate-support%40example.gov%22) |

## <a name="kind--family-name"></a>`Kind > family-name`

**Title:** family name

**Requirement:** Optional

The family name of the contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Smith"
```

## <a name="kind--fn"></a>`Kind > fn`

**Title:** formatted name

**Requirement:** Mandatory

The formatted text of the name of the contact

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"Climate Data Support Team"
```

```json
"Dr. Jane Smith"
```

## <a name="kind--given-name"></a>`Kind > given-name`

**Title:** given name

**Requirement:** Optional

The given name of the contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Jane"
```

## <a name="kind--organization-name"></a>`Kind > organization-name`

**Title:** organization name

**Requirement:** Optional

The name of the organization to contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"National Climate Data Center"
```

## <a name="kind--tel"></a>`Kind > tel`

**Title:** telephone

**Requirement:** Optional

The telephone number for the contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"+1-555-123-4567"
```

## <a name="kind--title"></a>`Kind > title`

**Title:** position title

**Requirement:** Optional

The position role of the person to contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Senior Climate Data Scientist"
```
