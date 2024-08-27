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
