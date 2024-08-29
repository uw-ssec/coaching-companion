from ._basetablemodel import BaseTableModel

class SupportingDocumentation(BaseTableModel, table=True):
    __tablename__ = "supporting_documentation"
    __table_args__ = {"schema": "public"}
    
    pass