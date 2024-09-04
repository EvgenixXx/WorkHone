import keyboard  # Импортируем библиотеку для отслеживания нажатий клавиш  
import time  # Импортируем библиотеку для задержки
from abc import ABC, abstractmethod  # Импортируем ABC и abstractmethod для создания абстрактных классов


# Определяем абстрактный класс Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Запускает двигатель транспортного средства"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Останавливает двигатель транспортного средства"""
        pass

    @abstractmethod
    def drive(self):
        """Двигает транспортное средство"""
        pass

    # Определяем подкласс Car, который наследует от Vehicle


class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__engine_running = False

    def start_engine(self):
        """Запускает двигатель автомобиля"""
        if not self.__engine_running:
            self.__engine_running = True
            print(f"{self.brand} {self.model}: Двигатель запущен.")

    def stop_engine(self):
        """Останавливает двигатель автомобиля"""
        if self.__engine_running:
            self.__engine_running = False
            print(f"{self.brand} {self.model}: Двигатель остановлен.")

    def drive(self):
        """Двигает автомобиль"""
        if self.__engine_running:
            print(f"{self.brand} {self.model} движется.")
        else:
            print(f"{self.brand} {self.model}: Сначала запустите двигатель!")

        # Определяем подкласс Motorcycle, который также наследует от Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__engine_running = False

    def start_engine(self):
        """Запускает двигатель мотоцикла"""
        if not self.__engine_running:
            self.__engine_running = True
            print(f"{self.brand} {self.model}: Двигатель запущен.")

    def stop_engine(self):
        """Останавливает двигатель мотоцикла"""
        if self.__engine_running:
            self.__engine_running = False
            print(f"{self.brand} {self.model}: Двигатель остановлен.")

    def drive(self):
        """Двигает мотоцикл"""
        if self.__engine_running:
            print(f"{self.brand} {self.model} движется.")
        else:
            print(f"{self.brand} {self.model}: Сначала запустите двигатель!")

        # Функция для управления транспортным средством с помощью клавиатуры


def keyboard_control(vehicle):
    print(
        f"Управление {vehicle.brand} {vehicle.model}. Нажмите 's' для запуска, 'd' для движения, 'x' для остановки, 'q' для выхода.")

    while True:
        if keyboard.is_pressed('s'):  # Если нажата клавиша 's'
            vehicle.start_engine()
            time.sleep(0.5)  # Задержка, чтобы избежать многократного вызова
        elif keyboard.is_pressed('d'):  # Если нажата клавиша 'd'
            vehicle.drive()
            time.sleep(0.5)  # Задержка, чтобы избежать многократного вызова
        elif keyboard.is_pressed('x'):  # Если нажата клавиша 'x'
            vehicle.stop_engine()
            time.sleep(0.5)  # Задержка, чтобы избежать многократного вызова
        elif keyboard.is_pressed('q'):  # Если нажата клавиша 'q'
            print("Выход из управления.")
            break
        time.sleep(0.1)  # Небольшая задержка для снижения нагрузки на процессор


# Создаем экземпляры классов Car и Motorcycle
my_car = Car("Toyota", "Camry")
my_motorcycle = Motorcycle("Yamaha", "MT-07")

# Запрашиваем у пользователя, с каким транспортным средством он хочет взаимодействовать
while True:
    vehicle_choice = input("Выберите транспортное средство (car/motorcycle/exit): ").strip().lower()

    if vehicle_choice == "car":
        keyboard_control(my_car)  # Управление автомобилем
    elif vehicle_choice == "motorcycle":
        keyboard_control(my_motorcycle)  # Управление мотоциклом
    elif vehicle_choice == "exit":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")