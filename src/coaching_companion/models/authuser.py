from sqlmodel import SQLModel, Field
from sqlalchemy import Text
from pydantic import field_validator
from datetime import datetime

@classmethod
def convert_datetime(cls, value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")

class AuthUser(SQLModel, table=True):
    __tablename__ = "auth_user"
    __table_args__ = {"schema": "public"}
    
    id: int | None = Field(primary_key=True)
    password: str = Field(max_length=128)
    last_login: str = Field()
    is_superuser: bool = Field()
    username: str = Field(max_length=255)
    email: str = Field(max_length=255)
    is_verified: bool = Field()
    is_active: bool = Field()
    is_staff: bool = Field()
    created_at: str = Field(default=None, sa_type=Text, sa_column_kwargs={"nullable": False})
    updated_at: str = Field(default=None, sa_type=Text, sa_column_kwargs={"nullable": False})
    first_name: str = Field(max_length=255)
    nestor_user_id: int = Field(default=None)
    last_name: str = Field(max_length=255)
    
    _created_at = field_validator("created_at")(convert_datetime)
    _updated_at = field_validator("updated_at")(convert_datetime)
    