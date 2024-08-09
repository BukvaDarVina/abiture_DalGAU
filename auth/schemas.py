import uuid
from typing import Optional

from fastapi_users import schemas, models


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: models.ID
    name: str
    lastname: str
    surname: str
    role_id: int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    name: str
    lastname: str
    surname: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass