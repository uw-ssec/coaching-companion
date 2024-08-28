from .basetablemodel import BaseTableModel, convert_timestamp_to_datetime

from datetime import datetime
from sqlmodel import Field
from pydantic import field_validator
from sqlalchemy import Text

class ActionPlans(BaseTableModel, table=True): # TODO: Update completed_at based on the int input type
    __tablename__ = "action_plans"
    __table_args__ = {"schema": "public"}
    
    completed_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime, not Optional[int]
    cycle_summary: str = Field(default=None, sa_type=Text)
    info: str = Field(default=None, sa_type=Text)  # Treated as text, equivalent to varchar without a strict length limit
    next_step_notes: str = Field(default=None, sa_type=Text)
    status: str = Field(default=None, max_length=20)
    step_info_NaN: str = Field(default=None, max_length=100)  # Consider renaming to follow Python naming conventions

    _completed_at = field_validator('completed_at')(convert_timestamp_to_datetime)