from .basetablemodel import BaseTableModel

from sqlmodel import Field

class AssessmentsEvaluation(BaseTableModel, table=True):
    __tablename__ = "assessments_evaluation"
    __table_args__ = {"schema": "public"}
    
    recipe_key: int = Field(default=None)
    title_eng: str = Field(default=None, max_length=255)  # English title