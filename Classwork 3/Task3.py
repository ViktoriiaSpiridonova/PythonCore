# 3.Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

number=int(input("Enter a digit number: "))
fact=1
for i in range(1, number+1):
    fact *= i
print("Factorial of",number,"is",fact)
