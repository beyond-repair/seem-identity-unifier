"""Locked snapshot of SEEM identities. Dated 2026-09-05. Not a live crawler.

Invariant: no SUPERSEDES edge exists among these identities.
Similarity of names is not identity equivalence.
"""

from __future__ import annotations

SNAPSHOT_DATE = "2026-09-05"
QUEUE_ID = "Q-FUNC-003"
CLAIM_CAP = "MODULE_SURFACE"

ALLOWED_RELATIONS = (
    "DISTINCT_FROM",
    "SHARES_NAMED_SURFACE_WITH",
    "CLUSTER_PEER_OF",
)

FORBIDDEN_RELATIONS = (
    "SUPERSEDES",
    "EQUIVALENT_TO",
    "SAME_AS",
)

IDENTITIES: dict[str, dict] = {
    "SEEM-2.0-Self-Evolving-Emergent-Mind": {
        "layout": "flat_python",
        "modules": (
            "seem.py",
            "banel.py",
            "dream_phase.py",
            "resonator_vsa.py",
        ),
        "also_present": (
            "telegram_bot.py",
            "demo.py",
            "BLUEPRINT.md",
        ),
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "offline symbolic substrate; largest named kernel modules at repo root",
    },
    "SEEM-Cognitive-Microservice": {
        "layout": "flat_plus_core",
        "modules": (
            "seem.py",
            "core/banel.py",
            "core/dream.py",
            "core/resonator.py",
        ),
        "also_present": (
            "telegram_bot.py",
            "WHITE_PAPER.md",
            "TECHNICAL_VSA_FHRR.md",
        ),
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "hyphenated microservice; overlapping names with 2.0, different tree",
    },
    "SEEM-Cognitive_Microservice": {
        "layout": "backend_package_plus_frontend",
        "modules": (
            "backend/seem/core/vsa.py",
            "backend/seem/learning/banel.py",
            "backend/seem/learning/dream.py",
            "backend/seem/api/server.py",
        ),
        "also_present": (
            "src/App.tsx",
            "package.json",
            "BLUEPRINT.md",
        ),
        "cap": "TREE_PRESENT_FUNCTIONS_UNAUDITED",
        "note": "underscore microservice; React UI + FastAPI-shaped backend; not a file-for-file copy",
    },
}

SHARED_SURFACES: tuple[dict, ...] = (
    {
        "surface": "kernel_entry",
        "names": ("seem.py", "backend/seem/api/server.py"),
        "claim": "named entrypoints exist; no shared import graph claimed",
    },
    {
        "surface": "banel",
        "names": ("banel.py", "core/banel.py", "backend/seem/learning/banel.py"),
        "claim": "BaNEL is a shared *name*; implementations unaudited for isomorphism",
    },
    {
        "surface": "dream",
        "names": ("dream_phase.py", "core/dream.py", "backend/seem/learning/dream.py"),
        "claim": "dream-phase is a shared *name*; no runtime coupling claimed",
    },
    {
        "surface": "vsa_resonator",
        "names": ("resonator_vsa.py", "core/resonator.py", "backend/seem/core/vsa.py"),
        "claim": "VSA/resonator surfaces exist under different paths",
    },
)


def distinct_pairs() -> tuple[tuple[str, str], ...]:
    names = tuple(IDENTITIES)
    out = []
    for i, a in enumerate(names):
        for b in names[i + 1 :]:
            out.append((a, b))
    return tuple(out)
