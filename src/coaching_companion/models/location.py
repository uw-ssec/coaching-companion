from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class Location(BaseTableModel, table=True):
    __tablename__ = "location"
    __table_args__ = {"schema": "public"}
    
    order_direction: str = Field(default=None, max_length=15, sa_type=String(15))
    recipe: str = Field(default=None, max_length=255, sa_type=String(255))
    children_sequencer: str = Field(default=None, max_length=10, sa_type=String(10))
    order_by: str = Field(default=None, max_length=50, sa_type=String(50))
    template: str = Field(default=None, max_length=100, sa_type=String(100))