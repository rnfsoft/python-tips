remainder = lambda x, y: x % y
print(remainder(10,3))

data = [1, 2, 3, 4, 5, 6, 7, 9]
print([d for d in data if d > 5])
print(list(filter(lambda x: x > 5, data)))


data = [1, 2, 3, 4, 5, 6, 7, 9]
print([x//2 for x in data])
print(list(map(lambda x: x//2, data)))

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