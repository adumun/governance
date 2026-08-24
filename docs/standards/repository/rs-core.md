# RS-CORE — Core Repository Standard

Status: **CANDIDATE SUCCESSOR**  
Predecessor: `cmartinezs/the-x-contract-registry/standards/core-repository-standard.md`  
Migration: `MIG-TXCR-GOV-001`

RS-CORE defines the minimum cross-cutting contract for repositories participating in the ADÜMÜN portfolio. Specialized concerns are handled by additional applicable profiles.

## 1. Identity

Every governed repository must make these facts unambiguous where applicable:

- repository name and purpose;
- primary class/profile;
- current repository status;
- bounded context / ownership boundary;
- explicit non-ownership where overlap is plausible;
- canonical/default branch;
- owner/accountability reference.

Recommended machine-readable location: `governance/repository-status.yaml` or an approved successor profile.

## 2. README baseline

A root README should make it easy to determine:

1. what the repository is;
2. why it exists;
3. whether it is active, experimental, maintenance-only, superseded, deprecated or archived;
4. how to validate/build/run it when applicable;
5. where canonical state/documentation lives;
6. important dependencies/consumers;
7. where a human or agent should go next.

## 3. Repository status

Candidate baseline vocabulary:

- `ACTIVE`
- `MAINTENANCE`
- `PAUSED`
- `EXPERIMENTAL`
- `SUPERSEDED`
- `DEPRECATED`
- `ARCHIVED`

Repository status is not an Initiative Lifecycle stage.

## 4. Source-of-truth boundary

Repositories must distinguish:

- repository-local canonical artifacts;
- external canonical sources such as Drive, a database/service or another repository;
- generated projections;
- imported/reference-only artifacts;
- historical/superseded material.

A dashboard, copied file or convenient provider view must not become authority accidentally.

## 5. Standard adoption

Repositories should declare applicable standards/profiles and conformance maturity in machine-readable form when automation or audit needs it. Applicability is evaluated by repository nature; standards are not inherited merely because another repository uses them.

## 6. Change control

Every active engineering/governance repository must define:

- direct-push policy;
- PR requirements;
- protected branch/ruleset expectations;
- required validation/checks;
- merge strategy when material;
- release/tag policy when applicable.

ADÜMÜN does not mandate one universal branching model. Branching is profile-driven. Material changes normally use PRs.

Dependent PRs must not accumulate: if PR N is a prerequisite for PR N+1 in the same workstream, merge/close PR N before opening PR N+1 unless a documented stacked/parallel exception declares dependency, merge order and conflict handling.

## 7. Validation

Provide one obvious validation entry point whenever practical. Validation should be deterministic where technically feasible.

Hosted GitHub Actions are not mandatory when unavailable or unjustified; accepted local validation with retained evidence remains mandatory where the applicable standard requires validation. A financial bypass changes where evidence is produced, not whether validation occurs.

## 8. Configuration and secrets

- Never commit credentials/private keys.
- Provide `.env.example` or equivalent when environment configuration exists.
- Document variables without storing secret values.
- Use provider/runtime secret stores in deployed systems.
- Machine-readable governance may reference secret identifiers, never secret values.
- Ignore known local secret/runtime artifacts.

## 9. Reproducibility

Use ecosystem-appropriate lock/version mechanisms when reproducibility matters. Material runtime/tool requirements must be documented.

## 10. Documentation and decisions

Use `docs/` or equivalent when complexity warrants it. Prefer indexed documentation over orphan files. Long-lived architectural/strategic decisions should be traceable through ADRs, decision records or an equivalent durable mechanism.

## 11. Agent instructions

Repositories actively operated by coding/AI agents should provide tool-neutral instructions, preferably `AGENTS.md`, including authoritative sources, validation commands, forbidden/unsafe actions, repository boundaries, expected workflow and migration/deprecation constraints.

Provider-specific instruction files may supplement but should not silently become the only knowledge source when multiple tools/agents are expected.

## 12. Generated content and provenance

Generated artifacts must be distinguishable from manually authoritative content and should retain generator/source, version/revision provenance and authoritative upstream references where useful.

## 13. Relationships

Operationally important cross-repository relationships should use the accepted ADÜMÜN relationship/registry model once that successor becomes CURRENT, rather than relying only on prose.

## 14. Deprecation

Superseded/deprecated repositories require durable in-repo evidence and successor lineage. Deletion is exceptional; archive is preferred when provenance remains useful.

## 15. Public/private hygiene

Before changing visibility to public, verify secret history, licensing rights, private/personal data, proprietary third-party material, environment/config leakage and internal-only identifiers/URLs.

## 16. Maintenance surface

Avoid duplicate instructions, schemas and executable tooling when one declared authority can be referenced. Copies are acceptable when intentionally vendored/generated and provenance/update mechanics are explicit.

## 17. Applicability over ceremony

Do not create artifacts merely to satisfy a visual template. Mandatory artifacts must answer a real operational, governance, integration or audit question.

## Successor status

This candidate preserves the predecessor's substantive core while replacing The X-specific identity and aligning change control with `STD-TOOL-001` and the current ADÜMÜN provider-neutral governance model. It must pass migration coverage review before becoming CURRENT.
