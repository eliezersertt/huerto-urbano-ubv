from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.plant import Plant
from app.schemas.plant import PlantCreate, PlantRead

router = APIRouter(prefix="/plants", tags=["plants"])


@router.get("", response_model=list[PlantRead])
def list_plants(db: Session = Depends(get_db)) -> list[Plant]:
    """Return all plants ordered by id."""
    return list(db.scalars(select(Plant).order_by(Plant.id)))


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
