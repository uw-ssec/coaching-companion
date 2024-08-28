from .basetablemodel import BaseTableModel

class Documentation(BaseTableModel, table=True):
    __tablename__ = "documentation"
    __table_args__ = {"schema": "public"}
    
    pass