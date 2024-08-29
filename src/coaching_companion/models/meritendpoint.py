from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class MeritEndpoint(BaseTableModel, table=True):
    __tablename__ = "merit_endpoint"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)