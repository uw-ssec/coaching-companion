from ._basetablemodel import BaseTableModel

from sqlmodel import Field
from sqlalchemy import Text

class UploadAndReflectionAssignment(BaseTableModel, table=True):
    __tablename__ = "upload_and_reflection_assignment"
    __table_args__ = {"schema": "public"}
    
    assignment_category: str = Field(default=None, max_length=15)
    components_limit: int = Field(default=None)
    grading_rubric: str = Field(default=None)
    instructions: str = Field(default=None, sa_type=Text)
    recipe_key: int = Field(default=None)