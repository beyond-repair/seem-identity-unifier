from unifier import __version__
from unifier.engine import report, validate
from unifier.identities import (
    FORBIDDEN_RELATIONS,
    IDENTITIES,
    RECHECK_DATE,
    RECHECK_NOTE,
    REREAD,
    SHARED_SURFACES,
    SNAPSHOT_DATE,
    VERSION,
    distinct_pairs,
)


def test_three_distinct_identities():
    result = validate()
    assert result["ok"] is True
    assert result["supersedes"] is False
    assert len(result["identities"]) == 3
    assert len(set(result["identities"])) == 3


def test_no_supersedes_relation():
    assert "SUPERSEDES" in FORBIDDEN_RELATIONS
    assert "EQUIVALENT_TO" in FORBIDDEN_RELATIONS
    assert "SAME_AS" in FORBIDDEN_RELATIONS
    for left, right in distinct_pairs():
        assert left != right


def test_underscore_and_hyphen_are_not_the_same_key():
    assert "SEEM-Cognitive-Microservice" in IDENTITIES
    assert "SEEM-Cognitive_Microservice" in IDENTITIES
    assert "SEEM-Cognitive-Microservice" != "SEEM-Cognitive_Microservice"


def test_layouts_differ():
    layouts = {rec["layout"] for rec in IDENTITIES.values()}
    assert layouts == {
        "flat_python",
        "flat_plus_core",
        "backend_package_plus_frontend",
    }


def test_shared_surfaces_are_names_not_isomorphisms():
    for surface in SHARED_SURFACES:
        claim = surface["claim"].lower()
        assert "isomorphism" not in claim or "not an isomorphism" in claim or "unaudited" in claim
        assert "equivalent" not in claim
        assert surface["names"]


def test_equal_default_dim_is_not_an_algebra():
    result = validate()
    assert result["default_dims"] == [16384, 16384, 16384]
    assert result["dim_parameters"] == ["dim", "dim", "dimension"]
    assert result["substrates"] == ["numpy", "torch", "numpy"]
    assert result["substrate_mismatch"] is True
    assert result["algebra"] == "NAME_ONLY"
    assert REREAD["runtime_import"] == "NOT_CLAIMED"
    assert REREAD["isomorphism"] == "NOT_CLAIMED"
    assert REREAD["mind"] == "NOT_CLAIMED"


def test_reread_pins_are_full_commits():
    names = list(IDENTITIES)
    assert list(REREAD["pins"]) == names
    for name in names:
        sha = REREAD["pins"][name]
        assert len(sha) == 40
        int(sha, 16)
        assert REREAD["vsa_file"][name] in IDENTITIES[name]["modules"]


def test_report_states_the_non_claims():
    text = report()
    assert text.endswith("OK")
    assert "queue=Q-FUNC-003" in text
    assert "supersedes=false" in text
    assert "algebra=NAME_ONLY" in text
    assert "substrate=numpy/torch/numpy" in text
    assert "substrate_mismatch=true" in text
    assert "default_dim=16384/16384/16384" in text
    assert "dim_parameter=dim/dim/dimension" in text
    assert "mind=NOT_CLAIMED" in text
    assert "runtime_import=NOT_CLAIMED" in text
    assert "recheck=2026-10-06" in text
    assert __version__ == VERSION == "0.1.1"


def test_recheck_does_not_replace_snapshot():
    r = validate()
    assert SNAPSHOT_DATE == "2026-09-05"
    assert RECHECK_DATE == "2026-10-06"
    assert r["snapshot"] == SNAPSHOT_DATE
    assert r["recheck"] == RECHECK_DATE
    assert "unaudited" in RECHECK_NOTE
    assert "SUPERSEDES still forbidden" in RECHECK_NOTE
