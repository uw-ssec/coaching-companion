from ._basetablemodel import BaseTableModel

from sqlmodel import Field
from sqlalchemy import Text

class Annotations(BaseTableModel, table=True):
    __tablename__ = "annotations"
    __table_args__ = {"schema": "public"}
    
    info: str = Field(default=None, sa_type=Text)  # Treated as text, equivalent to varchar without a strict length limit
    recipe_key: int = Field(default=None)