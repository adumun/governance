# ADÜMÜN Repository Standards Framework

Status: **CANDIDATE SUCCESSOR**  
Successor ID: **RS-FRAMEWORK**  
Predecessor: `cmartinezs/the-x-contract-registry/standards/repository-standard.md`  
Migration: `MIG-TXCR-GOV-001`

This document is the ADÜMÜN successor for repository standardization across the enterprise portfolio.

A repository does **not** adopt one universal template. Each repository adopts:

1. **RS-CORE**; and
2. one or more applicable profile standards according to its nature, risk, consumers, deployment model, lifecycle, visibility and operational role.

The objective is **composable conformance**, not cosmetic uniformity.

## 1. Standard families

The baseline profile vocabulary inherited from the predecessor remains candidate until each profile is migrated or revalidated:

- `RS-CORE` — Core Repository Standard
- `RS-GOV` — Governance & Initiative Repository
- `RS-CONTRACT` — Contract Provider / Machine Interface
- `RS-PRODUCT` — Product / Application
- `RS-SERVICE` — Backend / API / Worker Service
- `RS-FRONTEND` — Frontend / UI
- `RS-MONOREPO` — Multi-component Repository
- `RS-CAPABILITY` — Shared Capability
- `RS-LIBRARY` — Reusable Library / Package
- `RS-TOOLING` — CLI / Plugin / Automation / Developer Tool
- `RS-AI` — AI / Agentic System
- `RS-DATA` — Data / Persistence / Migration
- `RS-INFRA` — Infrastructure / Deployment
- `RS-EXPERIMENT` — Experiment / PoC / Spike
- `RS-CONTENT` — Content / Creative / Educational Assets
- `RS-TEMPLATE` — Template / Scaffold
- `RS-PUBLIC` — Public / Open Repository
- `RS-LEGACY` — Deprecated / Superseded / Archived

Profile IDs are not automatically CURRENT merely because they existed in the predecessor. `profile-catalog.md` remains a pending migration input.

## 2. Adoption model

Repository conformance is declared by profile, not by visual similarity. Adoption levels are:

- `REQUIRED`
- `APPLICABLE`
- `RECOMMENDED`
- `NOT_APPLICABLE`
- `DEFERRED`

Aliases may aid discovery but must not silently become canonical standard IDs.

## 3. Maturity model

Repository-standard maturity remains independent from initiative lifecycle and capability maturity:

- `R0 IDENTIFIED`
- `R1 DISCOVERABLE`
- `R2 MACHINE_READABLE`
- `R3 VALIDATED`
- `R4 INTEGRATED`
- `R5 GOVERNED_EVOLUTION`

## 4. Enforcement lifecycle

New repository rules normally progress:

`OBSERVED → CANDIDATE → PILOTED → STANDARDIZED → ENFORCED`

Rules should become blocking because evidence supports enforcement, not because uniformity is aesthetically desirable.

## 5. Authority and registries

Repository metadata, standard adoption, relationships and contract ownership must use ADÜMÜN successor registries when those registries become CURRENT. Until cutover, predecessor registries remain lineage/reference sources and must not be silently copied into a competing authority.

## 6. Migration principle

Do not mass-normalize existing repositories.

For each repository:

1. classify actual nature;
2. determine applicable standards;
3. reconcile source authority and consumers;
4. record current conformance honestly;
5. apply the smallest high-value improvements;
6. add deterministic validation after semantics stabilize;
7. migrate/deprecate only with lineage preserved.

## 7. Tooling and provider configuration

Provider configuration is governed through `STD-TOOL-001` and provider configuration profiles. GitHub, Jira or another provider may implement/project repository governance, but provider configuration does not create enterprise semantics.

## 8. Successor status

This document is a **CANDIDATE SUCCESSOR**. It becomes CURRENT only after migration coverage is checked against the predecessor framework and its dependent profile catalog/registries are either migrated or explicitly separated.
