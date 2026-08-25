# ADÜMÜN Provider Enforcement Boundary

Status: **CURRENT GOVERNANCE BOUNDARY**

Predecessor: `cmartinezs/the-x-contract-registry/PROVIDER_ENFORCEMENT.md` (blob `b0cdba4cb92aeb4c85c1dcdb91a062bdd253ebc2`).

Provider controls implement policy but do not define it.

## GitHub

Branch protection/rulesets, merge restrictions, status checks, repository visibility, Pages source configuration and app permissions are provider-side enforcement. Their absence MUST NOT be mistaken for a different ADÜMÜN policy.

A provider configuration profile should record `DESIRED`, `OBSERVED`, `ENFORCED`, `PARTIAL`, `UNAVAILABLE` or equivalent evidence-backed state separately from the governing rule.

When a provider control is unavailable because of billing, permissions or product limitations, the repository must retain the underlying governance requirement and use the approved alternate evidence/control path where one exists.

## Jira and other providers

Jira, GitHub Projects, MCP adapters and future providers project ADÜMÜN semantics; they do not own canonical work-state/type semantics. Provider-specific statuses, issue types, custom fields and transitions must map through approved provider-neutral contracts.

## General rule

`POLICY → CONFIGURATION PROFILE → PROVIDER ENFORCEMENT → OBSERVATION/EVIDENCE`.

Do not invert this chain by inferring policy from whatever a provider currently happens to permit.