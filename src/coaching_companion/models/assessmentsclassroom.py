from ._basetablemodel import BaseTableModel

class AssessmentsClassroom(BaseTableModel, table=True):
    __tablename__ = "assessments_classroom"
    __table_args__ = {"schema": "public"}
    
    pass