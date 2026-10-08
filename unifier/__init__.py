"""SEEM identity unifier. Identities remain distinct. Not a mind."""

from .identities import IDENTITIES, SHARED_SURFACES, VERSION

__version__ = VERSION


def validate():
    """Import the checker lazily so `python -m unifier.engine` stays a script."""
    from .engine import validate as _validate

    return _validate()


__all__ = ["IDENTITIES", "SHARED_SURFACES", "validate", "__version__"]
