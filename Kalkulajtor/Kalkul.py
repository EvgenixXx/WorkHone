# _*_coding:cp1251_*_
from DZ.Raschet import kalkulajtor
from DZ.Geometrija import geometrija
print('Выберите действие\nиз комбинации клавишь:''\n                      Калькулятор - "K"'
      '\n                      Геометрия - "G"')
comanda = input("Введите команду: ")
if comanda == "K":
      kalkulajtor()
elif comanda == "G":
      geometrija()