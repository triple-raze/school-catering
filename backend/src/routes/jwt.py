from models.jwt import AccessJWTCreate
from core.security import JWTService
from crud.jwt import JWTGateway
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import APIRouter

router = APIRouter(prefix="/jwt")

@router.post("/register")
async def register_account(data: AccessJWTCreate):
    access_token = JWTService.create_access_token(data)
    refresh_token = JWTService.create_refresh_token()
