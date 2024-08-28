from .basetablemodel import BaseTableModel

from sqlmodel import Field

class ManageStudents(BaseTableModel, table=True):
    __tablename__ = "manage_students"
    __table_args__ = {"schema": "public"}
    
    role_select: str = Field(default=None, max_length=50)