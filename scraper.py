import html5lib
from bs4 import BeautifulSoup
import requests

class scraper:
    def __init__(self, startPage, endPage):
        self.startPage = startPage
        self.endPage = endPage
    
    def scrapeArticle(self, link):
        # response = requests.get(self.startPage)
        # soup = BeautifulSoup(response.content, 'html5lib')
        with open(link) as fp:
            soup = BeautifulSoup(fp, 'html5lib')
        title = soup.find("h1")
        allLinks = soup.find(id = "bodyContent").find_all("a")
        return allLinks