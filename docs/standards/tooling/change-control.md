# ADÜMÜN Repository Change Control

Status: **CANDIDATE SUCCESSOR / CURRENT OPERATING RULE**

Predecessor: `cmartinezs/the-x-contract-registry/CHANGE_CONTROL.md` (blob `cb10b9f597ebd1644f92e40f0318a05aa17f1bde`).

## Policy

Material authority-bearing changes MUST use a pull request against the repository's canonical branch. Direct pushes are reserved for emergency recovery when the PR path is unavailable and require documented reconciliation.

A PR is mergeable only when applicable validation succeeds in an accepted execution environment; machine IDs and relationships remain valid; authority changes preserve provenance; breaking contracts follow compatibility policy; historical evidence is not rewritten; and material standards follow their maturity lifecycle unless a documented safety reason requires acceleration.

## Dependent PR sequencing

A workstream MUST NOT accumulate dependent PRs. Do not open PR N+1 while PR N is a direct prerequisite and remains open, unless an explicit stacked/parallel exception records dependency order, merge order and conflict/rebase strategy. Independent PRs may coexist.

## Financial bypass for hosted validation

GitHub-hosted Actions are not an absolute prerequisite when they cannot execute solely because of a verified billing/spending constraint. In that situation:

- do not pretend the hosted check passed;
- execute the same validation contract locally or in another available non-billable environment against the exact revision intended for merge;
- retain durable evidence of commands, versions, revision, timestamp and result;
- treat any local failure as blocking;
- classify unavailable hosted evidence as `HOSTED_VALIDATION_UNAVAILABLE_FINANCIAL`;
- classify non-reproducible provider-only checks as `UNKNOWN` or `DEFERRED` and assess materiality.

The bypass changes where validation is evidenced, not whether validation is required.

## Merge strategy

Squash is preferred for focused changes. Preserve multi-commit history when migration/provenance materially benefits from it. Rebase/merge are not forbidden when justified.

## Provider enforcement

Repository policy remains normative even when provider-side branch/ruleset enforcement is absent, temporarily blocked or financially unavailable. Provider configuration is an implementation of policy, never its semantic authority.