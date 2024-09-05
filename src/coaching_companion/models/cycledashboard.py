from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class CycleDashboard(BaseTableModel, table=True):
    __tablename__ = "cycle_dashboard"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100, sa_type=String(100), nullable=False)