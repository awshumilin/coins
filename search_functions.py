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

def vcoins_search(word_to_find, pages, search_result, counter):
    for i in range(1, pages + 1):
        link = f"https://www.vcoins.com/en/coins/ancient-2.aspx?page={i}"
        page = requests.get(link)
        print(f"page no {i}")
        soup = BeautifulSoup(page.text, "lxml")
        # find coins
        coins = soup.findAll("a", text=re.compile(word_to_find))
        for item in coins:
            # find prices
            prices = item.findParent("div", "item-info").findAll("span", re.compile("price"))

            # Photo saving
            pic_link = "https://www.vcoins.com" + item.findParent("div", "item-info").find("a")["href"]
            page_pic = requests.get(pic_link)
            soup_pic = BeautifulSoup(page_pic.text, "lxml")
            pic = soup_pic.find("img", title=re.compile(word_to_find))["src"]
            save_photo_to_file(pic, word_to_find, f"coin{counter}")
            counter += 1

            # saving results
            search_result.search_list.append(
                {'legend': item.text, 'price': locale.atof(prices[1]["content"]), 'currency': prices[0]["content"]})

    return search_result, counter

def make_search_result(word_to_find, pages, uppercase = True):
    search_result = SearchResult()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    counter = 1

    search_result, counter = vcoins_search(word_to_find, pages, search_result, counter)

    if uppercase == True:
        search_result, counter = vcoins_search(word_to_find.upper(), pages, search_result, counter)

    return search_result