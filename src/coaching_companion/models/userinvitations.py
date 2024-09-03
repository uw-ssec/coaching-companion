from ._basetablemodel import BaseTableModel

from sqlmodel import Field

class UserInvitations(BaseTableModel, table=True):
    __tablename__ = "user_invitations"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)