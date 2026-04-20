

**Title:** CUIRestriction

Information describing Controlled Unclassified Information (CUI) restrictions for a resource

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "CUIRestriction",
    "cuiBannerMarking": "CUI//SP-CTI",
    "designationIndicator": "Controlled by: Agency XYZ"
}
```

| Property                                                           | Type                    | Title/Description                |
| ------------------------------------------------------------------ | ----------------------- | -------------------------------- |
| - [@id](#@id )                                                     | string                  | -                                |
| - [@type](#@type )                                                 | string                  | -                                |
| + [cuiBannerMarking](#cuiBannerMarking )                           | string                  | CUI banner marking               |
| + [designationIndicator](#designationIndicator )                   | string                  | CUI designation indicator        |
| - [requiredIndicatorPerAuthority](#requiredIndicatorPerAuthority ) | null or array of string | required indicator per authority |

## <a name="@id"></a>[Optional] Property `CUIRestriction > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/cui-restrictions/dataset-001"
```

## <a name="@type"></a>[Optional] Property `CUIRestriction > @type`

**Requirement:** Optional

| **Type**    | `string`           |
| ----------- | ------------------ |
| **Default** | `"CUIRestriction"` |

## <a name="cuiBannerMarking"></a>[Optional] Property `CUIRestriction > cuiBannerMarking`

**Title:** CUI banner marking

**Requirement:** Optional

CUI (Controlled Unclassified Information) banner marking is required for any unclassified information that is deemed sensitive and requires protection; see information at https://www.archives.gov/cui/registry/category-marking-list

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"CUI//SP-CTI"
```

```json
"CUI//SP-PRVCY//SP-LEGAL"
```

## <a name="designationIndicator"></a>[Optional] Property `CUIRestriction > designationIndicator`

**Title:** CUI designation indicator

**Requirement:** Optional

Agency that designated the information as CUI; include at least "Controlled by:" and, when possible, contact information

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

**Examples:**

```json
"Controlled by: Agency XYZ"
```

```json
"Controlled by: DOC; POC: Jane Smith, mailto:jane.smith@example.gov, XXX-XXX-XXXX"
```

## <a name="requiredIndicatorPerAuthority"></a>[Optional] Property `CUIRestriction > requiredIndicatorPerAuthority`

**Title:** required indicator per authority

**Requirement:** Optional

List of free-text required indicators from the applicable authority (for example, category descriptions or distribution statements)

| **Type** | `null or array of string` |
| -------- | ------------------------- |

**Example:**

```json
[
    "Privacy Act of 1974",
    "Federal Records Act"
]
```

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [Indicator string](#requiredIndicatorPerAuthority_items) | -           |

### <a name="requiredIndicatorPerAuthority_items"></a>CUIRestriction > requiredIndicatorPerAuthority > Indicator string

**Title:** Indicator string

| **Type** | `string` |
| -------- | -------- |

