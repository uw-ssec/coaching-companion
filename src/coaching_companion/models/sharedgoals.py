from .basetablemodel import BaseTableModel, convert_timestamp_to_datetime

from sqlmodel import Field
from sqlalchemy import UUID
from pydantic import field_validator
from datetime import datetime
import uuid

class SharedGoals(BaseTableModel, table=True):
    __tablename__ = "shared_goals"
    __table_args__ = {"schema": "public"}
    
    completed_at: datetime = Field(default=None, sa_column_kwargs={"nullable": True})
    core_knowledge_categories: str = Field(default=None, max_length=100)
    cycle_summary: str = Field(default=None)
    info: str = Field(default=None)
    prototype_id: uuid.UUID = Field(default=None, sa_type=UUID)
    status: str = Field(default=None, max_length=20)

    _completed_at = field_validator('completed_at')(convert_timestamp_to_datetime)