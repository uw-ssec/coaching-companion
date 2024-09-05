from ._basetablemodel import BaseTableModel

from sqlmodel import Field, Integer

class Limit(BaseTableModel, table=True):
    __tablename__ = "limit"
    __table_args__ = {"schema": "public"}
    
    components_limit: int = Field(default=None, sa_type=Integer, nullable=False)
    recipe_key: int = Field(default=None, sa_type=Integer, nullable=False)