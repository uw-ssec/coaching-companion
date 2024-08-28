from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from sqlalchemy import Text, UUID
from pydantic import field_validator
from datetime import datetime
import uuid

class VideoReflection(BaseTableModel, table=True):
    __tablename__ = "video_reflection"
    __table_args__ = {"schema": "public"}
    
    idClassroom: int = Field(default=None) # Should this be a UUID?
    idRating: int = Field(default=None) # Should this be a UUID?
    idVHResponse: int = Field(default=None)
    parent_url: str = Field(default=None, sa_type=Text)
    procedure: str = Field(default=None, max_length=20)
    ratings_id: uuid.UUID = Field(default=None, sa_type=UUID)
    reflection_input: str = Field(default=None)
    updated_on: datetime = Field(default=None, sa_column_kwargs={"nullable": False})
    
    _parent_url = field_validator('parent_url')(convert_str_to_url)