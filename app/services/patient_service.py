from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.patient import Patient


def get_patient_by_id(
    db: Session,
    patient_id: int,
) -> Patient | None:
    return db.scalar(
        select(Patient).where(Patient.id == patient_id)
    )


def get_patients(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[Patient]:
    return list(
        db.scalars(
            select(Patient)
            .offset(skip)
            .limit(limit)
        ).all()
    )


def create_patient(
    db: Session,
    data: dict,
) -> Patient:
    patient = Patient(**data)

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient


def update_patient(
    db: Session,
    patient: Patient,
    data: dict,
) -> Patient:
    for key, value in data.items():
        if value is not None:
            setattr(patient, key, value)

    db.commit()
    db.refresh(patient)

    return patient