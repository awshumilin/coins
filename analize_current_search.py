
words_to_find = input("Words you want to find...").split()

import pandas as pd
import pandas_profiling

data = pd.read_csv(f'{words_to_find[0]}\{words_to_find[0]}.csv')
print(data[['legend', 'price', 'currency', 'century', 'material']])
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data['century'] = pd.to_numeric(data['century'], errors='coerce')

data1 = data.groupby('century')['legend'].count()
print(data1)
