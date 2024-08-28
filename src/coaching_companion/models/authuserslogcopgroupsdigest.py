from .basetablemodel import BaseTableModel

class AuthUsersLogCopGroupsDigest(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_cop_groups_digest"
    __table_args__ = {"schema": "public"}
    
    pass