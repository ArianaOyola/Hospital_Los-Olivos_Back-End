from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    document_number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    birth_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        String(250),
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="patient",
    )

    appointments: Mapped[list["Appointment"]] = relationship(
        "Appointment",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    medical_records: Mapped[list["MedicalRecord"]] = relationship(
        "MedicalRecord",
        back_populates="patient",
        cascade="all, delete-orphan",
    )