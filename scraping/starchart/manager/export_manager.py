import os, json
from util.toDataName import toDataName


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

        ZARIMAN = "Zariman"

        planet_ = toDataName(planet)
        print(f"Planet name: {planet_}")

        file_name = f"{PATH}{fileName}.json"

        if ZARIMAN not in planet_:
            with open(file_name, 'r') as file:
                data = json.load(file)

            data[planet_] = _dict

            with open(file_name, 'w') as file:
                json.dump(data, file, indent=2)
        else:
            print("Zariman used!")
            with open(file_name, 'r') as file:
                data = json.load(file)

            data[ZARIMAN] = _dict

            with open(file_name, 'w') as file:
                json.dump(data, file, indent=2)