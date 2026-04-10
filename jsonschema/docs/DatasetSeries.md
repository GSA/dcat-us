

**Title:** DatasetSeries

An ordered series of datasets

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

| Property                                     | Type               | Title/Description           |
| -------------------------------------------- | ------------------ | --------------------------- |
| - [@id](#@id )                               | string             | -                           |
| - [@type](#@type )                           | string             | -                           |
| - [contactPoint](#contactPoint )             | null or array      | contact point               |
| - [first](#first )                           | More than one type | first                       |
| - [last](#last )                             | More than one type | last                        |
| - [seriesMember](#seriesMember )             | null or array      | series member               |
| - [accrualPeriodicity](#accrualPeriodicity ) | More than one type | frequency                   |
| + [description](#description )               | string             | description                 |
| - [issued](#issued )                         | More than one type | release date                |
| - [modified](#modified )                     | More than one type | update/modification date    |
| - [publisher](#publisher )                   | More than one type | publisher                   |
| - [spatial](#spatial )                       | null or array      | spatial/geographic coverage |
| - [temporal](#temporal )                     | null or array      | temporal coverage           |
| + [title](#title )                           | string             | title                       |

## <a name="@id"></a>Property `DatasetSeries > @id`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

## <a name="@type"></a>Property `DatasetSeries > @type`

| **Type**    | `string`          |
| ----------- | ----------------- |
| **Default** | `"DatasetSeries"` |

## <a name="contactPoint"></a>Property `DatasetSeries > contactPoint`

**Title:** contact point

List of contacts that can be used for sending comments about the Dataset Series

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| [Kind](#contactPoint_items)     | Contact information for an individual or entity |

### <a name="contactPoint_items"></a>DatasetSeries > contactPoint > Kind

**Title:** Kind

Contact information for an individual or entity

| **Type**                  | `object`          |
| ------------------------- | ----------------- |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

## <a name="first"></a>Property `DatasetSeries > first`

**Title:** first

The first dataset in an ordered dataset series

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                    |
| ------------------------------------------------- |
| [Null allowed when not required](#first_anyOf_i0) |
| [Dataset](#first_anyOf_i1)                        |

### <a name="first_anyOf_i0"></a>Property `DatasetSeries > first > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="first_anyOf_i1"></a>Property `DatasetSeries > first > anyOf > Dataset`

**Title:** Dataset

inline description of the first dataset

| **Type**                  | `object`                |
| ------------------------- | ----------------------- |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

## <a name="last"></a>Property `DatasetSeries > last`

**Title:** last

The last dataset in an ordered dataset series

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                   |
| ------------------------------------------------ |
| [Null allowed when not required](#last_anyOf_i0) |
| [Dataset](#last_anyOf_i1)                        |

### <a name="last_anyOf_i0"></a>Property `DatasetSeries > last > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="last_anyOf_i1"></a>Property `DatasetSeries > last > anyOf > Dataset`

**Title:** Dataset

inline description of the last dataset

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_anyOf_i1) |

## <a name="seriesMember"></a>Property `DatasetSeries > seriesMember`

**Title:** series member

List of members of the Dataset Series

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                     |
| ------------------------------- | ------------------------------- |
| [Dataset](#seriesMember_items)  | Information about a set of data |

### <a name="seriesMember_items"></a>DatasetSeries > seriesMember > Dataset

**Title:** Dataset

Information about a set of data

| **Type**                  | `object`                   |
| ------------------------- | -------------------------- |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_anyOf_i1) |

## <a name="accrualPeriodicity"></a>Property `DatasetSeries > accrualPeriodicity`

**Title:** frequency

The frequency at which the Dataset Series is updated

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [Null allowed when not required](#accrualPeriodicity_anyOf_i0) |
| [item 1](#accrualPeriodicity_anyOf_i1)                         |
| [item 2](#accrualPeriodicity_anyOf_i2)                         |
| [item 3](#accrualPeriodicity_anyOf_i3)                         |

### <a name="accrualPeriodicity_anyOf_i0"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="accrualPeriodicity_anyOf_i1"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > item 1`

ISO 19115 Maintenance Frequency code, see https://infopolicy.github.io/dcat-us/#frequency-coding

| **Type** | `enum (of string)` |
| -------- | ------------------ |

Must be one of:
* "continual"
* "daily"
* "weekly"
* "fortnightly"
* "monthly"
* "quarterly"
* "biannually"
* "annually"
* "asNeeded"
* "irregular"
* "notPlanned"
* "unknown"

### <a name="accrualPeriodicity_anyOf_i2"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > item 2`

ISO-8601 Maintenance Frequency code for recurring values, see https://infopolicy.github.io/dcat-us/#frequency-coding

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                   |
| --------------------------------- | ----------------------------------------------------------------- |
| **Must match regular expression** | ```^R/P.+$``` [Test](https://regex101.com/?regex=%5ER%2FP.%2B%24) |

### <a name="accrualPeriodicity_anyOf_i3"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > item 3`

Dublin Core Collection Frequency Vocabulary, see https://infopolicy.github.io/dcat-us/#frequency-coding

| **Type** | `enum (of string)` |
| -------- | ------------------ |

Must be one of:
* "continuous"
* "daily"
* "weekly"
* "biweekly"
* "monthly"
* "quarterly"
* "semiannual"
* "annual"
* "irregular"
* "triennial"
* "biennial"
* "threeTimesAYear"
* "bimonthly"
* "semimonthly"
* "threeTimesAMonth"
* "semiweekly"
* "threeTimesAWeek"

## <a name="description"></a>Property `DatasetSeries > description`

**Title:** description

A free-text account of the Dataset Series

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

## <a name="issued"></a>Property `DatasetSeries > issued`

**Title:** release date

The date of formal issuance (e.g.,publication) of the Dataset Series

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                     |
| -------------------------------------------------- |
| [Null allowed when not required](#issued_anyOf_i0) |
| [Date string](#issued_anyOf_i1)                    |

### <a name="issued_anyOf_i0"></a>Property `DatasetSeries > issued > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="issued_anyOf_i1"></a>Property `DatasetSeries > issued > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_anyOf_i0) |
| [item 1](#issued_anyOf_i1_anyOf_i1) |
| [item 2](#issued_anyOf_i1_anyOf_i2) |
| [item 3](#issued_anyOf_i1_anyOf_i3) |

#### <a name="issued_anyOf_i1_anyOf_i0"></a>Property `DatasetSeries > issued > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="issued_anyOf_i1_anyOf_i1"></a>Property `DatasetSeries > issued > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="issued_anyOf_i1_anyOf_i2"></a>Property `DatasetSeries > issued > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_anyOf_i3"></a>Property `DatasetSeries > issued > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `DatasetSeries > modified`

**Title:** update/modification date

The most recent date on which the Dataset Series was changed or modified

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [Null allowed when not required](#modified_anyOf_i0) |
| [Date string](#modified_anyOf_i1)                    |

### <a name="modified_anyOf_i0"></a>Property `DatasetSeries > modified > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="modified_anyOf_i1"></a>Property `DatasetSeries > modified > anyOf > Date string`

**Title:** Date string

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_anyOf_i0) |
| [item 1](#modified_anyOf_i1_anyOf_i1) |
| [item 2](#modified_anyOf_i1_anyOf_i2) |
| [item 3](#modified_anyOf_i1_anyOf_i3) |

#### <a name="modified_anyOf_i1_anyOf_i0"></a>Property `DatasetSeries > modified > anyOf > Date string > anyOf > item 0`

| **Type**   | `string`    |
| ---------- | ----------- |
| **Format** | `date-time` |

#### <a name="modified_anyOf_i1_anyOf_i1"></a>Property `DatasetSeries > modified > anyOf > Date string > anyOf > item 1`

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `date`   |

#### <a name="modified_anyOf_i1_anyOf_i2"></a>Property `DatasetSeries > modified > anyOf > Date string > anyOf > item 2`

A year in YYYY format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_anyOf_i3"></a>Property `DatasetSeries > modified > anyOf > Date string > anyOf > item 3`

A year and month in YYYY-MM format

| **Type** | `string` |
| -------- | -------- |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `DatasetSeries > publisher`

**Title:** publisher

An entity (organization) responsible for ensuring the coherency of the Dataset Series

| **Type**                  | More than one type |
| ------------------------- | ------------------ |
| **Additional properties** | Any type allowed   |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [Null allowed when not required](#publisher_anyOf_i0) |
| [Agent](#publisher_anyOf_i1)                          |

### <a name="publisher_anyOf_i0"></a>Property `DatasetSeries > publisher > anyOf > Null allowed when not required`

**Title:** Null allowed when not required

| **Type** | `null` |
| -------- | ------ |

### <a name="publisher_anyOf_i1"></a>Property `DatasetSeries > publisher > anyOf > Agent`

**Title:** Agent

inline description of publisher

| **Type**                  | `object`                                                                |
| ------------------------- | ----------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                        |
| **Same definition as**    | [Agent](#first_anyOf_i1_sample_items_accessService_items_creator_items) |

## <a name="spatial"></a>Property `DatasetSeries > spatial`

**Title:** spatial/geographic coverage

A geographic region that is covered by the Dataset Series

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| [Location](#spatial_items)      | Information about a specific geographic location |

### <a name="spatial_items"></a>DatasetSeries > spatial > Location

**Title:** Location

Information about a specific geographic location

| **Type**                  | `object`                                                                   |
| ------------------------- | -------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                           |
| **Same definition as**    | [Location](#first_anyOf_i1_sample_items_accessService_items_spatial_items) |

## <a name="temporal"></a>Property `DatasetSeries > temporal`

**Title:** temporal coverage

A list of temporal periods that the Dataset Series covers

| **Type** | `null or array` |
| -------- | --------------- |

| Each item of this array must be | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| [PeriodOfTime](#temporal_items) | Information about a specific time period with a start- and/or end-time |

### <a name="temporal_items"></a>DatasetSeries > temporal > PeriodOfTime

**Title:** PeriodOfTime

Information about a specific time period with a start- and/or end-time

| **Type**                  | `object`                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Additional properties** | Any type allowed                                                                |
| **Same definition as**    | [PeriodOfTime](#first_anyOf_i1_sample_items_accessService_items_temporal_items) |

## <a name="title"></a>Property `DatasetSeries > title`

**Title:** title

A name given to the Dataset Series

| **Type**     | `string` |
| ------------ | -------- |
| **Required** | Yes      |

