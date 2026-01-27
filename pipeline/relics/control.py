
from controllers.scrape_controller import ScrapeControl
from controllers.query_controller import QueryControl


class Control:
    def __init__(self):
        try:
            print("\n\nScrape in progress. Do not exit application.")
            print("This may take several minutes depending on connection speed.\n")

            # ScrapeControl()
            QueryControl()
            
            print("\n\nScrape complete.")

        except Exception as e:
            print(f"Exception thrown: {e}")