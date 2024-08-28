from .basetablemodel import BaseTableModel

class AuthUsersLogCreatedAt(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_created_at"
    __table_args__ = {"schema": "public"}
    
    pass