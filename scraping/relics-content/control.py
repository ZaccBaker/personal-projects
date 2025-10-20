
from web.scraper import RelicsContentScraper
from manager.export_manager import Exportmanager

class Control:
    def __init__(self):
        try:
            sc = RelicsContentScraper()
            data = Exportmanager.get_data()

            print("\n\nScrape in progress. Do not exit application.")

            final_dict = {}

            for key in data:
                for relic in data[key]:
                    relic_path = relic.replace(" ","_")
                    address = f"https://wiki.warframe.com/w/{relic_path}"
                    contents_dict = sc.scrape(address)
                    final_dict.update({relic : contents_dict})

            Exportmanager.save_dict(final_dict)
            
            print("\n\nScrape complete.")
            
        except Exception as e:
            print(f"Exception thrown: {e}")