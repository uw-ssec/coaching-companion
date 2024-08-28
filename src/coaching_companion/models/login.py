from .basetablemodel import BaseTableModel

from sqlmodel import Field

class Login(BaseTableModel, table=True):
    __tablename__ = "login"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    login_disabled: bool = Field(default=None)
    template: str = Field(default=None, max_length=100)