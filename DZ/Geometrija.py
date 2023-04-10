# _*_coding:cp1251_*_
from math import sqrt, pi
def geometrija():
    def plosh_kruga(r):
        return pi * r ** 2
    def plosh_prjamoug(S):
        return j * i
    def treugolnik(T):
        return sqrt(p * (p - a) * (p - b) * (p - c))
    print("**********************************************************************************************************")
    print("     Геометрия     " * 5)
    print("**********************************************************************************************************")
    print('Выберите действие\nиз комбинации клавишь:''\n                      Площадь круга - "R"''\n                      Площадь прямоугольника - "P"'
        '\n                      Площадь треугольника - "T"')
    comanda2 = input("Введите команду: ")

    if comanda2 == "R":
        r = float(input("Введите радиус круга R= "))
        print("Радиус круга:")
        print("             R = ", plosh_kruga(r))
    elif comanda2 == "P":
        print("Стороны прямоугольника:")
        j = float(input("Введите сторону a: "))
        i = float(input("Введите сторону b: "))
        print("Площадь прямоугольника:")
        print("                       S =", plosh_prjamoug(j * i))
    elif comanda2 == "T":
        print("Введите стороны треугольника:")
        a = float(input('Введите сторону a: '))
        b = float(input('Введите сторону b: '))
        c = float(input('Введите сторону c: '))
        p = (a + b + c) / 2
        print("Площадь треугольника:")
        print("                     S =", treugolnik(sqrt(p * (p - a) * (p - b) * (p - c))))