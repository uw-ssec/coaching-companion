from ._basetablemodel import BaseTableModel

class RecordsReviewHandbook(BaseTableModel, table=True):
    __tablename__ = "records_review_handbook"
    __table_args__ = {"schema": "public"}
    
    pass