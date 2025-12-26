from fastapi import FastAPI

from app.api.v1 import auth
from app.core.configs import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(auth.router, prefix=settings.API_V1_STR, tags=["Authentication"])


@app.get("/")
async def root():
    return {"message": "Health check: API is running"}
