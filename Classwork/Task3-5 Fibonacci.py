Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

number=int(input("Enter the number: "))
a, b = 0,1
print(a)
while b < number:
    print(b)
    a, b=b, a+b
print(number)
