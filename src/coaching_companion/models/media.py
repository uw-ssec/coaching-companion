from ._basetablemodel import BaseTableModel, convert_str_to_url, convert_int_to_uuid

from sqlmodel import Field, String, Integer, Text, UUID, Boolean, BigInteger
from pydantic import field_validator
from datetime import datetime
import uuid

class Media(BaseTableModel, table=True):
    __tablename__ = "media"
    __table_args__ = {"schema": "public"}
    
    code: str = Field(default=None, max_length=100, sa_type=String(100))
    cqelcoach_resource: int = Field(default=None, sa_type=Integer)
    description: str = Field(default=None, sa_type=Text)
    disable_captions: bool = Field(default=None, sa_type=Boolean)
    filename: str = Field(default=None, max_length=100, sa_type=String(100))
    inputtypes: str = Field(default=None, max_length=50, sa_type=String(50))
    job_id: uuid.UUID = Field(default=None, sa_type=UUID)
    link: str = Field(default=None, sa_type=Text)
    media_type: str = Field(default=None, max_length=100, sa_type=String(100))
    name: str = Field(default=None, max_length=100, sa_type=String(100))
    on_cloudfront: str = Field(default=None, max_length=10, sa_type=String(10)) # Should this be a boolean?
    path: str = Field(default=None, max_length=50, sa_type=String(50))
    published: str = Field(default=None, max_length=50, sa_type=String(50))
    ratings_id: uuid.UUID = Field(default=None, sa_type=UUID)
    recipe_key: int = Field(default=None, sa_type=Integer)
    taxonomy: str = Field(default=None, max_length=255, sa_type=String(255))
    text: str = Field(default=None, sa_type=Text)
    vide_hightlight_location: str = Field(default=None, max_length=100, sa_type=String(100))
    video_hightlight_alias_id: uuid.UUID = Field(default=None, sa_type=UUID)
    video_hightlight_created_by: int = Field(default=None, foreign_key="public.auth_user.id", sa_type=BigInteger)
    video_hightlight_location: str = Field(default=None, max_length=100, sa_type=String(100))
    video_hightlight_submission: int = Field(default=None, sa_type=Text)
    video_hightlight_submission_at: datetime = Field(default=None, nullable=False)
    video_hightlight_submission_copy: int = Field(default=None, sa_type=Integer)
    vtt: str = Field(default=None, max_length=255, sa_type=String(255))
    
    _link = field_validator('link')(convert_str_to_url)

    _job_id = field_validator('job_id')(convert_int_to_uuid)
    _ratings_id = field_validator('ratings_id')(convert_int_to_uuid)
    _video_hightlight_alias_id = field_validator('video_hightlight_alias_id')(convert_int_to_uuid)