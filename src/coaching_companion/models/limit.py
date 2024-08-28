from .basetablemodel import BaseTableModel

from sqlmodel import Field

class Limit(BaseTableModel, table=True):
    __tablename__ = "limit"
    __table_args__ = {"schema": "public"}
    
    components_limit: int = Field(default=None)
    recipe_key: int = Field(default=None)