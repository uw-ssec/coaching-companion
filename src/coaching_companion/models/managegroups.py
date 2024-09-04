from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class ManageGroups(BaseTableModel, table=True):
    __tablename__ = "manage_groups"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100, sa_type=String(100))