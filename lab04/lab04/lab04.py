""" Lab 04 """


this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 0:
        return 0
    else:
        return skip_add(n-2) + n

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    def find_divisor(n, m, divisor):
        if type(n/divisor) == int and type(m/divisor) == int : return divisor
        else: find_divisor(n, m, divisor - 1)
    if a > b:
        return find_divisor(a, b, b)
    else:
        return find_divisor(a, b, a)

    
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)

def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    def get_max_digit(n, l):
        index = 0
        resIndex = 0
        res = 0
        for c in str(n):
            if c.isdigit() and index <= len(str(n)) - l:
                if res < int(c):
                    res = int(c)
                    resIndex = index
            index += 1
        return res, resIndex

    def rest_n(resIndex):
        res = 0
        index = 0
        for c in str(n):
            if c.isdigit() and index >= resIndex:
                res += int(c) * pow(10, len(str(n)) - 1 - index)
            index += 1
        return res
                
    if l == 0:
        return 0
    elif len(str(n)) <= l:
        return n
    else:
        max_digit, digit_index = get_max_digit(n, l)
        return max_digit * pow(10, l - 1) + max_subseq(rest_n(digit_index), l - 1)

        
 
