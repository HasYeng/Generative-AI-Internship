class SingletonMeta(type):
    """Singleton metaclass"""
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        """Create a new instance of the class if it does not exist. Otherwise, return the existing instance."""
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Hundred(metaclass=SingletonMeta):
    """A class that can only have one instance."""
    def __init__(self):
        self.name = 'hundred'
        self.value = 100


h1 = Hundred()
h2 = Hundred()
print(h1 is h2)
