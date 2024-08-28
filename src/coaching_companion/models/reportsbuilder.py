from .basetablemodel import BaseTableModel

from sqlmodel import Field

class ReportsBuilder(BaseTableModel, table=True):
    __tablename__ = "reports_builder"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    report_types: str = Field(default=None, max_length=50)