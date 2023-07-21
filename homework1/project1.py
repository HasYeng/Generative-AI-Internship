class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return self.__class__.__name__.lower()

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"Resource(name={self.name}, manufacturer={self.manufacturer})"

    def claim(self, n):
        if self._total - self._allocated >= n:
            self._allocated += n
        else:
            return -1

    def free_up(self, n):
        if self._allocated >= n:
            self._allocated -= n
        else:
            return -1

    def died(self, n):
        if self._total >= n:
            self._total -= n
        else:
            return -1

    def purchased(self, n):
        self._total += n


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_gb

    def __repr__(self):
        return f"Storage(name={self.name}, manufacturer={self.manufacturer}, capacity_GB={self.capacity_gb})"


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f"HDD(name={self.name}, manufacturer={self.manufacturer}, capacity_GB={self.capacity_gb}, size={self.size}, rpm={self.rpm})"


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f"SSD(name={self.name}, manufacturer={self.manufacturer}, capacity_GB={self.capacity_gb}, interface={self.interface})"


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, interface, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._interface = interface
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def interface(self):
        return self._interface

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return f"CPU(name={self.name}, manufacturer={self.manufacturer}, cores={self.cores})"


hdd = HDD("HDD", "Manufacturer", 20, 0, 1000, "Large", 7200)
ssd = SSD("SSD", "Manufacturer", 30, 0, 500, "SATA")
cpu = CPU("CPU", "Manufacturer", 10, 0, 8, "PCIe", "Socket Type", 65)

print(hdd)
print(ssd)
print(cpu)

hdd.claim(10)
print(hdd.allocated)

hdd.free_up(5)
print(hdd.allocated)

hdd.purchased(20)
print(hdd.total)

hdd.died(30)
print(hdd.total)
print(hdd.died(30))
