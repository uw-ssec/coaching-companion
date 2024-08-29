from ._basetablemodel import BaseTableModel

class Assignments(BaseTableModel, table=True):
    __tablename__ = "assignments"
    __table_args__ = {"schema": "public"}
    
    pass