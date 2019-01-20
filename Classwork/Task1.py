# 1.  Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.


a = int(input("Input number a ="))
b = int(input("Input number b ="))
if a >= b:
    print("{} is bigger".format(a))
else:
    print("{} is bigger".format(b))
 

# 2.  Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.

a = float(input("Input number a ="))
if a%2 == 0:
    print("{} is even".format(a))
else:
    print("{} is odd".format(a))
