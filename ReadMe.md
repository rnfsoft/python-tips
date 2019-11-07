List Comprehensions with if
    r = [n for n in range(1, 10)]
    print([n for n in r if n > 2 and n%2 ==0]) # [4, 6, 8]
    print([n for n in r if n> 2 if n%2 == 0]) # [4, 6, 8]

filter()

    col = [1, 2, 3, 4, 5, 6, 7]
    print(list(filter(lambda x: x > 5, col))) # [6,7]

pprint - Data pretty printe

Context managers

    from datetime import datetime

    class DataManager():
        def __init__(self):
            self.file = None
        
        def __enter__(self):
            now = str(datetime.now()).split(".")[0].replace(" ", "-").replace(":", "-") # 2019-11-06 15:58:43.370827 --> 2019-11-06-15-58-43
            filename = now +"-DATA.txt"
            self.file = open(filename, "w")
            return self.file

        def __exit__(self, exc_type, exc_value, exc_traceback):
            self.file.close()
            print("Exited")

    with DataManager() as data:
        data.write("hello") # create 2019-11-06-16-01-24-DATA.txt and write hello


Multiprocessing multiprocessing.py

    With Process: 1.4353456497192383 seconds
    With Pool: 3.249145269393921 seconds
    Without Multiprocessing: 19.022353410720825 seconds

Yield

    def createGenerator():
        print("Beginning of generator")
        for i in range(3):
            yield i
        print("After yield")

print("Before assignment")
my_generator = createGenerator()
print("After assignment")
for i in my_generator:
    print(i)

Lambda

    remainder = lambda x, y: x % y
    print(remainder(10,3)) # 1

Filter

    data = [1, 2, 3, 4, 5, 6, 7, 9]
    print([d for d in data if d > 5]) # [6, 7, 9]
    print(list(filter(lambda x: x > 5, data))) # [6, 7, 9]

