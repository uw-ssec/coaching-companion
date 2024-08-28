from .basetablemodel import BaseTableModel

class AuthUsersLogAllAttributes(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_all_attributes"
    __table_args__ = {"schema": "public"}
    
    pass