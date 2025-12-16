
from web.relic_scraper import RelicScraper
from web.content_scraper import RelicsContentScraper
from manager.data_manager import DataManager
from manager.export_manager import ExportManager

class Control:
    def __init__(self):
        try:
            print("\n\nScrape in progress. Do not exit application.")
            print("This may take several minutes depending on connection speed.\n")

            ### Relics ###
            rs = RelicScraper()
            relics_array = rs.scrape()

            #Uncomment for connection status
            # rs.connection_status()

            dm = DataManager()
            relics_dict = dm.organize_data(relics_array)

            # Uncomment for total relic count
            dm.relic_count(relics_dict)

            ExportManager(relics_dict)


            ### Relic Contents ###
            sc = RelicsContentScraper()
            data = ExportManager.get_data()

            final_dict = {}

            for key in data:
                for relic in data[key]:
                    relic_path = relic.replace(" ","_")
                    address = f"https://wiki.warframe.com/w/{relic_path}"
                    contents_dict = sc.scrape(address)
                    final_dict.update({relic : contents_dict})

            ExportManager.save_dict_content(final_dict)
            
            print("\n\nScrape complete.")

        except Exception as e:
            print(f"Exception thrown: {e}")