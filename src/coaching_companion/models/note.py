from ._basetablemodel import BaseTableModel

from sqlmodel import Field, Text

class Note(BaseTableModel, table=True):
    __tablename__ = "note"
    __table_args__ = {"schema": "public"}
    
    notes: str = Field(default=None, sa_type=Text)