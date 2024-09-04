class Animal:
    def speak(self):
        return 'Животное издает звук'

dog = Dog("Жмурик")
cat = Cat("Жорик")


def animal_sound(animal):
    print(animal.speak())



animal_sound(dog)
animal_sound(cat)