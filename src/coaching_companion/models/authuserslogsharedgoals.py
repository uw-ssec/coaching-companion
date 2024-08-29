from ._basetablemodel import BaseTableModel

class AuthUsersLogSharedGoals(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_shared_goals"
    __table_args__ = {"schema": "public"}
    
    pass