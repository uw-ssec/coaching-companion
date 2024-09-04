from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class Reports(BaseTableModel, table=True):
    __tablename__ = "reports"
    __table_args__ = {"schema": "public"}
    
    report_types: str = Field(default=None, max_length=50, sa_type=String(50))