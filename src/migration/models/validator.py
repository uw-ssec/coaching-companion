from typing import Optional
from sqlmodel import SQLModel, Field, FieldValidator
from datetime import datetime
from pydantic import HttpUrl
from sqlalchemy import BigInteger

# The BaseTableModel class is a base class for all the tables in the database.
class BaseTableModel(SQLModel, table=False):
    created_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})
    created_by: int = Field(default=None, foreign_key="auth_users.id", sa_column_kwargs={"type_": BigInteger, "nullable": False})
    title: str = Field(default=None, max_length=255)
    type: Optional[str] = Field(default=None, max_length=50)  # Optional varchar(50) field

    @FieldValidator('created_at', pre=True)
    # Validator for the created_at field to convert Unix timestamp to datetime.
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value)
    
"""
The following classes define the tables in the database. 
Each class inherits from the BaseTableModel class and specifies the fields for the table. 
The table=True argument is used to indicate that the class represents a table in the database. 
The fields are defined using the Field class from the SQLModel library, which allows specifying the field type, default value, and other properties.
The FieldValidator decorator is used to define validators for the fields, which can perform validation or transformation of the field values.
"""

class AWSDashboard(BaseTableModel, table=True):
    pass

class Access(BaseTableModel, table=True):
    content_create: str = Field(default=None, max_length=10)
    content_delete: str = Field(default=None, max_length=10)
    content_edit: str = Field(default=None, max_length=10)
    recipe_key: int
    repudiated_url: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    role_access: str = Field(default=None, max_length=50)

class AccreditationCertificate(BaseTableModel, table=True):
    pass
    
class AccreditationSubmission(BaseTableModel, table=True):
    pass
    
class ActionPlans(BaseTableModel, table=True): # TODO: Update completed_at based on the int input type
    id: int = Field(default=None, primary_key=True)
    completed_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime, not Optional[int]
    cycle_summary: str = Field(default=None, sa_column_kwargs={"type_": "Text"})
    info: str = Field(default=None, sa_column_kwargs={"type_": "Text"})  # Treated as text, equivalent to varchar without a strict length limit
    next_step_notes: str = Field(default=None, sa_column_kwargs={"type_": "Text"})
    status: str = Field(default=None, max_length=20)
    step_info_NaN: str = Field(default=None, max_length=100)  # Consider renaming to follow Python naming conventions

    @FieldValidator('completed_at', pre=True)
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value)

class AddPlayByPlay(BaseTableModel, table=True): # TODO: Does this table have a primary key?
    item_id: int = Field(default=None)
    timestamp: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime

    @FieldValidator('timestamp', pre=True)
    def validate_timestamp(cls, value: int) -> datetime:
        """Validator for the timestamp field to convert int to datetime."""
        return datetime.fromtimestamp(value)

class Alias(BaseTableModel, table=True): # TODO: Review @Dayton responses before making changes**
    pass

class TableAnnotations(SQLModel, table=True):
    info: str = Field(default=None, sa_column_kwargs={"type_": "Text"})  # Treated as text, equivalent to varchar without a strict length limit
    recipe_key: int = Field(default=None)

class AssessmentsClassroom(BaseTableModel, table=True):
    pass

class AssessmentsEvaluation(BaseTableModel, table=True):
    recipe_key: int = Field(default=None)
    title_eng: str = Field(default=None, max_length=255)  # English title

class AssessmentsLister(BaseTableModel, table=True):
    title_eng: str = Field(default=None, max_length=255)  # English title
    lister_authority: str = Field(default=None, max_length=50)  # Authority of the lister
    template: str = Field(default=None, max_length=100)

class AssessmentsRating(BaseTableModel, table=True):
    pass

class AssessmentsReport(BaseTableModel, table=True):
    title_eng: str = Field(default=None, max_length=255)  # English title
    title_esp: str = Field(default=None, max_length=255)  # Spanish title

class AssessmentsReportClassroom(BaseTableModel, table=True):
    title_eng: str = Field(default=None, max_length=255)  # English title

class AssessmentsSite(BaseTableModel, table=True):
    template: str = Field(default=None, max_length=100)

class Assets(BaseTableModel, table=True):
    annotations_key: str = Field(default=None, max_length=15)
    assets_editors: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    assets_members: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    cqelcoach_observation: int = Field(default=None)  # Connects to auth_users.id
    media_type: str = Field(default=None, max_length=100)  # Consider a separate table for normalization
    notes: str = Field(default=None, sa_column_kwargs={"nullable": True})
    observation_date: datetime = Field(default=None)  # Changed to datetime for consistency
    pbc_asset: str = Field(default=None, max_length=50)
    resource_tag: str = Field(default=None, max_length=255)    

class Assignments(BaseTableModel, table=True):
    pass

class CoachingPartnership(BaseTableModel, table=True):
    coach: str = Field(default=None, max_length=100)
    coachee: str = Field(default=None, max_length=100)
    coachee_user: str = Field(default=None, max_length=15)
    coach_user: str = Field(default=None, max_length=15)
    parent_url: str = Field(default=None, max_length=50)
    participant: str = Field(default=None, max_length=50)
    participant_user: str = Field(default=None, max_length=50)
    partnership_filters: str = Field(default=None, max_length=100)
    partnership_status: str = Field(default=None, max_length=25)
    pbc_members: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    pbc_roles: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    prototype_description: str = Field(default=None, max_length=200)
    prototype_status: str = Field(default=None, max_length=10)
    template: str = Field(default=None, max_length=100)

class CollaboraEndpoint(BaseTableModel, table=True):
    pass

class Comments(BaseTableModel, table=True):
    recipe_key: int
    submit: str = Field(default=None, max_length=50)  # Renamed from 'submit'
    Submit: str = Field(default=None, max_length=50)  # Renamed from 'Submit'
    text: str = Field(default=None, sa_column_kwargs={"type_": "Text"})
    timestamp: datetime = Field(default=None)  # Renamed from 'timestamp' and changed type

    @FieldValidator('timestamp', pre=True)
    def validate_timestamp(cls, value: int) -> datetime:
        """Validator for the timestamp field to convert int to datetime."""
        return datetime.fromtimestamp(value)