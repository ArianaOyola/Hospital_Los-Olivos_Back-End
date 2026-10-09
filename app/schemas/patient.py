from datetime import date

from pydantic import Field

from app.schemas.base import BaseSchema


class PatientCreate(BaseSchema):
    user_id: int
    document_number: str = Field(
        min_length=8,
        max_length=20,
    )
    phone: str | None = None
    birth_date: date | None = None
    address: str | None = None


class PatientUpdate(BaseSchema):
    phone: str | None = None
    birth_date: date | None = None
    address: str | None = None


class PatientResponse(BaseSchema):
    id: int
    user_id: int
    document_number: str
    phone: str | None
    birth_date: date | None
    address: str | None