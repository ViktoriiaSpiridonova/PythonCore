# 4.  Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа 
# з плаваючою крапкою. (Підказка: використати вбудовану функцію float ()).

list_number = [56,78,45,23]
print(list_number)
i = 0
for a in list_number:
    list_number[i] = float(a)
    i = i + 1
print(list_number)

list = [5, 6, 72, 48, 230]
for i in range(len(list)):
    list[i] = float(list[i])
print(list)
