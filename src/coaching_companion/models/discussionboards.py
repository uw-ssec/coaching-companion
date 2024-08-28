from .basetablemodel import BaseTableModel

from sqlmodel import Field
from sqlalchemy import Text

class DiscussionBoards(BaseTableModel, table=True):
    __tablename__ = "discussion_boards"
    __table_args__ = {"schema": "public"}
    
    role_designation: str = Field(default=None, max_length=50)
    description: str = Field(default=None, sa_type=Text)