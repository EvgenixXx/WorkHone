# _*_coding:cp1251_*_
x = input("Введите имя: ")
def upperfunc(func):
    def wrapper():
        print("Привет", x.upper()+"!")
    return wrapper
@upperfunc
def hello():
    print("Привет!",x)
hello()
