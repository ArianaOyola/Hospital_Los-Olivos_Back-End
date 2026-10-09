from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("doctors.id"),
        nullable=False,
    )

    appointment_id: Mapped[int | None] = mapped_column(
        ForeignKey("appointments.id"),
        unique=True,
        nullable=True,
    )

    diagnosis: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    treatment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    patient: Mapped["Patient"] = relationship(
        "Patient",
        back_populates="medical_records",
    )

    doctor: Mapped["Doctor"] = relationship(
        "Doctor",
        back_populates="medical_records",
    )

    appointment: Mapped["Appointment | None"] = relationship(
        "Appointment",
        back_populates="medical_record",
    )