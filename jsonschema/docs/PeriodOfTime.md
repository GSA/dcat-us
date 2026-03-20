# PeriodOfTime

**Title:** PeriodOfTime

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Information about a specific time period with a start- and/or end-time

| Property                   | Type        | Title/Description |
| -------------------------- | ----------- | ----------------- |
| - [@id](#@id )             | string      | -                 |
| - [@type](#@type )         | string      | -                 |
| - [endDate](#endDate )     | Combination | end date          |
| - [startDate](#startDate ) | Combination | start date        |

## <a name="@id"></a>Property `PeriodOfTime > @id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `iri`    |

## <a name="@type"></a>Property `PeriodOfTime > @type`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"PeriodOfTime"` |

## <a name="endDate"></a>Property `PeriodOfTime > endDate`

**Title:** end date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The end date of the period of time

| Any of(Option)              |
| --------------------------- |
| [item 0](#endDate_anyOf_i0) |
| [item 1](#endDate_anyOf_i1) |

### <a name="endDate_anyOf_i0"></a>Property `PeriodOfTime > endDate > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="endDate_anyOf_i1"></a>Property `PeriodOfTime > endDate > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#endDate_anyOf_i1_oneOf_i0) |
| [item 1](#endDate_anyOf_i1_oneOf_i1) |
| [item 2](#endDate_anyOf_i1_oneOf_i2) |
| [item 3](#endDate_anyOf_i1_oneOf_i3) |

#### <a name="endDate_anyOf_i1_oneOf_i0"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="endDate_anyOf_i1_oneOf_i1"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="endDate_anyOf_i1_oneOf_i2"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="endDate_anyOf_i1_oneOf_i3"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="startDate"></a>Property `PeriodOfTime > startDate`

**Title:** start date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The start date of the period of time

| Any of(Option)                |
| ----------------------------- |
| [item 0](#startDate_anyOf_i0) |
| [item 1](#startDate_anyOf_i1) |

### <a name="startDate_anyOf_i0"></a>Property `PeriodOfTime > startDate > anyOf > item 0`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="startDate_anyOf_i1"></a>Property `PeriodOfTime > startDate > anyOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

| One of(Option)                         |
| -------------------------------------- |
| [item 0](#startDate_anyOf_i1_oneOf_i0) |
| [item 1](#startDate_anyOf_i1_oneOf_i1) |
| [item 2](#startDate_anyOf_i1_oneOf_i2) |
| [item 3](#startDate_anyOf_i1_oneOf_i3) |

#### <a name="startDate_anyOf_i1_oneOf_i0"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="startDate_anyOf_i1_oneOf_i1"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="startDate_anyOf_i1_oneOf_i2"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year in YYYY format

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="startDate_anyOf_i1_oneOf_i3"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 3`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A year and month in YYYY-MM format

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
