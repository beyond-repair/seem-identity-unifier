<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy · a mind · identity collapse
```

</div>

---

# seem-identity-unifier

Claim-capped **identity map** (v0.1.1) for three SEEM repositories that share vocabulary and must not be collapsed:

- `SEEM-2.0-Self-Evolving-Emergent-Mind`
- `SEEM-Cognitive-Microservice` (hyphen)
- `SEEM-Cognitive_Microservice` (underscore)

This repository closes queue item **Q-FUNC-003** from `adl-function-census`.

It does **not** close `Q-FUNC-004` (OS constitution merge) or `Q-FUNC-005` (workforce lineage).

## Claim contract

| Claimed | Not claimed |
|---|---|
| Three distinct GitHub identities, layouts locked 2026-09-05 | Runtime equivalence of any pair |
| 2026-10-02 re-read: those locked paths still exist at the pinned commits | A live GitHub crawler |
| Named surfaces (seem / banel / dream / vsa) appear under different paths | Vector-space or AST isomorphism |
| Each pinned VSA file contains constructor literal 16384 | Equal algebras, equal parameter names, or one numeric library |
| Hyphen substrate is torch; the other two are numpy. Underscore parameter is `dimension`; the other two are `dim` | That 16384 here overrides the 4096/8192/16384 split in `seem-sunder-bridge` |
| No SUPERSEDES / SAME_AS / EQUIVALENT_TO edge is licensed | Merge, delete, or archive of any identity |
| Deterministic validation tests | A mind, or a unified identity |
| 2026-10-06 directory recheck: named paths still listed | Function-body audit |

Claim cap of this repo: **MODULE_SURFACE**.

Snapshot lock remains `2026-09-05`. The Sweep-256 recheck does not replace it.

## Why not SUPERSEDES

Default-branch trees differ in layout:

| Identity | Layout |
|---|---|
| SEEM-2.0 | flat `seem.py`, `banel.py`, `dream_phase.py`, `resonator_vsa.py` |
| SEEM-Cognitive-Microservice | `seem.py` + `core/{banel,dream,resonator}.py` |
| SEEM-Cognitive_Microservice | `backend/seem/**` + React `src/` |

Name collision is not identity collapse.
Portfolio SUPERSEDED (new work goes to `sovereign-clean-room`) is not an identity collapse.

## Install and run

Python 3.10+. From a fresh clone of the default branch:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m unifier
python -m pytest -q
```

`python -m unifier` (same as `python -m unifier.engine`) prints the contract and `OK`, then exits 0. A drifted contract prints `ERROR` and `FAIL`, then exits 1.

No configuration file. The checker does not use the network and does not import the three SEEM trees.

`requirements.txt` pins pytest for the existing workflow, which installs that file and runs pytest from the repository root. The install above is the supported path.

A passing run looks like:

```
queue=Q-FUNC-003
claim_cap=MODULE_SURFACE
version=0.1.1
snapshot=2026-09-05
reread=2026-10-02
recheck=2026-10-06
identities=3
pairs=3
surfaces=4
supersedes=false
runtime_import=NOT_CLAIMED
isomorphism=NOT_CLAIMED
algebra=NAME_ONLY
default_dim=16384/16384/16384
dim_parameter=dim/dim/dimension
substrate=numpy/torch/numpy
substrate_mismatch=true
mind=NOT_CLAIMED
OK
```

## Related

- `adl-function-census` Q-FUNC-003
- `seem-sunder-bridge` (Q-003 interop contract; explicitly left this gap open)
- `sunder-cleanroom-vsa-adapter` (Q-FUNC-002)
- `ADL-Governance`, `forge-aegis`, `aegis-repo-graph`


---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
