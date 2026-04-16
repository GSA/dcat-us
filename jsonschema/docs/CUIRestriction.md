

**Title:** CUIRestriction

A specific restriction on handling Controlled Unclassified Information (CUI)

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

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

## <a name="@type"></a>[Optional] Property `CUIRestriction > @type`

**Requirement:** Optional

| **Type**    | `string`           |
| ----------- | ------------------ |
| **Default** | `"CUIRestriction"` |

## <a name="cuiBannerMarking"></a>[Mandatory] Property `CUIRestriction > cuiBannerMarking`

**Title:** CUI banner marking

**Requirement:** Mandatory

CUI (Controlled Unclassified Information) banner marking is required for any unclassified information that is deemed sensitive and requires protection

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="designationIndicator"></a>[Mandatory] Property `CUIRestriction > designationIndicator`

**Title:** CUI designation indicator

**Requirement:** Mandatory

Designation Indicator shows which agency made the document CUI

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="requiredIndicatorPerAuthority"></a>[Optional] Property `CUIRestriction > requiredIndicatorPerAuthority`

**Title:** required indicator per authority

**Requirement:** Optional

List of free text of the required indicator

| **Type** | `null or array of string` |
| -------- | ------------------------- |

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [Indicator string](#requiredIndicatorPerAuthority_items) | -           |

### <a name="requiredIndicatorPerAuthority_items"></a>CUIRestriction > requiredIndicatorPerAuthority > Indicator string

**Title:** Indicator string

| **Type** | `string` |
| -------- | -------- |

