from ._basetablemodel import BaseTableModel, convert_timestamp_to_datetime

from sqlmodel import Field
from datetime import datetime
from pydantic import field_validator

class AddPlayByPlay(BaseTableModel, table=True): # TODO: Does this table have a primary key?
    __tablename__ = "add_play_by_play"
    __table_args__ = {"schema": "public"}
    
    item_id: int = Field(default=None)
    timestamp: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)
