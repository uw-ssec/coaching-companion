from ._basetablemodel import BaseTableModel

class ManageAuthUsers(BaseTableModel, table=True):
    __tablename__ = "manage_auth_users"
    __table_args__ = {"schema": "public"}
    
    pass