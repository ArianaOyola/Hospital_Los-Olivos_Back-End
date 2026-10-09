from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    specialty: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    license_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="doctor",
    )

    appointments: Mapped[list["Appointment"]] = relationship(
        "Appointment",
        back_populates="doctor",
        cascade="all, delete-orphan",
    )

    medical_records: Mapped[list["MedicalRecord"]] = relationship(
        "MedicalRecord",
        back_populates="doctor",
        cascade="all, delete-orphan",
    )