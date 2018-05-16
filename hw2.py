from operator import add, mul


# Q1
def product(n, term):
    """Return the product of the first n terms in the sequence formed 
    by applying term to the integers 1, ..., n.

    term -- a function that takes one argument
    """
    result, k = 1, 1
    while k <= n:
        result, k = result * term(k), k + 1
    return result

def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    return product(n, lambda x : x)

# Q2
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence.

    *** YOUR DESCRIPTION HERE ***
    """
    k, result = start, term(start)
    while k < n:
        result = combiner(result, term(k + 1))
        k += 1
    return result

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate."""
    return accumulate(add, 1, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate."""
    return accumulate(mul, 1, n, term)


# Q3
def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument
    """
    def double_f(x):
        return f(f(x))
    return double_f


# Q4
def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    """
    def repeated_f_n(x):
        result = f
        nonlocal n
        while n > 1:
            result = compose1(f, result)
            n -= 1
        return result(x)
    return repeated_f_n

def square(x):
    """Return x squared."""
    return x * x

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h


# Q5 (Extra)
def zero(f):
    """Church numeral 0."""
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1."""
    "*** YOUR CODE HERE ***"

def two(f):
    """Church numeral 2."""
    "*** YOUR CODE HERE ***"

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n."""
    "*** YOUR CODE HERE ***"

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(add_church(two, two))
    4
    """
    "*** YOUR CODE HERE ***"


