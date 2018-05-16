from math import *


def isnumber(thing):
    try:
        int(thing)
    except:
        return False
    return True

def type_check(fn, predicate, datum):
    if predicate(datum):
        return fn(datum)
    else:
        return False

def make_safe(fn, predicate):
    """
    >>> ss = make_safe(sqrt, isnumber)
    >>> ss(4)
    2.0
    >>> ss('h')
    False
    """
    def dispatch(datum):
        if predicate(datum):
            return fn(datum)
        else:
            return False
    return dispatch
