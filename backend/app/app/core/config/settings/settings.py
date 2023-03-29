import secrets
from typing import Optional, Any, List, Union, Dict

from pydantic import BaseSettings, PostgresDsn, validator, HttpUrl, EmailStr, AnyHttpUrl

class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRESQL_DATABASE_URL: Optional[PostgresDsn] = None

    @validator("POSTGRESQL_DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
