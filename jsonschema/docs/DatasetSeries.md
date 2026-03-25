

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

## <a name="@id"></a>Property `@id`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="@type"></a>Property `@type`

|             |                   |
| ----------- | ----------------- |
| **Type**    | `string`          |
| **Default** | `"DatasetSeries"` |

## <a name="contactPoint"></a>Property `contactPoint`

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

### <a name="contactPoint_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="contactPoint_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#contactPoint_anyOf_i1_items) | -           |

#### <a name="contactPoint_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                  |
| ----------------------------------------------- |
| [Kind](#contactPoint_anyOf_i1_items_oneOf_i0)   |
| [item 1](#contactPoint_anyOf_i1_items_oneOf_i1) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i0"></a>Property `Kind`

**Title:** Kind

inline description of the contact

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Additional properties** | Any type allowed  |
| **Defined in**            | [Kind](./Kind.md) |

##### <a name="contactPoint_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the contact

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="first"></a>Property `first`

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

### <a name="first_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="first_oneOf_i1"></a>Property `Dataset`

**Title:** Dataset

inline description of the first dataset

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Additional properties** | Any type allowed        |
| **Defined in**            | [Dataset](./Dataset.md) |

### <a name="first_oneOf_i2"></a>Property `item 2`

reference iri of the first dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="last"></a>Property `last`

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

### <a name="last_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="last_oneOf_i1"></a>Property `Dataset`

**Title:** Dataset

inline description of the last dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

### <a name="last_oneOf_i2"></a>Property `item 2`

reference iri of the last dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="seriesMember"></a>Property `seriesMember`

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

### <a name="seriesMember_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="seriesMember_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [item 1 items](#seriesMember_anyOf_i1_items) | -           |

#### <a name="seriesMember_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [Dataset](#seriesMember_anyOf_i1_items_oneOf_i0) |
| [item 1](#seriesMember_anyOf_i1_items_oneOf_i1)  |

##### <a name="seriesMember_anyOf_i1_items_oneOf_i0"></a>Property `Dataset`

**Title:** Dataset

inline description of the member dataset

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Additional properties** | Any type allowed           |
| **Same definition as**    | [Dataset](#first_oneOf_i1) |

##### <a name="seriesMember_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of the member dataset

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="accrualPeriodicity"></a>Property `accrualPeriodicity`

**Title:** frequency

The frequency at which the Dataset Series is updated

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#accrualPeriodicity_oneOf_i0)    |
| [frequency](#accrualPeriodicity_oneOf_i1) |
| [item 2](#accrualPeriodicity_oneOf_i2)    |

### <a name="accrualPeriodicity_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="accrualPeriodicity_oneOf_i1"></a>Property `frequency`

inline description of Frequency

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Additional properties** | Any type allowed            |
| **Defined in**            | [Frequency](./Frequency.md) |

### <a name="accrualPeriodicity_oneOf_i2"></a>Property `item 2`

reference iri of Frequency

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="description"></a>Property `description`

**Title:** description

A free-text account of the Dataset Series

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="descriptionMap"></a>Property `descriptionMap`

Language map for description. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

## <a name="issued"></a>Property `issued`

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

### <a name="issued_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="issued_anyOf_i1"></a>Property `item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#issued_anyOf_i1_oneOf_i0) |
| [item 1](#issued_anyOf_i1_oneOf_i1) |
| [item 2](#issued_anyOf_i1_oneOf_i2) |
| [item 3](#issued_anyOf_i1_oneOf_i3) |

#### <a name="issued_anyOf_i1_oneOf_i0"></a>Property `item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i1"></a>Property `item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="issued_anyOf_i1_oneOf_i2"></a>Property `item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="issued_anyOf_i1_oneOf_i3"></a>Property `item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="modified"></a>Property `modified`

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

### <a name="modified_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="modified_anyOf_i1"></a>Property `item 1`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#modified_anyOf_i1_oneOf_i0) |
| [item 1](#modified_anyOf_i1_oneOf_i1) |
| [item 2](#modified_anyOf_i1_oneOf_i2) |
| [item 3](#modified_anyOf_i1_oneOf_i3) |

#### <a name="modified_anyOf_i1_oneOf_i0"></a>Property `item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date-time`      |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i1"></a>Property `item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Format**                | `date`           |
| **Additional properties** | Any type allowed |

#### <a name="modified_anyOf_i1_oneOf_i2"></a>Property `item 2`

A year in YYYY format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D%24) |

#### <a name="modified_anyOf_i1_oneOf_i3"></a>Property `item 3`

A year and month in YYYY-MM format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Restrictions                      |                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[0-9]{4}-[0-9]{2}$``` [Test](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%5B0-9%5D%7B2%7D%24) |

## <a name="publisher"></a>Property `publisher`

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

### <a name="publisher_oneOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="publisher_oneOf_i1"></a>Property `Agent`

**Title:** Agent

inline description of publisher

|                           |                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                              |
| **Same definition as**    | [Agent](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_creator_anyOf_i1_items_oneOf_i0) |

### <a name="publisher_oneOf_i2"></a>Property `item 2`

reference iri of publisher

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="spatial"></a>Property `spatial`

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

### <a name="spatial_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="spatial_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 1 items](#spatial_anyOf_i1_items) | -           |

#### <a name="spatial_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                               |
| -------------------------------------------- |
| [Location](#spatial_anyOf_i1_items_oneOf_i0) |
| [item 1](#spatial_anyOf_i1_items_oneOf_i1)   |

##### <a name="spatial_anyOf_i1_items_oneOf_i0"></a>Property `Location`

**Title:** Location

inline description of Location

|                           |                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                         |
| **Additional properties** | Any type allowed                                                                                                                 |
| **Same definition as**    | [Location](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_spatial_anyOf_i1_items_oneOf_i0) |

##### <a name="spatial_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of Location

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="temporal"></a>Property `temporal`

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

### <a name="temporal_anyOf_i0"></a>Property `item 0`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="temporal_anyOf_i1"></a>Property `item 1`

|          |         |
| -------- | ------- |
| **Type** | `array` |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 1 items](#temporal_anyOf_i1_items) | -           |

#### <a name="temporal_anyOf_i1_items"></a>item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| One of(Option)                                    |
| ------------------------------------------------- |
| [PeriodOfTime](#temporal_anyOf_i1_items_oneOf_i0) |
| [item 1](#temporal_anyOf_i1_items_oneOf_i1)       |

##### <a name="temporal_anyOf_i1_items_oneOf_i0"></a>Property `PeriodOfTime`

**Title:** PeriodOfTime

inline description of PeriodOfTime

|                           |                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                              |
| **Additional properties** | Any type allowed                                                                                                                      |
| **Same definition as**    | [PeriodOfTime](#first_oneOf_i1_sample_anyOf_i1_items_oneOf_i0_accessService_anyOf_i1_items_oneOf_i0_temporal_anyOf_i1_items_oneOf_i0) |

##### <a name="temporal_anyOf_i1_items_oneOf_i1"></a>Property `item 1`

reference iri of PeriodOfTime

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `iri`    |

## <a name="title"></a>Property `title`

**Title:** title

A name given to the Dataset Series

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="titleMap"></a>Property `titleMap`

Language map for property title. E.g. {'es': 'spanish words', 'fr': 'french words'}

|          |                  |
| -------- | ---------------- |
| **Type** | `null or object` |

