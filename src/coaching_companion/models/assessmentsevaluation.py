from ._basetablemodel import BaseTableModel

from sqlmodel import Field, Integer, String

class AssessmentsEvaluation(BaseTableModel, table=True):
    __tablename__ = "assessments_evaluation"
    __table_args__ = {"schema": "public"}
    
    recipe_key: int = Field(default=None, sa_type=Integer)
    title_eng: str = Field(default=None, max_length=255, sa_type=String(255))  # English title