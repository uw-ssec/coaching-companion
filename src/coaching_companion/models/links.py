from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from sqlalchemy import Text
from pydantic import field_validator

class Links(BaseTableModel, table=True):
    __tablename__ = "links"
    __table_args__ = {"schema": "public"}
    
    target: str = Field(default=None, max_length=20)
    link_url: str = Field(default=None, sa_type=Text)
    color: str = Field(default=None, max_length=10)
    role_access: str = Field(default=None, max_length=50)
    
    _link_url = field_validator('link_url')(convert_str_to_url)