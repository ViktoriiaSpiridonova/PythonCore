# Задано чотирицифрове натуральне число. 
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число

num = str(input("Enter 4 digit number:"))
multiplic = 1
for i in num:
  multiplic *= int(i)
print("Multiplication is " + str(multiplic))
c = str(num)
print("Number in reverse is ", c[::-1])
s = str(num)
print("Sorted number is ", sorted(s))
