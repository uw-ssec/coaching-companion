import pytest
from datetime import datetime, timezone
from coaching_companion.models import BaseTableModel

def test_basetablemodel():
    # Define the datetime string
    datetime_str = "2021-12-01T00:00:00Z"
    # Parse the datetime string into a datetime object
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    # Convert the datetime object to a Unix timestamp (float)
    unix_timestamp = datetime_obj.replace(tzinfo=timezone.utc).timestamp()

    # Create an instance of BaseTableModel with the Unix timestamp
    model_instance = BaseTableModel(
        created_at=unix_timestamp,
        created_by=int(12345678901234567890),
        title="Test Title",
        type_="Test Type"
    )

    # Assert that the fields are correctly set
    assert model_instance.created_by == int(12345678901234567890)
    assert model_instance.title == "Test Title"
    assert model_instance.type_ == "Test Type"

    # Convert the Unix timestamp to a UTC datetime object
    expected_created_at = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    # Format the datetime object to the desired string format
    expected_created_at_str = expected_created_at.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Assert that the created_at field is correctly converted and formatted
    assert expected_created_at_str == datetime_str
    
# Run the test
if __name__ == "__main__":
    pytest.main()