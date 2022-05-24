import requests
import re
from bs4 import BeautifulSoup
import locale
import time
import os
from search_res import SearchResult


def save_photo_to_file(url, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file = folder + "\\" + filename + ".jpg"
    with open(file, 'wb') as out:
        out.write(requests.get(url).content)



pr = []
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
counter = 1

word_to_find = input("Word you want to find...")

search_result = SearchResult()

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
        # print(pic_link)
        page_pic = requests.get(pic_link)
        soup_pic = BeautifulSoup(page_pic.text, "lxml")
        pic = soup_pic.find("img", title=re.compile(word_to_find))["src"]
        # print(pic)
        save_photo_to_file(pic, word_to_find, f"coin{counter}")
        counter += 1

        print(prices[0]["content"], prices[1]["content"])
        pr.append(locale.atof(prices[1]["content"]))

        search_result.search_list.append({'legend':item.text, 'price':locale.atof(prices[1]["content"]), 'currency':prices[0]["content"]})

# print(pr)
print(search_result.search_list)
print(search_result.min_price())
print(search_result.max_price())
print(search_result.average_price())
# try:
#     print(f"total amount = {len(pr)}")
#     print(f"average price = {sum(pr) / len(pr)}")
#     print(f"max price = {max(pr)}")
#     print(f"min price = {min(pr)}")
# except(ZeroDivisionError):
#     print("Nothing")










