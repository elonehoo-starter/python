from __future__ import annotations

def greet(name: str) -> str:
    """Return a friendly greeting.

    Examples
    --------
    >>> greet("World")
    'Hello, World!'
    """
    clean = name.strip() if name is not None else ""
    target = clean or "there"
    return f"Hello, {target}!"
