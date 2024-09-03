from ._basetablemodel import BaseTableModel

class EaEvalSurvey(BaseTableModel, table=True): # Renamed from 'Ea_eval_survey'
    __tablename__ = "ea_eval_survey"
    __table_args__ = {"schema": "public"}
    
    pass