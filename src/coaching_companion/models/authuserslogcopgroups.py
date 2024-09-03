from ._basetablemodel import BaseTableModel

class AuthUsersLogCopGroups(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_cop_groups"
    __table_args__ = {"schema": "public"}
    
    pass