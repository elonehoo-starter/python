from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Health check")
def get_health() -> dict[str, str]:
    return {"status": "ok"}
