# DCAT-US 3 Schema Documentation

DCAT-US 3 is a schema for metadata about data assets. It's defined as a set of
JSON Schema files divided into "classes" that specify different types of information
that could appear in the metadata.

## Catalog

The top level class for DCAT-US 3 is [Catalog](./Catalog.md) which collects
information about other data elements and information about the overall
collection such as publisher, keywords, and contact information.

## Other classes

Inside of the DCAT-US 3 catalog, other classes are used to specify the format
of a particular metadata element. Alphabetically:

- [AccessRestriction](./AccessRestriction.md)
- [Activity](./Activity.md)
- [Address](./Address.md)
- [Agent](./Agent.md)
- [Attribution](./Attribution.md)
- [Catalog](./Catalog.md)
- [CatalogRecord](./CatalogRecord.md)
- [Checksum](./Checksum.md)
- [Concept](./Concept.md)
- [ConceptScheme](./ConceptScheme.md)
- [CUIRestriction](./CUIRestriction.md)
- [DataService](./DataService.md)
- [Dataset](./Dataset.md)
- [DatasetSeries](./DatasetSeries.md)
- [Distribution](./Distribution.md)
- [Document](./Document.md)
- [Identifier](./Identifier.md)
- [Kind](./Kind.md)
- [Location](./Location.md)
- [Metric](./Metric.md)
- [Organization](./Organization.md)
- [PeriodOfTime](./PeriodOfTime.md)
- [QualityMeasurement](./QualityMeasurement.md)
- [Relationship](./Relationship.md)
- [Standard](./Standard.md)
- [UseRestriction](./UseRestriction.md)
