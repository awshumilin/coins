import requests
import re
from bs4 import BeautifulSoup
import locale
import os
from search_res import SearchResult

def save_photo_to_file(url, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file = folder + "\\" + filename + ".jpg"
    with open(file, 'wb') as out:
        out.write(requests.get(url).content)

def save_result_to_file(result, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file = folder + "\\" + filename + ".txt"
    with open(file, 'w') as out:
        for item in result.search_list:
            out.write(str(item))
            out.write('\n')

def vcoins_search(word_to_find, pages, search_result, counter):
    for i in range(1, pages + 1):
        link = f"https://www.vcoins.com/en/coins/ancient-2.aspx?page={i}"
        page = requests.get(link)
        print(f"page no {i}, found {counter-1}")
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
            counter += 1

            # saving results
            search_result.search_list.append(
                {'legend': item.text, 'price': locale.atof(prices[1]["content"]), 'currency': prices[0]["content"], 'coin_page': pic_link, 'pic_link': pic})

    return search_result, counter

def make_search_result(word_to_find, pages, uppercase = True):
    search_result = SearchResult()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    counter = 1

    search_result, counter = vcoins_search(word_to_find, pages, search_result, counter)

    if uppercase:
        search_result, counter = vcoins_search(word_to_find.upper(), pages, search_result, counter)

    search_result = add_coin_info(search_result)

    return search_result

def add_coin_info(search_result):

    for item in search_result.search_list:
        item['century'] = None
        item['material'] = None
        if re.search('[Gg]old', item['legend']) != None:
            item['material'] = 'Gold'
        if re.search('A[Uu]', item['legend']) != None:
            item['material'] = 'Gold'
        if re.search('[Ss]ilver', item['legend']) != None:
            item['material'] = 'Silver'
        if re.search('A[Rr]', item['legend']) != None:
            item['material'] = 'Silver'
        if re.search('[Bb]ronze]', item['legend']) != None:
            item['material'] = 'Bronze'
        if re.search('A[Ee]', item['legend']) != None:
            item['material'] = 'Bronze'

        if re.search('6\d\d BC', item['legend']) != None:
            item['century'] = '7 BC'
        if re.search('5\d\d BC', item['legend']) != None:
            item['century'] = '6 BC'
        if re.search('4\d\d BC', item['legend']) != None:
            item['century'] = '5 BC'
        if re.search('3\d\d BC', item['legend']) != None:
            item['century'] = '4 BC'
        if re.search('2\d\d BC', item['legend']) != None:
            item['century'] = '3 BC'
        if re.search('1\d\d BC', item['legend']) != None:
            item['century'] = '2 BC'
        if re.search('[- ]\d\d BC', item['legend']) != None:
            item['century'] = '1 BC'
        if re.search('BC 6\d\d', item['legend']) != None:
            item['century'] = '7 BC'
        if re.search('BC 5\d\d', item['legend']) != None:
            item['century'] = '6 BC'
        if re.search('BC 4\d\d', item['legend']) != None:
            item['century'] = '5 BC'
        if re.search('BC 3\d\d', item['legend']) != None:
            item['century'] = '4 BC'
        if re.search('BC 2\d\d', item['legend']) != None:
            item['century'] = '3 BC'
        if re.search('BC 1\d\d', item['legend']) != None:
            item['century'] = '2 BC'
        if re.search('BC[- ]\d\d[- \.]', item['legend']) != None:
            item['century'] = '1 BC'
        if re.search('6\d\d AD', item['legend']) != None:
            item['century'] = '7 AD'
        if re.search('5\d\d AD', item['legend']) != None:
            item['century'] = '6 AD'
        if re.search('4\d\d AD', item['legend']) != None:
            item['century'] = '5 AD'
        if re.search('3\d\d AD', item['legend']) != None:
            item['century'] = '4 AD'
        if re.search('2\d\d AD', item['legend']) != None:
            item['century'] = '3 AD'
        if re.search('1\d\d AD', item['legend']) != None:
            item['century'] = '2 AD'
        if re.search('[- ]\d\d AD', item['legend']) != None:
            item['century'] = '1 AD'
        if re.search('AD 6\d\d', item['legend']) != None:
            item['century'] = '7 AD'
        if re.search('AD 5\d\d', item['legend']) != None:
            item['century'] = '6 AD'
        if re.search('AD 4\d\d', item['legend']) != None:
            item['century'] = '5 AD'
        if re.search('AD 3\d\d', item['legend']) != None:
            item['century'] = '4 AD'
        if re.search('AD 2\d\d', item['legend']) != None:
            item['century'] = '3 AD'
        if re.search('AD 1\d\d', item['legend']) != None:
            item['century'] = '2 AD'
        if re.search('AD[- ]\d\d[- \.]', item['legend']) != None:
            item['century'] = '1 AD'

    return search_result

def filter_search_result(search_result, word_to_find):
    temp_list = []
    for item in search_result.search_list:
        if re.search(word_to_find, item['legend']) != None:
            temp_list.append(item)

    search_result.search_list = temp_list

    return search_result