from ._basetablemodel import BaseTableModel

class UserLogAllAttributes(BaseTableModel, table=True):
    __tablename__ = "user_log_all_attributes"
    __table_args__ = {"schema": "public"}
    
    pass