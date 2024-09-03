from ._basetablemodel import BaseTableModel

class DualLanguageHandbook(BaseTableModel, table=True):
    __tablename__ = "dual_language_handbook"
    __table_args__ = {"schema": "public"}
    
    pass