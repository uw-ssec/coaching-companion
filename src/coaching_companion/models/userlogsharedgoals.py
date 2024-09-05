from ._basetablemodel import BaseTableModel

class UserLogSharedGoals(BaseTableModel, table=True):
    __tablename__ = "user_log_shared_goals"
    __table_args__ = {"schema": "public"}
    
    pass