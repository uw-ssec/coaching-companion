from .basetablemodel import BaseTableModel

from sqlmodel import Field

class Solotron(BaseTableModel, table=True):
    __tablename__ = "solotron"
    __table_args__ = {"schema": "public"}
    
    can_survey_components: str = Field(default=None, max_length=150)