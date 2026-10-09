from app.schemas.base import BaseSchema


class DoctorCreate(BaseSchema):
    user_id: int
    specialty: str
    license_number: str
    phone: str | None = None


class DoctorUpdate(BaseSchema):
    specialty: str | None = None
    license_number: str | None = None
    phone: str | None = None


class DoctorResponse(BaseSchema):
    id: int
    user_id: int
    specialty: str
    license_number: str
    phone: str | None