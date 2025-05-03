import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

for i in soup.find_all("a"):
    # print(i.get("href"))
    print(i.text)
    print("********************************")

print(soup.find_all("div", {"class": "yp-poi-box-2"}))