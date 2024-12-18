from typing import Optional
from sqlmodel import SQLModel, Field, String, BigInteger
from datetime import datetime, timezone
from pydantic import field_validator, HttpUrl
import uuid

# Reusable function to convert Unix timestamp to datetime
@classmethod
def convert_timestamp_to_datetime(cls, value):
    # Check if the value is already a datetime object
    if isinstance(value, datetime):
        # Format the datetime object to the desired string format
        return value.strftime("%Y-%m-%dT%H:%M:%SZ")
    # Convert the Unix timestamp to a UTC datetime object
    utc_datetime = datetime.fromtimestamp(value, tz=timezone.utc)
    # Format the datetime object to the desired string format
    formatted_datetime = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    return formatted_datetime

# Reusable function to convert string to datetime
@classmethod
def convert_str_to_datetime(cls, value):
    # Convert the string to a datetime object
    datetime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ") # Update to match the desired format (and tests0.)
    return datetime_obj

@classmethod
def convert_str_to_url(cls, value):
    # Convert the string to a URL object
    url = HttpUrl(value)
    return url

@classmethod
def convert_int_to_uuid(cls, value):
    if isinstance(value, int):
        # Convert integer to UUID (example logic, adjust as needed)
        return uuid.UUID(int=value)
    return value

# Source: https://www.udacity.com/blog/2021/05/managing-dates-with-javascript-date-formats.html

# The BaseTableModel class is a base class for all the tables in the database.
class BaseTableModel(SQLModel):
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=None, nullable=False)
    created_by: int = Field(default=None, foreign_key="public.auth_user.id", sa_type=BigInteger, nullable=False)
    title: str = Field(default=None, sa_type=String(255), max_length=255)  # Required varchar(255) field
    type_: Optional[str] = Field(default=None, sa_type=String(50), max_length=50)  # Optional varchar(50) field

    # Validator for the created_at field to convert Unix timestamp to datetime.
    _created_at = field_validator('created_at', mode="before")(convert_timestamp_to_datetime)