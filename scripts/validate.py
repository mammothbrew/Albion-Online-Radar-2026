# Build: 04f94a4bddfde6ed02389cc9b2e68f83

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
