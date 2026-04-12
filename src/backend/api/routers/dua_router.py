from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/dua", tags=["dua"])


@router.post("")
def create_dua() -> dict[str, str]:
    raise HTTPException(status_code=501, detail="Contract only")
