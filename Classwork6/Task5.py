# Знайти найбільший елемент в списку  використовуючи функцію reduce

from functools import reduce
items = [1, 45, 67, 115, 30, 435]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)
