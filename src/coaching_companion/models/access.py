from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from pydantic import field_validator
from sqlalchemy import Text

class Access(BaseTableModel, table=True):
    __tablename__ = "access"
    __table_args__ = {"schema": "public"}
    
    content_create: str = Field(default=None, max_length=10)
    content_delete: str = Field(default=None, max_length=10)
    content_edit: str = Field(default=None, max_length=10)
    recipe_key: int = Field(default=None)
    repudiated_url: str = Field(default=None, sa_type=Text)
    role_access: str = Field(default=None, max_length=50)
    
    _repudiated_url = field_validator('repudiated_url')(convert_str_to_url)