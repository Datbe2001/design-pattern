from abc import ABC, abstractmethod


# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

    @abstractmethod
    def get(self, subject):
        pass


# Concrete Observer: Khách hàng
class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print(f'{self.name} has been notified of price change to {subject.price}. Name {subject.name}')

    def get(self, subject):
        print(f'{self.name} has been notified of price access: {subject._price}')


# Subject class
class Product:
    def __init__(self, name, price):
        self._observers = []
        self._price = price
        self.name = name

    @property
    def price(self):
        self._notify_observers_get()
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price
        self._notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def _notify_observers_get(self):
        for observer in self._observers:
            observer.get(self)


# Sử dụng Observer Pattern
product = Product('Laptop', 1000)
customer1 = Customer('Alice')
customer2 = Customer('Bob')

product.add_observer(customer1)
product.add_observer(customer2)

print(f'Initial price: {product.name} - {product.price}')
product.price = 200

# =================================================================================================================

from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

# ConcreteObserver
class DisplayDevice(Observer):
    def update(self, temperature: float):
        print(f"Display Device: Updated temperature is {temperature}°C")

class AlarmSystem(Observer):
    def update(self, temperature: float):
        if temperature > 30:
            print("Alarm System: Warning! High temperature detected!")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# ConcreteSubject
class TemperatureSensor(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        print(f"TemperatureSensor: New temperature is {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

# Sử dụng Observer Pattern
sensor = TemperatureSensor()
display = DisplayDevice()
alarm = AlarmSystem()

sensor.register_observer(display)
sensor.register_observer(alarm)

sensor.set_temperature(10)  # Hiển thị nhiệt độ mới
sensor.set_temperature(35)  # Cảnh báo nhiệt độ cao
