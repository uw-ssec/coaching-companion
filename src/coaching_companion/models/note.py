from .basetablemodel import BaseTableModel

from sqlmodel import Field
from sqlalchemy import Text

class Note(BaseTableModel, table=True):
    __tablename__ = "note"
    __table_args__ = {"schema": "public"}
    
    notes: str = Field(default=None, sa_type=Text)