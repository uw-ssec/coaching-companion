from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class ResetPassword(BaseTableModel, table=True):
    __tablename__ = "reset_password"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255, sa_type=String(255))
    template: str = Field(default=None, max_length=100, sa_type=String(100))