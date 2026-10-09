from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.core.middleware import configure_middleware
from app.db.init_db import init_db
from app.routes.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "API para la gestión del "
        "Hospital Los Olivos"
    ),
    lifespan=lifespan,
)


configure_middleware(app)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "mensaje": "API del Hospital Los Olivos funcionando correctamente"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "servicio": "Hospital Los Olivos API",
    }