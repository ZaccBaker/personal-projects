
from web.scrapper import RelicScrapper
from manager.data_manager import DataManager
from manager.export_manager import ExportManager

class Control:
    def __init__(self):
        try:

            rs = RelicScrapper()
            relics_array = rs.scrape()

            #Uncomment for connection status
            # rs.connection_status()

            dm = DataManager()
            relics_dict = dm.organize_data(relics_array)

            # Uncomment for total relic count
            dm.relic_count(relics_dict)

            ExportManager(relics_dict)
            

        except Exception as e:
            print(f"Exception thrown: {e}")