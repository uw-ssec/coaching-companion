from .basetablemodel import BaseTableModel

class AuthUsersLogCompletedGoals(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_completed_goals"
    __table_args__ = {"schema": "public"}
    
    pass