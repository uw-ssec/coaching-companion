from .basetablemodel import BaseTableModel

from sqlmodel import Field

class ContactForm(BaseTableModel, table=True):
    __tablename__ = "contact_form"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)