Map

    data = [1, 2, 3, 4, 5, 6, 7, 9]
    print([x//2 for x in data]) # [0, 1, 1, 2, 2, 3, 3, 4]
    print(list(map(lambda x: x//2, data))) # [0, 1, 1, 2, 2, 3, 3, 4]

NamedTuple

    from collections import namedtuple
    Features = namedtuple('Features', ['age', 'gender', 'name'])
    row = Features(age=32, gender='male', name='Test')
    print(row.age) # 32

Counter

    from collections import Counter
    ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 45, 52, 22, 22, 22, 25, 16, 11, 15, 40, 30]
    value_counts = Counter(ages)
    print(value_counts) # Counter({22: 5, 25: 3, 30: 2, 24: 2,...})

DefaultDict

    from collections import defaultdict
    my_default_dict = defaultdict(int)
    for ch in 'you are super':
        my_default_dict[ch] += 1
    print(my_default_dict) # defaultdict(<class 'int'>, {'y': 1, 'o': 1, 'u': 2, ...})


Meta-Classes

Defines the behavior of an ordinary class and its instance

eg. class MyClass with 3 methods, add debug functionality to all the methods 

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


Decorator
    
    - Decorator 1
    def my_decorator(func):
        def wrapper_function(*args, **kwargs):
            print("{} is called with param {}".format(func.__name__, args))
            print(func(*args, **kwargs))
        return wrapper_function

    @my_decorator
    def add(x, y):
        return x + y

    add(5, 3)  # add is called with parameter (5, 3), 8

    - Decorator 2
    def validate_positive(func):
        def inner(*args, **kwargs):
            for arg in args:
                if arg <0:
                    raise Exception("Invalid Number!")
            result = func(*args, *kwargs)
            return result
        return inner

    @validate_positive
    def complicated_computation(x, y, z):
        return x**2 + y*10 - z

    print(complicated_computation(-1, 10, 7)) # Error: Invalid Number!

    - Class Decorator
    
    class ValidatePositive():
    def __init__(self, func):
        self.function = func
    
    def __call__(self, *args, **kwargs):
        for arg in args:
            if arg < 0:
                raise Exception("Invalid number!")
        return self.function(*args, **kwargs)

    @ValidatePositive
    def complicated_computation(x, y, z):
        return x**2 + y*10 - z

    print(complicated_computation(-1, 10, 7)) # Error: Invalid Number!


Frequency of Elements in a List

    from collections import Counter

    l = ['a','a','b','b','b','c','d','d','d','d','d']
    count = Counter(l)
    print(count) # Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})
    print(count['b']) # 3
    print(count.most_common(1)) # [('d', 5)]

Try except else

    a, b = 1,0

    try:
        print(a/b)
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('no exception raised')
    finally:
        print('no way')

Memory Usage of an Object

    import sys
    num = 21
    print(sys.getsizeof(num))

Merging Two Dictionaries

    dict_1={'apple':1, 'banana': 6}
    dict_2={'banana':4, 'orange': 8}
    print({**dict_1, **dict_2}) # {'apple': 9, 'banana': 4, 'orange': 8}

Flattering a List of Lists

    from iteration_utilities import deepflatten
    l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]
    print(list(deepflatten(l, depth=3))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Digitize

    num = 123456
    print(list(map(int, str(num)))) # [1, 2, 3, 4, 5, 6]
    print( [int(x) for x in str(num)]) # [1, 2, 3, 4, 5, 6]


Output of the division operation: float

    20/10
    >> 2.0

    100//11
    >> 9

    100.00//11
    >> 9.0

String formatting

    "{} love {}".format("I", "Programming")
    >> I love programming

    "{0}, {1}. {2}. {0}".format("A", "B", "C")
    >> A B C A

    "{c0}, {c1}. {c2}. {c0}".format(c0="A", c1="B", c2="C")
    >> A B C A

    me = "Robot" 
    str = f"{me} is a machine" # reference varialbes 
    str
    >> Robot is a machine

https://towardsdatascience.com/memory-management-in-python-6bea0c8aecc9

Avoid using the + operator for strings

    msg = 'hello %s world' % mymsg

Assign a function to a local variable:

    localFunc = function
    for i in range(n):
        localFunc(i)

Use itertools:

    from itertools import product, chain

    list(
        chain.from_iterable(function(shape, weight)
            for weight, shape in product([True, False], range(1,5))
        )
    )
https://towardsdatascience.com/python-tricks-101-what-every-new-programmer-should-know-c512a9787022

List comprehensions:

    [print('', x, end='\t') for x in "Hello" ];print()
    >> H   e   l   l   o

    [print(ord(x), end='\t') for x in "Hello" ];print()
    >> 72  101 108 108 111

    print([x ** 2 + 5 for x in my_list if x % 2 != 0])
    >> [6, 14, 30]

Lambda:

    my_list = [2, 1, 0, -1, -2]
    print(sorted(my_list, key=lambda x: x**2))
    >> [0, -1, 1, -2, 2]

Map:

    print(list(map(lambda x, y: x*y, [1,2,3], [4,5,6])))
    >> [4, 10, 18]

Zip:

    print([' '.join(x) for x in zip(alpha, num)])
    >> ['A 1', 'B 2']

References:
    
https://towardsdatascience.com/solid-programming-part-1-single-responsibility-principle-efca5e7c2a87

Single Responsibility Principle


https://medium.com/better-programming/zero-to-hero-python-cheat-sheet-primitive-data-types-44bd4b29fe95

https://medium.com/better-programming/20-python-snippets-you-should-learn-today-8328e26ff124

https://medium.com/better-programming/meta-programming-in-python-7fb94c8c7152

https://towardsdatascience.com/the-most-undervalued-standard-python-library-14021632f692

https://levelup.gitconnected.com/a-practical-introduction-to-python-lambda-functions-3b4a0702b6a1

https://medium.com/better-programming/what-does-the-yield-keyword-do-6b9304149462

https://towardsdatascience.com/a-hands-on-guide-to-multiprocessing-in-python-48b59bfcc89e

https://medium.com/@negoiddfelix/python-from-intermediate-to-superhero-1a86e518bb77
