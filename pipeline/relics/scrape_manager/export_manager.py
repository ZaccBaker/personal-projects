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


    def get_data():

        DIR = "exports/"
        PATH = "exports/relics.json"

        ExportManager.directory_check_content(DIR)
        try:
            with open(PATH, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"No relics.json: {e}")
            

    def directory_check_content(path : str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)


    def save_dict_content(_dict : dict) -> None:
        
        PATH = "exports/relics-content.json"

        with open(PATH, "w") as file:
            json.dump(_dict, file, indent=2)