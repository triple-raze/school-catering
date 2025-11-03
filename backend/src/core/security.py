from core import config
from models.jwt import JWTAccessCreate, JWTRefreshCreate
from jose import jwt
import time
import nanoid
import bcrypt

def create_access_token(data: JWTAccessCreate) -> str:
    payload = {
        "iss": data.issuer,
        "sub": data.subscripter,
        "aud": data.audience,
        "iat": int(time.time()),
        "exp": int(time.time()) + config.JWT_ACCESS_LIFETIME,
        "type": data.token_type,
        "user_ip": data.user_ip
    }
    return jwt.encode(payload, config.JWT_KEY)

def decode_access_token(token: str, data: JWTAccessCreate) -> str:
    return jwt.decode(token, config.JWT_KEY, audience=data.audience, issuer=data.issuer)

def create_refresh_token() -> JWTRefreshCreate:
    refresh_token = JWTRefreshCreate(
        nanoid.generate(size=32),
        created_at=int(time.time()),
        expires_at=int(time.time()) + config.JWT_REFRESH_LIFETIME
    )
    return refresh_token
    
def encode(value: str) -> str:
    salt = bcrypt.gensalt()
    return str(bcrypt.hashpw(value, salt))


