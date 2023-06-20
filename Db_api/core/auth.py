from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from ..models.UserModel import UserModel
from core.config import settings
from core.security import verify_password



oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/users/login"
)


async def authenticate(email: str, password: str, db: AsyncSession) -> Optional[UserModel]:
    async with db as session:
        query = select(UserModel).filter(UserModel.email == email)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()

        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        return user


def _create_token(type_token: str, life_time: timedelta, sub: str) -> str:
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    payload = {}

    sp = timezone('America/Sao_Paulo')
    expire = datetime.now(tz=sp) + life_time

    payload["type"] = type_token

    payload["exp"] = expire

    payload["iat"] = datetime.now(tz=sp)

    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def create_acess_token(sub: str) -> str:
    """
    https://jwt.io
    """
    return _create_token(
        type_token='access_token',
        life_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )