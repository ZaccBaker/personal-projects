from web.planet_scraper import PlanetScrapper
from web.mission_scraper import MissionScrapper
from manager.data_manager import DataManager
from manager.export_manager import ExportManager


class Controller:
    def __init__(self):
        FILENAME = "starchart"

        print("Scraping in progress...")
        em = ExportManager()

        ps = PlanetScrapper()
        planet_data = ps.scrape()

        planet_dict = DataManager.planet_dictonary(planet_data)
        em.save_dict(FILENAME,planet_dict)

        new_array = DataManager.planet_address(planet_data)

        ms = MissionScrapper()

        for planet in new_array:
            mission_data = ms.scrape(planet)
            new_dict = DataManager.starchart_dictonary(planet, mission_data)
            # print(new_dict)
            em.update(FILENAME,planet,new_dict)

        print("Scrape complete.")