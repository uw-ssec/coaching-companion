from ._basetablemodel import BaseTableModel

class UserLogReporting(BaseTableModel, table=True):
    __tablename__ = "user_log_reporting"
    __table_args__ = {"schema": "public"}
    
    pass