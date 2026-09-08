# Governance — seem-identity-unifier

**Sweep:** 118  
**Classification:** RESEARCH  
**Head (pre-lock):** `ae6e0c0dedb2ca4c7b034d3f29308ed38ba13aae`  
**Live CI:** run `33941447514` success (2026-09-05, workflow `ci`, event push, branch main)  
**Releases / tags:** none  
**Open Dependabot alerts:** none listed this cycle  
**Claim cap:** MODULE_SURFACE

## Demonstrated (tree + CI; not live GitHub crawl)

| Feature | State |
|---------|-------|
| Identity map of three named SEEM repos | VERIFIED (code + tests + CI) |
| Claim that no SUPERSEDES/SAME_AS/EQUIVALENT_TO edge is licensed by *this* module | VERIFIED (docs/CLAIM.md + README contract) |
| Deterministic pytest suite | VERIFIED (CI success 33941447514) |
| Live GitHub crawler | ABSENT |
| Runtime / AST / VSA isomorphism | NOT CLAIMED |
| Merge, delete, or archive of mapped identities | FORBIDDEN by this repo; archive/supersede remains operator-gated in ADL-Governance |

## Portfolio tension (do not silently overwrite)

ADL-Governance currently classifies the three mapped identities as **SUPERSEDED** *for new work* by `sovereign-clean-room`.
This repository forbids treating that lifecycle label as identity collapse.
Both statements stand:

- Successor for *new* SEEM runtime work: `sovereign-clean-room` (portfolio).
- Historical GitHub identities remain distinct artifacts (this module).

## Not allowed from this lock

- Promote this repo to ACTIVE product runtime.
- Claim Q-FUNC-004 or Q-FUNC-005 closed.
- Delete or rewrite history of mapped repos.
