from .basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field
from pydantic import field_validator
from sqlalchemy import Text, UUID
import uuid

class CopGroups(BaseTableModel, table=True):
    __tablename__ = "cop_groups"
    __table_args__ = {"schema": "public"}
    
    cop_admins: str = Field(default=None, max_length=100)
    cop_group_admin: str = Field(default=None, max_length=15)
    user_id: uuid.UUID | None = Field(default=None, sa_type=UUID) # Generates a new UUID if None exists
    cop_asset_creation: str = Field(default=None, max_length=15)
    hide_video_conferencing: str = Field(default=None, max_length=10)
    hide_cop_resources: str = Field(default=None, max_length=10)
    user_type: str = Field(default=None, max_length=50)
    parent_url: str = Field(sa_type=Text)
    cqelcoach_group: int = Field(default=None)
    cop_topic_creation: str = Field(default=None, max_length=15)
    cop_members: str = Field(default=None, max_length=100)
    disable_opt_out: str = Field(default=None, max_length=10)
    hide_cop_members: str = Field(default=None, max_length=10)
    
    _parent_url = field_validator('parent_url')(convert_str_to_url)