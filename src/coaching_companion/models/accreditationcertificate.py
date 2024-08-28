from .basetablemodel import BaseTableModel

from sqlmodel import Field

class AccreditationCertificate(BaseTableModel, table=True):
    __tablename__ = "accreditation_certificate"
    __table_args__ = {"schema": "public"}
    
    pass