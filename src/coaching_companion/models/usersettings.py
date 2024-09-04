from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class UserSettings(BaseTableModel, table=True):
    __tablename__ = "user_settings"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255, sa_type=String(255))
    recipe_name: str = Field(default=None, max_length=50, sa_type=String(50))