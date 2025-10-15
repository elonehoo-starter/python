from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/info", summary="Service info")
def get_info() -> dict[str, str]:
    # 简化实现：在运行期可注入真实服务名与版本
    return {"name": "api", "version": "0.1.0"}
