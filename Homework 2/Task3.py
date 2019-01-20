# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = int(input('Insert value a: '))
b = int(input('Insert value b: '))
a, b = b, a
print('Value a = ', a)
print('Value b = ', b)
