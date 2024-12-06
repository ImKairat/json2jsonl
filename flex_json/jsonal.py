"""
This method appends new data to the existing JSON data in the file.
It reads the current data, adds the new data, and writes it back to the file.
"""
import json
from enum import Enum


class FileMode(Enum):
    """
    File_mode Enum: Defines the modes for file operations, including READ, WRITE and APPEND.
    """
    READ: str = "r"
    WRITE: str = "w"
    APPEND: str = "a"


class JSON:
    """
    This class provides methods for reading and writing JSON files.
    It supports different file modes such as WRITE and APPEND.
    """
    def __init__(self, file_path: str):
        """
        Initializes the JSON class with the specified file path.
        """
        self.file_path: str = file_path       
    
    def read_json(self) -> dict | None:
        """
        Reads a JSON file and returns its contents as a dictionary or None if an error occurs.

        Returns:
            dict | None: Returns the contents of the JSON file as a dictionary, or None if an error occurs.
        """
        try:
            with open(file=self.file_path, mode=self.mode) as file:
                data: dict = json.load(file)
                return data
        except:
            raise
    
    def __append_json(self, data: dict) -> bool:
        """
        This private method appends new data to the existing JSON data in the file.
        It first attempts to read the current data from the file. If the file does not exist
        or contains invalid JSON, it initializes an empty list. The new data is then added
        to the existing data, and the combined data is written back to the file in JSON format.
        
        Args:
            data (dict): The new data to be appended to the existing JSON data.
        
        Returns:
            bool: Returns True if the data was appended successfully, False otherwise.
        """
        try: 
            old_data = self.read_json()
        except (FileNotFoundError, json.JSONDecodeError):
            old_data = []
        finally:
            old_data.append(data)
            self.write_json(data=old_data, mode=FileMode.WRITE)
        
    def write_json(self, data: dict, mode: FileMode = FileMode.WRITE) -> bool:
        """
        Writes JSON data to a file.

        Args:
            file_path (str): _description_
            data (dict): _description_
            mode (FileMode): _description_

        Returns:
            bool: Returns True if the data was written successfully, False otherwise.
        """
        try:
            match mode:
                case FileMode.WRITE:                    
                    with open(file=self.file_path, mode=mode.value) as file:
                        json.dump(data, file, indent=4)
                        return True
                case FileMode.APPEND:
                    return self.__append_json(data=data)
        except:
            raise
