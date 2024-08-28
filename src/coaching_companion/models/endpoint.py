from .basetablemodel import BaseTableModel

from sqlmodel import Field

class Endpoint(BaseTableModel, table=True):
    __tablename__ = "endpoint"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)