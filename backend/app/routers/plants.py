import io

import qrcode
import qrcode.image.svg
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models.plant import Plant
from app.schemas.plant import PlantCreate, PlantRead

router = APIRouter(prefix="/plants", tags=["plants"])


@router.get("", response_model=list[PlantRead])
def list_plants(db: Session = Depends(get_db)) -> list[Plant]:
    """Return all plants ordered by census number."""
    return list(
        db.scalars(select(Plant).order_by(Plant.census_number))
    )


@router.get("/census/{census_number}", response_model=PlantRead)
def get_plant_by_census(
    census_number: int,
    db: Session = Depends(get_db),
) -> Plant:
    """Return a single plant by its census number (the physical plate)."""
    plant: Plant | None = db.scalars(
        select(Plant).where(Plant.census_number == census_number)
    ).first()
    if plant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Planta no encontrada",
        )
    return plant


@router.get("/{plant_id}", response_model=PlantRead)
def get_plant(plant_id: int, db: Session = Depends(get_db)) -> Plant:
    """Return a single plant by id."""
    plant: Plant | None = db.get(Plant, plant_id)
    if plant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Planta no encontrada",
        )
    return plant


@router.get("/{plant_id}/qr", response_class=Response)
def get_plant_qr(plant_id: int, db: Session = Depends(get_db)) -> Response:
    """Return a QR code (SVG) that links to the plant web route."""
    plant: Plant | None = db.get(Plant, plant_id)
    if plant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Planta no encontrada",
        )

    target = plant.qr_code_url or (
        f"{settings.public_base_url}/planta/{plant.census_number}"
    )

    image = qrcode.make(
        target,
        image_factory=qrcode.image.svg.SvgImage,
        box_size=12,
    )
    buffer = io.BytesIO()
    image.save(buffer)

    return Response(
        content=buffer.getvalue(),
        media_type="image/svg+xml",
    )


@router.post(
    "",
    response_model=PlantRead,
    status_code=status.HTTP_201_CREATED,
)
def create_plant(
    payload: PlantCreate,
    db: Session = Depends(get_db),
) -> Plant:
    """Create a new plant."""
    plant = Plant(**payload.model_dump())
    db.add(plant)
    db.commit()
    db.refresh(plant)
    return plant
