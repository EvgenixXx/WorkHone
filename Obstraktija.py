# _*_coding:cp1251_*_
from abc import abstractmethod
class Transport:
    def __init__(self):
        pass
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass
# Класс самолет
class Plane(Transport):
    def __init__(self):
        pass
    def run(self):
        print("Самолет летит")
    def on(self):
        print("Самолет заведен")
    def off(self):
        print("Самолет заглушен")

    def vzlet(self):
        print("Самолет взлетает")
    def pos(self):
        print("Самолет садится")
# Класс Автомобиль
class Car(Transport):
    def __init__(self):
        pass
    def run(self):
        print("Автомобиль едет")
    def on(self):
        print("Автомобиль заведен")
    def off(self):
        print("Автомобиль заглушен")
    def vzlet(self):
        print("Автомобиль едет")
    def pos(self):
        print("Автомобиль остановился")
# Класс животные
class Animal():
    def __init__(self):
        pass
    def run(self):
        print("Животное бегает")
    def on(self):
        print("Животное бодрствует")
    def off(self):
        print("Животное спит")
    def pos(self):
        print("Животное сидит")
# Действия самолета
plane1 = Plane()
plane1.on()
plane1.vzlet()
plane1.run()
plane1.pos()
plane1.off()
print("****************************************************************************************************")
# Действия Автомобиля
car1 = Car()
car1.on()
car1.run()
car1.pos()
car1.off()
print("****************************************************************************************************")
# Действия животного
aanimal1 = Animal()
aanimal1.on()
aanimal1.run()
aanimal1.pos()
aanimal1.off()