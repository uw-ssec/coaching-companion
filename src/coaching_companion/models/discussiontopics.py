from ._basetablemodel import BaseTableModel, convert_timestamp_to_datetime

from sqlmodel import Field
from pydantic import field_validator
from datetime import datetime

class DiscussionTopics(BaseTableModel, table=True):
    __tablename__ = "discussion_topics"
    __table_args__ = {"schema": "public"}
    
    prevent_inline_media: bool = Field(default=None)
    update_created_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})

    _update_created_at = field_validator('update_created_at')(convert_timestamp_to_datetime)