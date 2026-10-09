from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if not user:
        return None

    if not user.is_active:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user


def create_user(
    db: Session,
    full_name: str,
    email: str,
    password: str,
    role: str = "patient",
) -> User:
    user = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
        role=role,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def create_user_token(user: User) -> str:
    return create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role": user.role,
        }
    )