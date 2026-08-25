# Provider & Tool Governance — ADÜMÜN

Status: CANDIDATE
Version: 0.1.0

## Purpose

Govern external tools and providers as replaceable implementations of enterprise capabilities rather than as the capabilities themselves.

## Core rule

`Capability != Provider`.

ADÜMÜN may use a provider today, replace it tomorrow, use several providers simultaneously, or build an internal implementation. Enterprise semantics, evidence and operating continuity must not depend unnecessarily on a single vendor.

## Lifecycle

Provider/tool entries use:

`CANDIDATE -> PLANNED -> CURRENT -> RETIRED`

`DEFERRED` is used when adoption is intentionally postponed despite an identified future role.

Usage state is tracked separately because an account can exist without becoming an operational dependency.

## Required metadata

Each provider/tool record should declare:

- stable provider ID;
- product and vendor;
- category;
- lifecycle and usage state;
- entitlement/plan state when known;
- capabilities enabled;
- strategic role;
- dependency level;
- substitution/exit strategy;
- cost status and known cost;
- financial treatment;
- adoption/rights gates where applicable;
- source/evidence and last review date when externally verified facts are recorded.

## Financial rules

1. Unknown cost is `null` / `TBD`, never zero.
2. Candidate, planned and deferred providers do not enter Corporate OPEX until activation/commitment creates an actual cost.
3. Current founder-paid tooling may remain Founder Work Dependency during the transition and migrate to Corporate OPEX only under the approved financial baseline rules.
4. Bundled tools must identify the parent subscription when that relationship is known.
5. Provider cost must be reconcilable with the Funding WHAT/live financial baseline.

## Dependency rules

For `MEDIUM`, `HIGH` or `CRITICAL` dependency, document at least one of:

- portable data/export path;
- provider-neutral contract/interface;
- alternate provider;
- open/self-hosted implementation;
- migration procedure.

Provider independence is risk-managed optionality, not an instruction to rebuild every SaaS product internally.

## Dashboard expectations

The operating dashboard should expose at minimum:

- current providers/tools;
- planned/candidate/deferred tools;
- known monthly provider spend;
- unknown-cost count;
- medium/high dependency count;
- provider-to-capability mapping;
- activation/adoption gates;
- substitution path status.

## Initial scope

The first registry includes ChatGPT, Claude, Gemini, GitHub, Google Drive, Google Docs, JetBrains, Figma, Miro, Jira and Suno. This list is intentionally non-exhaustive and should expand as the operating model discovers additional tooling.