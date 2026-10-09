from datetime import datetime

from pydantic import EmailStr, Field

from app.schemas.base import BaseSchema


class UserCreate(BaseSchema):
    full_name: str = Field(min_length=2, max_length=150)
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)
    role: str = "patient"


class UserUpdate(BaseSchema):
    full_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=150,
    )
    email: EmailStr | None = None
    role: str | None = None
    is_active: bool | None = None


class UserResponse(BaseSchema):
    id: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime