from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
class Scrape:
    def __init__(self,uid):
        self.uid = uid
        self.handle()
    def handle(self):
        html = urlopen('https://codeforces.com/profile/'+self.uid)
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        self.soup = soup