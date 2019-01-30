#Написати функцію, яка обчислює суму цифр введеного числа.

def sum_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum
    
number = int(input("Enter a number to calulate sum of its digits: "))
g = sum_digits(number)
print(sum_digits(number))

OR

number = int(input("Enter a number to calulate sum of its digits: "))
print(sum(map(int,str(number))))
