from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from fastapi import Depends, HTTPException, status, Request
from jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.scheme_name = "Bearer"
        self.tokenUrl = "http://localhost:8000/login"
        self.description = "JWT Authorization header using the Bearer scheme."

    async def __call__(self, request: Request):
        auth = await super(JWTBearer, self).__call__(request)
        data = validate_token(auth.credentials)
        if data.get("email") != "admin@fast.com":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
