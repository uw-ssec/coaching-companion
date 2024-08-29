from ._basetablemodel import BaseTableModel

class ProgramProfileSubmission(BaseTableModel, table=True):
    __tablename__ = "program_profile_submission"
    __table_args__ = {"schema": "public"}
    
    pass