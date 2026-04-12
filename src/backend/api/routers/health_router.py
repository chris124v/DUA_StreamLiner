from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
def live() -> dict[str, str]:
    raise HTTPException(status_code=501, detail="Contract only")


@router.get("/ready")
def ready() -> dict[str, str]:
    raise HTTPException(status_code=501, detail="Contract only")
