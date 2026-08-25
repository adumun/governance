# MIG-TXCR-GOV-FINAL — Governance Cutover

Status: **READY FOR MERGE**

This wave completes the repository-governance scope migration from `cmartinezs/the-x-contract-registry` to `adumun/governance`.

## Successors

- `standards/repository-standard.md` → `docs/standards/repository/repository-standards-framework.md`
- `standards/core-repository-standard.md` → `docs/standards/repository/rs-core.md`
- `standards/profile-catalog.md` → `docs/standards/repository/profile-catalog.md`
- `standards/github-pages-publication-standard.md` → `docs/standards/repository/rs-pages.md`
- `CHANGE_CONTROL.md` → `docs/standards/tooling/change-control.md`
- `PROVIDER_ENFORCEMENT.md` → `docs/standards/tooling/provider-enforcement.md`
- `registry/standards.yaml` → `registry/standards.yaml`
- repository governance inventory → `registry/repositories.yaml` plus historical predecessor metadata
- relationship/lineage governance → `registry/relationships.yaml` plus predecessor lineage reference

## Boundary

Audit semantics/evidence already cut over to `adumun/audit-framework`. Machine contract schemas and the legacy contract registry are intentionally excluded from this PR and are the only remaining material cutover required before global predecessor deprecation.

Legacy repository data is not erased. Dated portfolio observations are treated as historical evidence rather than silently promoted into current ADÜMÜN truth.

## Validation review

- all legacy governance files have an explicit destination or historical disposition;
- no audit authority is reintroduced into governance;
- no machine-contract semantic authority is duplicated here;
- provider configuration is separated from policy;
- dependent-PR sequencing rule is preserved;
- GitHub Actions financial bypass preserves mandatory validation.
