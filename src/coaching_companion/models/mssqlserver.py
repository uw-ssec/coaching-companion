from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from sqlalchemy import Text
from pydantic import field_validator

class MssqlServer(BaseTableModel, table=True):
    __tablename__ = "mssql_server"
    __table_args__ = {"schema": "public"}
    
    username: str = Field(default=None, max_length=50)
    password: str = Field(default=None, max_length=25)
    host: str = Field(default=None, sa_type=Text)
    name: str = Field(default=None, max_length=100)
    
    _host = field_validator('host')(convert_str_to_url)