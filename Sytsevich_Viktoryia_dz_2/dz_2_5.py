def output(prices):
    for price in prices:
        ruble = int(price)
        cent = int(round(((price - int(price)) * 100), 2))
        if price != prices[-1]:
            print((f'{ruble} руб {cent:02} коп'), end=', ')
        else:
            print((f'{ruble} руб {cent:02} коп'))


import random
prices = []
for i in range(10):
    i = round((random.uniform(1,100)), 2)
    prices.append(i)
output(prices)
print(f'id(prices)={id(prices)}')
prices.sort()
output(prices)
print(f'id(prices_2)={id(prices)}')
prices.sort(reverse=True)
output(prices)
from heapq import nlargest
big_5 = nlargest(5, prices)
output(big_5)