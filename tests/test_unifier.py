from unifier.engine import validate
from unifier.identities import (
    FORBIDDEN_RELATIONS,
    IDENTITIES,
    SHARED_SURFACES,
    distinct_pairs,
)


def test_three_distinct_identities():
    r = validate()
    assert r["ok"] is True
    assert r["supersedes"] is False
    assert len(r["identities"]) == 3
    assert len(set(r["identities"])) == 3


def test_no_supersedes_relation():
    assert "SUPERSEDES" in FORBIDDEN_RELATIONS
    for a, b in distinct_pairs():
        assert a != b


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
    for s in SHARED_SURFACES:
        assert "no" in s["claim"].lower() or "exist" in s["claim"].lower() or "name" in s["claim"].lower()
        assert s["names"]
