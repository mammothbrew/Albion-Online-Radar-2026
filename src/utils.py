# Build: 7082a177e9f49255f1dcdb16689d31b0

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
