from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String, Integer, Text

class UploadAndReflectionAssignment(BaseTableModel, table=True):
    __tablename__ = "upload_and_reflection_assignment"
    __table_args__ = {"schema": "public"}
    
    assignment_category: str = Field(default=None, max_length=15, sa_type=String(15))
    components_limit: int = Field(default=None, sa_type=Integer)
    grading_rubric: str = Field(default=None, sa_type=Text)
    instructions: str = Field(default=None, sa_type=Text)
    recipe_key: int = Field(default=None, sa_type=Integer)