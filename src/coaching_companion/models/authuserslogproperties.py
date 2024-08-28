from .basetablemodel import BaseTableModel

class AuthUsersLogProperties(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_properties"
    __table_args__ = {"schema": "public"}
    
    pass