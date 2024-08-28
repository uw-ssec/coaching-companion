from .basetablemodel import BaseTableModel

from sqlmodel import Field

class AssessmentsReportClassroom(BaseTableModel, table=True):
    __tablename__ = "assessments_report_classroom"
    __table_args__ = {"schema": "public"}
    
    title_eng: str = Field(default=None, max_length=255)  # English title