from ._basetablemodel import BaseTableModel

class CopAssets(BaseTableModel, table=True):
    __tablename__ = "cop_assets"
    __table_args__ = {"schema": "public"}
    
    pass