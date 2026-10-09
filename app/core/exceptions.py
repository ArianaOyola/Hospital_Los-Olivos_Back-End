from fastapi import HTTPException, status


class CredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Recurso no encontrado"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class ConflictException(HTTPException):
    def __init__(self, detail: str = "El recurso ya existe"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )