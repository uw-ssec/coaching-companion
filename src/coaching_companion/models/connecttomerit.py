from .basetablemodel import BaseTableModel

class ConnectToMerit(BaseTableModel, table=True):
    __tablename__ = "connect_to_merit"
    __table_args__ = {"schema": "public"}
    
    pass