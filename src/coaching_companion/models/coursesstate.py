from ._basetablemodel import BaseTableModel, convert_str_to_url

from sqlmodel import Field, String, Integer, Text
from pydantic import field_validator

class CoursesState(BaseTableModel, table=True):
    __tablename__ = "courses_state"
    __table_args__ = {"schema": "public"}
    
    sub_roles: str = Field(default=None, max_length=50, sa_type=String(50))
    course_name: str = Field(default=None, max_length=150, sa_type=String(150))
    course_identifier: str = Field(default=None, max_length=50, sa_type=String(50))
    course_number: str = Field(default=None, max_length=50, sa_type=String(50))
    lms_prototype: str = Field(default=None, max_length=50, sa_type=String(50))
    prototype_copy: int = Field(default=None, sa_type=Integer)
    lms_course_url: str = Field(default=None, sa_type=Text)
    
    _lms_course_url = field_validator('lms_course_url')(convert_str_to_url)