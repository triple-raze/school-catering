from datetime import datetime, timedelta, timezone
from typing import Literal
from uuid import uuid4

import bcrypt
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from core import config
from models.jwt import JWTCreate, JWTInstance, JWTRefreshPeristence, JWTSingleToken


def _create_token(
    user_id: int,
    lifetime: timedelta,
    token_type: Literal["access", "refresh"],
) -> JWTInstance:
    iat_date = datetime.now(timezone.utc)
    exp_date = datetime.now(timezone.utc) + lifetime

    iat_timestamp = int(iat_date.timestamp())
    exp_timestamp = int(exp_date.timestamp())

    jti = str(uuid4())

    payload = {
        "iat": iat_timestamp,
        "exp": exp_timestamp,
        "jti": jti,
        "user_id": user_id,
        "type": token_type,
    }
    return JWTInstance(
        token=jwt.encode(payload, config.JWT_KEY),
        issued_at=iat_timestamp,
        expires_at=exp_timestamp,
        jti=jti,
        user_id=user_id,
        type=token_type,
    )


def create_access_token(data: JWTCreate) -> JWTInstance:
    return _create_token(data.user_id, config.JWT_ACCESS_LIFETIME, "access")


def create_refresh_token(data: JWTCreate) -> JWTInstance:
    return _create_token(data.user_id, config.JWT_REFRESH_LIFETIME, "refresh")


def decode_token(data: JWTSingleToken) -> JWTRefreshPeristence:
    raw_data = jwt.decode(data.token, config.JWT_KEY)
    return JWTRefreshPeristence(
        issued_at=raw_data["iat"],
        expires_at=raw_data["exp"],
        jti=raw_data["jti"],
        user_id=raw_data["user_id"],
    )


def verify_token(data: JWTSingleToken) -> None:
    jwt.decode(data.token, config.JWT_KEY)


def encode(value: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(value.encode(), salt).decode()


def verify_hash(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login")
