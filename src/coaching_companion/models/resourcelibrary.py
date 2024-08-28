from .basetablemodel import BaseTableModel

class ResourceLibrary(BaseTableModel, table=True):
    __tablename__ = "resource_library"
    __table_args__ = {"schema": "public"}
    
    pass