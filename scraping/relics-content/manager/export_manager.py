
import os, json

class Exportmanager:

    def get_data():

        DIR = "exports/"
        PATH = "exports/relics.json"

        Exportmanager.directory_check(DIR)
        try:
            with open(PATH, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"No relics.json: {e}")
            

    def directory_check(path : str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)


    def save_dict(_dict : dict) -> None:
        
        PATH = "exports/relics-content.json"

        with open(PATH, "w") as file:
            json.dump(_dict, file, indent=2)
    