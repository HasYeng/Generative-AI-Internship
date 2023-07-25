class SlottedStruct(type):
    """Metaclass for generating slotted classes with common functionalities for N-dimensional points."""
    def __new__(cls, name, bases, namespace):
        if name != 'Point':
            dim = int(name[-2])
            namespace['__slots__'] = tuple(f'_{i}' for i in range(1, dim + 1))
            namespace['__init__'] = cls._init_coordinates
            namespace['__eq__'] = cls._eq_coordinates
            namespace['__hash__'] = cls._hash_coordinates
            namespace['__repr__'] = cls._repr_coordinates
            namespace['__str__'] = cls._str_coordinates

        return super().__new__(cls, name, bases, namespace)

    def _init_coordinates(self, *args):
        """Initialize the coordinates of the point."""
        for i, arg in enumerate(args, start=1):
            setattr(self, f'_{i}', arg)

    def _eq_coordinates(self, other):
        """Compare the coordinates of the point with another point for equality."""
        return isinstance(other, type(self)) and tuple(getattr(self, f'_{i}') for i in range(1, self.dim + 1)) == \
               tuple(getattr(other, f'_{i}') for i in range(1, self.dim + 1))

    def _hash_coordinates(self):
        """Compute the hash of the point based on its coordinates."""
        return hash(tuple(getattr(self, f'_{i}') for i in range(1, self.dim + 1)))

    def _repr_coordinates(self):
        """Generate a representation of the point based on its coordinates."""
        coord_str = ', '.join(str(getattr(self, f'_{i}')) for i in range(1, self.dim + 1))
        return f'Point{self.dim}D({coord_str})'

    def _str_coordinates(self):
        """Generate a string representation of the point based on its coordinates."""
        coord_str = ', '.join(str(getattr(self, f'_{i}')) for i in range(1, self.dim + 1))
        return f'({coord_str})'


class Point(metaclass=SlottedStruct):
    pass


# Testing with Point2D and Point3D
class Point2D(Point):
    dim = 2


class Point3D(Point):
    dim = 3


class Point4D(Point):
    dim = 4


class Point5D(Point):
    dim = 5


# Test
p1 = Point2D(1, 2)
p2 = Point2D(1, 2)
p3 = Point2D(2, 3)
p4 = Point3D(1, 2, 3)
p5 = Point3D(1, 2, 3)
p6 = Point3D(2, 3, 4)
p7 = Point4D(1, 2, 3, 4)
p8 = Point4D(1, 2, 3, 4)
p9 = Point4D(2, 3, 4, 5)
p10 = Point5D(1, 2, 3, 4, 5)
p11 = Point5D(1, 2, 3, 4, 5)
p12 = Point5D(2, 3, 4, 5, 6)

print(p1)
print(p7)
print(p10)

print(p1 == p2)
print(p1 == p3)
print(p4 == p5)
print(p4 == p6)
print(p7 == p8)
print(p7 == p9)
print(p10 == p11)
print(p10 == p12)

print(hash(p1))
print(hash(p4))
print(hash(p7))
print(hash(p10))
