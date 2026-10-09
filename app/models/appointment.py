from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("doctors.id"),
        nullable=False,
    )

    appointment_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="scheduled",
        nullable=False,
    )

    reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    patient: Mapped["Patient"] = relationship(
        "Patient",
        back_populates="appointments",
    )

    doctor: Mapped["Doctor"] = relationship(
        "Doctor",
        back_populates="appointments",
    )

    medical_record: Mapped["MedicalRecord | None"] = relationship(
        "MedicalRecord",
        back_populates="appointment",
        uselist=False,
    )