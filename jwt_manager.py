from jwt import encode, decode
from settings import settings

def create_token(data, secret: str=settings.JWT_SECRET_KEY, algorithm="HS256") -> str:
    return encode(data, secret, algorithm=algorithm)

def validate_token(token: str, secret: str=settings.JWT_SECRET_KEY, algorithms=["HS256"]) -> dict:
    return decode(token, secret, algorithms=algorithms)