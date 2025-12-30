from manager.export_manager import ExportManager
from manager.planet_manager import PlanetManager


DATAFILE = 'exports/starchart.json'

class Controller:
    def __init__(self):
        print("Controller initialized!")
        em = ExportManager()
        data = em.get_data(DATAFILE)
        print(data)
