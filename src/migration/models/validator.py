from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import HttpUrl, field_validator
from sqlalchemy import BigInteger

# The BaseTableModel class is a base class for all the tables in the database.
class BaseTableModel(SQLModel, table=False):
    created_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})
    created_by: int = Field(default=None, foreign_key="auth_users.id", sa_column_kwargs={"type_": BigInteger, "nullable": False})
    title: str = Field(default=None, max_length=255)
    type: Optional[str] = Field(default=None, max_length=50)  # Optional varchar(50) field

    @field_validator('created_at', pre=True)
    # Validator for the created_at field to convert Unix timestamp to datetime.
    @classmethod
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value)
    
"""
The following classes define the tables in the database. 
Each class inherits from the BaseTableModel class and specifies the fields for the table. 
The table=True argument is used to indicate that the class represents a table in the database. 
The fields are defined using the Field class from the SQLModel library, which allows specifying the field type, default value, and other properties.
The field_validator decorator is used to define validators for the fields, which can perform validation or transformation of the field values.
"""

class AWSDashboard(BaseTableModel, table=True):
    pass

class Access(BaseTableModel, table=True):
    content_create: str = Field(default=None, max_length=10)
    content_delete: str = Field(default=None, max_length=10)
    content_edit: str = Field(default=None, max_length=10)
    recipe_key: int = Field(default=None)
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

    @field_validator('completed_at', pre=True)
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value)

class AddPlayByPlay(BaseTableModel, table=True): # TODO: Does this table have a primary key?
    item_id: int = Field(default=None)
    timestamp: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime

    @field_validator('timestamp', pre=True)
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
    parent_url: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    participant: str = Field(default=None, max_length=50)
    participant_user: str = Field(default=None, max_length=50)
    partnership_filters: str = Field(default=None, max_length=100)
    partnership_status: str = Field(default=None, max_length=25)
    pbc_members: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    pbc_roles: str = Field(default=None, max_length=100)  # Consider a separate table for a many-to-many relationship
    prototype_description: str = Field(default=None, max_length=200)
    prototype_status: str = Field(default=None, max_length=10)
    template: str = Field(default=None, max_length=100) # Consider a separate table for normalization

class CollaboraEndpoint(BaseTableModel, table=True):
    pass

class Comments(BaseTableModel, table=True):
    recipe_key: int
    submit: str = Field(default=None, max_length=50)  # Renamed from 'submit'
    Submit: str = Field(default=None, max_length=50)  # Renamed from 'Submit'
    text: str = Field(default=None, sa_column_kwargs={"type_": "Text"})
    timestamp: datetime = Field(default=None)  # Renamed from 'timestamp' and changed type

    @field_validator('timestamp', pre=True)
    def validate_timestamp(cls, value: int) -> datetime:
        """Validator for the timestamp field to convert int to datetime."""
        return datetime.fromtimestamp(value)
    
class ConnectToMerit(BaseTableModel, table=True):
    pass

