import requests # Send HTTP requests to get web content
from bs4 import BeautifulSoup # Parse request
import itertools


class PlanetScrapper:
    def __init__(self):
        self._planets = []
    

    def scrape(self):
        ADDRESS = "https://wiki.warframe.com/w/Star_Chart"
        WEB_RESPONSE = requests.get(ADDRESS)

        soup = self.parse(WEB_RESPONSE)
        content_div = self.find_content(soup)
        tables = self.find_tables(content_div)

        self._planets = self.find_planets(tables)        
        # self.planet_count(self._planets)

        return self._planets

        
    def connection_status(self):
        print(f"\nStatus code : {requests.get("https://wiki.warframe.com/w/Void_Relic")}\n")


    def parse(self, response): # If you want to parse content
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup


    def organize(self, response): # If you want pretty output
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.prettify()


    def find_content(self, soup_content : BeautifulSoup): # Find main content div
        # Website content div <class="mw-body-content">
        content = soup_content.find("div", class_="mw-body-content")
        return content
    

    def find_tables(self, content_div : BeautifulSoup) -> BeautifulSoup:  # Find tables with relics
        # Website relics are in <table>
        tables = content_div.find_all('table', class_="wikitable")
        return tables
    
    
    def find_planets(self, tables) -> list: # Find relics, create masterlist
        
        planets_array = []

        for index, table in enumerate(tables, start=1):

            planet_items = table.find_all("figure", class_="mw-default-size mw-halign-left")
            planet_items_additional = table.find_all("figure", class_="mw-default-size mw-halign-center")

            for planet in itertools.chain(planet_items,planet_items_additional):
                planet_ = planet.find("a")
                planet_name = planet_.get("title")
                planets_array.append(planet_name.replace('\u00A0', ' ').strip())
        return planets_array
    

    def planet_count(self, planets : list) -> None:
        print(f"Planet Count: {len(planets)}\n{planets}")
        