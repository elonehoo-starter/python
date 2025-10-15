from __future__ import annotations

from pathlib import Path
from glob import glob


def main() -> None:
    import uvicorn  # noqa: WPS433 (import after path changes)

    # Start FastAPI app with auto-reload during development
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        factory=False,
    )


if __name__ == "__main__":
    main()
