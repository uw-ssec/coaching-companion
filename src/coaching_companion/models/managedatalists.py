from ._basetablemodel import BaseTableModel

class ManageDatalists(BaseTableModel, table=True):
    __tablename__ = "manage_datalists"
    __table_args__ = {"schema": "public"}
    
    pass