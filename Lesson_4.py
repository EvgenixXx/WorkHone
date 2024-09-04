from abc import ABC, abstractmethod  # Импортируем ABC и abstractmethod для создания абстрактных классов  


# Определяем абстрактный класс Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Запускает двигатель транспортного средства"""
        pass  # Абстрактный метод, который должен быть реализован в подклассах

    @abstractmethod
    def stop_engine(self):
        """Останавливает двигатель транспортного средства"""
        pass  # Абстрактный метод, который должен быть реализован в подклассах

    @abstractmethod
    def drive(self):
        """Двигает транспортное средство"""
        pass  # Абстрактный метод, который должен быть реализован в подклассах


# Определяем подкласс Car, который наследует от Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand  # Инициализация марки автомобиля
        self.model = model  # Инициализация модели автомобиля
        self.__engine_running = False  # Приватный атрибут для состояния двигателя

    def start_engine(self):
        """Запускает двигатель автомобиля"""
        self.__engine_running = True  # Устанавливаем состояние двигателя в 'работает'
        print(f"{self.brand} {self.model}: Двигатель запущен.")

    def stop_engine(self):
        """Останавливает двигатель автомобиля"""
        self.__engine_running = False  # Устанавливаем состояние двигателя в 'не работает'
        print(f"{self.brand} {self.model}: Двигатель остановлен.")

    def drive(self):
        """Двигает автомобиль"""
        if self.__engine_running:
            print(f"{self.brand} {self.model} движется.")  # Выводим сообщение о движении
        else:
            print(f"{self.brand} {self.model}: Сначала запустите двигатель!")  # Сообщение, если двигатель не запущен


# Определяем подкласс Motorcycle, который также наследует от Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand  # Инициализация марки мотоцикла
        self.model = model  # Инициализация модели мотоцикла
        self.__engine_running = False  # Приватный атрибут для состояния двигателя

    def start_engine(self):
        """Запускает двигатель мотоцикла"""
        self.__engine_running = True  # Устанавливаем состояние двигателя в 'работает'
        print(f"{self.brand} {self.model}: Двигатель запущен.")

    def stop_engine(self):
        """Останавливает двигатель мотоцикла"""
        self.__engine_running = False  # Устанавливаем состояние двигателя в 'не работает'
        print(f"{self.brand} {self.model}: Двигатель остановлен.")

    def drive(self):
        """Двигает мотоцикл"""
        if self.__engine_running:
            print(f"{self.brand} {self.model} движется.")  # Выводим сообщение о движении
        else:
            print(f"{self.brand} {self.model}: Сначала запустите двигатель!")  # Сообщение, если двигатель не запущен


# Функция, которая выполняет действия с транспортным средством
def vehicle_action(vehicle):
    vehicle.start_engine()  # Запускаем двигатель
    vehicle.drive()  # Двигаем транспортное средство
    vehicle.stop_engine()  # Останавливаем двигатель


# Создаем экземпляры классов Car и Motorcycle
my_car = Car("Toyota", "Camry")  # Создаем объект автомобиля
my_motorcycle = Motorcycle("Yamaha", "MT-07")  # Создаем объект мотоцикла

# Вызываем функцию vehicle_action для разных объектов
vehicle_action(my_car)  # Выводит действия для автомобиля
vehicle_action(my_motorcycle)  # Выводит действия для мотоцикла