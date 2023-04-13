# _*_coding:cp1251_*_
class Animal():  # Родительский (Базовый) класс
    def __init__(self, breed,  name, sex):  # Ввод первичных данных
        # Динамические свойства
        self.breed = breed      # Порода
        self.name = name        # Имя
        self.sex = sex          # Пол
        # Статические свойства
        self.age = 3.5          # Возраст
        # Навыки
        self.skills = "Идти по следу, обнаружение взрывчатых и наркотических средств"
    def info_Animal(self):     # Метод 1 "Информация о животном" и вывод в консоль
        print("Порода животного:  ", self.breed, "\nИмя животного:     ", self.name, "\nПол животного:     ", self.sex)
    def age_Animal(self):   # Метод 2 "Возраст животного" и вывод в консоль
        print("Возраст животного: ", str(self.age), "лет/года")
    def skiils_Animal(self):   # Способности и навыки и вывод в консоль
        print("Способности и навыки:", "\n                     " + self.skills + ".")
    def locotion_Animal(self):
        print("Местонахождение:", "\n                " + self.name, "Находиться на службе.")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# Создаем объект № 1. Ввод первичной информации
Animal_1 = Animal("Овчарка", "Рекс", "мальчик")
# Создаем объект № 2. Ввод первичной информации
Animal_2 = Animal("Питбуль", "Ада", "девочка")
print("*******************************************************************")
# # Вызов метода класса
# Animal_1.info_Animal()
# Animal_1.age_Animal()
# Animal_1.skiils_Animal()
# Animal_1.locotion_Animal()
# # Вызов метода класса
# Animal_2.info_Animal()
# Animal_2.age_Animal()
# Animal_2.skiils_Animal()
# Animal_2.locotion_Animal()
class Dog(Animal):  # Наследование класса (Класс наследник)
    def __init__(self, breed, name, sex):   # Входные пораметры
        super().__init__(self, name, sex)   # Берем поля из родительского класса
        self.age = 1                        # Ввод первичных данных
        self.name = name                    # Ввод первичных данных
        self.breed = breed                  # Ввод первичных данных
    def location(self):
        print("Местонахождение:", "\n                " + self.name, "Находиться на дрессировке.")

# Создаем объект № 1. Ввод первичной информации
Dogs = Dog("Овчарка", "Алмаз", "мальчик")

# Создаем объект № 2. Ввод первичной информации Объекст № 1 из родительского класса
Dogs_2 = Animal("Чау-Чау", "Гризли", "мальчик")
# Вызов метода класса
# Dogs.info_Animal()
# Dogs.age_Animal()
# Dogs.location()
# Dogs_2.locotion_Animal()