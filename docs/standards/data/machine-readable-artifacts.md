# Machine-Readable Artifacts & Lightweight Data Architecture

Maturity: CANDIDATE  
Version: 0.1.0

## Principle
ADÜMÜN uses a file-first, schema-governed, evidence-driven data architecture until evidence justifies a backend/database.

## Default formats
- YAML: human-maintained registries/configuration/state.
- JSON Schema: validation contracts and structural guarantees.
- JSON: generated exports, snapshots, events and interchange.
- Google Sheets: live human-operable tabular state and dashboards.
- Google Docs: narrative authority/context.
- GitHub: versioning of schemas, registries, templates and executable governance.

## Common fields
Authority-bearing records SHOULD include where applicable:
`schema_version`, `id`, `type`, `name`, `maturity`, `status`, `owner_domain`, `source_of_truth`, `last_reviewed`/`updated_at`, `evidence_refs`, `relationships`.

## Identifier conventions
Stable immutable IDs use uppercase domain prefixes such as:
`INIT-`, `OFFER-`, `CAP-`, `PROV-`, `BRAND-`, `OPP-`, `EVID-`, `M-F-`, `CHANNEL-`, `RISK-`, `DEC-`, `WORK-`.

## Value conventions
- fields: `lower_snake_case`
- enums: `UPPER_SNAKE_CASE`
- date: ISO 8601 `YYYY-MM-DD`
- timestamps: ISO 8601 with timezone
- CLP amounts: integers unless a different unit is explicitly declared
- unknown numeric value: `null`, never `0`
- booleans: JSON/YAML booleans
- status: governed vocabulary, not ad-hoc prose

## Schema governance
Every domain registry declares a schema/version. Breaking structural changes increment major version; backward-compatible additions increment minor version. Validation must run locally. GitHub Actions are optional and never the only validation path.

## Source of truth
Machine-readable representations identify their source of truth and maturity. They do not silently override human authority. If a structured registry becomes operational authority, an applicable human standard/canon must explicitly assign that role.

## Dashboard rule
Dashboards derive from structured registries/Sheets, not manual interpretation of narrative documents. Every metric declares source fields, formulas, null handling and inclusion criteria.

## Backend/database adoption gate
Introduce a backend/database only when recorded evidence demonstrates file-first limitations in scale, concurrency, transactions, query complexity, latency, access control, workflow automation or integrations. Record observed limitation, affected workflows, frequency/scale, workaround cost, required properties, expected value and migration/exit path.

## Minimum validation
Validate parseability, schema conformance, unique IDs, enum values, referential integrity, null handling and `source_of_truth` for authority-bearing records.
