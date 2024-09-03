from ._basetablemodel import BaseTableModel

class AssessmentsDashboard(BaseTableModel, table=True):
    __tablename__ = "assessments_dashboard"
    __table_args__ = {"schema": "public"}
    
    pass