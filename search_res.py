class SearchResult:
    search_list = []

    def min_price(self):
        min = 100000000
        for item in self.search_list:
            if item['price']<min:
                min = item['price']
        return min

    def max_price(self):
        max = 0
        for item in self.search_list:
            if item['price'] > max:
                max = item['price']
        return max

    def average_price(self):
        sum = 0
        for item in self.search_list:
            sum += item['price']
        return sum/len(self.search_list)




