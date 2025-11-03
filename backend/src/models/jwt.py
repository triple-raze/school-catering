from pydantic import BaseModel
from typing import Literal

class JWTRefreshReference(BaseModel):
    id: int

class JWTRefreshCreate(BaseModel):
    token: str
    expires_at: int
    created_at: int

class JWTRefreshPeristence(BaseModel):
    user_id: int
    token_hash: str
    expires_at: int
    created_at: int

class JWTRefreshRecord(JWTRefreshPeristence):
    id: int

class JWTAccessCreate(BaseModel):
    issuer: str
    subscripter: str
    audience: str
