from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv('.env.dev')

@dataclass
class Setting:
    JWT_SECRET_KEY: str

settings = Setting(
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
)