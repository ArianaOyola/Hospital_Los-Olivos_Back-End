from datetime import datetime

from app.schemas.base import BaseSchema


class MedicalRecordCreate(BaseSchema):
    patient_id: int
    doctor_id: int
    appointment_id: int | None = None
    diagnosis: str
    treatment: str | None = None
    notes: str | None = None


class MedicalRecordUpdate(BaseSchema):
    diagnosis: str | None = None
    treatment: str | None = None
    notes: str | None = None


class MedicalRecordResponse(BaseSchema):
    id: int
    patient_id: int
    doctor_id: int
    appointment_id: int | None
    diagnosis: str
    treatment: str | None
    notes: str | None
    created_at: datetime