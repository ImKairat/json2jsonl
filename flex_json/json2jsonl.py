import json
import jsonlines


class Json2jsonl:
    def __init__(self, json_name: str, jsonl_name: str = ""):
        self.jsonl_name = jsonl_name
        if jsonl_name == "":
            self.jsonl_name = json_name + "l"
        self.json_name = json_name
        
    def __read_json(self) -> dict | None:
        try:            
            # Load the JSON file
            with open(self.json_name, 'r') as json_file:
                data = json.load(json_file)
                return data
        except:
            return None
            
    def __write_jsonl(self, data: dict) -> bool:       
        try:
            # Open the JSONL file in write mode
            with jsonlines.open(self.jsonl_name, mode='w') as jsonl_file:
                for item in data:
                    jsonl_file.write(item)
                return True
        except:
            return False
            
    def start(self):
        try:
            data: dict | None = self.__read_json()
            if data is not None:
                self.__write_jsonl(data=data) 
                return True
            return False
        except:
            return False
        