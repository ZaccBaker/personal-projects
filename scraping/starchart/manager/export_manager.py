import os, json


PATH = "exports/"

class ExportManager:
    def __init__(self) -> None:
        self.directory_check(PATH)


    def directory_check(self, path : str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)


    def save_dict(self, fileName : str, _dict : dict) -> None:
        
        file_name = f"{PATH}{fileName}.json"

        with open(file_name, "w") as file:
            json.dump(_dict, file, indent=2)

    
    def update(self, fileName : str, planet : str, _dict : dict) -> None:

        file_name = f"{PATH}{fileName}.json"

        with open(file_name, 'r') as file:
            data = json.load(file) # Deserialize JSON to a Python dictionary

        # 2. Modify the Python object
        data[planet] = _dict

        # 3. Write the updated data back to the file
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=2) # Serialize and write to file