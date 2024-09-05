from ._basetablemodel import BaseTableModel

class UserLogCompletedGoals(BaseTableModel, table=True):
    __tablename__ = "user_log_completed_goals"
    __table_args__ = {"schema": "public"}
    
    pass