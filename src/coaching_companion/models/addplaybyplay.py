from ._basetablemodel import BaseTableModel, convert_timestamp_to_datetime, convert_int_to_uuid

from sqlmodel import Field, UUID
from datetime import datetime
from pydantic import field_validator
import uuid

class AddPlayByPlay(BaseTableModel, table=True): # TODO: Does this table have a primary key?
    __tablename__ = "add_play_by_play"
    __table_args__ = {"schema": "public"}
    
    item_id: uuid.UUID = Field(default=None, sa_type=UUID, nullable=False)
    timestamp: datetime = Field(default=None, nullable=False)  # Now a datetime

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)

    _item_id = field_validator('item_id')(convert_int_to_uuid)
