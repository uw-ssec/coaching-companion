from .basetablemodel import BaseTableModel

from sqlmodel import Field

class LtiEndpoint(BaseTableModel, table=True):
    __tablename__ = "lti_endpoint"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)