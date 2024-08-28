from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from pydantic import HttpUrl, field_validator
from sqlalchemy import BigInteger, Text

# Reusable function to convert Unix timestamp to datetime
@classmethod
def convert_timestamp_to_datetime(cls,value):
    # Convert the Unix timestamp to a UTC datetime object
    utc_datetime = datetime.fromtimestamp(value, tz=timezone.utc)
    # Format the datetime object to the desired string format
    formatted_datetime = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    return formatted_datetime

@classmethod
def convert_str_to_url(cls, value):
    # Convert the string to a URL object
    url = HttpUrl(value)
    return url

# Source: https://www.udacity.com/blog/2021/05/managing-dates-with-javascript-date-formats.html

# The BaseTableModel class is a base class for all the tables in the database.
class BaseTableModel(SQLModel, table=False):
    created_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})
    created_by: int = Field(default=None, foreign_key="auth_users.id", sa_column_kwargs={"type_": BigInteger, "nullable": False})
    title: str = Field(default=None, max_length=255)
    class_name: Optional[str] = Field(default=None, max_length=50)  # Optional varchar(50) field

    # Validator for the created_at field to convert Unix timestamp to datetime.
    _created_at = field_validator('created_at')(convert_timestamp_to_datetime)

"""
The following classes define the tables in the database. 
Each class inherits from the BaseTableModel class and specifies the fields for the table. 
The table=True argument is used to indicate that the class represents a table in the database. 
The fields are defined using the Field class from the SQLModel library, which allows specifying the field type, default value, and other properties.
The field_validator decorator is used to define validators for the fields, which can perform validation or transformation of the field values.
"""



class AWSDashboard(BaseTableModel, table=True):
    __tablename__ = "aws_dashboard"
    __table_args__ = {"schema": "public"}
    
    pass

class Access(BaseTableModel, table=True):
    __tablename__ = "access"
    __table_args__ = {"schema": "public"}
    
    content_create: str = Field(default=None, max_length=10)
    content_delete: str = Field(default=None, max_length=10)
    content_edit: str = Field(default=None, max_length=10)
    recipe_key: int = Field(default=None)
    repudiated_url: HttpUrl = Field(sa_type=Text)
    role_access: str = Field(default=None, max_length=50)

class AccreditationCertificate(BaseTableModel, table=True):
    __tablename__ = "accreditation_certificate"
    __table_args__ = {"schema": "public"}
    
    pass
    
class AccreditationSubmission(BaseTableModel, table=True):
    __tablename__ = "accreditation_submission"
    __table_args__ = {"schema": "public"}
    
    pass
    
class ActionPlans(BaseTableModel, table=True): # TODO: Update completed_at based on the int input type
    __tablename__ = "action_plans"
    __table_args__ = {"schema": "public"}
    
    id: int = Field(default=None, primary_key=True)
    completed_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime, not Optional[int]
    cycle_summary: str = Field(default=None, sa_type=Text)
    info: str = Field(default=None, sa_type=Text)  # Treated as text, equivalent to varchar without a strict length limit
    next_step_notes: str = Field(default=None, sa_type=Text)
    status: str = Field(default=None, max_length=20)
    step_info_NaN: str = Field(default=None, max_length=100)  # Consider renaming to follow Python naming conventions

    _completed_at = field_validator('completed_at')(convert_timestamp_to_datetime)

class AddPlayByPlay(BaseTableModel, table=True): # TODO: Does this table have a primary key?
    __tablename__ = "add_play_by_play"
    __table_args__ = {"schema": "public"}
    
    item_id: int = Field(default=None)
    timestamp: datetime = Field(default=None, sa_column_kwargs={"nullable": False})  # Now a datetime

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)

class Alias(BaseTableModel, table=True):
    __tablename__ = "alias"
    __table_args__ = {"schema": "public"}
    
    alias_id: int = Field(primary_key=True)
    children_sequencer: str = Field(max_length=10)
    created_at: datetime = Field()
    created_by: int = Field(foreign_key="auth_users.id")
    id: str = Field(max_length=50)
    login_disabled: bool = Field()
    media: str = Field(max_length=60)
    media_type: str = Field(max_length=100)
    on_cloudfront: str = Field(max_length=10)
    published: str = Field(max_length=50)
    ratings_id: str = Field(max_length=50)
    recipe: str = Field(max_length=255)
    recipe_key: int = Field()
    recipe_name: str = Field(max_length=50)
    report_types: str = Field(max_length=50)
    template: str = Field(max_length=100)
    title: str = Field(max_length=255)
    type: str = Field(max_length=50)

