class ValidType:
    """Descriptor class for validating attribute types"""
    def __init__(self, type_):
        self._type = type_

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f"Expected {self._type}, but got {type(value)}")
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]


class Int(ValidType):
    """Descriptor class for integer, inheritance from ValidType"""
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    """Descriptor class for float, inheritance from ValidType"""
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    """Descriptor class for list, inheritance from ValidType"""
    def __init__(self):
        super().__init__(list)


class Person:
    """Person class with attributes: age, height, tags, favorite_foods, and name"""
    age = Int()
    height = Float()
    tags = ValidType(tuple)
    favorite_foods = List()
    name = ValidType(str)

    def __init__(self, age, height, tags, favorite_foods, name):
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods
        self.name = name


# Testing class Person
person = Person(20, 180.5, ("Developer", "Python"), ["Pizza", "Pasta"], "Liam")
print(person.age)
print(person.height)
try:
    person2 = Person(20, "180.5", ["Developer", "Python"], ["Pizza", "Pasta"], "Lily")
except ValueError as ex:
    print(ex)
try:
    person.name = ("Jessie", "James")
except ValueError as ex:
    print(ex)
