THIS IS A DRAFT to be discussed and edited as needed by the CDO Tiger Team and the Data.gov team.

# Maintenance

DCAT-US v3.0 follows a semi-annual maintenance cycle covering schema governance, documentation, and agency communication. This document describes the process.

The CDO Tiger Team governs schema changes. The Data.gov team at GSA maintains this repository and coordinates the maintenance cycle. Major version changes (e.g., v4.0) are planned separately.

---

## Continuous, issue triage

Issues are triaged on a rolling basis as they are submitted, rather than batched to a specific time of year. The Data.gov team applies a classification label to each new issue within two weeks of submission:

- `bug` -- the schema behaves incorrectly or inconsistently with the specification
- `enhancement` -- a proposed addition or improvement to the schema
- `question` -- a request for clarification on schema intent or behavior

Issues approved for an upcoming release are assigned to the corresponding milestone. Issues received via Zendesk or CDO Council channels that are not yet on GitHub are cross-filed by the Data.gov team.

---

## Cycle 1: spring release (March/April)

### Schema review

- Tiger Team reviews issues in the Cycle 1 milestone and assigns a disposition: approved for PR, deferred, or closed as won't fix
- PRs are opened for approved non-breaking changes
- Breaking changes approved in Cycle 1 are deferred to Cycle 2 at the earliest, with a deprecation notice issued in Cycle 1 outreach (minimum 90-day agency implementation window required)
- Schema changes touching `accessRestriction`, `useRestriction`, or `cuiRestriction` fields must include a security considerations note in the PR

### Documentation

- Resolve all P1 (critical) documentation issues on resources.data.gov
- Validate all example records in documentation against the current schema
- Audit all DCAT-US pages on resources.data.gov against the live schema; file issues for any pages that are out of sync

### Release

- Merge approved PRs into the main branch
- Tag a point release using semantic versioning (e.g. v3.1)
- Include a changelog entry describing all changes in the release tag
- Confirm with the schema team whether the `conformsTo` URI requires updating for the new version

### Agency outreach

- Publish release notes to the CDO Council channel, Data.gov mailing list, and as GitHub release notes within two weeks of the release tag
- Include a 90-day grace period before any new requirements are enforced
- Note any deprecation notices for changes planned for Cycle 2

---

## Cycle 2: summer release and retrospective (July)

The July release aligns with the M-25-05 annual compliance reference date. Cycle 2 also includes the annual retrospective.

### Schema review

- Tiger Team reviews issues in the Cycle 2 milestone and assigns a disposition: approved for PR, deferred, or closed as won't fix
- PRs are opened for approved non-breaking changes
- Breaking changes approved in Cycle 1 with a prior deprecation notice may be included in this release
- Schema changes touching `accessRestriction`, `useRestriction`, or `cuiRestriction` fields must include a security considerations note in the PR

### Documentation

- Resolve all P1 and P2 documentation issues on resources.data.gov
- Publish updated migration guidance within 30 days of release if any field-level changes affect existing data.json implementations
- Update the changelog on resources.data.gov

### Release

- Merge approved PRs into the main branch
- Tag a point release using semantic versioning (e.g. v3.2)
- Include a changelog entry describing all changes in the release tag
- Confirm with the schema team whether the `conformsTo` URI requires updating for the new version

### Agency outreach

- Publish release notes to the CDO Council channel, Data.gov mailing list, and as GitHub release notes within two weeks of the release tag
- Include a 90-day grace period before any new requirements are enforced
- Host or contribute to a CDO Council touchpoint to collect agency implementation questions and blockers for schema team awareness

### Annual retrospective

- Review harvest validation error trends for the year using New Relic data
- Identify systemic field-level error patterns that may warrant schema clarification or guidance updates; file issues as needed
- Publish an annual compliance summary identifying agency cohorts that may benefit from targeted implementation assistance; share with the CDO Tiger Team
- The compliance summary is an implementation support tool, not an enforcement document
- Document lessons learned and priorities for the next annual cycle

---

## Change types and release rules

| Change type | Example | Earliest release | Notice required |
|---|---|---|---|
| Non-breaking addition | New optional field | Next cycle | None |
| Non-breaking clarification | Updated field description | Next cycle | None |
| Breaking change | Removed field, changed enum | Cycle after notice | Deprecation notice in prior cycle outreach |

Breaking changes require a minimum 90-day agency implementation window before enforcement.

---

## How to submit a change request

Open an issue on this repository using one of the labels above. Issues are triaged on a rolling basis. The Tiger Team reviews prioritized issues at each cycle.

If you have a time-sensitive issue, note that in the issue body. For questions about Data.gov harvesting or the resources.data.gov documentation, email [datagovhelp@gsa.gov](mailto:datagovhelp@gsa.gov).

---

## Governance

DCAT-US v3.0 is governed by the Federal Chief Data Officers Council Tiger Team in collaboration with the Data.gov team at GSA. The schema was developed collaboratively with the Federal Committee on Statistical Methodology and reflects more than a decade of implementation experience with DCAT-US v1.1.

Questions about the governance process can be directed to [datagovhelp@gsa.gov](mailto:datagovhelp@gsa.gov).