class ContactForm(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class CopAssets(BaseTableModel, table=True):
    pass

class CopGroups(BaseTableModel, table=True):
    cop_admins: str = Field(default=None, max_length=100)
    cop_group_admin: str = Field(default=None, max_length=15)
    user_id: int = Field(default=None)
    cop_asset_creation: str = Field(default=None, max_length=15)
    hide_video_conferencing: str = Field(default=None, max_length=10)
    hide_cop_resources: str = Field(default=None, max_length=10)
    user_type: str = Field(default=None, max_length=50)
    parent_url: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    cqelcoach_group: int = Field(default=None)
    cop_topic_creation: str = Field(default=None, max_length=15)
    cop_members: str = Field(default=None, max_length=100)
    disable_opt_out: str = Field(default=None, max_length=10)
    hide_cop_members: str = Field(default=None, max_length=10)

class CopLocation(BaseTableModel, table=True):
    template: str = Field(default=None, max_length=100)

class CoursesState(BaseTableModel, table=True):
    sub_roles: str = Field(default=None, max_length=50)
    course_name: str = Field(default=None, max_length=150)
    course_identifier: str = Field(default=None, max_length=50)
    course_number: str = Field(default=None, max_length=50)
    lms_prototype: str = Field(default=None, max_length=50)
    prototype_copy: int = Field(default=None)
    lms_course_url: str = Field(default=None, max_length=100)

class CycleDashboard(BaseTableModel, table=True):
    template: str = Field(default=None, max_length=100)

class DiscussionBoards(BaseTableModel, table=True):
    role_designation: str = Field(default=None, max_length=50)
    description: str = Field(default=None, sa_column_kwargs={"type_": "Text"})

class DiscussionTopics(BaseTableModel, table=True):
    id: str = Field(default=None, primary_key=True, max_length=50)
    prevent_inline_media: bool = Field(default=None)
    update_created_at: datetime = Field(default=None)

    @field_validator('update_created_at', pre=True)
    def validate_timestamp(cls, value: int) -> datetime:
        """Validator for the update_created_at field to convert int to datetime."""
        return datetime.fromtimestamp(value)

class Documentation(BaseTableModel, table=True):
    pass

class DualLanguageHandbook(BaseTableModel, table=True):
    pass

class DualLanguageSubmission(BaseTableModel, table=True):
    pass

class EaEvalSurvey(BaseTableModel, table=True): # Renamed from 'Ea_eval_survey'
    pass

class Endpoint(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)

class FamilySurveyLink(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class Grade(BaseTableModel, table=True):
    pass

class Inquisitor(BaseTableModel, table=True):
    pass

class InstructorMaterials(BaseTableModel, table=True):
    components_limit: int = Field(default=None)

class Item(BaseTableModel, table=True):
    filter_by: str = Field(default=None, max_length=100)

class Layout(BaseTableModel, table=True):
    class_: str = Field(default=None, max_length=10, alias='class') # Renamed from 'class'

class Limit(BaseTableModel, table=True):
    components_limit: int = Field(default=None)
    recipe_key: int = Field(default=None)

class Links(BaseTableModel, table=True):
    target: str = Field(default=None, max_length=20)
    link_url: str = Field(default=None, max_length=150)
    color: str = Field(default=None, max_length=10)
    role_access: str = Field(default=None, max_length=50)

class Lister(BaseTableModel, table=True):
    lister_authority_display: str = Field(default=None, max_length=20)
    repudiated_url: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    lister_authority: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)
    members: str = Field(default=None, max_length=100)

class Location(BaseTableModel, table=True):
    order_direction: str = Field(default=None, max_length=15)
    recipe: str = Field(default=None, max_length=255)
    children_sequencer: str = Field(default=None, max_length=10)
    order_by: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)

