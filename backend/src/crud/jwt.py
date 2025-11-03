from core.database import database
from models.jwt import JWTRefreshPeristence, JWTRefreshReference
from asyncpg import Record

async def get_refresh_token(jwt: JWTRefreshReference):
    return await database.fetchrow(
        "SELECT * FROM refresh_tokens WHERE id = $1", (jwt.id,)
    )

async def insert_refresh_token(jwt: JWTRefreshPeristence):
    return await database.execute(
        "INSERT INTO refresh_tokens (user_id, token_hash, created_at, expires_at) VALUES ($1, $2, $3) RETURNING *", 
        (jwt.user_id, jwt.token_hash, jwt.created_at, jwt.expires_at)
    )

async def delete_refresh_token(jwt: JWTRefreshReference):
    await database.execute(
        "DELETE FROM refresh_tokens WHERE id=$1", (jwt.id,)
    )
