from ._basetablemodel import BaseTableModel, convert_str_to_datetime

from sqlmodel import Field, String, Integer, Text
from pydantic import field_validator
from datetime import datetime

class Assets(BaseTableModel, table=True):
    __tablename__ = "assets"
    __table_args__ = {"schema": "public"}
    
    annotations_key: str = Field(default=None, max_length=15, sa_type=String(15))
    assets_editors: str = Field(default=None, max_length=100, sa_type=String(100))  # Consider a separate table for a many-to-many relationship
    assets_members: str = Field(default=None, max_length=100, sa_type=String(100))  # Consider a separate table for a many-to-many relationship
    cqelcoach_observation: int = Field(default=None, sa_type=Integer)  # Connects to auth_users.id
    media_type: str = Field(default=None, max_length=100, sa_type=String(100))  # Consider a separate table for normalization
    notes: str = Field(default=None, sa_type=Text, nullable=True)
    observation_date: datetime = Field(default=None, nullable=False)  # Changed to datetime for consistency
    pbc_asset: str = Field(default=None, max_length=50, sa_type=String(50))  # Consider a separate table for normalization
    resource_tag: str = Field(default=None, max_length=255, sa_type=String(255))  # Consider a separate table for normalization

    _observation_date = field_validator('observation_date')(convert_str_to_datetime)