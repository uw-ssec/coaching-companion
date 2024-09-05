from ._basetablemodel import BaseTableModel, convert_str_to_url, convert_int_to_uuid

from sqlmodel import Field, String, Text, UUID
from pydantic import field_validator
from datetime import datetime
import uuid

class VideoReflection(BaseTableModel, table=True):
    __tablename__ = "video_reflection"
    __table_args__ = {"schema": "public"}
    
    idClassroom: uuid.UUID = Field(default=None, sa_type=UUID) # Should this be a UUID?
    idRating: uuid.UUID = Field(default=None, sa_type=UUID) # Should this be a UUID?
    idVHResponse: uuid.UUID = Field(default=None, sa_type=UUID) # Should this be a UUID?
    parent_url: str = Field(default=None, sa_type=Text)
    procedure: str = Field(default=None, max_length=20, sa_type=String(20))
    ratings_id: uuid.UUID = Field(default=None, sa_type=UUID)
    reflection_input: str = Field(default=None, sa_type=Text)
    updated_on: datetime = Field(default=None, nullable=False)
    
    _parent_url = field_validator('parent_url')(convert_str_to_url)

    _idClassroom = field_validator('idClassroom')(convert_int_to_uuid)
    _idRating = field_validator('idRating')(convert_int_to_uuid)
    _idVHResponse = field_validator('idVHResponse')(convert_int_to_uuid)
    _ratings_id = field_validator('ratings_id')(convert_int_to_uuid)