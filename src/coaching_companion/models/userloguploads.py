from ._basetablemodel import BaseTableModel

class UserLogUploads(BaseTableModel, table=True):
    __tablename__ = "user_log_uploads"
    __table_args__ = {"schema": "public"}
    
    pass