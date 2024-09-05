from ._basetablemodel import BaseTableModel

class UserLogProperties(BaseTableModel, table=True):
    __tablename__ = "user_log_properties"
    __table_args__ = {"schema": "public"}
    
    pass