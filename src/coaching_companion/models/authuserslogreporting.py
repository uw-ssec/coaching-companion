from .basetablemodel import BaseTableModel

class AuthUsersLogReporting(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_reporting"
    __table_args__ = {"schema": "public"}
    
    pass