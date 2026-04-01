

**Title:** PeriodOfTime

Information about a specific time period with a start- and/or end-time

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                   | Type               | Title/Description |
| -------------------------- | ------------------ | ----------------- |
| - [@id](#@id )             | string             | -                 |
| - [@type](#@type )         | string             | -                 |
| - [endDate](#endDate )     | More than one type | end date          |
| - [startDate](#startDate ) | More than one type | start date        |

## <a name="@id"></a>Property `PeriodOfTime > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `PeriodOfTime > @type`

| **Type**    | `string`         |
| ----------- | ---------------- |
| **Default** | `"PeriodOfTime"` |

## <a name="endDate"></a>Property `PeriodOfTime > endDate`

**Title:** end date

The end date of the period of time

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                      |
| --------------------------------------------------- |
| [Null allowed when not required](#endDate_anyOf_i0) |
| [item 1](#endDate_anyOf_i1)                         |

### <a name="endDate_anyOf_i0"></a>Property `PeriodOfTime > endDate > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="endDate_anyOf_i1"></a>Property `PeriodOfTime > endDate > anyOf > item 1`

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#endDate_anyOf_i1_oneOf_i0) |
| [item 1](#endDate_anyOf_i1_oneOf_i1) |
| [item 2](#endDate_anyOf_i1_oneOf_i2) |
| [item 3](#endDate_anyOf_i1_oneOf_i3) |

#### <a name="endDate_anyOf_i1_oneOf_i0"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="endDate_anyOf_i1_oneOf_i1"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="endDate_anyOf_i1_oneOf_i2"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="endDate_anyOf_i1_oneOf_i3"></a>Property `PeriodOfTime > endDate > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="startDate"></a>Property `PeriodOfTime > startDate`

**Title:** start date

The start date of the period of time

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#startDate_anyOf_i0) |
| [item 1](#startDate_anyOf_i1)                         |

### <a name="startDate_anyOf_i0"></a>Property `PeriodOfTime > startDate > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="startDate_anyOf_i1"></a>Property `PeriodOfTime > startDate > anyOf > item 1`

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| One of(Option)                         |
| -------------------------------------- |
| [item 0](#startDate_anyOf_i1_oneOf_i0) |
| [item 1](#startDate_anyOf_i1_oneOf_i1) |
| [item 2](#startDate_anyOf_i1_oneOf_i2) |
| [item 3](#startDate_anyOf_i1_oneOf_i3) |

#### <a name="startDate_anyOf_i1_oneOf_i0"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="startDate_anyOf_i1_oneOf_i1"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="startDate_anyOf_i1_oneOf_i2"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="startDate_anyOf_i1_oneOf_i3"></a>Property `PeriodOfTime > startDate > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

