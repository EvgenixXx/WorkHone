# _*_coding:cp1251_*_

class Person():
    '''Данные объекта'''
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car
    def hello(self):
        print("Имя:       ", self.name, "\nВозраст:   ", str(self.age), "лет.", "\nСлужебный\nавтомобиль:",  self.car)

info = Person("Евгений", 38, "Lada")
info.hello()

print(info.car)
print(info.name)
print(info.age)