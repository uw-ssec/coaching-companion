from ._basetablemodel import BaseTableModel

class UserLogPartnerships(BaseTableModel, table=True):
    __tablename__ = "user_log_partnerships"
    __table_args__ = {"schema": "public"}
    
    pass