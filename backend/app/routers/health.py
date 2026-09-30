from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import get_engine

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Return service status and database connectivity."""
    database_status: str = "ok"
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception:
        database_status = "error"

    return {"status": "ok", "database": database_status}
