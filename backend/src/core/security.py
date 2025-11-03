from core.config import Config
from models.jwt import AccessJWTCreate
from jose import jwt
import time
import nanoid

class JWTService:
    def create_access_token(data: AccessJWTCreate) -> str:
        payload = {
            "iss": data.issuer,
            "sub": data.subscripter,
            "aud": data.audience,
            "iat": int(time.time()),
            "exp": int(time.time()) + Config.JWT_ACCESS_LIFETIME,
            "type": data.token_type,
            "user_ip": data.user_ip
        }
        return jwt.encode(payload, Config.JWT_KEY)

    def decode_access_token(token: str, data: AccessJWTCreate) -> str:
        return jwt.decode(token, Config.JWT_KEY, audience=data.audience, issuer=data.issuer)

    def create_refresh_token() -> str:
        return nanoid.generate(size=32)
    


