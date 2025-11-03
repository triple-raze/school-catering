from pydantic import BaseModel
from typing import Literal

class RefreshJWTReference(BaseModel):
    id: int

class RefreshJWTCreate(BaseModel):
    user_id: int
    token_hash: str
    expires_at: int
    created_at: int

class AccessJWTCreate(BaseModel):
    issuer: str
    subscripter: str
    audience: str
    token_type: Literal["access", "refresh"]
    user_ip: str
