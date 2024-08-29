from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class AuthUserSettings(BaseTableModel, table=True):
    __tablename__ = "auth_user_settings"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    recipe_name: str = Field(default=None, max_length=50)