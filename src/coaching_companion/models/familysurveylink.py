from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String

class FamilySurveyLink(BaseTableModel, table=True):
    __tablename__ = "family_survey_link"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255, sa_type=String(255), nullable=False)
    template: str = Field(default=None, max_length=100, sa_type=String(100), nullable=False)