
https://towardsdatascience.com/solid-programming-part-1-single-responsibility-principle-efca5e7c2a87

Single Responsibility Principle


https://medium.com/better-programming/zero-to-hero-python-cheat-sheet-primitive-data-types-44bd4b29fe95

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