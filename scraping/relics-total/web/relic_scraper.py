import requests # Send HTTP requests to get web content
from bs4 import BeautifulSoup # Parse request



class RelicScraper:
    def __init__(self):
        self._relics = []
    

    def scrape(self):
        ADDRESS = "https://wiki.warframe.com/w/Void_Relic"
        WEB_RESPONSE = requests.get(ADDRESS)

        soup = self.parse(WEB_RESPONSE)
        content_div = self.find_content(soup)
        tables = self.find_tables(content_div)

        self._relics = self.find_relics(tables)
        return self._relics

        
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
        tables = content_div.find_all('table', class_="wikitable mw-collapsible")
        return tables
    
    
    def find_relics(self, tables) -> list: # Find relics, create masterlist
        
        relics_array = []

        for index, table in enumerate(tables, start=1):
    
            relic_items = table.find_all("a")

            for li in relic_items:
                relic_name = li.get_text(strip=True)
                relics_array.append(relic_name.replace('\u00A0', ' ').strip())
        return relics_array
        