from core.database import database
from models.jwt import (
    JWTRefreshJTIReference,
    JWTRefreshPersistence,
    JWTRefreshRecord,
)
from models.teacher import TeacherIdReference


async def get_refresh_token_by_id(
    jwt: JWTRefreshJTIReference,
) -> JWTRefreshRecord | None:
    raw_record = await database.fetchrow(
        "SELECT * FROM refresh_tokens WHERE jti = $1",
        jwt.jti,
    )
    return JWTRefreshRecord(**raw_record) if raw_record else None


async def get_refresh_token_by_user_id(
    user: TeacherIdReference,
) -> JWTRefreshRecord | None:
    raw_record = await database.fetchrow(
        "SELECT * FROM refresh_tokens WHERE user_id = $1",
        user.id,
    )
    return JWTRefreshRecord(**raw_record) if raw_record else None


async def create_refresh_token(jwt: JWTRefreshPersistence) -> JWTRefreshRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO refresh_tokens (user_id, jti, issued_at, expires_at) "
        "VALUES ($1, $2, $3, $4) RETURNING *",
        jwt.user_id,
        jwt.jti,
        jwt.issued_at,
        jwt.expires_at,
    )
    return JWTRefreshRecord(**raw_record) if raw_record else None


async def delete_refresh_token_by_jti(jwt: JWTRefreshJTIReference) -> None:
    await database.execute("DELETE FROM refresh_tokens WHERE jti=$1", jwt.jti)


async def delete_refresh_token_by_user_id(user: TeacherIdReference) -> None:
    await database.execute("DELETE FROM refresh_tokens WHERE user_id=$1", user.id)
