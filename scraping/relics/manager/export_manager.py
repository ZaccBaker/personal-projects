import os, json

class ExportManager:
    def __init__(self, _dict : dict) -> None:
        PATH = "exports/"

        self.directory_check(PATH)
        self.save_dict(PATH,_dict)


    def directory_check(self, path : str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)


    def save_dict(self, path : str, _dict : dict) -> None:
        
        file_name = f"{path}relics.json"

        with open(file_name, "w") as file:
            json.dump(_dict, file, indent=2)