## <Scraping> Relics-Content
### Contributors
Zac Baker

### About
A web scrapping program that gets the entire list of the contents in each relic from Warframe's wiki. Fast and reliable way to get and format to a json file.

*Disclaimer: This program requires the relics.json file that is produced from the "relics" scraper. It will not run properly without it.*

### Lessons learned
Getting more hands on with scraping data from a website is an interesting experience. This time around was more smooth as I was able to understand the process better and use blocks of code from the previous one. Being able to dynamically change the address for the HTML request was not necessarily hard but I was surprised I got it down fairly easily. Hardest part was figuring out how to organize the data from the tables better. Since the initial way it was done resulted in a lot of empty strings in the list, I settled on removing None types from it an manually sorting it. This is possible due to the structure of the data I was looking for, thankfully.

### Languages
Python