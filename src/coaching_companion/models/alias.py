from .basetablemodel import BaseTableModel

from sqlmodel import Field

class Alias(BaseTableModel, table=True):
    __tablename__ = "alias"
    __table_args__ = {"schema": "public"}
    
    children_sequencer: str = Field(default=None, max_length=10)
    login_disabled: bool = Field(default=None)
    media: str = Field(default=None, max_length=60)
    media_type: str = Field(default=None, max_length=100)
    on_cloudfront: str = Field(default=None, max_length=10)
    published: str = Field(default=None, max_length=50)
    ratings_id: int = Field(default=None, max_length=50)
    recipe: str = Field(default=None, max_length=255)
    recipe_key: int = Field(default=None)
    recipe_name: str = Field(default=None, max_length=50)
    report_types: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)