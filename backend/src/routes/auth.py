from fastapi import FastAPI
from fastapi.responses import JSONResponse

from core.database import database_init
from models.jwt import JWTSingleToken
from models.teacher import TeacherLogin, TeacherRegister
from services import auth_service

router = FastAPI(prefix="/auth", lifespan=database_init)


@router.post("/register")
async def register_account(data: TeacherRegister) -> JSONResponse:
    tokens = await auth_service.register(data)

    return JSONResponse(
        {
            "access": tokens.access_token,
            "refresh": tokens.refresh_token,
        },
        status_code=201,
    )


@router.post("/login")
async def login_account(data: TeacherLogin) -> JSONResponse:
    tokens = await auth_service.login(data)

    return JSONResponse(
        {
            "access": tokens.access_token,
            "refresh": tokens.refresh_token,
        },
        status_code=201,
    )


@router.post("/refresh")
async def refresh_access_token(refresh_token: JWTSingleToken) -> JSONResponse:
    data = await auth_service.refresh(refresh_token)

    return JSONResponse({"access": data.token}, status_code=201)


@router.post("/logout")
async def logout_from_account(refreah_token: JWTSingleToken) -> JSONResponse:
    await auth_service.logout(refreah_token)

    return JSONResponse({"detail": "Success"}, status_code=200)


@router.post("/delete")
async def delete_account(teacher: TeacherLogin) -> JSONResponse:
    await auth_service.delete(teacher)

    return JSONResponse({"detail": "Success"}, status_code=200)
