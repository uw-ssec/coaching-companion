from ._basetablemodel import BaseTableModel

class StudentSubmissionsSlug(BaseTableModel, table=True):
    __tablename__ = "student_submissions_slug"
    __table_args__ = {"schema": "public"}
    
    pass