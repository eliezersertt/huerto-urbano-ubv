from collections.abc import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

_engine: Engine | None = None


def get_engine() -> Engine:
    """Create the database engine on first use."""
    global _engine

    if _engine is None:
        if not settings.database_url:
            raise RuntimeError(
                "DATABASE_URL is not set. Add your Supabase connection "
                "string to backend/.env"
            )
        _engine = create_engine(
            settings.database_url,
            pool_pre_ping=True,
        )

    return _engine


def get_session_factory() -> sessionmaker[Session]:
    """Return a session factory bound to the database engine."""
    return sessionmaker(bind=get_engine(), autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


def get_db() -> Generator[Session, None, None]:
    """Provide a database session per request."""
    db: Session = get_session_factory()()
    try:
        yield db
    finally:
        db.close()
