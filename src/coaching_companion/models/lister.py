from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from sqlalchemy import Text
from pydantic import field_validator

class Lister(BaseTableModel, table=True):
    __tablename__ = "lister"
    __table_args__ = {"schema": "public"}
    
    lister_authority_display: str = Field(default=None, max_length=20)
    repudiated_url: str = Field(default=None, sa_type=Text)
    lister_authority: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)
    members: str = Field(default=None, max_length=100)
    
    _reputed_url = field_validator('repudiated_url')(convert_str_to_url)