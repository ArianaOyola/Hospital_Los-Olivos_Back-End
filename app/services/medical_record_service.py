from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.medical_record import MedicalRecord


def get_medical_record_by_id(
    db: Session,
    record_id: int,
) -> MedicalRecord | None:
    return db.scalar(
        select(MedicalRecord).where(
            MedicalRecord.id == record_id
        )
    )


def get_medical_records(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[MedicalRecord]:
    return list(
        db.scalars(
            select(MedicalRecord)
            .order_by(MedicalRecord.created_at.desc())
            .offset(skip)
            .limit(limit)
        ).all()
    )


def create_medical_record(
    db: Session,
    data: dict,
) -> MedicalRecord:
    record = MedicalRecord(**data)

    db.add(record)
    db.commit()
    db.refresh(record)

    return record