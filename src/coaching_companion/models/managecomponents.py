from ._basetablemodel import BaseTableModel

class ManageComponents(BaseTableModel, table=True):
    __tablename__ = "manage_components"
    __table_args__ = {"schema": "public"}
    
    pass