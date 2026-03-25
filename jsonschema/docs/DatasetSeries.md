

**Title:** DatasetSeries

An ordered series of datasets

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                     | Type               | Title/Description                                                                   |
| -------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| - [@id](#@id )                               | string             | -                                                                                   |
| - [@type](#@type )                           | string             | -                                                                                   |
| - [contactPoint](#contactPoint )             | More than one type | contact point                                                                       |
| - [first](#first )                           | More than one type | first                                                                               |
| - [last](#last )                             | More than one type | last                                                                                |
| - [seriesMember](#seriesMember )             | More than one type | series member                                                                       |
| - [accrualPeriodicity](#accrualPeriodicity ) | More than one type | frequency                                                                           |
| + [description](#description )               | string             | description                                                                         |
| - [descriptionMap](#descriptionMap )         | null or object     | Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}    |
| - [issued](#issued )                         | More than one type | release date                                                                        |
| - [modified](#modified )                     | More than one type | update/modification date                                                            |
| - [publisher](#publisher )                   | More than one type | publisher                                                                           |
| - [spatial](#spatial )                       | More than one type | spatial/geographic coverage                                                         |
| - [temporal](#temporal )                     | More than one type | temporal coverage                                                                   |
| + [title](#title )                           | string             | title                                                                               |
| - [titleMap](#titleMap )                     | null or object     | Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'} |

## <a name="@id"></a>Property `DatasetSeries > @id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `DatasetSeries > @type`

|             |                   |
| ----------- | ----------------- |
| **Type**    | `string`          |
| **Default** | `"DatasetSeries"` |

## <a name="contactPoint"></a>Property `DatasetSeries > contactPoint`

**Title:** contact point

List of contacts that can be used for sending comments about the Dataset Series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#contactPoint_anyOf_i0) |
| [item 1](#contactPoint_anyOf_i1) |

### <a name="contactPoint_anyOf_i0"></a>Property `DatasetSeries > contactPoint > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="contactPoint_anyOf_i1"></a>Property `DatasetSeries > contactPoint > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items) | -           |

#### <a name="contactPoint_anyOf_i1_items"></a>DatasetSeries > contactPoint > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Kind](#contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i1) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > Kind`

**Title:** Kind

inline description of the contact

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > contactPoint > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of the contact

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="first"></a>Property `DatasetSeries > first`

**Title:** first

The first dataset in an ordered dataset series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)             |
| -------------------------- |
| [item 0](#first_oneOf_i0)  |
| [Dataset](#first_oneOf_i1) |
| [item 2](#first_oneOf_i2)  |

### <a name="first_oneOf_i0"></a>Property `DatasetSeries > first > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="first_oneOf_i1"></a>Property `DatasetSeries > first > oneOf > Dataset`

**Title:** Dataset

inline description of the first dataset

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

### <a name="first_oneOf_i2"></a>Property `DatasetSeries > first > oneOf > item 2`

reference iri of the first dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="last"></a>Property `DatasetSeries > last`

**Title:** last

The last dataset in an ordered dataset series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)            |
| ------------------------- |
| [item 0](#last_oneOf_i0)  |
| [Dataset](#last_oneOf_i1) |
| [item 2](#last_oneOf_i2)  |

### <a name="last_oneOf_i0"></a>Property `DatasetSeries > last > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="last_oneOf_i1"></a>Property `DatasetSeries > last > oneOf > Dataset`

**Title:** Dataset

inline description of the last dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

### <a name="last_oneOf_i2"></a>Property `DatasetSeries > last > oneOf > item 2`

reference iri of the last dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="seriesMember"></a>Property `DatasetSeries > seriesMember`

**Title:** series member

List of members of the Dataset Series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#seriesMember_anyOf_i0) |
| [item 1](#seriesMember_anyOf_i1) |

### <a name="seriesMember_anyOf_i0"></a>Property `DatasetSeries > seriesMember > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="seriesMember_anyOf_i1"></a>Property `DatasetSeries > seriesMember > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#seriesMember_anyOf_i1_items) | -           |

#### <a name="seriesMember_anyOf_i1_items"></a>DatasetSeries > seriesMember > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [Dataset](#seriesMember_anyOf_i1_items_oneOf_i0) |
| [item 1](#seriesMember_anyOf_i1_items_oneOf_i1)  |

##### <a name="seriesMember_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > Dataset`

**Title:** Dataset

inline description of the member dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

##### <a name="seriesMember_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > seriesMember > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of the member dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accrualPeriodicity"></a>Property `DatasetSeries > accrualPeriodicity`

**Title:** frequency

The frequency at which the Dataset Series is updated

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)                         |
| -------------------------------------- |
| [item 0](#accrualPeriodicity_anyOf_i0) |
| [item 1](#accrualPeriodicity_anyOf_i1) |
| [item 2](#accrualPeriodicity_anyOf_i2) |
| [item 3](#accrualPeriodicity_anyOf_i3) |

### <a name="accrualPeriodicity_anyOf_i0"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accrualPeriodicity_anyOf_i1"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > item 1`

ISO 19115 Maintenance Frequency code, see https://infopolicy.github.io/dcat-us/#frequency-coding

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

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

|          |          |
| -------- | -------- |
| **Type** | `string` |

| Restrictions                      |                                                                   |
| --------------------------------- | ----------------------------------------------------------------- |
| **Must match regular expression** | ```^R/P.+$``` [Test](https://regex101.com/?regex=%5ER%2FP.%2B%24) |

### <a name="accrualPeriodicity_anyOf_i3"></a>Property `DatasetSeries > accrualPeriodicity > anyOf > item 3`

Dublin Core Collection Frequency Vocabulary, see https://infopolicy.github.io/dcat-us/#frequency-coding

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

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

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="descriptionMap"></a>Property `DatasetSeries > descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="issued"></a>Property `DatasetSeries > issued`

**Title:** release date

The date of formal issuance (e.g.,publication) of the Dataset Series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)             |
| -------------------------- |
| [item 0](#issued_anyOf_i0) |
| [item 1](#issued_anyOf_i1) |

### <a name="issued_anyOf_i0"></a>Property `DatasetSeries > issued > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="issued_anyOf_i1"></a>Property `DatasetSeries > issued > anyOf > item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > issued > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `DatasetSeries > modified`

**Title:** update/modification date

The most recent date on which the Dataset Series was changed or modified

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#modified_anyOf_i0) |
| [item 1](#modified_anyOf_i1) |

### <a name="modified_anyOf_i0"></a>Property `DatasetSeries > modified > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="modified_anyOf_i1"></a>Property `DatasetSeries > modified > anyOf > item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `DatasetSeries > modified > anyOf > item 1 > oneOf > item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `DatasetSeries > publisher`

**Title:** publisher

An entity (organization) responsible for ensuring the coherency of the Dataset Series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                |
| ----------------------------- |
| [item 0](#publisher_oneOf_i0) |
| [Agent](#publisher_oneOf_i1)  |
| [item 2](#publisher_oneOf_i2) |

### <a name="publisher_oneOf_i0"></a>Property `DatasetSeries > publisher > oneOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="publisher_oneOf_i1"></a>Property `DatasetSeries > publisher > oneOf > Agent`

**Title:** Agent

inline description of publisher

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

### <a name="publisher_oneOf_i2"></a>Property `DatasetSeries > publisher > oneOf > item 2`

reference iri of publisher

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `DatasetSeries > spatial`

**Title:** spatial/geographic coverage

A geographic region that is covered by the Dataset Series

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)              |
| --------------------------- |
| [item 0](#spatial_anyOf_i0) |
| [item 1](#spatial_anyOf_i1) |

### <a name="spatial_anyOf_i0"></a>Property `DatasetSeries > spatial > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="spatial_anyOf_i1"></a>Property `DatasetSeries > spatial > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#spatial_anyOf_i1_items) | -           |

#### <a name="spatial_anyOf_i1_items"></a>DatasetSeries > spatial > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#spatial_anyOf_i1_items_oneOf_i1)   |

##### <a name="spatial_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > Location`

**Title:** Location

inline description of Location

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > spatial > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of Location

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `DatasetSeries > temporal`

**Title:** temporal coverage

A list of temporal periods that the Dataset Series covers

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| Any of(Option)               |
| ---------------------------- |
| [item 0](#temporal_anyOf_i0) |
| [item 1](#temporal_anyOf_i1) |

### <a name="temporal_anyOf_i0"></a>Property `DatasetSeries > temporal > anyOf > item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="temporal_anyOf_i1"></a>Property `DatasetSeries > temporal > anyOf > item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>DatasetSeries > temporal > anyOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#temporal_anyOf_i1_items_oneOf_i1)       |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > PeriodOfTime`

**Title:** PeriodOfTime

inline description of PeriodOfTime

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [PeriodOfTime](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `DatasetSeries > temporal > anyOf > item 1 > item 1 items > oneOf > item 1`

reference iri of PeriodOfTime

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `DatasetSeries > title`

**Title:** title

A name given to the Dataset Series

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `DatasetSeries > titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

