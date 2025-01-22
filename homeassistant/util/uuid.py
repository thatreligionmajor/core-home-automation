"""Helpers to generate uuids."""
import secrets


def random_uuid_hex() -> str:
    """Generate a random UUID hex.

    This uuid should not be used for cryptographically secure
    operations.
    """
    return "%032x" % secrets.SystemRandom().getrandbits(32 * 4)
