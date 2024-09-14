#create a function #add that takes any numbers of args and returns the sum

def add(*args):
    return sum(args)

print(add(5,4,3,2,1))


#multiple key word arguments or **kwargs, **kwargs has a dictionary data formart

def func(**kwargs):
    print(kwargs)

func(money="cash", car="skyline", house_location = "beverly hills")