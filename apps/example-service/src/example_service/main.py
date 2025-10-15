from __future__ import annotations

import sys
from pathlib import Path
from glob import glob
from fastapi import FastAPI


def _bootstrap_monorepo_paths() -> None:
    """Add all packages/*/src directories to sys.path for local development."""
    root = Path(__file__).resolve().parents[4]
    for src in glob(str(root / "packages" / "*" / "src")):
        if src not in sys.path:
            sys.path.insert(0, src)


_bootstrap_monorepo_paths()

from base_api import health, info  # noqa: E402
from example_util import greet  # noqa: E402


app = FastAPI(title="example-service")
app.include_router(health)
app.include_router(info)


@app.get("/greet/{name}", summary="Greet someone")
def greet_api(name: str) -> dict[str, str]:
    return {"message": greet(name)}


# For `uvicorn example_service.main:app --reload`
__all__ = ["app"]
