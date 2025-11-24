from core import security
from exceptions.auth import (
    InvalidPasswordException,
    UserAlreadyExistsException,
    UserNotFoundException,
)
from models.jwt import JWTCreate, JWTPairTokens, JWTRefreshPeristence, JWTSingleToken
from models.teacher import (
    TeacherCreate,
    TeacherIdReference,
    TeacherLogin,
    TeacherRecord,
    TeacherRegister,
)
from repositories import jwt_repository, teacher_repository


async def _create_tokens(teacher: TeacherIdReference) -> JWTPairTokens:
    create_token_data = JWTCreate(user_id=teacher.id)

    access_token_data = security.create_access_token(create_token_data)
    refresh_token_data = security.create_refresh_token(create_token_data)

    refresh_token_record = JWTRefreshPeristence(
        user_id=teacher.id,
        jti=refresh_token_data.jti,
        issued_at=refresh_token_data.issued_at,
        expires_at=refresh_token_data.expires_at,
    )

    await jwt_repository.create_refresh_token(refresh_token_record)

    return JWTPairTokens(
        access_token=access_token_data.token,
        refresh_token=refresh_token_data.token,
    )


async def _verify_login_data(login_teacher_data: TeacherLogin) -> TeacherRecord:
    teacher_record = await teacher_repository.get_teacher_by_login(
        login_teacher_data,
    )

    if not teacher_record:
        raise UserNotFoundException

    verified = security.verify_hash(
        login_teacher_data.password,
        teacher_record.password_hash,
    )

    if not verified:
        raise InvalidPasswordException

    await jwt_repository.delete_refresh_token_by_user_id(teacher_record)

    return teacher_record


def _hash_teacher_password(teacher: TeacherRegister) -> TeacherCreate:
    password_hash = security.encode(teacher.password)

    return TeacherCreate(
        login=teacher.login,
        password_hash=password_hash,
        first_name=teacher.first_name,
        second_name=teacher.second_name,
        patronymic=teacher.patronymic,
    )


async def register(user_create_teacher_data: TeacherRegister) -> JWTPairTokens:
    create_teacher_data = _hash_teacher_password(user_create_teacher_data)

    account_exists = await teacher_repository.get_teacher_by_login(
        user_create_teacher_data,
    )

    if account_exists:
        raise UserAlreadyExistsException

    teacher_record = await teacher_repository.create_teacher(create_teacher_data)

    return await _create_tokens(teacher_record)


async def login(teacher: TeacherLogin) -> JWTPairTokens:
    teacher_record = await _verify_login_data(teacher)

    return await _create_tokens(teacher_record)


async def refresh(refresh_token: JWTSingleToken) -> JWTSingleToken:
    token_data = security.decode_token(refresh_token)

    jwt = security.create_access_token(token_data)

    return JWTSingleToken(token=jwt.token)


async def logout(refresh_token: JWTSingleToken) -> None:
    token = security.decode_token(refresh_token)

    await jwt_repository.delete_refresh_token_by_jti(token)


async def delete(
    delete_teacher_data: TeacherLogin,
) -> None:
    await _verify_login_data(delete_teacher_data)

    teacher = await teacher_repository.get_teacher_by_login(delete_teacher_data)

    teacher_reference = TeacherIdReference(id=teacher.id)

    await jwt_repository.delete_refresh_token_by_user_id(teacher_reference)

    await teacher_repository.delete_teacher_by_id(teacher_reference)
