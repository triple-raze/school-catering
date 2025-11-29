from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel


class JWTCreate(BaseModel):
    user_id: int


class JWTInstance(JWTCreate):
    token: str
    jti: UUID
    issued_at: int
    expires_at: int
    type: Literal["access", "refresh"]


class JWTRefreshJTIReference(BaseModel):
    jti: UUID


class JWTRefreshPersistence(BaseModel):
    user_id: int
    jti: UUID
    issued_at: datetime
    expires_at: datetime


class JWTRefreshRecord(JWTRefreshPersistence):
    id: int


class JWTPairTokens(BaseModel):
    refresh_token: str
    access_token: str


class JWTSingleToken(BaseModel):
    token: str
