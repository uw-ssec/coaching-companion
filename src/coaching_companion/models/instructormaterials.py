from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class InstructorMaterials(BaseTableModel, table=True):
    __tablename__ = "instructor_materials"
    __table_args__ = {"schema": "public"}
    
    components_limit: int = Field(default=None)