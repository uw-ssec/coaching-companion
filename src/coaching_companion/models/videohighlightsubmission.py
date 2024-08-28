from .basetablemodel import BaseTableModel

class VideoHighlightSubmission(BaseTableModel, table=True):
    __tablename__ = "video_highlight_submission"
    __table_args__ = {"schema": "public"}
    
    pass