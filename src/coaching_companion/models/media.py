from ._basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from sqlalchemy import Text, UUID
from pydantic import field_validator
from datetime import datetime
import uuid

class Media(BaseTableModel, table=True):
    __tablename__ = "media"
    __table_args__ = {"schema": "public"}
    
    code: str = Field(default=None, max_length=100)
    cqelcoach_resource: int = Field(default=None)
    description: str = Field(default=None, sa_type=Text)
    disable_captions: bool = Field(default=None)
    filename: str = Field(default=None, max_length=100)
    inputtypes: str = Field(default=None, max_length=50)
    job_id: uuid.UUID = Field(default=None, sa_type=UUID)
    link: str = Field(default=None, sa_type=Text)
    media_type: str = Field(default=None, max_length=100)
    name: str = Field(default=None, max_length=100)
    on_cloudfront: str = Field(default=None, max_length=10) # Should this be a boolean?
    path: str = Field(default=None, max_length=50)
    published: str = Field(default=None, max_length=50)
    ratings_id: uuid.UUID = Field(default=None, sa_type=UUID)
    recipe_key: int = Field(default=None)
    taxonomy: str = Field(default=None, max_length=255)
    text: str = Field(default=None)
    vide_hightlight_location: str = Field(default=None, max_length=100)
    video_hightlight_alias_id: uuid.UUID = Field(default=None, sa_type=UUID)
    video_hightlight_created_by: int = Field(default=None, foreign_key="public.auth_user.id")
    video_hightlight_location: str = Field(default=None, max_length=100)
    video_hightlight_submission: int = Field(default=None, sa_type=Text)
    video_hightlight_submission_at: datetime = Field(default=None)
    video_hightlight_submission_copy: int = Field(default=None)
    vtt: str = Field(default=None, max_length=255)
    
    _link = field_validator('link')(convert_str_to_url)