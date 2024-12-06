"""
This module contains tests for the file manager functionalities, specifically
for reading and writing JSON data. It ensures that the read_json and write_json
functions work correctly and handle exceptions as expected.
"""
import pytest  # type: ignore
from flex_json.jsonal import FileMode

        
class TestWriteJSON:        
    def test_write_mode(self, get_dict, object_JSON):
        for i in range(10):
            writen_scsfly: bool = object_JSON.write_json(
                data=get_dict,
                mode=FileMode.WRITE
                )
            assert writen_scsfly, f"Failed to write JSON data to test_file.json on: {i}"
            
    def test_append_mode(self, get_dict, object_JSON):
        for i in range(10):
            writen_scsfly: bool = object_JSON.write_json(
                data=get_dict,
                mode=FileMode.APPEND
                )
            assert writen_scsfly, f"Failed to append JSON data to test_file.json on: {i}"


def test_read_json(object_JSON):
    data: dict | None = object_JSON.read_json()
    assert data is not None, "Failed to read JSON data from file"
