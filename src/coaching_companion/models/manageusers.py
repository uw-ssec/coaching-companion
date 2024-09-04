from ._basetablemodel import BaseTableModel

class ManageUsers(BaseTableModel, table=True):
    __tablename__ = "manage_users"
    __table_args__ = {"schema": "public"}
    
    pass