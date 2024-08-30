import pytest
from datetime import datetime, timezone
from coaching_companion.models import AuthUsersLogCopGroupsDigest

def test_authuserslogcopgroupsdigest():
    # Define the datetime string
    datetime_str = "2021-12-01T00:00:00Z"
    # Parse the datetime string into a datetime object
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    # Convert the datetime object to a Unix timestamp (float)
    unix_timestamp = datetime_obj.replace(tzinfo=timezone.utc).timestamp()
    
    # Create an instance of AuthUsersLogCopGroupsDigest
    dashboard = AuthUsersLogCopGroupsDigest(
        created_at=unix_timestamp,
        created_by=int(12345678901234567890),
        title="Test AuthUsersLogCopGroupsDigest Title",
        type_="authuserslogcopgroupsdigest"
    )

    # Assert that the fields are correctly set
    assert dashboard.created_by == int(12345678901234567890)
    assert dashboard.title == "Test AuthUsersLogCopGroupsDigest Title"
    assert dashboard.type_ == "authuserslogcopgroupsdigest"

    # Convert the Unix timestamp to a UTC datetime object
    expected_created_at = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    # Format the datetime object to the desired string format
    expected_created_at_str = expected_created_at.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Assert that the created_at field is correctly converted and formatted
    assert expected_created_at_str == datetime_str

def test_authuserslogcopgroupsdigest_default_values():
    # Define the datetime string
    datetime_str = "2021-12-01T00:00:00Z"
    # Parse the datetime string into a datetime object
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    # Convert the datetime object to a Unix timestamp (float)
    unix_timestamp = datetime_obj.replace(tzinfo=timezone.utc).timestamp()
    
    # Create an instance of AuthUsersLogCopGroupsDigest without optional fields
    dashboard = AuthUsersLogCopGroupsDigest(title="Test Dashboard", created_at=unix_timestamp)

    # Assert that the default values are correctly set
    assert dashboard.id is None
    assert dashboard.created_by is None
    assert isinstance(dashboard.created_at, float)

def test_authuserslogcopgroupsdigest_name_max_length():
    # Define the datetime string
    datetime_str = "2021-12-01T00:00:00Z"
    # Parse the datetime string into a datetime object
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    # Convert the datetime object to a Unix timestamp (float)
    unix_timestamp = datetime_obj.replace(tzinfo=timezone.utc).timestamp()
    
    # Create an instance of AuthUsersLogCopGroupsDigest with a name exceeding max_length
    long_name = "A" * 300
    # Validate the title
    with pytest.raises(ValueError):
        AuthUsersLogCopGroupsDigest.model_validate({"title": long_name})
    # Validate the created_by
    with pytest.raises(ValueError):
        AuthUsersLogCopGroupsDigest.model_validate({"created_by": long_name})
    # Validate the created_at
    with pytest.raises(ValueError):
        AuthUsersLogCopGroupsDigest.model_validate({"created_at": long_name})
    # Validate the type_
    with pytest.raises(ValueError):
        AuthUsersLogCopGroupsDigest.model_validate({"type_": long_name})

# Run the tests
if __name__ == "__main__":
    pytest.main()
    
# References:
# - https://github.com/fastapi/sqlmodel/issues/52
    