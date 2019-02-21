# Напишіть скрипт, який обчислює площу прямокутника a*b, 
# площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, 
# а з нього функцію pow() та значення змінної пі).

from math import pow, pi

def rectangle():
    a = float(input("Enter width: "))
    b = float(input("Enter length: "))
    print("Square = {}".format(a*b))
def triangle():
    c = float(input("Enter basis: "))
    h = float(input("Enter height: "))
    print("Square = {}".format(0.5 * (c * h)))
def circle():
    r = float(input("Enter radius: "))
    print("Square = {}".format(round(pi * pow(r, 2),3)))

figure = input("1 - rectangle,\n2 - triangle,\n3 - circle : ")
if figure == "1":
    rectangle()
elif figure == "2":
    triangle()
elif figure == "3":
    circle()
else:
    print("Error input number")
