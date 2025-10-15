from __future__ import annotations

from fastapi import FastAPI

from base_api import health, info
from shared import greet


app = FastAPI(title="api")
app.include_router(health)
app.include_router(info)


@app.get("/greet/{name}", summary="Greet someone")
def greet_api(name: str) -> dict[str, str]:
    return {"message": greet(name)}


__all__ = ["app", "greet_api"]
