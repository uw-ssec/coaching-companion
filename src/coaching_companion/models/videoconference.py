from ._basetablemodel import BaseTableModel

class VideoConference(BaseTableModel, table=True):
    __tablename__ = "video_conference"
    __table_args__ = {"schema": "public"}
    
    pass