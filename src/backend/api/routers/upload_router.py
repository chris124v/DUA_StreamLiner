from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/{generation_id}")
def upload(generation_id: str) -> dict[str, str]:
    _ = generation_id
    raise HTTPException(status_code=501, detail="Contract only")
