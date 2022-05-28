
from search_res import SearchResult
from search_functions import make_search_result

words_to_find = input("Words you want to find...").split()

search_results = []

for j in range(len(words_to_find)):
    print(words_to_find[j])
    search_results.append(make_search_result(words_to_find[j], 5))

for j in range(len(words_to_find)):
    print('---------------------------')
    print(f'search word no {j+1} - {words_to_find[j]}')
    print(f'Total results: {len(search_results[j].search_list)}')
    #print(search_results[j].search_list)
    print(f'Minimal price: {search_results[j].min_price()}')
    print(f'Maximum price: {search_results[j].max_price()}')
    print(f'Average price: {search_results[j].average_price()}')












