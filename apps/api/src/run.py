from __future__ import annotations

import sys
from pathlib import Path
from glob import glob


def _bootstrap_monorepo_paths() -> None:
    root = Path(__file__).resolve().parents[4]
    for src in glob(str(root / "packages" / "*" / "src")):
        if src not in sys.path:
            sys.path.insert(0, src)
    for app_src in glob(str(root / "apps" / "*" / "src")):
        if app_src not in sys.path:
            sys.path.insert(0, app_src)


def main() -> None:
    _bootstrap_monorepo_paths()
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
