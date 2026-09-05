"""SEEM identity unifier. Identities remain distinct."""

from .identities import IDENTITIES, SHARED_SURFACES
from .engine import validate

__all__ = ["IDENTITIES", "SHARED_SURFACES", "validate"]
