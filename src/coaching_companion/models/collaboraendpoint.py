from ._basetablemodel import BaseTableModel

class CollaboraEndpoint(BaseTableModel, table=True):
    __tablename__ = "collabora_endpoint"
    __table_args__ = {"schema": "public"}
    
    pass