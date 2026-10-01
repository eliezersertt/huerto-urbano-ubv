from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import health, plants

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0",
)

# CORS is temporarily open ("*") so the deployed frontend (Vercel) can
# reach this API. Starlette echoes the origin when credentials are on.
# Restrict the origins once the frontend domain is fixed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(plants.router)


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a welcome message for the API."""
    return {"message": "Huerto Urbano API"}
