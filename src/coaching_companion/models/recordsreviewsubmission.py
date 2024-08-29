from ._basetablemodel import BaseTableModel

class RecordsReviewSubmission(BaseTableModel, table=True):
    __tablename__ = "records_review_submission"
    __table_args__ = {"schema": "public"}
    
    pass