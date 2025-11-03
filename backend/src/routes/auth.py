from models.teacher import TeacherCreate, TeacherRecord
from models.jwt import JWTAccessCreate, JWTRefreshPeristence
from core import security
import crud
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register_account(teacher: TeacherCreate, request: Request):
    teacher: TeacherRecord = crud.teacher.insert_teacher(teacher)
    
    url = f"{request.url.scheme}://{request.url.hostname}"

    data = JWTAccessCreate(
        issuer=url,
        subscripter=teacher.id,
        audience=url,
    )

    access_token = security.create_access_token(data)
    raw_refresh_token = security.create_refresh_token()

    refresh_token = JWTRefreshPeristence(
        user_id=teacher.id,
        token_hash=security.encode(raw_refresh_token),
        created_at=raw_refresh_token.created_at,
        expires_at=raw_refresh_token.expires_at
    )

    crud.jwt.insert_refresh_token(refresh_token)

    return JSONResponse({"refresh_token": refresh_token, "access_token": access_token}, status_code=201)
