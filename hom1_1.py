#1
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class FileStorage(Storage):
    def save(self):
        print("Save to file")

    def load(self):
        print("Load from file")

    def delete(self):
        print("Delete from file")


class DatabaseStorage(Storage):
    def save(self):
        print("Save to database")

    def load(self):
        print("Load from database")

    def delete(self):
        print("Delete from database")


# 2

class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['__setattr__'] = Meta.__setattr__
        return super().__new__(cls, name, bases, attrs)

    def __setattr__(self, key, value):
        if key in self.__annotations__:
            if not isinstance(value, self.__annotations__[key]):
                raise TypeError(f"Invalid type for {key}")
        object.__setattr__(self, key, value)


class MyClass(metaclass=Meta):
    x: int
    y: str
    z: bool


obj = MyClass()
obj.x = 20
obj.y = "123"
obj.z = True
#obj.x = "20"


# 3
class Vehicle:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def drive(self):
        print(f"Driving")


class Car(Vehicle):
    def __init__(self, color, price, model):
        super().__init__(color, price)
        self.model = model

    def drive(self):
        print(f"Driving {self.model}")


class Motorcycle(Vehicle):
    def __init__(self, color, price, model):
        super().__init__(color, price)
        self.model = model

    def drive(self):
        print(f"Driving {self.model}")


class Bicycle(Vehicle):
    def __init__(self, color, price, size):
        super().__init__(color, price)
        self.size = size

    def drive(self):
        print(f"Driving Bicycle")


def driving(vehicle):
    print("**")
    vehicle.drive()
    print("**")


car = Car("Yellow", 500000, "Koenigsegg")
motorcycle = Motorcycle("Red", 22000, "Harley-Davidson")
bicycle = Bicycle("Black", 1000, 22)
car.drive()
motorcycle.drive()
bicycle.drive()
driving(car)
driving(motorcycle)
driving(bicycle)
