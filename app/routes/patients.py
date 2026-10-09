from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models.user import User
from app.schemas.patient import (
    PatientCreate,
    PatientResponse,
    PatientUpdate,
)
from app.services.patient_service import (
    create_patient,
    get_patient_by_id,
    get_patients,
    update_patient,
)


router = APIRouter(
    prefix="/patients",
    tags=["Pacientes"],
)


@router.get(
    "/",
    response_model=list[PatientResponse],
)
def list_patients(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin", "doctor")
    ),
):
    return get_patients(db)


@router.get(
    "/{patient_id}",
    response_model=PatientResponse,
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    patient = get_patient_by_id(db, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado",
        )

    return patient


@router.post(
    "/",
    response_model=PatientResponse,
    status_code=201,
)
def create_new_patient(
    data: PatientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    return create_patient(
        db,
        data.model_dump(),
    )


@router.put(
    "/{patient_id}",
    response_model=PatientResponse,
)
def update_existing_patient(
    patient_id: int,
    data: PatientUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    patient = get_patient_by_id(db, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado",
        )

    return update_patient(
        db,
        patient,
        data.model_dump(
            exclude_unset=True
        ),
    )