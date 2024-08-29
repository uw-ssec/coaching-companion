from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class FamilySurveyLink(BaseTableModel, table=True):
    __tablename__ = "family_survey_link"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)