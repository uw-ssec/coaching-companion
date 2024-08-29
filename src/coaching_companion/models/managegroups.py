from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class ManageGroups(BaseTableModel, table=True):
    __tablename__ = "manage_groups"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)