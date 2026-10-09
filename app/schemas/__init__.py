from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
    AppointmentUpdate,
)
from app.schemas.doctor import (
    DoctorCreate,
    DoctorResponse,
    DoctorUpdate,
)
from app.schemas.medical_record import (
    MedicalRecordCreate,
    MedicalRecordResponse,
    MedicalRecordUpdate,
)
from app.schemas.patient import (
    PatientCreate,
    PatientResponse,
    PatientUpdate,
)
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)

__all__ = [
    "LoginRequest",
    "TokenResponse",
    "AppointmentCreate",
    "AppointmentResponse",
    "AppointmentUpdate",
    "DoctorCreate",
    "DoctorResponse",
    "DoctorUpdate",
    "MedicalRecordCreate",
    "MedicalRecordResponse",
    "MedicalRecordUpdate",
    "PatientCreate",
    "PatientResponse",
    "PatientUpdate",
    "UserCreate",
    "UserResponse",
    "UserUpdate",
]