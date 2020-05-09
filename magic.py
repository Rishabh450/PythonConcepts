movie = 12.39126


# print(movie.__class__)
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def length(self):
        return len(self.cars)
    # used for indexing of class object

    def __getitem__(self, item):
        return f'{self.cars[item]}'

    def __repr__(self):
        return f'Garage:Cars={self.cars}'

    @property
    def carsize(self):
        return  len(self)








garage = Garage();
garage.cars.append('Audi')
garage.cars.append('Lambo')
print(garage.cars)
print(garage.length())
print(len(garage))
print(garage[0])
print(garage)
print(garage.carsize)
