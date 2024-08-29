from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class Logout(BaseTableModel, table=True):
    __tablename__ = "logout"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    recipe_name: str = Field(default=None, max_length=50)