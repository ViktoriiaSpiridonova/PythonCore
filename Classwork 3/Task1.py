# Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

list_of_numbers=[int(input("Enter a number:")) for i in range(int(input("Enter amount of numbers:")))]
print("Max number is {}".format(max(list_of_numbers)))

or

list = [1, 89, 80, 65, 17]
x=max(list)
y=min(list)
print("The maximum number from list is ", x)
print("The minimum number in list is ", y)
