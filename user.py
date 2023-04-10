from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "example@org.com",
                "password": "s~ldi7r44eAKS47___12#1"
            }
        }