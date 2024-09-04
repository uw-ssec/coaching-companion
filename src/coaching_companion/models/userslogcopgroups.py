from ._basetablemodel import BaseTableModel

class UserLogCopGroups(BaseTableModel, table=True):
    __tablename__ = "user_log_cop_groups"
    __table_args__ = {"schema": "public"}
    
    pass