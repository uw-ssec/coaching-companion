from ._basetablemodel import BaseTableModel

class UserLogCopGroupsDigest(BaseTableModel, table=True):
    __tablename__ = "user_log_cop_groups_digest"
    __table_args__ = {"schema": "public"}
    
    pass