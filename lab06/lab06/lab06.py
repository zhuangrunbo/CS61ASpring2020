this_file = 'lab06.py'
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    n = n
    adder = -1
    def adder_value(x):
        nonlocal n
        nonlocal adder
        adder += 1

        return n + x + adder

    return adder_value
    
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    pre_pre_fib = 0
    pre_fib = 0

    def next_fib():
        nonlocal pre_pre_fib
        nonlocal pre_fib
        
        current_fib  = pre_fib + pre_pre_fib
        if pre_pre_fib == 0:
            pre_pre_fib = pre_fib
            pre_fib = 1
        else:
            pre_pre_fib = pre_fib
            pre_fib = current_fib

        return current_fib

    return next_fib

# Generators
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for e in it:
        yield e * multiplier

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    res = []
    
    def hailstone_value(n):
        nonlocal res
        res.append(n)
        
        while n != 1: 
            if n % 2 == 0:
                n = int(n/2)
            else:
                n = int(n * 3 + 1)
            res.append(n)
            
    hailstone_value(n)

    return res
