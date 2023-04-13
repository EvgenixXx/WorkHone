# _*_coding:cp1251_*_
from CassProg import Animal, Dogs, Dogs_2, Animal_1, Animal_2
print("     Базовый/Родительский класс.         " * 4)
print()
print("     Объект № 1")
# Вызов метода класса
Animal_1.info_Animal()
Animal_1.age_Animal()
Animal_1.skiils_Animal()
Animal_1.locotion_Animal()
print()
print("     Объект № 2")
# Вызов метода класса
Animal_2.info_Animal()
Animal_2.age_Animal()
Animal_2.skiils_Animal()
Animal_2.locotion_Animal()
print()
print("     Класс наследник.         " * 4)
print()
print("     Объект № 1")
# Вызов метода класса
Dogs.info_Animal()
Dogs.age_Animal()
Dogs.location()
print()
print("     Объект № 2 из родительского класса 'Объект № 1''")
# Вызов метода класса
Dogs_2.info_Animal()
Dogs_2.locotion_Animal()