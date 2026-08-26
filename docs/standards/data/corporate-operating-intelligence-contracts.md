# STD-COI-001 — Corporate Operating Intelligence Contract & Read-Model Semantics

Maturity: CANDIDATE  
Version: 1.0.0  
Initiative: INIT-ACC-001  
Capability: CAP-COI-001 — Corporate Operating Intelligence & Control  
Decision authority: DEC-ACC-G7-001  
Scope: S8 / first-horizon read-model/agent-first delivery only

## 1. Purpose

This standard defines the consumer-independent semantic and technical contract for the first-horizon Corporate Operating Intelligence (COI) read model. It encodes the already accepted solution direction without creating a new source of business truth.

Canonical flow:

`Authoritative sources -> bounded deterministic readers/adapters -> semantic/integrity validation -> materialized DERIVED_NON_AUTHORITATIVE read models -> multiple consumers`

Source authorities remain authoritative. COI contracts and materializations are derived interoperability surfaces and must never silently promote themselves to business authority.

## 2. Mandatory invariants

1. Consumer presentation may change; semantic meaning, source authority and provenance may not.
2. Canonical contracts are provider-neutral and file/JSON-first.
3. Every material answer exposes canonical concept identity, concern family, semantic class, value state, authority, provenance, freshness/as-of information and generation context.
4. `UNKNOWN`, `MISSING`, `STALE` and `RECONCILIATION_REQUIRED` are explicit governed states. They must not be replaced by inference, zero, empty string, a guessed status or a previous value presented as current.
5. Financial concepts that are economically distinct remain distinct, including target, pipeline, booked/committed, billed/invoiced, collected cash, recognized revenue and predictable coverage.
6. Operational states that govern different concerns remain distinct, including initiative lifecycle state, lifecycle stage, gate state, product readiness, capability maturity, work state and delivery state.
7. Materialized read models are `DERIVED_NON_AUTHORITATIVE` and reconstructable from governed upstream evidence plus deterministic derivation rules.
8. A validation failure blocks publication of the affected slice and produces an explicit degraded/reconciliation state; it never authorizes semantic inference.
9. Provider-specific IDs, APIs, field names and transport details belong in mappings/adapters, not canonical COI meaning.
10. A database, visual Control Center, writeback, approval engine, event bus, vector search and provider selection are outside this contract.

## 3. First-horizon concern families

The bounded concern families are:

- `FH-CF-01` — Funding / Finance boundary.
- `FH-CF-02` — Initiative Lifecycle / Portfolio.
- `FH-CF-03` — Enterprise Decisions.
- `FH-CF-04` — Structural Ownership.
- `FH-CF-05` — Cross-domain Source Health / Corporate Operating Snapshot.

No consumer may introduce a new first-horizon concern family by presentation convention alone.

## 4. Canonical concept contract

A canonical concept is an immutable governed identifier for one material business meaning. Its registry entry must declare at minimum:

- stable `concept_id`;
- bounded `concern_family`;
- governed `semantic_class`;
- business meaning;
- value kind and unit policy where applicable;
- expected authority posture;
- permitted value states;
- stewardship owner;
- source/evidence references.

A Material Answer may use a canonical concept only when that concept is registered. Its semantic class must match the concept registry. Changing the economic or operational meaning behind an existing concept ID is a breaking change; create a successor concept instead.

## 5. Material Answer / QuickLookupResult

`Material Answer` is the common semantic envelope. `QuickLookupResult` is a consumer presentation of that envelope, not a separate authority or semantic contract.

A material answer must expose:

- answer identity;
- concern family and canonical concept;
- value state and value when allowed;
- semantic class;
- authority metadata;
- provenance/source references;
- freshness/as-of context;
- confidentiality/authorization state;
- limitations and drill-through/source relationship;
- generation timestamp.

`KNOWN` requires a material value. `UNKNOWN`, `MISSING`, `RECONCILIATION_REQUIRED`, `RESTRICTED` and `NOT_APPLICABLE` must not silently carry a material value. `STALE` must be paired with stale freshness metadata and must never be presented as current.

## 6. Authority metadata

Authority metadata identifies the status of the represented fact, not the trustworthiness of a UI or consumer. Governed modes include source authority, registry authority and derived/non-authoritative projections plus explicitly labeled observation, estimate or assumption where allowed by the bounded source contract.

Every derived COI read model has authority mode `DERIVED_NON_AUTHORITATIVE`. A derived answer may reference an authoritative source, but the derived envelope does not inherit that source's authority.

## 7. Provenance and source-reference contract

Provenance must make a material answer traceable to governed inputs. Source references are stable logical references, not provider-specific transport coordinates. A source reference must be resolvable by the bounded adapter/mapping layer to the governed source revision or record used for the derivation.

Where derivation occurs, the read-model metadata must record deterministic derivation identity/version and the input source references. Human-readable derivation notes may supplement this metadata but do not replace it.

## 8. Freshness / as-of contract

Freshness and as-of are distinct:

- `as_of` states the business/source time represented by the fact or snapshot;
- `generated_at` states when the derived artifact was produced;
- `retrieved_at` states when a source was read;
- freshness state expresses whether the artifact satisfies its governed freshness policy.

Allowed first-horizon freshness states are `CURRENT`, `STALE`, `UNKNOWN` and `REVIEW_REQUIRED`. A missing as-of value must remain explicit when the source cannot support one; it must not be synthesized from retrieval or generation time.

## 9. Unknown, missing, stale and reconciliation semantics