class Annotations(SQLModel, table=True):
    __tablename__ = "annotations"
    __table_args__ = {"schema": "public"}
    
    info: str = Field(default=None, sa_type=Text)  # Treated as text, equivalent to varchar without a strict length limit
    recipe_key: int = Field(default=None)

class AssessmentsClassroom(BaseTableModel, table=True):
    __tablename__ = "assessments_classroom"
    __table_args__ = {"schema": "public"}
    
    pass

class AssessmentsDashboard(BaseTableModel, table=True):
    __tablename__ = "assessments_dashboard"
    __table_args__ = {"schema": "public"}
    
    pass

class AssessmentsEvaluation(BaseTableModel, table=True):
    __tablename__ = "assessments_evaluation"
    __table_args__ = {"schema": "public"}
    
    recipe_key: int = Field(default=None)
    title_eng: str = Field(default=None, max_length=255)  # English title

class AssessmentsLister(BaseTableModel, table=True):
    __tablename__ = "assessments_lister"
    __table_args__ = {"schema": "public"}
    
    title_eng: str = Field(default=None, max_length=255)  # English title
    lister_authority: str = Field(default=None, max_length=50)  # Authority of the lister
    template: str = Field(default=None, max_length=100)

class AssessmentsRating(BaseTableModel, table=True):
    __tablename__ = "assessments_rating"
    __table_args__ = {"schema": "public"}
    
    pass

class AssessmentsReport(BaseTableModel, table=True):
    __tablename__ = "assessments_report"
    __table_args__ = {"schema": "public"}
    
    title_eng: str = Field(default=None, max_length=255)  # English title
    title_esp: str = Field(default=None, max_length=255)  # Spanish title

class AssessmentsReportClassroom(BaseTableModel, table=True):
    __tablename__ = "assessments_report_classroom"
    __table_args__ = {"schema": "public"}
    
    title_eng: str = Field(default=None, max_length=255)  # English title

class AssessmentsSite(BaseTableModel, table=True):
    __tablename__ = "assessments_site"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)

class Assets(BaseTableModel, table=True):
    __tablename__ = "assets"
    __table_args__ = {"schema": "public"}
    
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
    __tablename__ = "assignments"
    __table_args__ = {"schema": "public"}
    
    pass

class CoachingPartnership(BaseTableModel, table=True):
    __tablename__ = "coaching_partnership"
    __table_args__ = {"schema": "public"}
    
    coach: str = Field(default=None, max_length=100)
    coachee: str = Field(default=None, max_length=100)
    coachee_user: str = Field(default=None, max_length=15)
    coach_user: str = Field(default=None, max_length=15)
    parent_url: HttpUrl = Field(sa_type=Text)
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
    __tablename__ = "collabora_endpoint"
    __table_args__ = {"schema": "public"}
    
    pass

class Comments(BaseTableModel, table=True):
    __tablename__ = "comments"
    __table_args__ = {"schema": "public"}
    
    recipe_key: int
    submit: str = Field(default=None, max_length=50)  # Renamed from 'submit'
    Submit: str = Field(default=None, max_length=50)  # Renamed from 'Submit'
    text: str = Field(default=None, sa_type=Text)
    timestamp: datetime = Field(default=None)  # Renamed from 'timestamp' and changed type

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)
    
class ConnectToMerit(BaseTableModel, table=True):
    __tablename__ = "connect_to_merit"
    __table_args__ = {"schema": "public"}
    
    pass

class ContactForm(BaseTableModel, table=True):
    __tablename__ = "contact_form"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class CopAssets(BaseTableModel, table=True):
    __tablename__ = "cop_assets"
    __table_args__ = {"schema": "public"}
    
    pass

class CopGroups(BaseTableModel, table=True):
    __tablename__ = "cop_groups"
    __table_args__ = {"schema": "public"}
    
    cop_admins: str = Field(default=None, max_length=100)
    cop_group_admin: str = Field(default=None, max_length=15)
    user_id: int = Field(default=None)
    cop_asset_creation: str = Field(default=None, max_length=15)
    hide_video_conferencing: str = Field(default=None, max_length=10)
    hide_cop_resources: str = Field(default=None, max_length=10)
    user_type: str = Field(default=None, max_length=50)
    parent_url: HttpUrl = Field(sa_type=Text)
    cqelcoach_group: int = Field(default=None)
    cop_topic_creation: str = Field(default=None, max_length=15)
    cop_members: str = Field(default=None, max_length=100)
    disable_opt_out: str = Field(default=None, max_length=10)
    hide_cop_members: str = Field(default=None, max_length=10)

