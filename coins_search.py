import requests
import re
from bs4 import BeautifulSoup


import time

pr = []

for i in range(1,10):
    link = f"https://www.vcoins.com/en/coins/ancient-2.aspx?page={i}"
    page = requests.get(link)
    #print(f"page no {i}")
    soup = BeautifulSoup(page.text, "lxml")
    coins = soup.findAll("a", text=re.compile("DRACHM"))
    for item in coins:
        #print(item.text)
        prices = item.findParent("div", "item-detail").findAll("span", "newitemsprice")
        #print(prices[0]["content"], prices[1]["content"])
        pr.append(prices[1]["content"])

print(pr)
# print(f"total amount = {len(pr)}")
# print(f"average price = {sum(pr)/len(pr)}")
# print(f"max price = {max(pr)}")
# print(f"min price = {min(pr)}")






