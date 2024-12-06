import os
import sys

# Dynamically determine the project root and add it to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
import pytest  # type: ignore
from flex_json.jsonal import JSON


@pytest.fixture
def object_JSON():
    """Returns a JSON object with some sample data."""
    return JSON(file_path="test_file.json")

@pytest.fixture
def get_dict():
    return {
        'meta': {
            'latitude': '42.5',
            'longitude': '74.5',
            'magnitude': '4.5',
            'registration_date': '2024-01-22',
            'registration_time': '12:34:56.789',
            'status': 'processed',
            'time_in_source': '12:34:56.789'
        },
        'near_places': ['Bishkek', 'Osh'],
        'phases': ['P', 'S']
    }
    