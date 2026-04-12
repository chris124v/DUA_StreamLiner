from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/result", tags=["result"])


@router.get("/{generation_id}")
def result(generation_id: str) -> dict[str, str]:
    _ = generation_id
    raise HTTPException(status_code=501, detail="Contract only")
