from ._basetablemodel import BaseTableModel

from sqlmodel import Field
from sqlalchemy import Text
from datetime import datetime

class Assets(BaseTableModel, table=True):
    __tablename__ = "assets"
    __table_args__ = {"schema": "public"}
    
    annotations_key: str = Field(default=None, max_length=15)
    assets_editors: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    assets_members: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    cqelcoach_observation: int = Field(default=None)  # Connects to auth_users.id
    media_type: str = Field(default=None, max_length=100)  # Consider a separate table for normalization
    notes: str = Field(default=None, sa_type=Text, sa_column_kwargs={"nullable": True})
    observation_date: datetime = Field(default=None)  # Changed to datetime for consistency
    pbc_asset: str = Field(default=None, max_length=50)
    resource_tag: str = Field(default=None, max_length=255)    