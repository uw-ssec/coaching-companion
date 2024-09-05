from ._basetablemodel import BaseTableModel, convert_str_to_url, convert_int_to_uuid

from sqlmodel import Field, Integer, String, Text, UUID
from pydantic import field_validator
import uuid

class CopGroups(BaseTableModel, table=True):
    __tablename__ = "cop_groups"
    __table_args__ = {"schema": "public"}
    
    cop_admins: str = Field(default=None, max_length=100, sa_type=String(100))
    cop_group_admin: str = Field(default=None, max_length=15, sa_type=String(15))
    user_id: uuid.UUID = Field(default=None, sa_type=UUID) # Generates a new UUID if None exists
    cop_asset_creation: str = Field(default=None, max_length=15, sa_type=String(15))
    hide_video_conferencing: str = Field(default=None, max_length=10, sa_type=String(10))
    hide_cop_resources: str = Field(default=None, max_length=10, sa_type=String(10))
    user_type: str = Field(default=None, max_length=50, sa_type=String(50))
    parent_url: str = Field(default=None, sa_type=Text)
    cqelcoach_group: int = Field(default=None, sa_type=Integer)
    cop_topic_creation: str = Field(default=None, max_length=15, sa_type=String(15))
    cop_members: str = Field(default=None, max_length=100, sa_type=String(100))
    disable_opt_out: str = Field(default=None, max_length=10, sa_type=String(10))
    hide_cop_members: str = Field(default=None, max_length=10, sa_type=String(10))
    
    _parent_url = field_validator('parent_url')(convert_str_to_url)

    _user_id = field_validator('user_id')(convert_int_to_uuid)