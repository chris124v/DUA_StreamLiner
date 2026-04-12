from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/logout", tags=["logout"])


@router.post("")
def logout() -> dict[str, str]:
    raise HTTPException(status_code=501, detail="Contract only")
