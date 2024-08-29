from ._basetablemodel import BaseTableModel

class StudentSubmissions(BaseTableModel, table=True):
    __tablename__ = "student_submissions"
    __table_args__ = {"schema": "public"}
    
    pass