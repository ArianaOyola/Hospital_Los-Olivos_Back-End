from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models.user import User
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
    AppointmentUpdate,
)
from app.services.appointment_service import (
    create_appointment,
    get_appointment_by_id,
    get_appointments,
    update_appointment,
)


router = APIRouter(
    prefix="/appointments",
    tags=["Citas"],
)


@router.get(
    "/",
    response_model=list[AppointmentResponse],
)
def list_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_appointments(db)


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse,
)
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    appointment = get_appointment_by_id(
        db,
        appointment_id,
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Cita no encontrada",
        )

    return appointment


@router.post(
    "/",
    response_model=AppointmentResponse,
    status_code=201,
)
def create_new_appointment(
    data: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin", "doctor")
    ),
):
    return create_appointment(
        db,
        data.model_dump(),
    )


@router.put(
    "/{appointment_id}",
    response_model=AppointmentResponse,
)
def update_existing_appointment(
    appointment_id: int,
    data: AppointmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin", "doctor")
    ),
):
    appointment = get_appointment_by_id(
        db,
        appointment_id,
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Cita no encontrada",
        )

    return update_appointment(
        db,
        appointment,
        data.model_dump(
            exclude_unset=True
        ),
    )