class CopLocation(BaseTableModel, table=True):
    __tablename__ = "cop_location"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)

class CoursesState(BaseTableModel, table=True):
    __tablename__ = "courses_state"
    __table_args__ = {"schema": "public"}
    
    sub_roles: str = Field(default=None, max_length=50)
    course_name: str = Field(default=None, max_length=150)
    course_identifier: str = Field(default=None, max_length=50)
    course_number: str = Field(default=None, max_length=50)
    lms_prototype: str = Field(default=None, max_length=50)
    prototype_copy: int = Field(default=None)
    lms_course_url: str = Field(default=None, max_length=100)

class CycleDashboard(BaseTableModel, table=True):
    __tablename__ = "cycle_dashboard"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)

class DiscussionBoards(BaseTableModel, table=True):
    __tablename__ = "discussion_boards"
    __table_args__ = {"schema": "public"}
    
    role_designation: str = Field(default=None, max_length=50)
    description: str = Field(default=None, sa_type=Text)

class DiscussionTopics(BaseTableModel, table=True):
    __tablename__ = "discussion_topics"
    __table_args__ = {"schema": "public"}
    
    id: str = Field(default=None, primary_key=True, max_length=50)
    prevent_inline_media: bool = Field(default=None)
    update_created_at: datetime = Field(default=None)

    _update_created_at = field_validator('update_created_at')(convert_timestamp_to_datetime)

class Documentation(BaseTableModel, table=True):
    __tablename__ = "documentation"
    __table_args__ = {"schema": "public"}
    
    pass

class DualLanguageHandbook(BaseTableModel, table=True):
    __tablename__ = "dual_language_handbook"
    __table_args__ = {"schema": "public"}
    
    pass

class DualLanguageSubmission(BaseTableModel, table=True):
    __tablename__ = "dual_language_submission"
    __table_args__ = {"schema": "public"}
    
    pass

class EaEvalSurvey(BaseTableModel, table=True): # Renamed from 'Ea_eval_survey'
    __tablename__ = "ea_eval_survey"
    __table_args__ = {"schema": "public"}
    
    pass

class Endpoint(BaseTableModel, table=True):
    __tablename__ = "endpoint"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)

class FamilySurveyLink(BaseTableModel, table=True):
    __tablename__ = "family_survey_link"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class Grade(BaseTableModel, table=True):
    __tablename__ = "grade"
    __table_args__ = {"schema": "public"}
    
    pass

class Inquisitor(BaseTableModel, table=True):
    __tablename__ = "inquisitor"
    __table_args__ = {"schema": "public"}
    
    pass

class InstructorMaterials(BaseTableModel, table=True):
    __tablename__ = "instructor_materials"
    __table_args__ = {"schema": "public"}
    
    components_limit: int = Field(default=None)

class Item(BaseTableModel, table=True):
    __tablename__ = "item"
    __table_args__ = {"schema": "public"}
    
    filter_by: str = Field(default=None, max_length=100)

class Layout(BaseTableModel, table=True):
    __tablename__ = "layout"
    __table_args__ = {"schema": "public"}
    
    class_: str = Field(default=None, max_length=10, alias='class') # Renamed from 'class'

class Limit(BaseTableModel, table=True):
    __tablename__ = "limit"
    __table_args__ = {"schema": "public"}
    
    components_limit: int = Field(default=None)
    recipe_key: int = Field(default=None)

class Links(BaseTableModel, table=True):
    __tablename__ = "links"
    __table_args__ = {"schema": "public"}
    
    target: str = Field(default=None, max_length=20)
    link_url: str = Field(default=None, max_length=150)
    color: str = Field(default=None, max_length=10)
    role_access: str = Field(default=None, max_length=50)

class Lister(BaseTableModel, table=True):
    __tablename__ = "lister"
    __table_args__ = {"schema": "public"}
    
    lister_authority_display: str = Field(default=None, max_length=20)
    repudiated_url: HttpUrl = Field(sa_type=Text)
    lister_authority: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)
    members: str = Field(default=None, max_length=100)

class Location(BaseTableModel, table=True):
    __tablename__ = "location"
    __table_args__ = {"schema": "public"}
    
    order_direction: str = Field(default=None, max_length=15)
    recipe: str = Field(default=None, max_length=255)
    children_sequencer: str = Field(default=None, max_length=10)
    order_by: str = Field(default=None, max_length=50)
    template: str = Field(default=None, max_length=100)

