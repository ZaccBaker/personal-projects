import os, json

PATH = "exports/"

class ExportManager:
    def __init__(self) -> None:
        self.directory_check(PATH)


    def directory_check(self, path : str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)


    def get_data(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data