from ._basetablemodel import BaseTableModel

class ManageMenus(BaseTableModel, table=True):
    __tablename__ = "manage_menus"
    __table_args__ = {"schema": "public"}
    
    pass