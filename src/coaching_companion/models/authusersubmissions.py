from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from sqlalchemy import Text
from pydantic import field_validator

class AuthUserSubmissions(BaseTableModel, table=True):
    __tablename__ = "auth_user_submissions"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    can_view: str = Field(default=None, max_length=150)
    repudiated_url: str = Field(default=None, sa_type=Text)
    can_submit: str = Field(default=None, max_length=150) # Should this be a boolean field?
    content_administrator: str = Field(default=None, max_length=10)
    
    _repudiated_url = field_validator('repudiated_url')(convert_str_to_url)