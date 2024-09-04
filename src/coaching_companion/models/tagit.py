from ._basetablemodel import BaseTableModel, convert_timestamp_to_datetime

from sqlmodel import Field
from pydantic import field_validator
from datetime import datetime

class Tagit(BaseTableModel, table=True):
    __tablename__ = "tagit"
    __table_args__ = {"schema": "public"}

    timestamp: datetime = Field(default=None, nullable=False)

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)