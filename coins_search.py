
from search_res import SearchResult
from search_functions import *

words_to_find = input("Words you want to find...").split()

save_images = True

search_result = make_search_result(words_to_find[0], 5)

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













