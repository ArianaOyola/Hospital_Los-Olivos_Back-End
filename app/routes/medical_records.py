from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models.user import User
from app.schemas.medical_record import (
    MedicalRecordCreate,
    MedicalRecordResponse,
)
from app.services.medical_record_service import (
    create_medical_record,
    get_medical_record_by_id,
    get_medical_records,
)


router = APIRouter(
    prefix="/medical-records",
    tags=["Historias clínicas"],
)


@router.get(
    "/",
    response_model=list[MedicalRecordResponse],
)
def list_medical_records(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin", "doctor")
    ),
):
    return get_medical_records(db)


@router.get(
    "/{record_id}",
    response_model=MedicalRecordResponse,
)
def get_medical_record(
    record_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    record = get_medical_record_by_id(
        db,
        record_id,
    )

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Historia clínica no encontrada",
        )

    return record


@router.post(
    "/",
    response_model=MedicalRecordResponse,
    status_code=201,
)
def create_new_medical_record(
    data: MedicalRecordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin", "doctor")
    ),
):
    return create_medical_record(
        db,
        data.model_dump(),
    )