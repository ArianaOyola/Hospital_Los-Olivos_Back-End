from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.appointment import Appointment


def get_appointment_by_id(
    db: Session,
    appointment_id: int,
) -> Appointment | None:
    return db.scalar(
        select(Appointment).where(
            Appointment.id == appointment_id
        )
    )


def get_appointments(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[Appointment]:
    return list(
        db.scalars(
            select(Appointment)
            .order_by(Appointment.appointment_date)
            .offset(skip)
            .limit(limit)
        ).all()
    )


def create_appointment(
    db: Session,
    data: dict,
) -> Appointment:
    appointment = Appointment(**data)

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment


def update_appointment(
    db: Session,
    appointment: Appointment,
    data: dict,
) -> Appointment:
    for key, value in data.items():
        if value is not None:
            setattr(appointment, key, value)

    db.commit()
    db.refresh(appointment)

    return appointment