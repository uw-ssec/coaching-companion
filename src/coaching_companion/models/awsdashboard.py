from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class AWSDashboard(BaseTableModel, table=True):
    __tablename__ = "aws_dashboard"
    __table_args__ = {"schema": "public"}
    
    pass