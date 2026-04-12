from fastapi import FastAPI

from dua_business.api.routers.auth_router import router as auth_router
from dua_business.api.routers.dua_router import router as dua_router
from dua_business.api.routers.health_router import router as health_router
from dua_business.api.routers.logout_router import router as logout_router
from dua_business.api.routers.result_router import router as result_router
from dua_business.api.routers.status_router import router as status_router
from dua_business.api.routers.upload_router import router as upload_router

app = FastAPI(title="DUA Business API Skeleton")
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(dua_router)
app.include_router(status_router)
app.include_router(upload_router)
app.include_router(result_router)
app.include_router(logout_router)
