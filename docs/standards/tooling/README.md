# Tool Usage, Configuration, Integration & Template Governance

Status: CANDIDATE IMPLEMENTATION NOTES  
Human source: `STD-TOOL-001` candidate in ADÜMÜN Corporate HQ / Standards & Policies.

## Scope
This area will contain provider-neutral tooling governance plus provider profiles for GitHub, Jira and future complementary tools.

## Provider-neutral rule
ADÜMÜN owns canonical semantics. Tool providers implement or project those semantics through explicit mappings and configuration profiles.

## Current candidate work
- GitHub repository configuration baseline and branching profiles
- Jira project/workflow configuration profile
- repository/project templates where provider capabilities allow
- tool selection and complementary-tool assessment criteria
- configuration-as-code guidance
- provider mapping and MCP integration boundaries
- PR accumulation/dependency rule

## PR dependency rule
A workstream must not open a dependent PR while its prerequisite PR remains open, unless an explicit parallelization/stacked-PR exception declares dependency, merge order and conflict/rebase handling.

## Planned provider profiles
- `profiles/github/`
- `profiles/jira/`

## Planned template families
- GitHub repository templates by repository profile
- PR/issue templates
- Jira project/workflow/issue templates where supported
- AGENTS/README/governance templates
- evidence/decision/ADR templates

## Complementary tool assessments
Recommendations must state the capability gap, expected benefit, integration model, ownership, cost/licensing, data/security implications and exit/portability risk. Popularity alone is not a selection criterion.
