from fastapi import FastAPI , APIRouter , Depends
from helper.config import get_settings , Settings





base_router = APIRouter(
    prefix = "/api/v1",
    tags=['api_v1']
)

@base_router.get("/")
async def home(app_settings:Settings = Depends(get_settings)):
    # Access the environment variables
    APP_NAME = app_settings.APP_NAME
    APP_VERSION = app_settings.APP_VERSION

    return {"APP_NAME" : APP_NAME ,
            "APP_VERSION" : APP_VERSION}