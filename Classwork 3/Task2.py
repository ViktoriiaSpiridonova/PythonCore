# В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

even = [x for x in range(1,11) if x % 2 == 0]
print(even)
odd = [x for x in range(1,11) if x % 2 == 1 and x % 3 == 0]
print(odd)
number = [x for x in range(1,11) if x % 2 == 1 and x % 3 == 1]
print(number)
