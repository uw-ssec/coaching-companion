from ._basetablemodel import BaseTableModel, convert_timestamp_to_datetime

from sqlmodel import Field, Integer, String, Text
from pydantic import field_validator
from datetime import datetime

class Comments(BaseTableModel, table=True):
    __tablename__ = "comments"
    __table_args__ = {"schema": "public"}
    
    recipe_key: int = Field(default=None, sa_type=Integer)
    submit: str = Field(default=None, max_length=50, sa_type=String(50))  # Renamed from 'submit'
    Submit: str = Field(default=None, max_length=50, sa_type=String(50))  # Renamed from 'Submit'
    text: str = Field(default=None, sa_type=Text)
    timestamp: datetime = Field(default=None, nullable=False)  # Renamed from 'timestamp' and changed type

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)