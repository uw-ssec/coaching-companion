from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from pydantic import field_validator, HttpUrl
from sqlalchemy import BigInteger

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
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=None, sa_column_kwargs={"nullable": False})
    created_by: int = Field(default=None, foreign_key="auth_users.id", sa_type=BigInteger, sa_column_kwargs={"nullable": False})
    title: str = Field(default=None, max_length=255)
    type_: Optional[str] = Field(default=None, max_length=50)  # Optional varchar(50) field

    # Validator for the created_at field to convert Unix timestamp to datetime.
    _created_at = field_validator('created_at')(convert_timestamp_to_datetime)