- `UNKNOWN`: the contract permits the concept but available evidence does not establish its value.
- `MISSING`: the governed source is expected to provide the value/record but it is absent.
- `STALE`: a prior value exists but fails the applicable freshness policy.
- `RECONCILIATION_REQUIRED`: available governed evidence conflicts, cannot be deterministically reconciled, or violates an integrity rule.
- `RESTRICTED`: a value exists but the current consumer is not authorized to receive it.
- `NOT_APPLICABLE`: the concept does not apply to the bounded object.

These states are semantically different and must not be normalized into one generic null/error state.

## 10. Derivation metadata

Every materialized read model must declare deterministic derivation metadata sufficient to reproduce the projection:

- derivation identifier and version;
- deterministic flag = true;
- inference flag = false for first-horizon canonical materialization;
- input source references;
- contract/schema references;
- generator/revision reference where available;
- derivation rule or mapping reference;
- rebuild command/procedure reference.

If a result cannot be reproduced from governed inputs under the declared rules, it is not a conforming first-horizon COI materialization.

## 11. Source-health contract

Source health is first-class operating metadata and is not inferred from business values. It must distinguish at minimum availability, freshness and reconciliation/integrity status. A source may be available but stale, available but reconciliation-required, degraded/partial, unavailable or unknown.

Source-health records must expose source identity, observation/retrieval time, last successful read when known, freshness state, reconciliation state and bounded issue/evidence references. Source failure never authorizes substitution from a semantically different source.

## 12. Materialized read-model metadata and envelope

Every materialized read model must carry metadata independent of its consumer payload:

- stable read-model ID and contract version;
- `DERIVED_NON_AUTHORITATIVE` authority;
- generation time and snapshot as-of;
- applicable concern families;
- freshness and reconciliation status;
- source references/source-health summary;
- derivation/rebuild metadata;
- schema/contract references;
- deterministic generator revision when available.

The first-horizon cross-domain Corporate Operating Snapshot is the materialization contract currently identified as `RM-COI-001`. It composes governed records from all five bounded concern families without collapsing their semantic classes or source authority.

## 13. Versioning and evolution

Semantic versioning applies to COI contracts and governed vocabularies:

- PATCH: documentation/clarification or validator defect fix that changes no accepted instance semantics.
- MINOR: backward-compatible additive field, vocabulary or concept addition. Existing conforming instances remain valid and retain meaning.
- MAJOR: removal, required-field change, type change, enum removal/rename, concept meaning change, authority/freshness/value-state semantic change, or any change that can reinterpret an existing accepted instance.

Breaking changes require a successor schema/concept, explicit migration path and predecessor/successor lineage. Silent reinterpretation is prohibited.

## 14. Compatibility policy

Within a major version:

- consumers must ignore no governed meaning; they may ignore optional presentation-only fields only when their contract allows it;
- producers may add only fields/vocabulary explicitly admitted by a compatible schema/version;
- unknown governed enum/concept values fail closed;
- a consumer declaring support for a version must preserve all authority, freshness, provenance and unknown-state semantics of that version;
- provider mappings may not redefine canonical concepts or semantic classes.

Backward compatibility is semantic as well as structural. A JSON instance that still parses but changes economic or operational meaning is breaking.

## 15. Ownership and stewardship

- Accountable delivery owner: Corporate Technology & Platform.
- Semantic/data stewardship: Data, Knowledge & AI together with each bounded domain authority.
- Governance/assurance: Governance & Audit.
- Source truth authority: the original bounded authoritative sources/registries.
- Machine-contract implementation home: `adumun/machine-contracts`.
- Human semantic/governance specification home: `adumun/governance` plus accepted initiative decisions/evidence.

No schema maintainer may expand domain meaning unilaterally.

## 16. Canonical registration requirements

A promoted COI contract must be registered in the canonical machine contract authority index with:

- stable contract ID/name/version;
- semantic authority reference to this standard and applicable bounded source authority;
- successor/schema path;
- maturity/status;
- evidence/provenance references.

A canonical concept must be present in the COI concept registry before use in a conforming material answer. Registry additions must pass deterministic local validation.

## 17. Regeneration and rebuildability

Read models are disposable projections. Conformance requires that they can be deleted and rebuilt from governed upstream evidence using the declared deterministic mappings/rules. Rebuilds must not depend on hidden conversational memory, manual interpretation, unavailable paid CI or an undeclared database state.

Rebuild evidence must identify the exact code/contract revision, input/source references and validation command/results. When GitHub Actions are unavailable, exact-revision local validation evidence is authoritative for this milestone.

## 18. Deterministic validation minimum

Validation must fail on at least:

- schema/parse errors;
- unregistered canonical concepts;
- semantic-class mismatch with the concept registry;
- unknown concern/value/freshness/authority vocabulary;
- `KNOWN` without value;
- prohibited material value on explicit non-value states;
- stale/value-state inconsistency;
- derived read model without derived authority;
- missing provenance/derivation/rebuild metadata where required;
- duplicate stable IDs;
- broken contract/source references;
- missing contract-authority registration;
- unsupported breaking change without major-version/migration lineage.

## 19. Relationship to existing standards

This standard specializes, rather than duplicates, the enterprise Machine-Readable Artifacts & Lightweight Data Architecture rules: file-first defaults, explicit source of truth, local validation, semantic versioning and no backend/database requirement without evidence remain in force.

It also reuses existing Initiative Lifecycle, Decision Governance, Work Management and structural authority contracts where those domains already have canonical schemas. COI indexes/reads those meanings; it does not redefine them.

## 20. M1 boundary

STD-COI-001 defines contracts only. It does not authorize or implement source readers, runtime services, databases, provider selection, credentials, deployment, UI, writeback, approvals, event buses, queues or vector search.
