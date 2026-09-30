from pydantic import BaseModel, ConfigDict


class PlantBase(BaseModel):
    """Shared fields for a plant."""

    census_number: int | None = None
    common_name: str | None = None
    scientific_name: str | None = None
    origin: str | None = None
    dap: float | None = None
    trunk_shape: str | None = None
    height: float | None = None
    qr_code_url: str | None = None


class PlantCreate(PlantBase):
    """Payload used to create a plant."""


class PlantRead(PlantBase):
    """A plant returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
