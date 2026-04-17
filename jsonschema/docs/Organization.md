

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

| Property                                   | Type                    | Title/Description  |
| ------------------------------------------ | ----------------------- | ------------------ |
| - [@id](#@id )                             | string                  | -                  |
| - [@type](#@type )                         | string                  | -                  |
| + [name](#name )                           | string                  | name               |
| - [subOrganizationOf](#subOrganizationOf ) | null or array           | suborganization of |
| - [altLabel](#altLabel )                   | null or string          | alternative label  |
| - [notation](#notation )                   | null or array of string | notation           |
| - [prefLabel](#prefLabel )                 | null or string          | preferred label    |

## <a name="@id"></a>[Optional] Property `Organization > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/organizations/census-bureau"
```

## <a name="@type"></a>[Optional] Property `Organization > @type`

**Requirement:** Optional

| **Type**    | `string`         |
| ----------- | ---------------- |
| **Default** | `"Organization"` |

## <a name="name"></a>[Optional] Property `Organization > name`

**Title:** name

**Requirement:** Optional

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

## <a name="subOrganizationOf"></a>[Optional] Property `Organization > subOrganizationOf`

**Title:** suborganization of

**Requirement:** Optional

Represents hierarchical containment of Organizations or OrganizationalUnits; indicates an Organization which contains this Organization

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be          | Description                                                                       |
| ---------------------------------------- | --------------------------------------------------------------------------------- |
| [Organization](#subOrganizationOf_items) | An organization involved with a resource, including parent or child organizations |

### <a name="subOrganizationOf_items"></a>Organization > subOrganizationOf > Organization

**Title:** Organization

An organization involved with a resource, including parent or child organizations

| **Type**                  | `object`              |
| ------------------------- | --------------------- |
| **Additional properties** | Any type allowed      |
| **Same definition as**    | [Organization](#root) |

## <a name="altLabel"></a>[Optional] Property `Organization > altLabel`

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

## <a name="notation"></a>[Optional] Property `Organization > notation`

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
| [Abbreviation](#notation_items) | -           |

### <a name="notation_items"></a>Organization > notation > Abbreviation

**Title:** Abbreviation

| **Type** | `string` |
| -------- | -------- |

## <a name="prefLabel"></a>[Optional] Property `Organization > prefLabel`

**Title:** preferred label

**Requirement:** Optional

Preferred or legal name of the organization

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"United States Census Bureau"
```

