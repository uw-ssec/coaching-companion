from ._basetablemodel import BaseTableModel

class UserLogCreatedAt(BaseTableModel, table=True):
    __tablename__ = "user_log_created_at"
    __table_args__ = {"schema": "public"}
    
    pass