from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String, Text

class Tracker(BaseTableModel, table=True):
    __tablename__ = "tracker"
    __table_args__ = {"schema": "public"}
    
    description: str = Field(default=None, sa_type=Text)
    template: str = Field(default=None, max_length=100, sa_type=String(100))