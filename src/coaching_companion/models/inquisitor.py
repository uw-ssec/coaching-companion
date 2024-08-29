from ._basetablemodel import BaseTableModel

class Inquisitor(BaseTableModel, table=True):
    __tablename__ = "inquisitor"
    __table_args__ = {"schema": "public"}
    
    pass