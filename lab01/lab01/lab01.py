"""Lab 1: Expressions and Control Structures"""

def both_positive(a, b):
    """Returns True if both a and b are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return a > 0 and b > 0 # You can replace this line!

def sum_digits(x):
    """Sum all the digits of x.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    string = str(x)
    sum = 0
    for i in string:
        sum += int(i)
    return sum
