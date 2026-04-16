

**Title:** UseRestriction

A restriction on usage of another item

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "UseRestriction",
    "restrictionStatus": "https://example.gov/concepts/unrestricted",
    "specificRestriction": "https://creativecommons.org/publicdomain/zero/1.0/",
    "restrictionNote": "This data may be used for any purpose without restriction."
}
```

| Property                                       | Type               | Title/Description    |
| ---------------------------------------------- | ------------------ | -------------------- |
| - [@id](#@id )                                 | string             | -                    |
| - [@type](#@type )                             | string             | -                    |
| - [restrictionNote](#restrictionNote )         | null or string     | restriction note     |
| + [restrictionStatus](#restrictionStatus )     | object             | restriction status   |
| - [specificRestriction](#specificRestriction ) | More than one type | specific restriction |

## <a name="@id"></a>[Optional] Property `UseRestriction > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/restrictions/use-restriction-001"
```

## <a name="@type"></a>[Optional] Property `UseRestriction > @type`

**Requirement:** Optional

| **Type**    | `string`           |
| ----------- | ------------------ |
| **Default** | `"UseRestriction"` |

**Example:**

```json
"UseRestriction"
```

## <a name="restrictionNote"></a>[Optional] Property `UseRestriction > restrictionNote`

**Title:** restriction note

**Requirement:** Optional

Significant information pertaining to the use or reproduction of the data

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"This data may be used for any purpose without restriction."
```

```json
"This data may be used for research purposes. Commercial use requires written permission from the data steward."
```

## <a name="restrictionStatus"></a>[Mandatory] Property `UseRestriction > restrictionStatus`

**Title:** restriction status

**Requirement:** Mandatory

Indication of whether or not there are use restrictions on the archival materials

| **Type**                  | More than one type      |
| ------------------------- | ----------------------- |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Concept](./Concept.md) |

**Examples:**

```json
"https://example.gov/concepts/unrestricted"
```

```json
{
    "@id": "https://example.gov/concepts/restricted-commercial",
    "@type": "Concept",
    "prefLabel": "Restricted - Commercial Use",
    "altLabel": "Commercial Restriction",
    "definition": "The resource has restrictions on commercial use but is available for research and non-commercial purposes.",
    "notation": [
        "RST-COM"
    ],
    "inScheme": {
        "@id": "https://example.gov/concept-schemes/restriction-status",
        "@type": "ConceptScheme",
        "title": "Restriction Status"
    }
}
```

## <a name="specificRestriction"></a>[Recommended] Property `UseRestriction > specificRestriction`

**Title:** specific restriction

**Requirement:** Recommended

The specific NARA restriction associated with the use restriction

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

**Examples:**

```json
"https://creativecommons.org/publicdomain/zero/1.0/"
```

```json
{
    "@id": "https://example.gov/concepts/nara-restriction-copyright",
    "@type": "Concept",
    "prefLabel": "Copyright Restriction",
    "definition": "Materials protected by copyright with limited use permissions.",
    "notation": [
        "CR"
    ],
    "inScheme": {
        "@id": "https://example.gov/concept-schemes/nara-restrictions",
        "@type": "ConceptScheme",
        "title": "NARA Restrictions"
    }
}
```

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [Null allowed when not required](#specificRestriction_anyOf_i0) |
| [Concept](#specificRestriction_anyOf_i1)                        |

### <a name="specificRestriction_anyOf_i0"></a>Property `UseRestriction > specificRestriction > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="specificRestriction_anyOf_i1"></a>Property `UseRestriction > specificRestriction > anyOf > Concept`

**Title:** Concept

inline description of the specific restriction

| **Type**                  | More than one type                      |
| ------------------------- | --------------------------------------- |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [restrictionStatus](#restrictionStatus) |

