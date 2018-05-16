"""Submission for CS 61A Homework 3.

Name: 
Login:
Collaborators:
"""

def str_interval(x):
    """Return a string representation of interval x.
    
    >>> str_interval(make_interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(make_interval(-1, 2), make_interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return make_interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Q1
def make_interval(a, b):
    """Construct an interval from a to b."""
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

# Q2
def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert upper_bound(y) != 0, 'divided by 0'
    assert lower_bound(y) != 0, 'divided by 0'
    reciprocal_y = make_interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3
def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-9 to -2'
    """
    negative_y = make_interval(min(-lower_bound(y), -upper_bound(y)), \
                               max(-lower_bound(y), -upper_bound(y)))
    return add_interval(x, negative_y)

# Q4
def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(make_interval(1, 2), make_interval(4, 8)))
    '4 to 16'
    >>> str_interval(mul_interval_fast(make_interval(1, 2), make_interval(-4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(1, 2), make_interval(-8, -4)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(-1, 2), make_interval(-4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(-1, 2), make_interval(-8, -4)))
    '-16 to 8'
    >>> str_interval(mul_interval_fast(make_interval(-2, -1), make_interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(make_interval(-2, -1), make_interval(-4, 8)))
    '-16 to 8'
    >>> str_interval(mul_interval_fast(make_interval(-2, -1), make_interval(-8, -4)))
    '4 to 16'
    """
    xl, xu, yl, yu = lower_bound(x), upper_bound(x), lower_bound(y), upper_bound(y)
    if xl >= 0:
        if yl >= 0:
            return make_interval(xl * yl, xu * yu)
        if yl <= 0 <= yu:
            return make_interval(xu * yl, xu * yu)
        if yu <= 0:
            return make_interval(xu * yl, xl * yu)
    if xl <= 0 <= xu:
        if yl >= 0:
            return make_interval(xl * yu, xu * yu)
        if yl <= 0 <= yu:
            return make_interval(min(xl * yu, yl * xu), max(xl * yl, xu * yu))
        if yu <= 0:
            return make_interval(xu * yl, xl * yl)
    if xu <= 0:
        if yl >= 0:
            return make_interval(xl * yu, xu * yl)
        if yl <= 0 <= yu:
            return make_interval(xl * yu, xl * yl)
        if yu <= 0:
            return make_interval(xu * yu, xl * yl)

# Q5
def make_center_width(c, w):
    """Construct an interval from center and width."""
    return make_interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2

def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.
    
    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    width = abs(c * p) / 100
    return make_interval(c - width, c + width)

def percent(x):
    """Return the percentage tolerance of interval x.
    
    >>> percent(make_interval(1, 3))
    50.0
    """
    return width(x) * 100 / center(x)

# Q6
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

"""Lem complains that Alyssa's program gives different answers for the two ways
of computing. This is a serious complaint.

Demonstrate that Lem is right with some well chosen print statements."""


# Q7

"""Tell whether par2 is a better program for parallel resistances than par1 and
why.  Write the explanation as a string below."""

"*** YOUR CODE HERE ***"

# Q8
def quadratic(x, a, b, c):
    """Return the interval that is the range of values taken on by the
    the quadratic defined by a, b, and c, over the domain interval x.

    >>> str_interval(quadratic(make_interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(make_interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    xl, xu = lower_bound(x), upper_bound(x)
    f = lambda x : a * x * x + b * x + c
    if a == 0:
        return add_interval((mul_interval(make_interval(b, b), x)), make_interval(c, c))
    elif a > 0:
        ex_p = -b/(2*a)
        if ex_p <= xl:
            return make_interval(f(xl), f(xu))
        if xl <= ex_p <= xu:
            return make_interval(f(ex_p), max(f(xl), f(xu)))
        if xu <= ex_p:
            return make_interval(f(xu), f(xl))
    elif a < 0:
        ex_p = -b/(2*a)
        if ex_p <= xl:
            return make_interval(f(xu), f(xl))
        if xl <= ex_p <= xu:
            return make_interval(min(f(xl), f(xu)), f(ex_p))
        if xu <= ex_p:
            return make_interval(f(xl), f(xu))

# Q9  [Extra problem to be repeated next week.]
def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0 

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = make_interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.
    
    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    result = zero
    for i in seq:
        if non_zero(i):
            result = add_interval(zero, square_interval(i))
    return result

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.
    
    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(add_interval, map(square_interval, filter(non_zero, seq)))

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.
    
    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    def s(seq):
        for i in seq:
            if non_zero(i):
                yield square_interval(i)
    return reduce(add_interval, s(seq))

# Q10 (Extra)

def polynomial(x, c):
    """Return the interval that is the range the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(make_interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(make_interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> r = polynomial(make_interval(0.5, 2.25), (10, 24, -6, -8, 3))
    >>> round(lower_bound(r), 5)
    18.0
    >>> round(upper_bound(r), 5)
    23.0
    """
    "*** YOUR CODE HERE ***"

