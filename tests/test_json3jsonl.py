import pytest # type: ignore
from flex_json import Json2jsonl


def test_json2jsonl():
    json_path: str = "./tests/MOCK_DATA.json"
    j2jl = Json2jsonl(json_name=json_path)
        
    assert j2jl.start() == True