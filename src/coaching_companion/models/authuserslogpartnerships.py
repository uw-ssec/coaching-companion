from .basetablemodel import BaseTableModel

class AuthUsersLogPartnerships(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_partnerships"
    __table_args__ = {"schema": "public"}
    
    pass