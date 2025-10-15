from __future__ import annotations

# Re-export routers at top-level to keep `from base_api import health, info` working
from routers import health, info  # type: ignore[F401]

__all__ = ["health", "info"]
