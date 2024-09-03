from ._basetablemodel import BaseTableModel

class RatingsRubric(BaseTableModel, table=True):
    __tablename__ = "ratings_rubric"
    __table_args__ = {"schema": "public"}
    
    pass