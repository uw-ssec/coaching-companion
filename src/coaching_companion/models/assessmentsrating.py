from .basetablemodel import BaseTableModel

class AssessmentsRating(BaseTableModel, table=True):
    __tablename__ = "assessments_rating"
    __table_args__ = {"schema": "public"}
    
    pass