class Login(BaseTableModel, table=True):
    __tablename__ = "login"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    login_disabled: bool = Field(default=None)
    template: str = Field(default=None, max_length=100)

class Logout(BaseTableModel, table=True):
    __tablename__ = "logout"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    recipe_name: str = Field(default=None, max_length=50)

class LtiEndpoint(BaseTableModel, table=True):
    __tablename__ = "lti_endpoint"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)

class ManageComponents(BaseTableModel, table=True):
    __tablename__ = "manage_components"
    __table_args__ = {"schema": "public"}
    
    pass

class ManageDatalists(BaseTableModel, table=True):
    __tablename__ = "manage_datalists"
    __table_args__ = {"schema": "public"}
    
    pass

class ManageGroups(BaseTableModel, table=True):
    __tablename__ = "manage_groups"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)

class ManageMenus(BaseTableModel, table=True):
    __tablename__ = "manage_menus"
    __table_args__ = {"schema": "public"}
    
    pass

class ManageRecipes(BaseTableModel, table=True):
    __tablename__ = "manage_recipes"
    __table_args__ = {"schema": "public"}
    
    pass

class ManageSite(BaseTableModel, table=True):
    __tablename__ = "manage_site"
    __table_args__ = {"schema": "public"}
    
    pass

class ManageStudents(BaseTableModel, table=True):
    __tablename__ = "manage_students"
    __table_args__ = {"schema": "public"}
    
    role_select: str = Field(default=None, max_length=50)

class ManageAuthUsers(BaseTableModel, table=True):
    __tablename__ = "manage_auth_users"
    __table_args__ = {"schema": "public"}
    
    pass

class Media(BaseTableModel, table=True):
    __tablename__ = "media"
    __table_args__ = {"schema": "public"}
    
    code: str = Field(default=None, max_length=100)
    cqelcoach_resource: int = Field(default=None)
    description: str = Field(default=None)
    disable_captions: bool = Field(default=None)
    filename: str = Field(default=None, max_length=100)
    inputtypes: str = Field(default=None, max_length=50)
    job_id: str = Field(default=None, max_length=50)
    link: HttpUrl = Field(sa_type=Text)
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
    __tablename__ = "media_database"
    __table_args__ = {"schema": "public"}
    
    pass

class MeritEndpoint(BaseTableModel, table=True):
    __tablename__ = "merit_endpoint"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)

class MssqlServer(BaseTableModel, table=True):
    __tablename__ = "mssql_server"
    __table_args__ = {"schema": "public"}
    
    username: str = Field(default=None, max_length=50)
    password: str = Field(default=None, max_length=25)
    host: str = Field(default=None, sa_type=Text) # Consider using a URL field type
    name: str = Field(default=None, max_length=100)

class Note(BaseTableModel, table=True):
    __tablename__ = "note"
    __table_args__ = {"schema": "public"}
    
    notes: str = Field(default=None)

class ProgramProfileSubmission(BaseTableModel, table=True):
    __tablename__ = "program_profile_submission"
    __table_args__ = {"schema": "public"}
    
    pass

class RatingsRubric(BaseTableModel, table=True):
    __tablename__ = "ratings_rubric"
    __table_args__ = {"schema": "public"}
    
    pass

class RecordsReviewHandbook(BaseTableModel, table=True):
    __tablename__ = "records_review_handbook"
    __table_args__ = {"schema": "public"}
    
    pass

class RecordsReviewSubmission(BaseTableModel, table=True):
    __tablename__ = "records_review_submission"
    __table_args__ = {"schema": "public"}
    
    pass

class ReflectionAssignment(BaseTableModel, table=True):
    __tablename__ = "reflection_assignment"
    __table_args__ = {"schema": "public"}
    
    assignment_category: str = Field(default=None, max_length=15)
    components_limit: int = Field(default=None)
    instructions: str = Field(default=None, sa_type=Text)
    recipe_key: int = Field(default=None)

class Reports(BaseTableModel, table=True):
    __tablename__ = "reports"
    __table_args__ = {"schema": "public"}
    
    report_types: str = Field(default=None, max_length=50)

class ReportsBuilder(BaseTableModel, table=True):
    __tablename__ = "reports_builder"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    report_types: str = Field(default=None, max_length=50)

class Resetpassword(BaseTableModel, table=True):
    __tablename__ = "reset_password"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class ResourceLibrary(BaseTableModel, table=True):
    __tablename__ = "resource_library"
    __table_args__ = {"schema": "public"}
    
    pass

class SharedAssets(BaseTableModel, table=True):
    __tablename__ = "shared_assets"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)

