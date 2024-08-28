from .basetablemodel import BaseTableModel

from sqlmodel import Field

class AssessmentsSite(BaseTableModel, table=True):
    __tablename__ = "assessments_site"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)