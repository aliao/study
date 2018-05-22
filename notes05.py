def evens(n):
    """ Return the n-th even number. """
    return 2 * n


def make_seq_generator(fn):
    """
    >>> generate_evens = make_seq_generator(evens)
    >>> for i in range(4):
    ...     print(generate_evens())
    0
    2
    4
    6
    """
    i = 0
    def dispatch():
        nonlocal i
        result = fn(i)
        i += 1
        return result
    return dispatch

def make_counter(start_val):
    """
    >>> counter1 = make_counter(4)
    >>> counter2 = make_counter(42)
    >>> counter1('count')
    5
    >>> counter1('count')
    6
    >>> counter2('count')
    43
    >>> counter2('reset')
    0
    >>> counter1('count')
    7
    >>> counter = make_counter(3)
    >>> counter('count')
    4
    >>> clone = counter('clone')
    >>> clone('count')
    5
    >>> counter('reset')
    0
    >>> clone('count')
    6
    """
    count = start_val
    def dispatch(msg):
        nonlocal count
        if msg == 'count':
            count += 1
            return count
        elif msg == 'reset':
            count = 0
            return count
        elif msg == 'clone':
            return make_counter(count)
    return dispatch
