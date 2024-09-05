from ._basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field, String, Text
from pydantic import field_validator

class CoachingPartnership(BaseTableModel, table=True):
    __tablename__ = "coaching_partnership"
    __table_args__ = {"schema": "public"}
    
    coach: str = Field(default=None, max_length=100, sa_type=String(100))
    coachee: str = Field(default=None, max_length=100, sa_type=String(100))
    coachee_user: str = Field(default=None, max_length=15, sa_type=String(15))
    coach_user: str = Field(default=None, max_length=15, sa_type=String(15))
    parent_url: str = Field(default=None, sa_type=Text)
    participant: str = Field(default=None, max_length=50, sa_type=String(50))
    participant_user: str = Field(default=None, max_length=50, sa_type=String(50))
    partnership_filters: str = Field(default=None, max_length=100, sa_type=String(100))
    partnership_status: str = Field(default=None, max_length=25, sa_type=String(25))
    pbc_members: str = Field(default=None, max_length=100, sa_type=String(100))  # Consider a separate table for a many-to-many relationship
    pbc_roles: str = Field(default=None, max_length=100, sa_type=String(100))  # Consider a separate table for a many-to-many relationship
    prototype_description: str = Field(default=None, max_length=200, sa_type=String(200))
    prototype_status: str = Field(default=None, max_length=10, sa_type=String(10))
    template: str = Field(default=None, max_length=100, sa_type=String(100)) # Consider a separate table for normalization
    
    _parent_url = field_validator('parent_url')(convert_str_to_url)