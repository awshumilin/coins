class SearchResult:

    def __init__(self):
        self.search_list = []

    def min_price(self):
        min = 10000000000
        for item in self.search_list:
            if item['price']<min:
                min = item['price']

        if min == 10000000000:
            return "Nothing found!"
        else:
            return min

    def max_price(self):
        max = 0
        for item in self.search_list:
            if item['price'] > max:
                max = item['price']

        if max == 0:
            return "Nothing found!"
        else:
            return max

    def average_price(self):
        sum = 0
        for item in self.search_list:
            sum += item['price']
        if len(self.search_list) != 0:
            return sum/len(self.search_list)
        else:
            return "Nothing found!"




