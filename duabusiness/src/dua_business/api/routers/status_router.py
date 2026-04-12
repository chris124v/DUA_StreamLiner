from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/status", tags=["status"])


@router.get("/{generation_id}")
def get_status(generation_id: str) -> dict[str, str]:
    _ = generation_id
    raise HTTPException(status_code=501, detail="Contract only")
