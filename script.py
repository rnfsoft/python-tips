def debug_function(func):
    def wrapper(*args, **kwargs):
        print("{} is called with param {}".format(func.__qualname__, args[1:]))
        return func(*args, **kwargs)
    return wrapper

def debug_all_methods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug_function(val))
    return cls

class MetaClassDebug(type):
    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debug_all_methods(obj)
        return obj

class MyClass(metaclass=MetaClassDebug):
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y

myClass = MyClass()
print(myClass.add(2,3))
print(myClass.sub(2,3))