class Login(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    login_disabled: bool = Field(default=None)
    template: str = Field(default=None, max_length=100)

class Logout(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    recipe_name: str = Field(default=None, max_length=50)

class LtiEndpoint(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)

class ManageComponents(BaseTableModel, table=True):
    pass

class ManageDatalists(BaseTableModel, table=True):
    pass

class ManageGroups(BaseTableModel, table=True):
    template: str = Field(default=None, max_length=100)

class ManageMenus(BaseTableModel, table=True):
    pass

class ManageRecipes(BaseTableModel, table=True):
    pass

class ManageSite(BaseTableModel, table=True):
    pass

class ManageStudents(BaseTableModel, table=True):
    role_select: str = Field(default=None, max_length=50)

class ManageAuthUsers(BaseTableModel, table=True):
    pass

class Media(BaseTableModel, table=True):
    code: str = Field(default=None, max_length=100)
    cqelcoach_resource: int = Field(default=None)
    description: str = Field(default=None)
    disable_captions: bool = Field(default=None)
    filename: str = Field(default=None, max_length=100)
    id: str = Field(default=None, max_length=50) # Foreign Key?
    inputtypes: str = Field(default=None, max_length=50)
    job_id: str = Field(default=None, max_length=50)
    link: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    media_type: str = Field(default=None, max_length=100)
    name: str = Field(default=None, max_length=100)
    on_cloudfront: str = Field(default=None, max_length=10)
    path: str = Field(default=None, max_length=50)
    published: str = Field(default=None, max_length=50)
    ratings_id: str = Field(default=None, max_length=50)
    recipe_key: int = Field(default=None)
    taxonomy: str = Field(default=None, max_length=255)
    text: str = Field(default=None)
    vide_hightlight_location: str = Field(default=None, max_length=100)
    video_hightlight_alias_id: int = Field(default=None)
    video_hightlight_created_by: int = Field(default=None, foreign_key="auth_users.id")
    video_hightlight_location: str = Field(default=None, max_length=100)
    video_hightlight_submission: int = Field(default=None)
    video_hightlight_submission_at: int = Field(default=None)
    video_hightlight_submission_copy: int = Field(default=None)
    vtt: str = Field(default=None, max_length=255)

class MediaDatabase(BaseTableModel, table=True):
    pass

class MeritEndpoint(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)

class MssqlServer(BaseTableModel, table=True):
    username: str = Field(default=None, max_length=50)
    password: str = Field(default=None, max_length=25)
    host: str = Field(default=None, max_length=100) # Consider using a URL field type
    name: str = Field(default=None, max_length=100)

class Note(BaseTableModel, table=True):
    notes: str = Field(default=None)

class ProgramProfileSubmission(BaseTableModel, table=True):
    pass

class RatingsRubric(BaseTableModel, table=True):
    pass

class RecordsReviewHandbook(BaseTableModel, table=True):
    pass

class RecordsReviewSubmission(BaseTableModel, table=True):
    pass

class ReflectionAssignment(BaseTableModel, table=True):
    assignment_category: str = Field(default=None, max_length=15)
    components_limit: int = Field(default=None)
    instructions: str = Field(default=None)
    recipe_key: int = Field(default=None)

class Reports(BaseTableModel, table=True):
    report_types: str = Field(default=None, max_length=50)

class ReportsBuilder(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    report_types: str = Field(default=None, max_length=50)

class ResetPassword(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class ResourceLibrary(BaseTableModel, table=True):
    pass

class SharedAssets(BaseTableModel, table=True):
    template: str = Field(default=None, max_length=100)

class SharedGoals(BaseTableModel, table=True):
    completed_at: datetime = Field(default=None)
    core_knowledge_categories: str = Field(default=None, max_length=100)
    cycle_summary: str = Field(default=None)
    info: str = Field(default=None)
    prototype_id: int = Field(default=None)
    status: str = Field(default=None, max_length=20)

    @field_validator('completed_at', pre=True)
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value)

class Solotron(BaseTableModel, table=True):
    can_survey_components: str = Field(default=None, max_length=150)

class StudentSubmissions(BaseTableModel, table=True):
    pass

class StudentSubmissionsSlug(BaseTableModel, table=True):
    pass

class SupportingDocumentation(BaseTableModel, table=True):
    pass

class Tagit(BaseTableModel, table=True):
    timestamp: datetime = Field(default=None)

    @field_validator('timestamp', pre=True)
    def validate_timestamp(cls, value: int) -> datetime:
        """Validator for the timestamp field to convert int to datetime."""
        return datetime.fromtimestamp(value)

class Tracker(BaseTableModel, table=True):
    description: str = Field(default=None)
    template: str = Field(default=None, max_length=100)

class UnassignedAssets(BaseTableModel, table=True):
    template: str = Field(default=None, max_length=100)

class UploadAndReflectionAssignment(BaseTableModel, table=True):
    assignment_category: str = Field(default=None, max_length=15)
    components_limit: int = Field(default=None)
    grading_rubric: str = Field(default=None)
    instructions: str = Field(default=None)
    recipe_key: int = Field(default=None)

class UserInvitations(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class AuthUserSettings(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    recipe_name: str = Field(default=None, max_length=50)

class AuthUserSubmissions(BaseTableModel, table=True):
    recipe: str = Field(default=None, max_length=255)
    can_view: str = Field(default=None, max_length=150)
    repudiated_url: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    can_submit: str = Field(default=None, max_length=150)
    content_administrator: str = Field(default=None, max_length=10)

class AuthUsersLogAllAttributes(BaseTableModel, table=True):
    pass

class AuthUsersLogCompletedGoals(BaseTableModel, table=True):
    pass

class AuthUsersLogCopGroups(BaseTableModel, table=True):
    pass

class AuthUsersLogCopGroupsDigest(BaseTableModel, table=True):
    pass

class AuthUsersLogCreatedAt(BaseTableModel, table=True):
    pass

class AuthUsersLogPartnerships(BaseTableModel, table=True):
    pass

class AuthUsersLogProperties(BaseTableModel, table=True):
    pass

class AuthUsersLogReporting(BaseTableModel, table=True):
    pass

class AuthUsersLogSharedGoals(BaseTableModel, table=True):
    pass

class AuthUsersLogUploads(BaseTableModel, table=True):
    pass

class VideoConference(BaseTableModel, table=True):
    pass

class VideoHighlightSubmission(BaseTableModel, table=True):
    pass

class VideoReflection(BaseTableModel, table=True):
    idClassroom: int = Field(default=None)
    idRating: int = Field(default=None)
    idVHResponse: int = Field(default=None)
    parent_url: HttpUrl = Field(sa_column_kwargs={"type_": "Text"})
    procedure: str = Field(default=None, max_length=20)
    ratings_id: str = Field(default=None, max_length=50)
    reflection_input: str = Field(default=None)
    updated_on: datetime = Field(default=None)