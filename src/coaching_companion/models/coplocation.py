from .basetablemodel import BaseTableModel

from sqlmodel import Field

class CopLocation(BaseTableModel, table=True):
    __tablename__ = "cop_location"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)