class SharedGoals(BaseTableModel, table=True):
    __tablename__ = "shared_goals"
    __table_args__ = {"schema": "public"}
    
    completed_at: datetime = Field(default=None)
    core_knowledge_categories: str = Field(default=None, max_length=100)
    cycle_summary: str = Field(default=None)
    info: str = Field(default=None)
    prototype_id: int = Field(default=None)
    status: str = Field(default=None, max_length=20)

    _completed_at = field_validator('completed_at')(convert_timestamp_to_datetime)

class Solotron(BaseTableModel, table=True):
    __tablename__ = "solotron"
    __table_args__ = {"schema": "public"}
    
    can_survey_components: str = Field(default=None, max_length=150)

class StudentSubmissions(BaseTableModel, table=True):
    __tablename__ = "student_submissions"
    __table_args__ = {"schema": "public"}
    
    pass

class StudentSubmissionsSlug(BaseTableModel, table=True):
    __tablename__ = "student_submissions_slug"
    __table_args__ = {"schema": "public"}
    
    pass

class SupportingDocumentation(BaseTableModel, table=True):
    __tablename__ = "supporting_documentation"
    __table_args__ = {"schema": "public"}
    
    pass

class Tagit(BaseTableModel, table=True):
    __tablename__ = "tagit"
    __table_args__ = {"schema": "public"}

    timestamp: datetime = Field(default=None)

    _timestamp = field_validator('timestamp')(convert_timestamp_to_datetime)

class Tracker(BaseTableModel, table=True):
    __tablename__ = "tracker"
    __table_args__ = {"schema": "public"}
    
    description: str = Field(default=None)
    template: str = Field(default=None, max_length=100)

class UnassignedAssets(BaseTableModel, table=True):
    __tablename__ = "unassigned_assets"
    __table_args__ = {"schema": "public"}
    
    template: str = Field(default=None, max_length=100)

class UploadAndReflectionAssignment(BaseTableModel, table=True):
    __tablename__ = "upload_and_reflection_assignment"
    __table_args__ = {"schema": "public"}
    
    assignment_category: str = Field(default=None, max_length=15)
    components_limit: int = Field(default=None)
    grading_rubric: str = Field(default=None)
    instructions: str = Field(default=None, sa_type=Text)
    recipe_key: int = Field(default=None)

class UserInvitations(BaseTableModel, table=True):
    __tablename__ = "user_invitations"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    template: str = Field(default=None, max_length=100)

class AuthUserSettings(BaseTableModel, table=True):
    __tablename__ = "auth_user_settings"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    recipe_name: str = Field(default=None, max_length=50)

class AuthUserSubmissions(BaseTableModel, table=True):
    __tablename__ = "auth_user_submissions"
    __table_args__ = {"schema": "public"}
    
    recipe: str = Field(default=None, max_length=255)
    can_view: str = Field(default=None, max_length=150)
    repudiated_url: HttpUrl = Field(sa_type=Text)
    can_submit: str = Field(default=None, max_length=150) # Should this be a boolean field?
    content_administrator: str = Field(default=None, max_length=10)

class AuthUsersLogAllAttributes(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_all_attributes"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogCompletedGoals(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_completed_goals"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogCopGroups(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_cop_groups"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogCopGroupsDigest(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_cop_groups_digest"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogCreatedAt(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_created_at"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogPartnerships(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_partnerships"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogProperties(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_properties"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogReporting(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_reporting"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogSharedGoals(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_shared_goals"
    __table_args__ = {"schema": "public"}
    
    pass

class AuthUsersLogUploads(BaseTableModel, table=True):
    __tablename__ = "auth_users_log_uploads"
    __table_args__ = {"schema": "public"}
    
    pass

class VideoConference(BaseTableModel, table=True):
    __tablename__ = "video_conference"
    __table_args__ = {"schema": "public"}
    
    pass

class VideoHighlightSubmission(BaseTableModel, table=True):
    __tablename__ = "video_highlight_submission"
    __table_args__ = {"schema": "public"}
    
    pass

class VideoReflection(BaseTableModel, table=True):
    __tablename__ = "video_reflection"
    __table_args__ = {"schema": "public"}
    
    idClassroom: int = Field(default=None)
    idRating: int = Field(default=None)
    idVHResponse: int = Field(default=None)
    parent_url: HttpUrl = Field(sa_type=Text)
    procedure: str = Field(default=None, max_length=20)
    ratings_id: str = Field(default=None, max_length=50)
    reflection_input: str = Field(default=None)
    updated_on: datetime = Field(default=None)
