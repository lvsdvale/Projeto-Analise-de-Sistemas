from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    
    api: str = '/api/'
    DB_URL: str = 'postgresql+asyncpg://UTF:trabalhosutf@localhost:5432/timemaker'
    DBBaseModel = declarative_base()

    JWT_TOKEN: str = '0cwNWhmFmF_OCUaYT0y6uSUFgYzYjX7KzK1lz6f8bZ8'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*365

    class config:
        case_sensitive = True

settings = Settings()