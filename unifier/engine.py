"""Deterministic validation of the identity contract.

Does not import SEEM-2.0, either Cognitive Microservice tree, sunder, or
sovereign-clean-room.
"""

from __future__ import annotations

from .identities import (
    ALLOWED_RELATIONS,
    FORBIDDEN_RELATIONS,
    IDENTITIES,
    QUEUE_ID,
    RECHECK_DATE,
    RECHECK_NOTE,
    REREAD,
    REREAD_DATE,
    SHARED_SURFACES,
    SNAPSHOT_DATE,
    VERSION,
    distinct_pairs,
)


class ContractError(ValueError):
    pass


def _hex40(value: str) -> bool:
    if len(value) != 40:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def validate() -> dict:
    if QUEUE_ID != "Q-FUNC-003":
        raise ContractError("queue id drift")
    if SNAPSHOT_DATE != "2026-09-05":
        raise ContractError("snapshot date must remain the lock date")
    if RECHECK_DATE != "2026-10-06":
        raise ContractError("recheck date drift")
    if "isomorphism" in RECHECK_NOTE.lower():
        raise ContractError("recheck note overclaims")
    if "SUPERSEDES still forbidden" not in RECHECK_NOTE:
        raise ContractError("recheck must keep SUPERSEDES forbidden")
    if len(IDENTITIES) != 3:
        raise ContractError("exactly three SEEM identities are in scope")
    names = list(IDENTITIES)
    if len(set(names)) != 3:
        raise ContractError("identity keys must be unique")
    for name, rec in IDENTITIES.items():
        if not rec.get("modules"):
            raise ContractError(f"{name} missing modules")
        if rec.get("cap") != "TREE_PRESENT_FUNCTIONS_UNAUDITED":
            raise ContractError(f"{name} cap must remain unaudited at this layer")
    pairs = distinct_pairs()
    if len(pairs) != 3:
        raise ContractError("expected C(3,2)=3 distinct pairs")
    if "SUPERSEDES" in ALLOWED_RELATIONS:
        raise ContractError("SUPERSEDES must not be allowed")
    for rel in FORBIDDEN_RELATIONS:
        if rel in ALLOWED_RELATIONS:
            raise ContractError(f"forbidden relation leaked: {rel}")
    if len(SHARED_SURFACES) < 3:
        raise ContractError("shared surface table too thin")
    if REREAD.get("date") != REREAD_DATE:
        raise ContractError("reread date drift")
    pins = REREAD.get("pins") or {}
    if list(pins) != names:
        raise ContractError("reread pins must follow the identity order")
    for name, sha in pins.items():
        if not _hex40(sha):
            raise ContractError(f"{name} pin is not a 40-character commit")
    dims = REREAD.get("default_dim_literal") or {}
    params = REREAD.get("dim_parameter") or {}
    substrates = REREAD.get("substrate") or {}
    if list(dims) != names or list(params) != names or list(substrates) != names:
        raise ContractError("reread dim/substrate tables must cover every identity")
    if any(not isinstance(value, int) or value < 1 for value in dims.values()):
        raise ContractError("default dim literals must be positive integers")
    if len(set(params.values())) < 2:
        raise ContractError("dim parameter names differ; do not collapse them")
    if len(set(substrates.values())) < 2:
        raise ContractError("numeric substrates differ; do not collapse them")
    if REREAD.get("algebra") != "NAME_ONLY":
        raise ContractError("algebra must stay NAME_ONLY")
    for key in ("runtime_import", "isomorphism", "mind"):
        if REREAD.get(key) != "NOT_CLAIMED":
            raise ContractError(f"{key} must stay NOT_CLAIMED")
    vsa_files = REREAD.get("vsa_file") or {}
    for name, path in vsa_files.items():
        modules = IDENTITIES[name]["modules"]
        if path not in modules:
            raise ContractError(f"{name} vsa file is not one of its locked modules")
    return {
        "ok": True,
        "identities": names,
        "pairs": pairs,
        "surfaces": [s["surface"] for s in SHARED_SURFACES],
        "supersedes": False,
        "version": VERSION,
        "snapshot": SNAPSHOT_DATE,
        "reread": REREAD_DATE,
        "recheck": RECHECK_DATE,
        "algebra": "NAME_ONLY",
        "substrate_mismatch": True,
        "default_dims": [dims[name] for name in names],
        "dim_parameters": [params[name] for name in names],
        "substrates": [substrates[name] for name in names],
    }


def report() -> str:
    result = validate()
    dims = "/".join(str(value) for value in result["default_dims"])
    params = "/".join(result["dim_parameters"])
    substrates = "/".join(result["substrates"])
    lines = [
        f"queue={QUEUE_ID}",
        f"claim_cap=MODULE_SURFACE",
        f"version={result['version']}",
        f"snapshot={result['snapshot']}",
        f"reread={result['reread']}",
        f"recheck={result['recheck']}",
        f"identities={len(result['identities'])}",
        f"pairs={len(result['pairs'])}",
        f"surfaces={len(result['surfaces'])}",
        "supersedes=false",
        "runtime_import=NOT_CLAIMED",
        "isomorphism=NOT_CLAIMED",
        "algebra=NAME_ONLY",
        f"default_dim={dims}",
        f"dim_parameter={params}",
        f"substrate={substrates}",
        "substrate_mismatch=true",
        "mind=NOT_CLAIMED",
        "OK",
    ]
    return "\n".join(lines)


def main() -> int:
    try:
        text = report()
    except ContractError as exc:
        print(f"ERROR {exc}")
        print("FAIL")
        return 1
    print(text)
    return 0 if text.endswith("OK") else 1


if __name__ == "__main__":
    raise SystemExit(main())
