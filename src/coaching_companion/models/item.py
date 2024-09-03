from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class Item(BaseTableModel, table=True):
    __tablename__ = "item"
    __table_args__ = {"schema": "public"}
    
    filter_by: str = Field(default=None, max_length=100)