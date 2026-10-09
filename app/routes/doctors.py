from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_roles
from app.models.user import User
from app.schemas.doctor import (
    DoctorCreate,
    DoctorResponse,
    DoctorUpdate,
)
from app.services.doctor_service import (
    create_doctor,
    get_doctor_by_id,
    get_doctors,
)


router = APIRouter(
    prefix="/doctors",
    tags=["Médicos"],
)


@router.get(
    "/",
    response_model=list[DoctorResponse],
)
def list_doctors(
    db: Session = Depends(get_db),
):
    return get_doctors(db)


@router.get(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    doctor = get_doctor_by_id(db, doctor_id)

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Médico no encontrado",
        )

    return doctor


@router.post(
    "/",
    response_model=DoctorResponse,
    status_code=201,
)
def create_new_doctor(
    data: DoctorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    return create_doctor(
        db,
        data.model_dump(),
    )