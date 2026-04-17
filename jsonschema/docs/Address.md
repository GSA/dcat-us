

**Title:** Address

A single physical address

| **Type**                  | `object`         |
| ------------------------- | ---------------- |
| **Additional properties** | Any type allowed |

**Example:**

```json
{
    "@type": "Address",
    "street-address": "151 Patton Avenue",
    "locality": "Asheville",
    "region": "NC",
    "postal-code": "28801",
    "country-name": "United States"
}
```

| Property                             | Type           | Title/Description   |
| ------------------------------------ | -------------- | ------------------- |
| - [@id](#@id )                       | string         | -                   |
| - [@type](#@type )                   | string         | -                   |
| - [country-name](#country-name )     | null or string | country             |
| - [locality](#locality )             | null or string | locality            |
| - [postal-code](#postal-code )       | null or string | postal code         |
| - [region](#region )                 | null or string | administrative area |
| - [street-address](#street-address ) | null or string | street address      |

## <a name="@id"></a>[Optional] Property `Address > @id`

**Requirement:** Optional

| **Type**   | `string` |
| ---------- | -------- |
| **Format** | `iri`    |

**Example:**

```json
"https://example.gov/addresses/hq-001"
```

## <a name="@type"></a>[Optional] Property `Address > @type`

**Requirement:** Optional

| **Type**    | `string`    |
| ----------- | ----------- |
| **Default** | `"Address"` |

## <a name="country-name"></a>[Optional] Property `Address > country-name`

**Title:** country

**Requirement:** Optional

The country of the Address

| **Type** | `null or string` |
| -------- | ---------------- |

**Example:**

```json
"United States"
```

## <a name="locality"></a>[Optional] Property `Address > locality`

**Title:** locality

**Requirement:** Optional

The city of the Address

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"Asheville"
```

```json
"Washington"
```

## <a name="postal-code"></a>[Optional] Property `Address > postal-code`

**Title:** postal code

**Requirement:** Optional

The postal code of the Address

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"28801"
```

```json
"20230"
```

## <a name="region"></a>[Optional] Property `Address > region`

**Title:** administrative area

**Requirement:** Optional

The administrative area of the Address. Depending on the country, this corresponds to a province, a county, a region, or a state

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"NC"
```

```json
"DC"
```

## <a name="street-address"></a>[Optional] Property `Address > street-address`

**Title:** street address

**Requirement:** Optional

The street name and civic number of an Address

| **Type** | `null or string` |
| -------- | ---------------- |

**Examples:**

```json
"151 Patton Avenue"
```

```json
"1401 Constitution Ave NW"
```

