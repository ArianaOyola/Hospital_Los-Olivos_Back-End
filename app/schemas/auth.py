from pydantic import EmailStr, Field

from app.schemas.base import BaseSchema


class LoginRequest(BaseSchema):
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)


class TokenResponse(BaseSchema):
    access_token: str
    token_type: str = "bearer"