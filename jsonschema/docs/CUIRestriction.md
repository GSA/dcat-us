

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

## <a name="@id"></a>Property `CUIRestriction > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `CUIRestriction > @type`

| **Type**    | `string`           |
| ----------- | ------------------ |
| **Default** | `"CUIRestriction"` |

## <a name="cuiBannerMarking"></a>Property `CUIRestriction > cuiBannerMarking`

**Title:** CUI banner marking

CUI (Controlled Unclassified Information) banner marking is required for any unclassified information that is deemed sensitive and requires protection

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="designationIndicator"></a>Property `CUIRestriction > designationIndicator`

**Title:** CUI designation indicator

Designation Indicator shows which agency made the document CUI

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="requiredIndicatorPerAuthority"></a>Property `CUIRestriction > requiredIndicatorPerAuthority`

**Title:** required indicator per authority

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

