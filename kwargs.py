#using the kwargs in class

class Car:
    def __init__(self, **kwargs):
        #will be using a getter method here to pull the data from kwargs, so that if the kwarg is not provided, our program does not run into error
        self.make = kwargs.get("make", "Data Not Found")
        self.model = kwargs.get("model", "Data Not Found")
        self.year = kwargs.get("year", "Data Not Found")


my_car = Car()
#prints "Data Not Found"
my_car.make = "Nissan"

my_real_car = Car(make="Nissan", model="GodZilla", year=1997)

print(my_real_car.make, my_real_car.model, my_real_car.year)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)