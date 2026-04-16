

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Kind",
    "fn": "Climate Data Support Team",
    "hasEmail": "mailto:climate-support@example.gov",
    "organization-name": "National Climate Data Center",
    "tel": "+1-555-123-4567"
}
```

| Property                                   | Type           | Title/Description |
| ------------------------------------------ | -------------- | ----------------- |
| - [@id](#@id )                             | string         | -                 |
| - [@type](#@type )                         | string         | -                 |
| - [address](#address )                     | null or array  | address           |
| + [hasEmail](#hasEmail )                   | string         | Email             |
| - [family-name](#family-name )             | null or string | family name       |
| + [fn](#fn )                               | string         | formatted name    |
| - [given-name](#given-name )               | null or string | given name        |
| - [organization-name](#organization-name ) | null or string | organization name |
| - [tel](#tel )                             | null or string | telephone         |
| - [title](#title )                         | null or string | position title    |

## <a name="@id"></a>[Optional] Property `Kind > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/contacts/climate-support-001"
```

## <a name="@type"></a>[Optional] Property `Kind > @type`

**Requirement:** Optional

| **Type**    | `string` |
| ----------- | -------- |
| **Default** | `"Kind"` |

## <a name="address"></a>[Optional] Property `Kind > address`

**Title:** address

**Requirement:** Optional

The address of the contact

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description               |
| ------------------------------- | ------------------------- |
| [Address](#address_items)       | A single physical address |

### <a name="address_items"></a>Kind > address > Address

**Title:** Address

A single physical address

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Address](./Address.md) |

## <a name="hasEmail"></a>[Mandatory] Property `Kind > hasEmail`

**Title:** Email

**Requirement:** Mandatory

Email address for the contact

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

## <a name="family-name"></a>[Optional] Property `Kind > family-name`

**Title:** family name

**Requirement:** Optional

The family name of the contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Smith"
```

## <a name="fn"></a>[Mandatory] Property `Kind > fn`

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

## <a name="given-name"></a>[Optional] Property `Kind > given-name`

**Title:** given name

**Requirement:** Optional

The given name of the contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Jane"
```

## <a name="organization-name"></a>[Optional] Property `Kind > organization-name`

**Title:** organization name

**Requirement:** Optional

The name of the organization to contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"National Climate Data Center"
```

## <a name="tel"></a>[Optional] Property `Kind > tel`

**Title:** telephone

**Requirement:** Optional

The telephone number for the contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"+1-555-123-4567"
```

## <a name="title"></a>[Optional] Property `Kind > title`

**Title:** position title

**Requirement:** Optional

The position role of the person to contact

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"Senior Climate Data Scientist"
```

