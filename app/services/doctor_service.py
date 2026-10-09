from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.doctor import Doctor


def get_doctor_by_id(
    db: Session,
    doctor_id: int,
) -> Doctor | None:
    return db.scalar(
        select(Doctor).where(Doctor.id == doctor_id)
    )


def get_doctors(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[Doctor]:
    return list(
        db.scalars(
            select(Doctor)
            .offset(skip)
            .limit(limit)
        ).all()
    )


def create_doctor(
    db: Session,
    data: dict,
) -> Doctor:
    doctor = Doctor(**data)

    db.add(doctor)
    db.commit()
    db.refresh(doctor)

    return doctor