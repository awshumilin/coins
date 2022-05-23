import requests
import re
from bs4 import BeautifulSoup
import locale
import time


def save_photo_to_file(url, filename):
    file = "coins_pics\\" + filename + ".jpg"
    with open(file, 'wb') as out:
        out.write(requests.get(url).content)



pr = []
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
counter = 1

word_to_find = "Ardashir"

for i in range(1,5):
    link = f"https://www.vcoins.com/en/coins/ancient-2.aspx?page={i}"
    page = requests.get(link)
    print(f"page no {i}")
    soup = BeautifulSoup(page.text, "lxml")
    coins = soup.findAll("a", text=re.compile(word_to_find))
    for item in coins:
        print(item.text)
        prices = item.findParent("div", "item-info").findAll("span", re.compile("price"))

        # Photo saving
        pic_link = "https://www.vcoins.com" + item.findParent("div", "item-info").find("a")["href"]
        print(pic_link)
        page_pic = requests.get(pic_link)
        soup_pic = BeautifulSoup(page_pic.text, "lxml")
        pic = soup_pic.find("img", title=re.compile(word_to_find))["src"]
        print(pic)
        save_photo_to_file(pic, f"coin{counter}")
        counter += 1

        print(prices[0]["content"], prices[1]["content"])
        pr.append(locale.atof(prices[1]["content"]))

print(pr)
try:
    print(f"total amount = {len(pr)}")
    print(f"average price = {sum(pr) / len(pr)}")
    print(f"max price = {max(pr)}")
    print(f"min price = {min(pr)}")
except(ZeroDivisionError):
    print("Nothing")










