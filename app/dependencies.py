from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.exceptions import CredentialsException
from app.core.security import decode_access_token
from app.database import get_db
from app.models.user import User
from app.services.user_service import get_user_by_id


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise CredentialsException()

    user_id = payload.get("sub")

    if not user_id:
        raise CredentialsException()

    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        raise CredentialsException()

    user = get_user_by_id(db, user_id)

    if not user or not user.is_active:
        raise CredentialsException()

    return user


def require_roles(*roles: str):
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in roles:
            raise CredentialsException()

        return current_user

    return role_dependency