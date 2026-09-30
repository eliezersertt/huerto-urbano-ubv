from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Plant(Base):
    """A plant registered in the urban garden."""

    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    nombre_comun: Mapped[str] = mapped_column(String(120), nullable=False)

    especie_cientifica: Mapped[str | None] = mapped_column(String(160))

    descripcion: Mapped[str | None] = mapped_column(Text)

    qr_code_url: Mapped[str | None] = mapped_column(String(500), index=True)
