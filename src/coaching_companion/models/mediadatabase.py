from ._basetablemodel import BaseTableModel

class MediaDatabase(BaseTableModel, table=True):
    __tablename__ = "media_database"
    __table_args__ = {"schema": "public"}
    
    pass