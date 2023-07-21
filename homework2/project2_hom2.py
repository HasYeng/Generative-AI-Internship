import collections.abc


class Int:
    """Descriptor class for integer values with optional bounds"""
    def __init__(self, min_value=None, max_value=None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        """Validate that the assigned value is an integer and within bounds"""
        if not isinstance(value, int):
            raise TypeError(f"Expected {self._name} to be an integer, but got {type(value)}")
        if self._min_value is not None and value < self._min_value:
            raise ValueError(f"{self._name} must be at least {self._min_value}")
        if self._max_value is not None and value > self._max_value:
            raise ValueError(f"{self._name} cannot exceed {self._max_value}")
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]


class Point2D:
    """Class representing a point on a 2D plane"""
    x = Int(0, 100)
    y = Int(0, 100)

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2DSequence:
    """Validator class for a sequence of Point2D instances"""
    def __init__(self, min_length=None, max_length=None):
        self._min_length = min_length
        self._max_length = max_length

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        """Validate that the assigned value is a sequence of Point2D instances within the given length range"""
        if not isinstance(value, collections.abc.Sequence):
            raise TypeError(f"{self._name} must be a sequence of Point2D instances")
        if self._min_length is not None and len(value) < self._min_length:
            raise ValueError(f"{self._name} must contain at least {self._min_length} items")
        if self._max_length is not None and len(value) > self._max_length:
            raise ValueError(f"{self._name} cannot contain more than {self._max_length} items")
        for index, point in enumerate(value):
            if not isinstance(point, Point2D):
                raise TypeError(f"Point at index {index} in {self._name} is not a Point2D instance")
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]


class Polygon:
    """Class representing a polygon shape"""
    vertices = Point2DSequence(3, 6)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, point):
        vertices = self.vertices + (point,)
        self.vertices = vertices


# Testing the Polygon class
polygon = Polygon(Point2D(0, 0), Point2D(1, 1), Point2D(2, 2), Point2D(2, 2))
polygon.append(Point2D(3, 3))
try:
    polygon.append(Point2D(3, 300))
except ValueError as ex:
    print(ex)
try:
    polygon.append(123)
except TypeError as ex:
    print(ex)
try:
    polygon.append(Point2D(3, 3))
    polygon.append(Point2D(3, 3))
except ValueError as ex:
    print(ex)




