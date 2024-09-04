from ._basetablemodel import BaseTableModel

from sqlmodel import Field, String, Integer, Boolean, UUID
import uuid

class Alias(BaseTableModel, table=True):
    __tablename__ = "alias"
    __table_args__ = {"schema": "public"}
    
    children_sequencer: str = Field(default=None, max_length=10, sa_type=String(10))
    login_disabled: bool = Field(default=None, sa_type=Boolean)
    media: str = Field(default=None, max_length=60, sa_type=String(60))
    media_type: str = Field(default=None, max_length=100, sa_type=String(100))
    on_cloudfront: str = Field(default=None, max_length=10, sa_type=String(10))
    published: str = Field(default=None, max_length=50, sa_type=String(50))
    ratings_id: uuid.UUID = Field(default=None, sa_type=UUID)
    recipe: str = Field(default=None, max_length=255, sa_type=String(255))
    recipe_key: int = Field(default=None, sa_type=Integer)
    recipe_name: str = Field(default=None, max_length=50, sa_type=String(50))
    report_types: str = Field(default=None, max_length=50, sa_type=String(50))
    template: str = Field(default=None, max_length=100, sa_type=String(100))