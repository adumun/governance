# ADÜMÜN Governance

Version-controlled implementation home for ADÜMÜN governance standards, profiles, templates and executable governance assets.

Human-readable corporate canons and standards remain authoritative in their declared scopes. This repository provides versioned representations, profiles, templates and implementation guidance.

## Initial scope
- repository and change-control governance
- tool usage/configuration/integration profiles
- lifecycle/work-management implementation guidance
- governance templates
- migration/deprecation lineage
- brand and transitional-identity governance
- Quick Start documentation
- machine-readable funding/public-activation registries and dashboard specifications
- enterprise provider/tool governance and dependency tracking
- conversation/result formalization
- machine-readable artifact/data-model standards
- pre-execution transversal closure tracking

## Authority rule
Repository content becomes normative only when an applicable ADÜMÜN authority source explicitly assigns that status. Drafts and candidate profiles must declare their maturity.

## Quick Start
Start here when recovering context:
- `docs/quick-start/enterprise.md` — enterprise operating context
- `docs/quick-start/funding.md` — CLP 3M funding objective and six-month operating logic
- `docs/quick-start/public-presence.md` — The X: Codename → ADÜMÜN, marketing, press and inbound demand

Quick Starts are navigational. They do not override an applicable canon, approved standard, financial baseline or live registry.

## Conversation / documentation governance
- `docs/standards/documentation/result-formalization.md`
- `registry/policies/result-formalization.yaml`

Core rule: a material result is not considered closed while it exists only in conversation history. The conversation should summarize the important points and identify the durable artifacts created/updated.

## Machine-readable / processable entry points
- `docs/standards/data/machine-readable-artifacts.md` — file-first/schema-governed data standard
- `schemas/common-record.schema.json` — common authority-bearing record contract
- `schemas/pre-execution-closure.schema.json` — pre-execution closure schema
- `registry/brand-identities.yaml` — current/successor public identities and transition lineage
- `registry/funding-activation.yaml` — WHAT targets plus current activation portfolio
- `registry/providers.yaml` — current/planned/candidate/deferred provider and tool landscape
- `registry/pre-execution-closure.yaml` — 25 cross-cutting closure items before H0 execution
- `registry/dashboards/funding-activation.yaml` — reproducible funding + provider dashboard metrics/views
- `registry/dashboards/pre-execution-closure.yaml` — H0 closure/blocker dashboard contract

Default: YAML for maintained registries, JSON Schema for validation contracts, JSON for generated interchange/snapshots, Sheets for live human-operable structured views. Backend/database adoption requires evidence.

## Tool / provider governance
- `docs/standards/tooling/provider-governance.md`

Core rule: **Capability != Provider**. ChatGPT, Claude, Gemini, GitHub, Google Drive/Docs/Sheets, JetBrains, Figma, Miro, Jira, Suno and future tools are implementations or enablers of enterprise capabilities, not the capability definitions themselves.

## Branding and public activation
- `docs/standards/brand/brand-governance.md`
- `docs/standards/brand/transitional-identity.md`
- `migration/branding/the-x-codename-to-adumun.md`

The current transitional public identity is **The X: Codename**. ADÜMÜN is the canonical successor; public activation is gate-controlled.
