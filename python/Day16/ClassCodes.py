import requests
import bs4 as bs
from bs4 import BeautifulSoup
r=requests.get("https://webscraper.io/test-sites/e-commerce/more/computers")
print(r.status_code)
#print(r.text)
b=BeautifulSoup(r.text,"html.parser")
#print(b.prettify())
print(b.find_all('button'))