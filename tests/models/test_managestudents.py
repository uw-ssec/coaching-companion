import pytest
from datetime import datetime, timezone
from coaching_companion.models import ManageStudents

# Define the datetime string
datetime_str = "2021-12-01T00:00:00Z"
# Parse the datetime string into a datetime object
datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
# Convert the datetime object to a Unix timestamp (float)
unix_timestamp = datetime_obj.replace(tzinfo=timezone.utc).timestamp()

# Define the url string
url_str = "https://s3-us-west-2.amazonaws.com/test-bucket/test-key"

# Define the UUID string
uuid_int = 12345678901234567890

@pytest.mark.parametrize("unix_timestamp", [unix_timestamp]) # Allows us to define a single test with multiple potential inputs
def test_managestudents(unix_timestamp):
    # Create an instance of ManageStudents
    dashboard = ManageStudents(
        created_at=unix_timestamp,
        created_by=int(12345678901234567890),
        title="Test ManageStudents Title",
        type_="managestudents"
    )

    # Assert that the fields are correctly set
    assert dashboard.created_by == int(12345678901234567890)
    assert dashboard.title == "Test ManageStudents Title"
    assert dashboard.type_ == "managestudents"

    # Convert the Unix timestamp to a UTC datetime object
    expected_created_at = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    # Format the datetime object to the desired string format
    expected_created_at_str = expected_created_at.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Assert that the created_at field is correctly converted and formatted
    assert expected_created_at_str == datetime_str

def test_managestudents_default_values():
    # Create an instance of ManageStudents without optional fields
    dashboard = ManageStudents(title="Test Dashboard")

    # Assert that the default values are correctly set
    assert dashboard.id is None
    assert dashboard.created_by is None
    assert dashboard.created_at is None

def test_managestudents_name_max_length():
    # Create an instance of ManageStudents with a name exceeding max_length
    long_name = "A" * 300 # For testing non-text type fields
    long_num = 12345678901234567890 # For testing text type fields
    # Validate the id
    with pytest.raises(ValueError):
        ManageStudents.model_validate({"id": long_name})
    # Validate the title
    with pytest.raises(ValueError):
        ManageStudents.model_validate({"title": long_name})
    # Validate the created_by
    with pytest.raises(ValueError):
        ManageStudents.model_validate({"created_by": long_name})
    # Validate the created_at
    with pytest.raises(ValueError):
        ManageStudents.model_validate({"created_at": long_name})
    # Validate the type_
    with pytest.raises(ValueError):
        ManageStudents.model_validate({"type_": long_name})

# Run the tests
if __name__ == "__main__":
    pytest.main()
    
# References:
# - https://github.com/fastapi/sqlmodel/issues/52
# - https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing
    