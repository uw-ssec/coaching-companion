from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class AssessmentsLister(BaseTableModel, table=True):
    __tablename__ = "assessments_lister"
    __table_args__ = {"schema": "public"}
    
    title_eng: str = Field(default=None, max_length=255, sa_type=String(255))  # English title
    lister_authority: str = Field(default=None, max_length=50, sa_type=String(50))  # Authority of the lister
    template: str = Field(default=None, max_length=100, sa_type=String(100))  # Template