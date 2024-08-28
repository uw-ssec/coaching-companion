from .basetablemodel import BaseTableModel

from sqlmodel import Field

class CycleDashboard(BaseTableModel, table=True):
    __tablename__ = "cycle_dashboard"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)