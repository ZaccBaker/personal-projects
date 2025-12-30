import requests # Send HTTP requests to get web content
from bs4 import BeautifulSoup # Parse request
import itertools


class MissionScrapper:
    def __init__(self):
        self._missions = []
    

    def scrape(self, planet : str):
        address = f"https://wiki.warframe.com/w/{planet}"
        # print(planet)
        WEB_RESPONSE = requests.get(address)

        soup = self.parse(WEB_RESPONSE)
        content_div = self.find_content(soup)
        tables = self.find_tables(content_div)
        
        self._missions = self.find_missions(tables)        

        return self._missions

        
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
        tables = content_div.find_all('table', class_="wikitable sortable")[:1]
        return tables
    
    
    def find_missions(self, tables) -> list: # Find relics, create masterlist
        missions_array = []

        for index, table in enumerate(tables, start=1):
            table_body = table.find("tbody")

            for data in table_body.find_all("tr"):
                tds = data.find_all("td")[:3]
                if len(tds) < 3:
                    continue

                vals = [td.get_text(" ", strip=True) for td in tds]
                # print("\tTDS - ", vals)
                missions_array.append([vals[1],vals[2]])
        return missions_array
    
        