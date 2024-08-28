from .basetablemodel import BaseTableModel

class ManageSite(BaseTableModel, table=True):
    __tablename__ = "manage_site"
    __table_args__ = {"schema": "public"}
    
    pass