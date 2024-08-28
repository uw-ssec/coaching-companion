from .basetablemodel import BaseTableModel

class AuthUsersLogUploads(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_uploads"
    __table_args__ = {"schema": "public"}
    
    pass