def add(*args):
    sums = 0
    for n in args:
        sums += n
    return sums


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs['multiply']


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='Toyota', model='Camry')
print(my_car.make)