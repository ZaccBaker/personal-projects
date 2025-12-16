import requests # Send HTTP requests to get web content
from bs4 import BeautifulSoup # Parse request

class RelicsContentScraper:
    def __init__(self):
        self._rcontents = []

    
    def scrape(self, address : str):
        web_response = requests.get(address)

        soup = self.parse(web_response)
        content_div = self.find_content(soup)
        table = self.find_table(content_div)

        contents = self.find_contents(table)
        # print(f"Contents : {self._rcontents}")
        self._rcontents = self.organize_contents(contents)
        # print(f"\n\nContents dict: {self._rcontents}")

        return self._rcontents

    
    def parse(self, response):
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup


    def find_content(self, soup_content : BeautifulSoup) -> BeautifulSoup:
        content = soup_content.find("div", class_="mw-body-content")
        return content
    

    def find_table(self, content_div : BeautifulSoup) -> BeautifulSoup:
        table = content_div.find_all('table', class_="wikitable")
        return table
    

    def find_contents(self, table) -> list:
        
        content_array = []

        for index, row in enumerate(table[:1], start=1):

            content_items = row.find_all("a")

            for a in content_items:
                content_name = a.get_text(strip=True)
                content_array.append(content_name)
        return content_array
    

    def organize_contents(self, contents) -> dict:

        content_dict = {
            "Common" : [],
            "Uncommon": [],
            "Rare" : []
        }

        organized_contents = list(filter(None, contents))
        # print(f"Organized contents: {organized_contents}")
        for index, item in enumerate(organized_contents):
            if index <= 2:
                content_dict["Common"].append(item)
            elif index <= 4:
                content_dict["Uncommon"].append(item)
            elif index == 5:
                content_dict["Rare"].append(item)
        return content_dict
        
