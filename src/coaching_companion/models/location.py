from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class Location(BaseTableModel, table=True):
    __tablename__ = "location"
    __table_args__ = {"schema": "public"}
    
    order_direction: str = Field(default=None, max_length=15)
    recipe: str = Field(default=None, max_length=255)
    children_sequencer: str = Field(default=None, max_length=10)
    order_by: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)