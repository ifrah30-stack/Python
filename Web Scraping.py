import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

for quote in soup.select(".quote"):
    print(quote.find("span").text)
