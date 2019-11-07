r = [n for n in range(1, 10)]
print([n for n in r if n > 2 and n%2 ==0])
print([n for n in r if n> 2 if n%2 == 0])
# col = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(lambda x: x > 5, col)))


# from functools import reduce
# example = [1, 2, 3, 4, 5, 6] # sum: 15
# print(reduce(lambda x, y: x*y, example)) # 6!


# from pprint import pprint
# var = 5
# print ('var' in globals())
# print('var' in locals())
# pprint(locals())
# pprint(globals())

# from datetime import datetime

# class DataManager():
#     def __init__(self):
#         self.file = None
    
#     def __enter__(self):
#         now = str(datetime.now()).split(".")[0].replace(" ", "-").replace(":", "-") # 2019-11-06 15:58:43.370827 --> 2019-11-06-15-58-43
#         filename = now +"-DATA.txt"
#         self.file = open(filename, "w")
#         return self.file

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()
#         print("Exited")

# with DataManager() as data:
#     data.write("hello") # create 2019-11-06-16-01-24-DATA.txt and write hello

# class ValidatePositive():
#     def __init__(self, func):
#         self.function = func
    
#     def __call__(self, *args, **kwargs):
#         for arg in args:
#             if arg < 0:
#                 raise Exception("Invalid number!")
#         return self.function(*args, **kwargs)

# @ValidatePositive
# def complicated_computation(x, y, z):
#     return x**2 + y*10 - z

# print(complicated_computation(-1, 10, 7)) # Error: Invalid Number!

# def validate_positive(func):
#     def inner(*args, **kwargs):
#         for arg in args:
#             if arg <0:
#                 raise Exception("Invalid Number!")
#         result = func(*args, *kwargs)
#         return result
#     return inner

# @validate_positive
# def complicated_computation(x, y, z):
#     return x**2 + y*10 - z

# print(complicated_computation(-1, 10, 7))

# def squares(a, b):    
#     while a < b:        
#         yield a**2
#         a += 1

# for num in squares(5, 10):
#     print(num)

# sequene = squares(5, 10)
# print(next(sequene))
# print(next(sequene))

# remainder = lambda x, y: x % y
# print(remainder(10,3))

# data = [1, 2, 3, 4, 5, 6, 7, 9]
# print([d for d in data if d > 5])
# print(list(filter(lambda x: x > 5, data)))


# data = [1, 2, 3, 4, 5, 6, 7, 9]
# print([x//2 for x in data])
# print(list(map(lambda x: x//2, data)))

# def debug_function(func):
#     def wrapper(*args, **kwargs):
#         print("{} is called with param {}".format(func.__qualname__, args[1:]))
#         return func(*args, **kwargs)
#     return wrapper

# def debug_all_methods(cls):
#     for key, val in vars(cls).items():
#         if callable(val):
#             setattr(cls, key, debug_function(val))
#     return cls

# class MetaClassDebug(type):
#     def __new__(cls, clsname, bases, clsdict):
#         obj = super().__new__(cls, clsname, bases, clsdict)
#         obj = debug_all_methods(obj)
#         return obj

# class MyClass(metaclass=MetaClassDebug):
#     def add(self, x, y):
#         return x + y
#     def sub(self, x, y):
#         return x - y

# myClass = MyClass()
# print(myClass.add(2,3))
# print(myClass.sub(2,3))

# from collections import namedtuple

# Features = namedtuple('Features', ['age', 'gender', 'name'])
# row = Features(age=32, gender='male', name='Test')
# print(row.age)


# from collections import Counter
# ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 45, 52, 22, 22, 22, 25, 16, 11, 15, 40, 30]
# value_counts = Counter(ages)
# print(value_counts)


# from collections import defaultdict
# my_default_dict = defaultdict(int)
# for ch in 'you are super':
#     my_default_dict[ch] += 1
# print(my_default_dict)