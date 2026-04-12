from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login() -> dict[str, str]:
    raise HTTPException(status_code=501, detail="Contract only")
