
from search_res import SearchResult
from search_functions import *
import pandas as pd
import pandas_profiling

words_to_find = input("Words you want to find...").split()

save_images = False

search_result = make_search_result(words_to_find[0], 50)

if len(words_to_find) > 1:
    for i in range(1, len(words_to_find)):
        search_result = filter_search_result(search_result, words_to_find[i])

if save_images:
    counter = 0
    for item in search_result.search_list:
        counter += 1
        save_photo_to_file(item['pic_link'], words_to_find[0], f"coin{counter}")

save_result_to_file(search_result, words_to_find[0], words_to_find[0])
save_result_to_csv_file(search_result, words_to_find[0], words_to_find[0])

print(f'Total results after filter {len(search_result.search_list)}')

print('---------------------------')
print(f'Total results: {len(search_result.search_list)}')
#print(search_result.search_list)
print(f'Minimal price: {search_result.min_price()}')
print(f'Maximum price: {search_result.max_price()}')
print(f'Average price: {search_result.average_price()}')

data = pd.read_csv(f'{words_to_find[0]}\{words_to_find[0]}.csv')
print(data[['legend', 'price', 'currency', 'century', 'material']])
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data['century'] = pd.to_numeric(data['century'], errors='coerce')

profile = data.profile_report(title='Pandas Profiling Report', progress_bar=False)
profile.to_file(f"{words_to_find[0]}\{words_to_find[0]}.html")















