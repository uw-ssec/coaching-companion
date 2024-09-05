from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String, Text

class DiscussionBoards(BaseTableModel, table=True):
    __tablename__ = "discussion_boards"
    __table_args__ = {"schema": "public"}
    
    role_designation: str = Field(default=None, max_length=50, sa_type=String(50))
    description: str = Field(default=None, sa_type=Text) # Long text field