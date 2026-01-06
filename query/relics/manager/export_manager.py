import os, json


PATH = "exports/"
ASSETS = "assets/"

class ExportManager:
    def __init__(self) -> None:        
        self.directoryCheck(PATH)


    def directoryCheck(self, path : str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)


    def getAssetData(self, fileName : str) -> dict:
        try:
            with open(f"{ASSETS}{fileName}.json", "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Exception (getAssetData): {e}")

    
    def saveExportData(self, fileName : str, data : str) -> None:
        try:
            with open(f"{PATH}{fileName}.txt", "w") as file:
                file.write(data)
            print(f"Successfully saved to {fileName}.txt")
        except Exception as e:
            print(f"Exception (saveExportData): {e}")
