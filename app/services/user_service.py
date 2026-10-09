from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User


def get_user_by_id(
    db: Session,
    user_id: int,
) -> User | None:
    return db.scalar(
        select(User).where(User.id == user_id)
    )


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    return db.scalar(
        select(User).where(User.email == email)
    )


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[User]:
    return list(
        db.scalars(
            select(User)
            .offset(skip)
            .limit(limit)
        ).all()
    )


def update_user(
    db: Session,
    user: User,
    data: dict,
) -> User:
    if "password" in data:
        data["password_hash"] = hash_password(
            data.pop("password")
        )

    for key, value in data.items():
        if value is not None:
            setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user