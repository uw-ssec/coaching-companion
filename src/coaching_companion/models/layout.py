from ._basetablemodel import BaseTableModel

from sqlmodel import Field  

class Layout(BaseTableModel, table=True):
    __tablename__ = "layout"
    __table_args__ = {"schema": "public"}
    
    class_: str = Field(default=None, max_length=10)