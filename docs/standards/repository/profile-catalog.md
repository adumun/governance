# ADÜMÜN Repository Standard Profiles

Status: **CANDIDATE SUCCESSOR / MIGRATED FROM LEGACY**

Predecessor: `cmartinezs/the-x-contract-registry/standards/profile-catalog.md` (blob `2c61420b5d884e12d18e2813d5faecd8fd9ba7c3`).

A repository adopts `RS-CORE` plus every profile that reflects a real concern it owns. Profiles are composable and non-exclusive. Repository classification, initiative lifecycle, capability maturity and business-unit hierarchy remain separate dimensions.

## Profiles

- `RS-GOV` — Governance & Initiative: lifecycle/governance artifacts, standards, policy, decisions, risks, evidence or portfolio metadata.
- `RS-CONTRACT` — Contract Provider / Machine Interface: schemas, manifests, events, DTOs, projections, protocols and other machine-consumed contracts. Canonical machine semantics live in `adumun/machine-contracts`; this profile governs adoption and repository obligations.
- `RS-PRODUCT` — Product / Application: business/user-facing products.
- `RS-SERVICE` — Backend / API / Worker Service. `RS-API` is a documentation alias only and MUST NOT be persisted as a canonical adopted ID.
- `RS-FRONTEND` — UI / Client.
- `RS-MONOREPO` — Multi-component Repository.
- `RS-CAPABILITY` — Shared Capability.
- `RS-LIBRARY` — Reusable Package / SDK.
- `RS-TOOLING` — CLI / Plugin / Automation Runtime.
- `RS-AI` — AI / Agentic Repository.
- `RS-DATA` — Data / Persistence / Migration.
- `RS-INFRA` — Infrastructure / Deployment.
- `RS-PAGES` — GitHub Pages Publication.
- `RS-EXPERIMENT` — Experiment / PoC / Spike.
- `RS-CONTENT` — Content / Creative / Educational.
- `RS-TEMPLATE` — Template / Scaffold / Reference Architecture.
- `RS-PUBLIC` — Public / Open Repository.
- `RS-LEGACY` — Deprecated / Superseded / Archived Repository.

## Cross-profile obligations

Every applicable profile inherits `RS-CORE`. Profiles add constraints; they do not silently weaken higher-level requirements. A repository may adopt multiple profiles simultaneously.

Common obligations include explicit bounded context and authority, deterministic validation where machine-consumed interfaces exist, explicit ownership and consumers, versioned compatibility where consumers depend on a contract, secrets/privacy boundaries, traceable evidence, and explicit deprecation/lineage rather than destructive replacement.

## Legacy profile semantics retained

The following legacy principles remain normative candidates pending formal promotion:

- `RS-GOV`: stable IDs, explicit provenance, no inferred gate pass, generated views non-authoritative.
- `RS-CONTRACT`: one semantic authority per contract, stable ID/version, fixtures, deterministic validation, producer/consumer registry, breaking-change policy.
- `RS-CAPABILITY`: reuse must be evidence-based; capability maturity is distinct from initiative lifecycle.
- `RS-TOOLING`: dry-run/propose/apply separation for consequential actions, idempotency, deterministic verification, explicit unsupported behavior.
- `RS-AI`: provider/model adapters do not redefine domain semantics; prompts and structured outputs are versioned when material.
- `RS-DATA`: canonical owner, migrations, retention/privacy, lineage.
- `RS-INFRA`: reproducibility, least privilege, cost visibility, rollback.
- `RS-LEGACY`: successor explicit, new consumers disallowed, history preserved, archive only after migration evidence.

## Adoption declaration

Repository-local adoption SHOULD be machine-readable when useful. Minimum logical shape:

```yaml
repositoryStandards:
  framework: ADUMUN
  profiles:
    - id: RS-CORE
      adoption: REQUIRED
    - id: RS-CONTRACT
      adoption: APPLICABLE
```

Allowed adoption values: `REQUIRED | APPLICABLE | RECOMMENDED | NOT_APPLICABLE | DEFERRED`.

The canonical profile registry is `registry/standards.yaml` in this repository.