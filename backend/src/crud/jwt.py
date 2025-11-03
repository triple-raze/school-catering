from core.database import database
from models.jwt import RefreshJWTCreate, RefreshJWTReference
from asyncpg import Record

class JWTGateway:
    async def get_refresh_token(jwt: RefreshJWTReference):
        return await database.fetchrow(
            "SELECT * FROM refresh_tokens WHERE id = $1", (jwt.id,)
        )

    async def create_refresh_token(jwt: RefreshJWTCreate):
        await database.execute(
            "INSERT INTO refresh_tokens (user_id, token_hash, created_at, expires_at) VALUES ($1, $2, $3)"
            (jwt.user_id, jwt.token_hash, jwt.created_at, jwt.expires_at)
        )

    async def delete_refresh_token(jwt: RefreshJWTReference):
        await database.execute(
            "DELETE FROM refresh_tokens WHERE id=$1", (jwt.id,)
        )
