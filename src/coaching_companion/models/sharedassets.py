from .basetablemodel import BaseTableModel

from sqlmodel import Field

class SharedAssets(BaseTableModel, table=True):
    __tablename__ = "shared_assets"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)