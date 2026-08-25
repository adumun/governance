# RS-PAGES — GitHub Pages Publication Standard

Status: **CANDIDATE SUCCESSOR / MIGRATED FROM LEGACY**

Predecessor: `cmartinezs/the-x-contract-registry/standards/github-pages-publication-standard.md` (blob `91ef4c9cf4ecc6364b057c8451ad5064ed3d4a61`).

## Canonical rule

For ADÜMÜN repositories publishing static sites through GitHub Pages, the default publication topology is:

```text
main/master (canonical source)
  → local/deterministic validation
  → deterministic public build
  → generated gh-pages snapshot
  → GitHub Pages: Deploy from a branch / gh-pages / root
```

`gh-pages` is generated publication output and MUST NOT become development or semantic authority.

## Actions policy

GitHub Actions MUST NOT be the default Pages publication mechanism. It is an exception path requiring durable evidence of a material technical or operational need that branch publication cannot reasonably satisfy.

Convenience, template defaults, or an existing workflow are insufficient justification. This rule also protects ADÜMÜN from avoidable hosted-runner cost and remains compatible with the enterprise financial-bypass policy.

An Actions exception must record at least: rationale, assessment of why branch publication is inadequate, cost impact, operational benefit, approving authority, approval date and review trigger.

## Publication gate

Before publication, the repository must identify the exact canonical revision, run its deterministic validation/build contract, validate the generated public tree, reject secrets/internal-only material, and verify the final Pages base path. Interactive surfaces should run browser-level regression checks when materially justified.

Publication stops on failed required validation.

## Public-surface boundary

The generated Pages tree SHOULD contain only intentional public output. It SHOULD NOT include `.github/`, internal governance artifacts, tests, source-only tooling, `.env*`, credentials, private datasets, internal evidence, or unrelated repository metadata.

## Retroactive adoption

Existing Pages repositories are classified as one of:

`CONFORMING_BRANCH | BRANCH_REMEDIATION_REQUIRED | ACTIONS_EXCEPTION_APPROVED | ACTIONS_EXCEPTION_REQUIRED | MIGRATION_TO_BRANCH_REQUIRED | UNKNOWN`.

Migration must preserve canonical-source authority and public behavior. Historical workflows remain provenance and are not rewritten.