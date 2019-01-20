# 3.  Перевірити чи список містить непарні числа. (Підказка: використати оператор break)
          
list_number = [2,4,6,8,10]
contain_odd = False
for item in list_number:
    if not item % 2 == 0:
        contain_odd = True
        break
if contain_odd:
    print('There are odd numbers in list')
else:
    print('There are only even numbers in list')
