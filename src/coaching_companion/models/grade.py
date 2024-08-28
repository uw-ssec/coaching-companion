from .basetablemodel import BaseTableModel

class Grade(BaseTableModel, table=True):
    __tablename__ = "grade"
    __table_args__ = {"schema": "public"}
    
    pass