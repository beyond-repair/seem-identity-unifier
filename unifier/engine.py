"""Deterministic validation of the identity contract."""

from __future__ import annotations

from .identities import (
    ALLOWED_RELATIONS,
    FORBIDDEN_RELATIONS,
    IDENTITIES,
    QUEUE_ID,
    SHARED_SURFACES,
    distinct_pairs,
)


class ContractError(ValueError):
    pass


def validate() -> dict:
    if QUEUE_ID != "Q-FUNC-003":
        raise ContractError("queue id drift")
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
    return {
        "ok": True,
        "identities": names,
        "pairs": pairs,
        "surfaces": [s["surface"] for s in SHARED_SURFACES],
        "supersedes": False,
    }


def main() -> None:
    result = validate()
    print(result)


if __name__ == "__main__":
    main()
