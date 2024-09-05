from ._basetablemodel import BaseTableModel

class AWSDashboard(BaseTableModel, table=True):
    __tablename__ = "aws_dashboard"
    __table_args__ = {"schema": "public"}
    
    pass