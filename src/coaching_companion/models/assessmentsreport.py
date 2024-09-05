from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class AssessmentsReport(BaseTableModel, table=True):
    __tablename__ = "assessments_report"
    __table_args__ = {"schema": "public"}
    
    title_eng: str = Field(default=None, max_length=255, sa_type=String(255))  # English title
    title_esp: str = Field(default=None, max_length=255, sa_type=String(255))  # Spanish title