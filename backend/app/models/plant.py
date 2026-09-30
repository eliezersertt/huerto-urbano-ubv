from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Plant(Base):
    """A plant registered in the urban garden census."""

    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    census_number: Mapped[int | None] = mapped_column(Integer, unique=True)

    common_name: Mapped[str | None] = mapped_column(String(120))

    scientific_name: Mapped[str | None] = mapped_column(String(160))

    origin: Mapped[str | None] = mapped_column(String(120))

    dap: Mapped[float | None] = mapped_column(Float)

    trunk_shape: Mapped[str | None] = mapped_column(String(80))

    height: Mapped[float | None] = mapped_column(Float)

    qr_code_url: Mapped[str | None] = mapped_column(String(500), index=True)
