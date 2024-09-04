from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String, Boolean

class Login(BaseTableModel, table=True):
    __tablename__ = "login"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255, sa_type=String(255))
    login_disabled: bool = Field(default=None, sa_type=Boolean)
    template: str = Field(default=None, max_length=100, sa_type=String(100))