# Executive Decision Record Operations

**Implementation ID:** `ADM-ORG-DER-OPS-001`  
**Implements:** `ADM-ORG-DER-001 — Executive Decision Record & Exception System`  
**Maturity:** `CANDIDATE`  
**Authority:** implementation guidance only; it does not replace the human canon or source records.

## Purpose

This operational layer makes the DEC/EXC/RSK/DSS registry machine-checkable and consumable by executive tooling without transferring substantive decision authority to software or agents.

It provides four capabilities:

1. stable next-ID calculation;
2. structural and cross-record integrity validation;
3. review/expiry diagnostics;
4. generation of a non-authoritative Control Center read model.

## Source-of-truth rule

Actual records under `records/decisions/`, `records/exceptions/`, `records/risks/` and `records/dissent/` remain the authoritative machine-readable objects for this registry. Generated snapshots, dashboards and summaries are projections and must always preserve stable record IDs.

The templates under `records/_templates/` are not actual decisions and are intentionally excluded from ID allocation, validation and analytics.

## Local setup

```bash
python -m pip install -r tools/requirements.txt
```

GitHub Actions are not required. Local execution with retained evidence is an acceptable validation path under repository governance.

## Commands

### Validate the registry

```bash
python tools/decision_registry.py validate
```

For reproducible historical/audit checks:

```bash
python tools/decision_registry.py validate --today 2026-08-25
```

`ERROR` findings fail validation. `WARNING` findings report lifecycle/review conditions without silently editing the source record. `--strict` can be used when warnings must also fail a local gate.

### Allocate the next ID

```bash
python tools/decision_registry.py next-id DEC
python tools/decision_registry.py next-id EXC --year 2026
```

Supported prefixes are `DEC`, `EXC`, `RSK`, and `DSS`. IDs are monotonic within record type and year and are never inferred from filenames alone.

The command only proposes the next available ID from current repository state. The caller must still create the actual record through the governed change path. Concurrent creation must be reconciled before merge; the tool does not provide distributed locking.

### Build the Control Center projection

```bash
python tools/decision_registry.py snapshot
```

Or write a generated JSON snapshot:

```bash
python tools/decision_registry.py snapshot --output generated/control-center/executive-decisions.json
```

A snapshot is not produced when integrity errors exist. This prevents dashboards from normalizing broken or orphaned governance records into apparently valid operational data.

## Validation behavior

The validator checks, at minimum:

- known record type;
- stable ID format and type-prefix match;
- duplicate IDs;
- lifecycle status vocabulary by record type;
- confidentiality vocabulary;
- materiality vocabulary where directly represented;
- mandatory dates and core ownership fields;
- decision owner for DEC;
- approving authority for active/approved EXC;
- accepting authority and monitoring owner for accepted RSK;
- dissent acknowledgment consistency;
- required DEC linkage for EXC/RSK/DSS;
- referenced record existence;
- referenced record type consistency;
- decision review dates reached;
- expired exceptions not moved to a terminal lifecycle state;
- accepted risks whose expiry/review date has passed.

The validator deliberately does **not** determine whether a business decision was wise, whether an exception was substantively justified, whether a risk is acceptable, or whether dissent is professionally correct. Those remain governance judgments.

## Date diagnostics and lifecycle mutation

Date-based diagnostics never mutate source records automatically.

Example: when an active exception passes `expiryDate`, the tool emits `EXCEPTION_EXPIRED`. A competent owner or governed automation may then update the record to `REVIEW_DUE`, `EXPIRED`, `REVOKED`, or another authorized state based on actual circumstances.

This separation prevents a clock from fabricating a governance decision.

## Relationship integrity

`DEC` is the primary event. `EXC`, `RSK`, and `DSS` must resolve to an actual DEC record unless a future approved standard explicitly expands the governed source types.

DEC back-links (`linkedExceptions`, `linkedRiskAcceptances`, `linkedDissent`) are also validated when present. Missing reverse links are not currently treated as errors because the source contract permits bidirectional lineage "when tooling allows"; this can be strengthened after real usage evidence.

## Material dissent projection

DSS currently does not carry its own materiality field in the canonical template. For the read model, material dissent inherits the materiality context of its linked DEC. This is a projection rule only and does not rewrite the DSS source record.

## Read-model contract

The dashboard contract is versioned at:

`registry/dashboards/executive-decisions.yaml`

The generated JSON includes:

- headline counts;
- open decisions;
- decisions awaiting input;
- review/expiry due records;
- active exceptions;
- accepted risks awaiting review;
- material dissent linked to material decisions;
- decisions lacking execution outcome evidence;
- validation findings.

Protected source evidence is intentionally omitted from the general projection. Only metadata necessary for navigation and governance status should appear unless a later access-control design authorizes more.

## Operational sequence for a new real record

1. Determine that a qualifying governance event actually exists under `ADM-ORG-DER-001`.
2. Run `next-id` for the required record type.
3. Copy the matching template into the appropriate actual-record folder and replace placeholders with real evidence.
4. Run `validate` locally.
5. Correct all integrity errors; review warnings explicitly.
6. Submit through the repository's branch/PR process.
7. After merge, regenerate the read model when needed.
8. Preserve validation output or equivalent evidence with the change/audit context when material.

## Non-authority principle

Tool access, commit rights, file creation and automated validation do not imply decision authority. The tooling may draft, validate, identify broken relationships, surface review conditions and build projections. It may not fabricate decision ownership, approval, exception authorization, risk acceptance or dissent.

## Calibration trigger

After the first real DEC/EXC/RSK/DSS records exist, review this implementation against observed usage. Candidate questions include whether reverse links should become mandatory, whether review states should be machine-transitionable under pre-authorization, whether schemas should become stricter, and which read-model fields are genuinely useful to the Control Center.
