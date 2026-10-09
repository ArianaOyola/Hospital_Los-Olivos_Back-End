from datetime import datetime

from app.schemas.base import BaseSchema


class AppointmentCreate(BaseSchema):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: str | None = None


class AppointmentUpdate(BaseSchema):
    appointment_date: datetime | None = None
    status: str | None = None
    reason: str | None = None


class AppointmentResponse(BaseSchema):
    id: int
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    status: str
    reason: str | None