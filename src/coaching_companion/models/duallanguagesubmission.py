from .basetablemodel import BaseTableModel

class DualLanguageSubmission(BaseTableModel, table=True):
    __tablename__ = "dual_language_submission"
    __table_args__ = {"schema": "public"}
    
    pass