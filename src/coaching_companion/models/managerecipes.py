from ._basetablemodel import BaseTableModel

class ManageRecipes(BaseTableModel, table=True):
    __tablename__ = "manage_recipes"
    __table_args__ = {"schema": "public"}
    
    pass