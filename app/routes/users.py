from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user, require_roles
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.auth_service import create_user
from app.services.user_service import (
    get_user_by_email,
    get_user_by_id,
    get_users,
    update_user,
)


router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
)


@router.get(
    "/",
    response_model=list[UserResponse],
)
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    return get_users(db)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado",
        )

    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201,
)
def create_new_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    existing_user = get_user_by_email(db, data.email)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="El correo electrónico ya está registrado",
        )

    return create_user(
        db=db,
        full_name=data.full_name,
        email=data.email,
        password=data.password,
        role=data.role,
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_existing_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles("admin")
    ),
):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado",
        )

    update_data = data.model_dump(
        exclude_unset=True
    )

    return update_user(
        db,
        user,
        update_data,
    )