# _*_coding:cp1251_*_
from math import sqrt, pi
print('Выбирите действие\nиз комбинации клавишь:''\n                      Калькулятор - "K"'
      '\n                      Площадь круга - "R"''\n                      Площадь прчмоугольника - "P"'
      '\n                      Площадь треугольника - "T"')
comanda = input("Введите команду: ")
def summ(a, b):  # Функция сложения
    return a + b  # Вывод результата
def vysh(a, b):  # Функция вычитания
    return a - b  # Вывод результата
def pro(a, b):  # Функция сложения
    return a * b  # Вывод результата
def raz(a, b):  # Функция сложения
    return a / b  # Вывод результата
def plosh_kruga(r):
    return pi * r ** 2
def plosh_prjamoug(S):
    return j * i
def treugolnik(T):
    return sqrt(p * (p - a) * (p - b) * (p - c))
if comanda == "K":
    print("**********************************************************************************************************")
    print("     Калькулятор     "*5)
    print("**********************************************************************************************************")
    while True:  # Бесконечный цикл пользования
        a = float(input("Введите число 1: "))  # пользователь вводит число 1
        b = float(input("Введите число 2: "))  # пользователь вводит число 2
        c = input("Введите действие: ")  # пользователь вводит операцию ( +, -, *, / )
        # для выхода из калькулятора нажмите "s"
        if c == "+":
            print("Результат: ", summ(a, b))
        elif c == "-":
            print("Результат: ", vysh(a, b))
        elif c == "*":
            print("Результат: ", pro(a, b))
        elif c == "/":
            print("Результат: ", raz(a, b))
        elif c == "s":
            break
elif comanda == "R":
    r = float(input("Введите радиус круга R= "))
    print("Радиус круга:")
    print("             R = ", plosh_kruga(r))
elif comanda == "P":
    print("Стороны прямоугольника:")
    j = float(input("Введите сторону a: "))
    i = float(input("Введите сторону b: "))
    print("Площадь прямоугольника:")
    print("                       S =", plosh_prjamoug(j * i))
elif comanda == "T":
    print("Введите стороны треугольника:")
    a = float(input('Введите сторону a: '))
    b = float(input('Введите сторону b: '))
    c = float(input('Введите сторону c: '))
    p = (a + b + c) / 2
    print("Площадь треугольника:")
    print("                     S =", treugolnik(sqrt(p * (p - a) * (p - b) * (p - c))))