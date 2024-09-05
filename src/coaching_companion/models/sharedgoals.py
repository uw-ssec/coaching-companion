from ._basetablemodel import BaseTableModel, convert_timestamp_to_datetime, convert_int_to_uuid

from sqlmodel import Field
from sqlalchemy import UUID, String, Text
from pydantic import field_validator
from datetime import datetime
import uuid

class SharedGoals(BaseTableModel, table=True):
    __tablename__ = "shared_goals"
    __table_args__ = {"schema": "public"}
    
    completed_at: datetime = Field(default=None, nullable=False)
    core_knowledge_categories: str = Field(default=None, max_length=100, sa_type=String(100))
    cycle_summary: str = Field(default=None, sa_type=Text)
    info: str = Field(default=None, sa_type=Text)
    prototype_id: uuid.UUID = Field(default=None, sa_type=UUID)
    status: str = Field(default=None, max_length=20, sa_type=String(20))

    _completed_at = field_validator('completed_at')(convert_timestamp_to_datetime)

    _prototype_id = field_validator('prototype_id')(convert_int_to_uuid)