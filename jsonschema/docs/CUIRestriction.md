# CUIRestriction

**Title:** CUIRestriction

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A specific restriction on handling Controlled Unclassified Information (CUI)

| Property                                                           | Type        | Title/Description                |
| ------------------------------------------------------------------ | ----------- | -------------------------------- |
| - [@id](#@id )                                                     | string      | -                                |
| - [@type](#@type )                                                 | string      | -                                |
| + [cuiBannerMarking](#cuiBannerMarking )                           | string      | CUI banner marking               |
| + [designationIndicator](#designationIndicator )                   | string      | CUI designation indicator        |
| - [requiredIndicatorPerAuthority](#requiredIndicatorPerAuthority ) | Combination | required indicator per authority |

## <a name="@id"></a>Property `CUIRestriction > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `CUIRestriction > @type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `string`           |
| **Required** | No                 |
| **Default**  | `"CUIRestriction"` |

## <a name="cuiBannerMarking"></a>Property `CUIRestriction > cuiBannerMarking`

**Title:** CUI banner marking

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** CUI (Controlled Unclassified Information) banner marking is required for any unclassified information that is deemed sensitive and requires protection

## <a name="designationIndicator"></a>Property `CUIRestriction > designationIndicator`

**Title:** CUI designation indicator

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Designation Indicator shows which agency made the document CUI

## <a name="requiredIndicatorPerAuthority"></a>Property `CUIRestriction > requiredIndicatorPerAuthority`

**Title:** required indicator per authority

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** List of free text of the required indicator

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#requiredIndicatorPerAuthority_anyOf_i0) |
| [item 1](#requiredIndicatorPerAuthority_anyOf_i1) |

### <a name="requiredIndicatorPerAuthority_anyOf_i0"></a>Property `CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="requiredIndicatorPerAuthority_anyOf_i1"></a>Property `CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [item 1 items](#requiredIndicatorPerAuthority_anyOf_i1_items) | -           |

#### <a name="requiredIndicatorPerAuthority_anyOf_i1_items"></a>CUIRestriction > requiredIndicatorPerAuthority > anyOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
